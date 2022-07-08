import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from sikemasapp.admin import opd
from .models import *
from rest_framework import viewsets, permissions
from .serializers import *


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def apiOverView(request):
    api_urls = {
        'Peoples': '/peopleoverview/',
        'Opds': '/opdoverview/',
        'Services': '/serviceoverview/',
        'Questionnaires': '/questionnaireoverview/',
        'Staffs': '/staffoverview/'
    }
    return Response(api_urls)
#API People
@api_view(['GET', 'POST'])
#@permission_classes((permissions.AllowAny,))
def apiOverView_People(request):
     api_urls = {
          'ShowPeople':'show-people',
     }
     return Response(api_urls)
 
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def showpeople(request):
    people = People.objects.all()
    serializer = peopleSerializer(people, many = True)
    return Response(serializer.data)

@api_view(['POST','GET'])
@permission_classes([permissions.IsAuthenticated])
def addpeople(request):
    serializer = peopleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Registrasi
class StaffViewset(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = staffSerializer
    permissions_classes = [permissions.IsAuthenticated]
    
@api_view(['POST','GET'])
@permission_classes([permissions.IsAuthenticated])
def addstaff(request):
    serializer = staffSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def showstaff(request):
    staff = Staff.objects.all()
    serializer = staffSerializer(staff, many = True)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def addpeople(request):
    serializer = peopleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

class peopleViewset(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = peopleSerializer
    permissions_classes = [permissions.IsAuthenticated]



@api_view(['GET', 'POST'])
# @permission_classes((permissions.AllowAny,))
def apiOverView_Opd(request):
    api_urls = {
        'ShowOPD': 'show-opd',
        'ShowOPDDetail': 'show-opd-detail/<opd_id>',
        'AddOPD': 'add-opd',
        'EditOPD': 'update/<opd_id>',
        'DeleteOPD': 'delete/<opd_id>'
    }
    return Response(api_urls)

@api_view(['GET', 'POST'])
#@permission_classes((permissions.AllowAny,))
def apiOverView_Service(request):
     api_urls = {
          'ShowService':'show-services/<str:opd_id>',
          'AddService':'add-service/<str:opd_id>',
          'DeleteService':'delete-service/<service_id>'
     }
     return Response(api_urls)

@api_view(['GET'])
# @permission_classes((permissions.AllowAny,))
def apiOverView_Staff(request):
    api_urls = {
        'addStaff': 'add-staff/<str:username>',
    }
    return Response(api_urls)

#API CRUD OPD
#Retrieve OPD
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def showopd(request):
    opd = Opd.objects.all()
    serializer = opdSerializer(opd, many=True)
    return Response(serializer.data)

#Retrive OPD
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def showopddetail(request, opd_id):
    opd = Opd.objects.get(opd_id=opd_id)
    serializer = opdSerializer(opd, many=False)
    return Response(serializer.data)

#Create OPD
@api_view(['POST', 'GET'])
@permission_classes([permissions.IsAdminUser])
def addopd(request):
    serializer = opdSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    elif Opd.objects.filter(opd_id=opd.request.data["opd_id"]).exists():
        raise serializers.ValidationError("This opd already exists.", status=406)
    return Response(serializer.data, status=201)


#Update OPD
@api_view(['PUT', 'GET'])
@permission_classes([permissions.IsAdminUser])
def editopd(request, opd_id):
    opd = Opd.objects.get(opd_id=opd_id)
    serializer = opdSerializer(instance=opd, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#Delete OPD
@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def destroyopd(request, opd_id):
    opd = Opd.objects.get(opd_id=opd_id)
    opd.delete()
    return Response("Item is successfully deleted!")

#ViewSet
class OpdViewSet(viewsets.ModelViewSet):
    queryset = Opd.objects.all()
    serializer_class = opdSerializer
    permission_classes = [permissions.IsAuthenticated]

#<<<<<<< Create-Api-Profile

#Update Profile
@api_view(['POST','GET'])
@permission_classes([permissions.IsAdminUser])
def updateprofile(request):
    serializer = staffSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

class staffViewset(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = staffSerializer
    permissions_classes = [permissions.IsAuthenticated]

# SERVICE FOR ADMIN
# Show Service
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def showservice(request):
    service = Service.objects.all()
    serializer = serviceSerializer(service, many = True)
    return Response(serializer.data)

# Show Service Detail(id_service)
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def showservicedetail(request,service_id):
    service = Service.objects.get(service_id=service_id)
    serializer = serviceSerializer(service, many = False)
    return Response(serializer.data)
# Add Service
@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def addservice(request):
    serializer = serviceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Delete Service
@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def destroyservice(request,service_id):
    service = Service.objects.get(service_id=service_id)
    service.delete()
    return Response("Item is successfully deleted!")

#>>>>>>> master

#questionnaire
@api_view(['POST','GET'])
@permission_classes([permissions.IsAuthenticated])
def addstaff(request):
    serializer = staffSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

class questionnaireViewset(viewsets.ModelViewSet):
    queryset = SikemasappQuestionnaire.objects.all()
    serializer_class = questionnaireSerializer
    permissions_classes = [permissions.IsAuthenticated]

@api_view(['GET'])
def apiOverView_Questionnaire(request):
     api_urls = {
     }
     return Response(api_urls)

#UAS
#Questionnaire for People

class RespondenViewSet(viewsets.ModelViewSet):
    queryset = Responden.objects.all()
    serializer_class = respondenSerializer

@api_view(['GET', 'POST'])
# @permission_classes((permissions.AllowAny,))

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def showquestionnaire(request):
    questionnaire = SikemasappQuestionnaire.objects.all()
    serializer = questionnaireSerializer(questionnaire, many=True)
    return Response(serializer.data)

def apiOverView_Responden(request):
    api_urls = {
        'addpeople': 'people/add-people/',
        'fillquestionnaire': 'fill-questionnaire/',
        'showresult': 'responden/show-result/',
        'editresult': 'responden/edit-result/<str:people_id>',
        'destroyresult': 'responden/destroy-result/<str:people_id>'

    }
    return Response(api_urls)

@api_view(['PUT', 'GET'])
def fillquestionnaire(request):
    serializer = respondenSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({
        'List Data': serializer.data,
        'Links': {
        'addpeople': 'http://127.0.0.1:8000/people/add-people',
        'showresult': 'responden/show-result/',
        'editresult': 'responden/edit-result/<str:people_id>',
        'destroyresult': 'responden/destroy-result/<str:people_id>'}},status=201)

@api_view(['GET'])
def showresult(request, people_id):
    responden = Responden.objects.get(people_id=people_id)
    serializer = respondenSerializer(responden, many=False)
    return Response({
        'List Data': serializer.data,
        'Links': {
        'addpeople': 'people/add-people/',
        'fillquestionnaire': 'http://127.0.0.1:8000/responden/fill-questionnaire',
        'editresult': 'responden/edit-result/<str:people_id>',
        'destroyresult': 'responden/destroy-result/<str:people_id>'}})

@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def destroyresponden(request,people_id, question_id):
    responden = Responden.objects.get(people_id=people_id, question_id=question_id )
    responden.delete()
    return Response({
        'Delete Succesfully'
        'Links': {
        'chooseservice': 'choose-services/',
        'fillquestionnaire': 'fill-questionnaire/',
        'showresult': 'show-result/'}})


@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def editresponden(request,people_id, question_id):
    responden = Responden.objects.get(people_id=people_id, question_id=question_id )
    serializer = respondenSerializer(instance = responden, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
 