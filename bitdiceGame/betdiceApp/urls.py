from django.urls import path
from . import views
app_name = 'betdiceApp'
urlpatterns = [
        path('',views.index,name='index'),
        path('bet/',views.bet,name ='bet')
        ]
