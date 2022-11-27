from django.shortcuts import render,HttpResponse
from machinelearning import spam_predictor
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import MessageSerializer
# Create your views here.

def index(request):
    return render(request,"index.html")

def predict(request):
    message = request.GET.get('message',"")
    result = spam_predictor.predictSpam(message)
    result_message = ""
    if(result == 1) : result_message = "Spam"
    else: result_message = "Ham"
    return HttpResponse(result_message)

@api_view(["POST"])
def predictApi(request):
    if request.method == 'POST':
        messageSerializer = MessageSerializer(data = request.data)
        data = {}
        if messageSerializer.is_valid():
            message = messageSerializer.data
            print(message['message'])
            result = spam_predictor.predictSpam(message['message'])
            data['message'] = message['message']
            if(result == 1): data['Spam'] = True
            else : data['Spam'] = False
    return Response(data)