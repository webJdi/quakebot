from django.shortcuts import render, redirect
from .forms import InputForm
from .predictor import predictor
import pandas as pd
from .plot import create_plot
import os
from django.conf import settings
# Create your views here.

def predict(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            prediction = predictor(data)
            predround = round(prediction,4)
            return redirect(f'/results/?prediction={predround}')
    else:
        form = InputForm()
    
    context = {'form':form}
    return render(request,"form.html",context)

def home(request):
    return render(request, "index.html")

def results(request):
    pred = request.GET.get('prediction')
    
    return render(request, 'result.html',{'prediction':pred})

def plot(request):
    path = os.path.join(settings.BASE_DIR, 'quakepredict', 'data.csv')
    geo_data = pd.read_csv(path)
    geo_data['date_time'] = geo_data['Date']+ " " + geo_data['Time (utc)']

    if geo_data['date_time'].dtypes == 'object':
        geo_data['date_time'] = pd.to_datetime(geo_data['date_time'],dayfirst=True)
    geo_data['Latitude'] = geo_data['Latitude'].str.extract(r'(\d+\.\d+)')[0].astype(float) * geo_data['Latitude'].str.extract(r'([NS])')[0].map({'N': 1, 'S': -1})
    geo_data['Longitude'] = geo_data['Longitude'].str.extract(r'(\d+\.\d+)')[0].astype(float) * geo_data['Longitude'].str.extract(r'([EW])')[0].map({'E': 1, 'W': -1})

    plothtml = create_plot(geo_data)
    return render(request,"plot.html",{'plothtml':plothtml})