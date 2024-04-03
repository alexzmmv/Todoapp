from django import forms

class todoaddform(forms.Form):
    user_input=forms.CharField(label="Enter the task:")
    user_input_description=forms.CharField(label="Enter the task description:")