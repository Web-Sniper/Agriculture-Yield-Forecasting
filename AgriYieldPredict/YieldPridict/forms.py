from django import forms

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