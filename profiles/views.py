from django.shortcuts import render

# Create your views here.
from .models import Profile
from .forms import ProfileModelForm


def userProfile(request):
    obj = Profile.objects.get(user=request.user)

    form = ProfileModelForm(request.POST or None,
                            request.FILES or None, instance=obj)
    confirm=False
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm=True

    return render(request, 'profiles/profile.html', {'obj': obj, 'form': form, 'confirm':confirm})
