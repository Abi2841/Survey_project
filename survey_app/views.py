from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, redirect
from .models import ElectionSurveyDetails
from django.db.models import Count
def home(request):
    return render(request, 'survey_app/home.html')

def greeting(request):
    return render(request,'survey_app/greetings.html')

def survey_form(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("gender")
        dob = request.POST.get("dob")
        city = request.POST.get("city")
        party_name = request.POST.get("party_name")
        ElectionSurveyDetails.objects.create(
            first_name=first_name, last_name=last_name, gender=gender,
            dob=dob, city=city, party_name=party_name
        )
        return redirect('greetings')
    return render(request, "survey_app/survey_form.html")

def survey_results(request):
    results = ElectionSurveyDetails.objects.values("party_name").annotate(
        votes=Count("party_name")
    )
    return render(request, "survey_app/survey_results.html", {"results": results})