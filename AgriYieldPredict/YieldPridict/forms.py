from django import forms
import numpy as np
import pandas as pd

class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="",
        widget= forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder" : "Enter Name"
            }
        )
    )
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Email"
            }
        )
    )
    contact = forms.IntegerField(
        label="",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Contact"
            }
        )
    )
    feedback = forms.CharField(
        label="",
        widget= forms.Textarea(
            attrs={
                "class" : "form-control",
                "placeholder" : "Your Feedback"
            }
        )
    )
class PredictionForm(forms.Form):
    data = pd.read_csv('E:\Major project\AgriYieldPredict\static\datasets\district_UP.csv')
    x = data.iloc[ :,:].values
    AREA_CHOICE = (('Select','Select Area'),)
    for i in x:
        AREA_CHOICE = AREA_CHOICE+(tuple(i),)
    area = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class' : 'form-control'
            }
        ),
        choices = AREA_CHOICE,
        label=""
    )
    data2 = pd.read_csv('E:\Major project\AgriYieldPredict\static\datasets\months.csv')
    MONTH_CHOICE = (('Select', 'Select Month'),)
    y = data2.iloc[:,:].values
    for j in y:
        MONTH_CHOICE = MONTH_CHOICE+(tuple(j),)
    month = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class' : 'form-control'
            }
        ),
        choices = MONTH_CHOICE,
        label=""
    )
    data3 = pd.read_csv('E:\Major project\AgriYieldPredict\static\datasets\soil.csv')
    SOIL_CHOICE = (('Select', 'Select Soil Type'),)
    z = data3.iloc[:, :].values
    for k in z:
        SOIL_CHOICE = SOIL_CHOICE + (tuple(k),)
    soil = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        ),
        choices=SOIL_CHOICE,
        label=""
    )
