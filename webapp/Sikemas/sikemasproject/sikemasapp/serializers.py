from rest_framework.decorators import authentication_classes
from rest_framework.permissions import IsAuthenticated
from .models import *
from rest_framework import serializers


class opdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opd
        fields = '__all__'

class staffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff

class serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class questionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = SikemasappQuestionnaire
        fields = 'questionnaire_id','question_text','choice_one','choice_two','choice_three','choice_four'

class peopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'

class respondenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responden
        fields = '__all__'

