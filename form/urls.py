from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('registration/',home,name='registration'),
    path('login/',login,name='login')

    
]