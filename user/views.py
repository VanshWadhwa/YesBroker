from django.shortcuts import render , redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from project.models import Project
from property.models import Property
from django.contrib import messages




@ login_required
def favourite_list(request):
    # new = Project.newmanager.filter(favourites=request.user)
    project_list = Project.objects.filter(favourites=request.user)
    print(project_list)
    property_list = Property.objects.filter(favourites=request.user)
    return render(request,
                  'user/favourites.html',

                  context={
                      
                      'project_list': project_list,
                      'property_list': property_list,

                   })


@ login_required
def favourite_add(request, id):
    project = get_object_or_404(Project, id=id)
    if project.favourites.filter(id=request.user.id).exists():
        project.favourites.remove(request.user)
        messages.success(request , 'Removed from your favourites')

    else:
        project.favourites.add(request.user)
        messages.success(request , 'Added to your favourites')

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@ login_required
def favourite_add_property(request, id):
    property = get_object_or_404(Property, id=id)
    if property.favourites.filter(id=request.user.id).exists():
        property.favourites.remove(request.user)
        messages.success(request , 'Removed from your favourites')

    else:
        property.favourites.add(request.user)
        messages.success(request , 'Added to your favourites')

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'user/profile.html', context)
