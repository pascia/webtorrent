from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from ipware import get_client_ip
import csv
import sys
import os
import time
import sqlite3 as sql

def main(request):
    ip, is_routable = get_client_ip(request)

    context={
        'ip' : ip
        }

    return render(request, "main.html", context)
