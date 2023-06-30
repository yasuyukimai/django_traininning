from . import views
from django.urls import path

app_name = 'app'

urlpatterns = [
    path('',views.index, name='detail.html'),
    #path('app/<int:question=id>/aa', views.aa, name = 'aa'),

]