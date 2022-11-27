from django.shortcuts import render,HttpResponse
from machinelearning import spam_predictor
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