"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views
from accounts import views as accountViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('accounts/',accountViews.accountView,name='accounts'),
    path('accounts/signup/',accountViews.signup,name='signup'),
    path('accounts/login/',accountViews.loginUser,name='login'),
    path('accounts/logout/',accountViews.logoutUser,name='logout'),
    path('activate/<uidb64>/<token>/',accountViews.activate, name='activate'),
    path('validateEmail/',accountViews.validateEmail,name='validateEmail'),
    path('validatePass/',accountViews.validatePass,name='validatePass',),
    path('numericPass/',accountViews.numericPass,name='numericPass',),
    path('comparePass/',accountViews.comparePass,name='comparePass',),
    path('commanPass/',accountViews.commanPassCheck,name='commanPass',),
]
