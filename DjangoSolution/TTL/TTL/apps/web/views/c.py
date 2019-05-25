from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    # TEST
    return HttpResponse("Hello, world. You're at the C index.")
