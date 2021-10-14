from django.shortcuts import render
from .models import Property
from project.models import Project
from client.forms import ClientForm
from django.views.generic import DetailView
import os
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.


# def property_detail(request):
#     context = {}
#     return render(request, 'property/property-detail.html', context=context)


# class PropertyDetailView(DetailView):
#     model = Property

#     def get(self, **kwargs):

def PropertyDetailView(request , pk):


    property = Property.objects.get(id = pk)

    # context = {
    #     'property' : property,
    #     'total_available_units' : total_available_units,
    #     'property_for_sale'  : property_for_sale,
    #     'property_for_rent' : property_for_rent,
    # }

    # total_available_units = Property.objects.get( developer = 'DSR SSC The Classe').count()
    # total_available_units = Property.objects.get( projectName = 'DSR SSC The Classe').count()
    total_available_units = Property.objects.filter(projectName = 'DSR SSC The Classe').count()
    # MOD
    # property_for_sale = Property.objects.filter(forSale = True).count()
    property_for_sale = Property.objects.filter(forSale = 'Available').count()
    # MOD
    # property_for_rent = Property.objects.filter(forRent = True).count()
    property_for_rent = Property.objects.filter(forRent = 'Available').count()

 

    clientForm  = ClientForm()

    if request.method == 'POST':
        form = ClientForm(request.POST)
        print(request.POST)
        if form.is_valid():
            messages.success(request , 'We got your request , We will soon revert back to you : )')
            form.save()
            

    # context = {}
    # return render(request , 'client/client_form.html' , context)
    
    context = {
        'property' : property,
        'total_available_units' : total_available_units,
        'property_for_sale'  : property_for_sale,
        'property_for_rent' : property_for_rent,
        'clientForm' : clientForm,
    }



    path = os. getcwd()
    print("path ", path)
    return render(request, 'property/property_detail.html', context=context)



def show_property_list(request , slug):
    context = {}

  
    # property_name = request.GET.get('property')
    print("property_name : " ,slug)

    # filtered_projects = ProjectFilter(
    #     request.GET,
    # )

    try:
        properties=Property.objects.filter(projectName = slug )
        print(properties)
    except Property.DoesNotExist:
        properties = None

    category = Project.objects.filter(developer = 'DSR SSC The Classe')
    # completionTime = Project.objects.filter(projectName = 'DSR SSC The Classe')
    # property_for_rent = Property.objects.filter(forRent = True).count()

 
    context['filtered_projects'] = properties
    context['category'] = "Mix Highrise Society"
    # print('cATEGORYU'  , category)
    context['completionTime'] = "01-12-2025"


    

    paginated_filtered_projects = Paginator(properties, 9)
    page_number = request.GET.get('page')
    project_page_obj = paginated_filtered_projects.get_page(page_number)

    context['project_page_obj'] = project_page_obj

    return render(request, 'property/property_list.html', context=context)


# def PropertyDetailView(request , pk):


#     # property = Property.objects.get(id = pk)

#     # context = {
#     #     'property' : property
#     # }
    
#     # path = os. getcwd()
#     # print("path ", path)
#     # return render(request, 'property/new.html')
    





def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'phone_number': form.cleaned_data['phone_number'], 
			'email_address':form.cleaned_data['email_address'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("main:homepage")
      
	form = ContactForm()
	return render(request, "property/contact.html", {'form':form})
    
def render_pdf_view(request):
    
    template_path = 'property/user_printer.html'
    context = {'myvar': 'Send me the template'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    filename = 'Property-Details'
    response['Content-Disposition'] = 'attachment; filename="' + filename + '.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')

    messages.success(request , 'Pdf File has been downloaded')
    
    return response