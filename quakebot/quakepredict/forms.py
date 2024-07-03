from django import forms

class InputForm(forms.Form):
    depth = forms.FloatField(label='Depth(km)')
    lat = forms.FloatField(label='Latitude')
    long = forms.FloatField(label='Longitude')