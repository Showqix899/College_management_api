from django.urls import path,include

from rest_framework import routers
from .views import studentView
router=routers.DefaultRouter()
router.register(r'info',studentView)


urlpatterns = [
    path('',include(router.urls))
]

