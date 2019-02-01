from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import utils

@api_view(['GET'])
def home(request):
    response = {'message': 'welcome to api'}
    return Response(data=response)

@api_view(['GET'])
def qa_set(request):
    if request.query_params.get('anwser'):
      response = utils.get_set_by_anwser_id(request.query_params['anwser'])
    elif request.query_params.get('question'):
      response = utils.get_set_by_qusetion_id(request.query_params['question'])
    else:
      response = {'finish':True, 'message': 'error occured ( params )'}
    return Response(data=response)

@api_view(['GET'])
def question_list(request):
    response = utils.get_question_list()
    return Response(data=response)

@api_view(['POST'])
def log_conversation(request):
    print(utils.create_log(request.data))
    response = {'logged':True, 'message': 'response from log coversation'}
    return Response(data=response)
