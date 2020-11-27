from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    user = request.user
    message = 'Hello'
    return render(request, 'main/index.html', {'hello': message, 'user': user})
