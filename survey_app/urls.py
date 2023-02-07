from . import views
from django.urls import path
urlpatterns = [
    path('survey/',views.home,name = 'home'),
    path('survey/thankyou',views.greeting,name = 'greetings'),
    path('survey/fill', views.survey_form,name='survey_form'),
    path('survey/result',views.survey_results,name='results')
]