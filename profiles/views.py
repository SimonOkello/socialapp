from django.shortcuts import render

from .models import Profile
from .forms import ProfileModelForm

# Create your views here.
def profile_view(request):
    obj = Profile.objects.get(user=request.user)
    form =ProfileModelForm(instance=obj)
    confirm=False
    if request.method=='POST':
        form =ProfileModelForm(request.POST, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()
            confirm=True
    context={'obj':obj, 'form':form,'confirm':confirm}
    return render(request, 'profiles/profile.html', context)