from django.urls import path
#rest framework
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import RegisterStaffView,LoginStaffView,StaffLogoutView

urlpatterns = [
    path('register/',RegisterStaffView.as_view(),name='register'),
    path('login/',LoginStaffView.as_view(),name='login'),
    path('token/obtain', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', StaffLogoutView.as_view(), name='logout'),
]
