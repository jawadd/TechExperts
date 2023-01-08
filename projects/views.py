from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def projects(request):
    context = {'course_name': 'Learning Django with Dennis Ivy',
               'course_detail': 'A self paced course and will probably take up to 1 month to complete it'}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    return render(request, 'projects/singleProject.html')
