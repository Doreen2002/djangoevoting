from django.shortcuts import render
from .models import Rcandidates
# Create your views here.
context ={
        "candidate":Rcandidates.objects.all()
    }
def Rcandidate(request):
    
    if request.method == "POST":
        post = Rcandidates()
        post.organ = request.POST.get("organ")
        post.position =  request.POST.get("position")
        post.intake =  request.POST.get("intake")
        post.course =  request.POST.get("course")
        post.studentno =  request.POST.get("studentno")
        post.save()
    return render(request, "evelyhone/Rcandidate.html")
def Dcandidate(request):
    return render(request, "evelyhone/Dcandidate.html", context)
def home(request):
    return render(request, "evelyhone/home.html")
def Rvoter(request):
    return render(request, "evelyhone/Rvoter.html")

