"""Rahal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from first_app import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('blog', views.BlogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('home/',views.home, name='home'),
    path ('about/', views.about, name='about'),
    path('contact/',views.contact,name='contact'),
    path('add/',views.add , name='add'),
    path('login/',views.login_user,name='login'),
    path('register/',views.register, name="register"),
    path('logout/', views.logout_user, name='logout'),
    path('detials/<int:pk>', views.blogDetails, name='detials'),
    path('profile/<int:pk>', views.userProfile, name='profile'),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
