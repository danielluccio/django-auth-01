from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def login_user(request):
    return render(request, 'accounts/login_user.html')


@login_required
def private_page_1(request):
    return render(request, "accounts/private_page_1.html")

@login_required
def private_page_2(request):
    return render(request, "accounts/private_page_2.html")
