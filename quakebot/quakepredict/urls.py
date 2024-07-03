from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='home'),
    path('form/',views.predict,name='form'),
    path('results/',views.results,name='results'),
    path('plot/',views.plot,name='plot')
]