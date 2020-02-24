from django.shortcuts import render
from django.shortcuts import render
from django.http  import HttpResponse,Http404
import datetime as dt
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import *
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
# from token import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})