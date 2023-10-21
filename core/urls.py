"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls import handler404
from django.conf import settings
from django.conf.urls.static import static
from core import views

handler404 = 'core.views.pagina_404'

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('/', views.home, name='home'),
    path('logar/', views.logar, name='logar'),
    path('logar/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.logar, name='register'),
    path('register/', auth_views.RegisterView.as_view(), name='register'),
    path('dologin/', views.dologin, name='dologin'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
