from django import forms

class feedback(forms.Form):
    name = forms.CharField(
        label="Enter Your Name: ",
        widget= forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder" : "Enter Name"
            }
        )
    )
    email = forms.EmailField(
        label="Enter Your Email: ",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Name"
            }
        )
    )
    contact = forms.IntegerField(
        label="Enter Your Name: ",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Name"
            }
        )
    )