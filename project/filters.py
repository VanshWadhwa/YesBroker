import django_filters
# import autocomplete

from .models import Project

class ProjectFilter(django_filters.FilterSet):
    
    # category = django_filters.ModelChoiceFilter(
    #     field_name='category', lookup_expr='isnull',
    #     null_label='Uncategorized',
    #     queryset=Project.objects.all() ,
    #     # queryset=Project.objects.filter(category = 'com')
    # )

    CATEGORY_CHOICES = (
        ("Com Lowrise Office","Com Lowrise Office"),
        ("Com Lowrise Retail" , "Com Lowrise Retail"),
        ("Res Countryside Farms & Plots" , "Res Countryside Farms & Plots"),
        ("Res Highrise Society" , "Res Highrise Society"),
        ("Res Lowrise Society" , "Res Lowrise Society"),
        ("Res Lowrise Standalone" , "Res Lowrise Standalone"),
        ("Res Midrise Society" , "Res Midrise Society"),
        ("Res Urban Villas" , "Res Urban Villas"),
    )

    RERA_CHOICES = (
        ("True","True"),
        ("False" , "False"),
    )
    AGE_CHOICES = (
        ("Com Lowrise Office","Com Lowrise Office"),
        ("Com Lowrise Retail" , "Com Lowrise Retail"),
        ("Fake" , "Fake"),
        ("Res Countryside Farms & Plots" , "Res Countryside Farms & Plots"),
        ("Res Highrise Society" , "Res Highrise Society"),
        ("Res Lowrise Society" , "Res Lowrise Society"),
        ("Res Lowrise Standalone" , "Res Lowrise Standalone"),
        ("Res Midrise Society" , "Res Midrise Society"),
        ("Res Urban Villas" , "Res Urban Villas"),
    )
    # url = "/project/search/?address"
    category = django_filters.ChoiceFilter(label  = 'Category' , choices = CATEGORY_CHOICES )
    rera = django_filters.ChoiceFilter( choices = RERA_CHOICES ,label  = 'RERA'   )

    # rera = django_filters.BooleanFilter(field_name='rera', lookup_expr='isnull' ,label  = 'RERA' )
    society = django_filters.CharFilter( lookup_expr='icontains' , label  = 'Society' )
    developer = django_filters.CharFilter( lookup_expr='icontains' , label  = 'Developer' )

    # developer = django_filters.CharFilter(name='devname', lookup_expr='icontains', widget=autocomplete.ModelSelect2(url=url))


# class ProjectFilter(django_filters.FilterSet):

    # CATEGORY_CHOICES = (
    #     ("Com Lowrise Office","Com Lowrise Office"),
    #     ("Com Lowrise Retail" , "Com Lowrise Retail")
    #     ("Fake" , "Fake")
    #     ("Res Countryside Farms & Plots" , "Res Countryside Farms & Plots")
    #     ("Res Highrise Society" , "Res Highrise Society")
    #     ("Res Lowrise Society" , "Res Lowrise Society")
    #     ("Res Lowrise Standalone" , "Res Lowrise Standalone")
    #     ("Res Midrise Society" , "Res Midrise Society")
    #     ("Res Urban Villas" , "Res Urban Villas")
    # )
#     category = django_filters.ChoiceFilter(label  = 'Category' , choices = CATEGORY_CHOICES )
#     #  devname = django_filters.CharFilter(name='devname', lookup_expr='icontains', widget=autocomplete.ModelSelect2(url=devname_url))
#     society      = django_filters.CharFilter( lookup_expr='icontains')
#     developer = django_filters.CharFilter( lookup_expr='icontains')

#     class Meta:

#         model = Project
#         fields = [
#             # "category",
#             "rera",
#             "society",
#             "developer",
#             "completion",
#             "age",
#             "rating",
#             # "contact",
#             "subLocality",
#             "locality",
#             "zone",
#             # "projectPinCode",
#             # "googlePin",
#             # "units",
#             # "land",
#             # "floor",
#             # "block",
#             # "bhk",
#             "area",
#             "price",
#             # "promotersMembers",
#             # "landOwnerDetails",
#             # "surveyNumber"
#        ]
