from django.contrib import admin
from django.urls import path
from form import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path("login/",views.login,name='login'),
    path("query/",views.query,name='query'),
    path("delete/<int:pk>",views.delete,name='delete'),
    path("edit/<int:pk>",views.edit,name='edit'),

]

    
