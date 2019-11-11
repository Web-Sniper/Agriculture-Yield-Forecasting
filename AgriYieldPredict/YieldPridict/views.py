from django.shortcuts import render
from .forms import FeedbackForm,PredictionForm
from .models import Feedback
from django.http.response import HttpResponse
def index(request):
    return render(request, "index.html")
def prediction(request):
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
    return render(request,'crops.html')