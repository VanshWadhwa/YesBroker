from .forms import DateTimeForm
from django.core import paginator
from django.shortcuts import render 
import datetime
from utils.Scheduler1 import create_event_for_meeting

from .models import Project
from property.models import Property
from .filters import ProjectFilter
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib import messages


# Create your views here.



def show_all_filter_page(request):

    context = {}

    filtered_projects = ProjectFilter(
        request.GET,
        queryset=Project.objects.all().order_by("-id")
    )


    context['filtered_projects'] = filtered_projects

    paginated_filtered_projects = Paginator(filtered_projects.qs, 9)
    page_number = request.GET.get('page')
    project_page_obj = paginated_filtered_projects.get_page(page_number)
    property_for_sale = Property.objects.filter(forSale = 'Available').count()
    property_for_rent = Property.objects.filter(forRent = 'Available').count()



    context['project_page_obj'] = project_page_obj
    context['property_for_sale'] = property_for_sale
    context['property_for_rent'] = property_for_rent

    try:
        properties=Property.objects.filter(projectName = 'DSR SSC The Classe')
        # print("DSR : "  ,properties[1].projectName)
    except Property.DoesNotExist:
        properties = None

    total_available_units = Property.objects.filter(projectName = 'DSR SSC The Classe').count()


    dtform = DateTimeForm()

    print('request.method ' , request.method)

    if request.method == 'project':
            dtform = DateTimeForm(request.project or None)

            dtformDict = dtform.data

            # print('dt-->')
                # print('dt-->')
            # print('dtformDict ' , dtformDict)
            dateTimeInput = dtformDict['meeting-date-time']
            # print('dateTime : ' , dateTimeInput)

            create_event_for_meeting(dateTimeInput , summary= 'Meeting from yb')
            print('Meeting scheduled')

            messages.success(request , 'Your meeting has been scheduled')



            # if 'date2' in request.project and 'date3' in request.project:
            #     date1Con = datetime.datetime.strptime(date1, '%d/%b/%Y %H:%M')
            #     dateFormat = date1Con.strftime('%d-%m-%Y %H:%M')
            #     s_date = datetime.datetime.strptime(dateFormat, "%d-%m-%Y %H:%M")

            #     date2 = dtformDict['date3']
            #     date2Con = datetime.datetime.strptime(date2, '%d/%b/%Y %H:%M')
            #     date2Format = date2Con.strftime('%d-%m-%Y %H:%M')
            #     e_date = datetime.datetime.strptime(date2Format, "%d-%m-%Y %H:%M")

            #     print('dt-->')
            #     # print('dt-->')
            #     print(s_date, e_date)
            #     print('dt-->')


    context['total_available_units'] = total_available_units
    context['dtform'] = dtform

    

    
    return render(request, 'project/show_all_filter_page.html', context=context)


def home_page(request):

    # projects=Project.objects.all().distinct()
    # projects=Project.objects.order_by('category').values_list('category', flat=True).distinct()

    # context = {
    #     "projects" : projects,
    # }

    return render(request, 'project/index3.html', {})
    # return render(request, 'project/home.html', {})
    # return render(request, 'project/index.html', context=context)

def premium_services(request):

    # projects=Project.objects.all().distinct()
    # projects=Project.objects.order_by('category').values_list('category', flat=True).distinct()

    # context = {
    #     "projects" : projects,
    # }

    return render(request, 'project/premium-services.html', {})
def login(request):

    # projects=Project.objects.all().distinct()
    # projects=Project.objects.order_by('category').values_list('category', flat=True).distinct()

    # context = {
    #     "projects" : projects,
    # }

    return render(request, 'project/login.html', {})

    
def search_address(request):
    address = request.GET.get('address')
    print("address : " , address)
    payload = []
    if address:
        address_objs = Project.objects.filter(developer__icontains = address)
        # address_objs = Project.objects.filter(developer_icontain = address)
        # print("address_objs : ", address_objs)

        for address_obj in address_objs:
            payload.append(address_obj.developer)

    return JsonResponse({'status' : 200 , 'data' : payload})

def developer_view(request):
    projects = Project.objects.order_by('-developer').values_list('developer', flat=True).distinct() 
    print("project : " ,projects)


    return render(request, 'project/developer.html', {
        'projects' : projects
    })

