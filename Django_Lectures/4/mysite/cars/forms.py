from django import forms
from .models import Review
from django.forms import ModelForm
# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First_name', max_length=100)
#     last_name = forms.CharField(label='Last_name', max_length=100)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Please write your review here',
#                              widget=forms.Textarea(attrs={'class':'myform', 'rows':'2','cols':'2'}))

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"   #['first_name', 'last_name', 'stars']

        labels = {
            'first_name':'YOUR FIRST NAME',
            'last_name':'Last Name',
            'stars':'Rating'
        }

        error_messages = {
            'stars':{
                'min_value':"YO! Min value is 1", #chack the documentation for the keys
                'max_value':"YO! YO! Max value is 5"
            }
        }
