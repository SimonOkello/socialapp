from django.shortcuts import render

# Create your views here.
from .models import Profile

def userProfile(request):
    obj = Profile.objects.get(user=request.user)

    return render(request, 'profiles/profile.html', {'obj':obj})