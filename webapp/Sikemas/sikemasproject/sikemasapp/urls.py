from django.urls import path,include
from django.urls.resolvers import URLPattern
from sikemasapp import *
from django.contrib import admin
from django.conf.urls.static import static
from sikemasapp.viewset_api import *
from sikemasapp.views import *
from rest_framework import routers
from sikemasapp import views, viewset_api
from django.urls import path, include
from . import views
from sikemasapp.viewset_api import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('opd', viewset_api.OpdViewSet)
router.register('staff', viewset_api.staffViewset)
router.register('people', viewset_api.peopleViewset)
router.register('questionnaire', viewset_api.questionnaireViewset)
router.register('staff', viewset_api.staffViewset)
router.register('people', viewset_api.peopleViewset)
router.register('responden', viewset_api.RespondenViewSet)
urlpatterns = [
#API
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('apioverview',viewset_api.apiOverView, name='apioverview'),
    
#API People
path('api/show-people',viewset_api.showpeople, name='show-people'), 
path('api/add-people', viewset_api.addpeople, name='add-people'),



#API Staff
path('api/add-staff', viewset_api.addstaff, name='add-staff'),
path('api/show-staff',viewset_api.showstaff, name='show-staff'), 


#Viewset
    path('api/peopleviewset/', viewset_api.peopleViewset, name = "peopleviewset" ),
    path('api/opdviewset/', viewset_api.OpdViewSet, name = "opdviewset" ),
    path('api/questionnaireviewset/', viewset_api.questionnaireViewset, name = "questionnaireviewset" ),
    path('api/staffviewset/', viewset_api.staffViewset, name = "staffviewset" ),
    path('api/peopleviewset/', viewset_api.peopleViewset, name = "peopleviewset" ),
    path('api/respondenviewset/', viewset_api.RespondenViewSet, name = "respondenviewset" ),
    

#Overview
    path('api/opdoverview',viewset_api.apiOverView_Opd, name='opd-overview'),
    path('api/peopleoverview',viewset_api.apiOverView_People, name='people-overview'),
    path('api/questionnaireoverview',viewset_api.apiOverView_Questionnaire, name='questionnaire-overview'),
    path('api/staffoverview',viewset_api.apiOverView_Staff, name='staff-overview'),
    path('api/peopleoverview',viewset_api.apiOverView_People, name='people-overview'),
    path('api/respondenoverview',viewset_api.apiOverView_Responden, name='responden-overview'),

#API CRUD OPD
    path('opd/add-opd', viewset_api.addopd, name='add-opd'),  
    path('opd/show-opd',viewset_api.showopd, name='show-opd'),   
    path('opd/show-opd/<str:opd_id>',viewset_api.showopddetail, name='show-opd'), 
    path('opd/edit-opd/<str:opd_id>', viewset_api.editopd, name='edit-opd'),  
    path('opd/destroy-opd/<str:opd_id>', viewset_api.destroyopd, name='destroy-opd'),

 
#API Profile
    path('api/profile', viewset_api.updateprofile, name="profile"),

#API Questionnaire
    path('api/show-questionnaire',viewset_api.showquestionnaire, name='show-questionnaire'), 

#UAS Questionnaire for People
    path('responden/fill-questionnaire', viewset_api.fillquestionnaire, name='fill-questionnaire'), 
    path('responden/show-result/<str:people_id>',viewset_api.showresult, name='show-result'),
    path('responden/delete-result/<str:people_id>/<str:question_id>',viewset_api.destroyresponden, name='destroyresponden'),
    path('responden/edit-result/<str:people_id>/<str:question_id>',viewset_api.editresponden, name='editresponden'),
    
#CRD (Create Retrieve Delete) Service
    path('show-services/<str:opd_id>', views.show_service, name='show-services'),
    path('add-service/<str:opd_id>', views.add_service, name='add-service'),
    path('delete-service/<service_id>', views.destroy_service, name='delete-service'),


#WEB
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login', views.masuk, name='masuk'), 
    path('opd', views.inputdata, name='opd'),
    path('service/<str:opd_id>/<str:peopleid>', views.service, name='layanan'),
    path('registrasi/', views.registrasi, name='registrasi'),
    path('registrasi', views.dataregistrasi, name='dataregistrasi'),
    path('status-pengisian-kuesioner/', views.penutup, name='penutup'),
    path('people', views.people, name='people'),
    
    #CRUD (Create Retrieve Update Delete) OPD
    path('add-opd', views.add_opd, name='add-opd'),  
    path('show-opd',views.show_opd, name='show-opd'),  
    path('edit/<opd_id>', views.edit_opd, name='edit-opd'),  
    path('update/<opd_id>', views.update_opd, name='update-opd'),  
    path('delete/<opd_id>', views.destroy_opd, name='hapus-opd'),
    
    path('profile/', views.profile, name='profile'),
    path('update-profile/', views.updateprofile, name='update_profile'),
    path('Menu-CRUD-OPD/', views.Menu_CRUD_OPD, name='Menu_CRUD_OPD'),
    path('kuesioner/<str:peopleid>', views.kuesioner, name='kuesioner'),
]