from django.urls import path

from .views import userProfile

app_name = 'profiles'

urlpatterns = [
    
    path('my-profile', userProfile, name='profile' )
]