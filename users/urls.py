from django.urls import path, include
import django.contrib.auth.urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)

from users import views

app_name = 'users'

# Auth urls
urlpatterns = [
        path('sigh_in', views.SighInView.as_view(), name='sigh_in'),
        path('', include("django.contrib.auth.urls"),),
        path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
