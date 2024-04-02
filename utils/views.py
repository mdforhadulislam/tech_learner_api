
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import *
from .serializers import *


def respons_setup(message: str, data: any, statuss: int):
    return Response({
        'messsage': message,
        'data': data,
        'status': statuss
    }, status.HTTP_200_OK)


@api_view(["GET"])
def session_data(request, id):
    try:
        all_session = Session.objects.get(id=id)
        all_session_data_serializer = SessionSerializers(all_session)
        all_session_data = all_session_data_serializer.data
        return respons_setup('get all categories', all_session_data, 200)
    except Exception as error:
        print(error)
        return respons_setup('there was an servier said error', {}, 400)


@api_view(["GET"])
def tag_data(request, id):
    try:
        all_tag = Tag.objects.get(id=id)
        all_tag_data_serializer = TagSerializers(all_tag)
        all_tag_data = all_tag_data_serializer.data
        return respons_setup('get all categories', all_tag_data, 200)
    except Exception as error:
        print(error)
        return respons_setup('there was an servier said error', {}, 400)


@api_view(["GET"])
def aboutData(request):
    try:
        all_about_data = About.objects.all()
        all_about_data_serializer = AboutSerializer(all_about_data, many=True)
        all_about_data = all_about_data_serializer.data
        return respons_setup('get all landing subscription', all_about_data, 200)
    except Exception as error:
        return respons_setup('there was an servier said error', {}, 400)


@api_view(["GET"])
def teamProfileData(request):
    try:
        all_team_profile_data = TeamProfile.objects.all()
        all_team_profile_data_serializer = TeamProfileSerializer(
            all_team_profile_data, many=True)
        all_team_profile_data = all_team_profile_data_serializer.data
        return respons_setup('get all landing subscription', all_team_profile_data, 200)
    except Exception as error:
        return respons_setup('there was an servier said error', {}, 400)


@api_view(["GET"])
def questionAndAnswerData(request):
    try:
        all_question_answer_data = FrequentlyAskedQuestions.objects.all()
        all_question_answer_data_serializer = FrequentlyAskedQuestionsSerializer(
            all_question_answer_data, many=True)
        all_question_answer_data = all_question_answer_data_serializer.data
        return respons_setup('get all landing subscription', all_question_answer_data, 200)
    except Exception as error:
        return respons_setup('there was an servier said error', {}, 400)


@api_view(["GET"])
def helpAboutData(request):
    try:
        all_help_about_data = HelpAbout.objects.all()
        all_help_about_data_serializer = HelpAboutSerializer(
            all_help_about_data, many=True)
        all_help_about_data = all_help_about_data_serializer.data
        return respons_setup('get all landing subscription', all_help_about_data, 200)
    except Exception as error:
        return respons_setup('there was an servier said error', {}, 400)


@api_view(["POST", "GET"])
def helpContactData(request):
    try:
        if request.method == 'GET':
            all_help_contact_data = HelpContact.objects.all()
            all_help_contact_data_serializer = HelpContactSerializer(
                all_help_contact_data, many=True)
            all_help_contact_data = all_help_contact_data_serializer.data
            return respons_setup('get all landing subscription', all_help_contact_data, 200)

        if request.method == 'POST':
            serializer = HelpContactSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

    except Exception as error:
        return respons_setup('there was an servier said error', {}, 400)
