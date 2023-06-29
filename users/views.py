from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate
from django.db import transaction
from django.contrib.auth import login

from .forms import UserCreateForm


# Create your views here.
class SighInView(View):
    def get(self, request):
        form = UserCreateForm()
        return render(request, 'registration/regist.html', {'form': form})

    # @transaction.atomic
    def post(self, request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = form.save()
            user = authenticate(request, username=username, password=password)
            return redirect('book:list')
        else:
            form = UserCreateForm()
            messeage = 'Форма не валидна'
            return render(request, 'registration/regist.html', {'form': form, 'messeage': messeage})
