from django.urls import path
from . import views
urlpatterns = [
    #/Achievements/
    path('',views.certi, name='certi'),

    #/Achievements/12
    path('<id>',views.detail, name='detail')
]