# -*- coding: utf-8 -*-


import sys
print (sys.path)
import datetime


from django.http import HttpResponse
from django.shortcuts import render



def hello(request):
    return HttpResponse("Hello world")


def dk_homepage(request):
    var = {
        'title': 'This is an ASCII title',
        'navbar': 'NavBar is here',
        'footer': 'Footer is here',
        'header': 'Header info'
    }
    template = 'bg/index.html'
    return render(request, template, var)
#    return HttpResponse('DK HomePage')


def current_params(request):
    paths = str(sys.path)
    now = datetime.datetime.now()
    html = '<html><body><p>%s</p><p>%s</p></body></html>' % (now, paths)
    return HttpResponse(html)

