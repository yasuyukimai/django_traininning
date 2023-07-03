from . import views
from django.urls import path
from .views import ListView

app_name = 'app'

urlpatterns = [
    path('',views.ListView.as_view(), name='list'),
    #path('app/<int:question=id>/aa', views.aa, name = 'aa'),

]