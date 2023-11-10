"""
URL configuration for backend project.

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
from django.urls import path, include
from cortofilm.views import CreateUserView, ListUserView, MakeSuperuserView,RevokeSuperuserView,UserDetailView
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doc/', include_docs_urls(title = "CortoFilm Api")),
    path('users/', ListUserView.as_view(), name='list-users'),
    path('user/create/', CreateUserView.as_view(), name='create-user'),
    path('user/<int:pk>/makesuperuser/', MakeSuperuserView.as_view(), name='make-superuser'),
    path('user/<int:pk>/revokesuperuser/', RevokeSuperuserView.as_view(), name='revoke-superuser'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
