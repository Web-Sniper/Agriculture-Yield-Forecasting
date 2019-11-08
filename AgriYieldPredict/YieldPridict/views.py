from django.shortcuts import render

def index(request):
    return render(request, "index.html")
def prediction(request):
    return render(request, "prediction.html")
def contact(request):
    return render(request,"contact.html")
def query(request):
    return render(request, "query.html")