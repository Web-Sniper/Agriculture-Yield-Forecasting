from django.shortcuts import render
from .forms import FeedbackForm,PredictionForm
from .models import Feedback,Crops
import pandas as pd
def index(request):
    return render(request, "index.html")
def prediction(request):
    crops = []
    if request.method=='POST':
        predictionForm = PredictionForm(request.POST)
        if predictionForm.is_valid():
            area = request.cleaned_data.get('area')
            soil = request.cleaned_data.get('soil')
            season = request.cleaned_data.get('month')
            data = pd.read_csv('E:\Major project\AgriYieldPredict\static\datasets\predicted.csv',encoding='ISO-8859-1')
            data = data.iloc[:,:].values
            for i in data:
                name = i[0]
                expenditure = i[1]
                sellingP = i[2]
                profit = i[3]
                duration = i[4]
                soil = i[5]
                season = i[6]
                crops.append(name=name,expenditure=expenditure,sellingP=sellingP,profit=profit,duration=duration,soil=soil,season=season)
            predictionForm = PredictionForm()
            return render(request, "prediction.html", {"form": predictionForm,'crops':crops})
    else:
        predictionForm = PredictionForm()
        return render(request, "prediction.html",{"form":predictionForm})
def contact(request):
    return render(request,"contact.html")
def feedback(request):
    if request.method=="POST":
        feedback = FeedbackForm(request.POST)
        if feedback.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            contact = request.POST.get("contact")
            feedback1 = feedback.cleaned_data.get("feedback")
            data = Feedback(
                name=name,
                email=email,
                contact=contact,
                feedback=feedback1
            )
            data.save()
            feedback = FeedbackForm()
            alert = "<script>alert('Data Saved......')</script>"
            return render(request, "query.html", {"abcd": feedback, "alert": alert})
        else:
            feedback = FeedbackForm()
            alert = "<script>alert('Invalid User Data.....')</script>"
            return render(request, "query.html", {"abcd": feedback, "alert": alert})
    else:
        feedback = FeedbackForm()
        return render(request, "query.html", {"abcd": feedback})
def weather(request):
    return render(request,'weather.html')
def crops(request):
    data = []
    crop = pd.read_csv('E:\Major project\AgriYieldPredict\static\datasets\crop_sheet.csv',encoding='ISO-8859-1')
    y = crop.iloc[:, :].values
    for i in y:
        name = i[0]
        name = name.title()
        type = i[1]
        time = i[2]
        des = i[3]
        data.append(dict(name=name,type=type,time=time,des=des))
    return render(request,'crops.html',{'data':data})