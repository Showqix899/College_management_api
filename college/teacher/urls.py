from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import TeacherView,SubjectView


router=DefaultRouter()
router.register(r'teachers',TeacherView)
router.register(r'subjects',SubjectView)

urlpatterns = [
    
    path('',include(router.urls)),
    path('',include(router.urls))
]
