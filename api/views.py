from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.http import Http404
import hashlib
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from django.utils.crypto import get_random_string
from django.conf import settings
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse("Hello world")


def test(request):
    return HttpResponse("Hello world Test")


def test1(request):
    return HttpResponse("Hello world Test1")
