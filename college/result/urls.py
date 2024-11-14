from django.urls import path

from .views import StudentResultView,StudentResultUpdatedeleteView,StudentResultDetail

urlpatterns = [
    path('student_result/',StudentResultView.as_view(),name="student_result"),
    path('student_result/<int:pk>/',StudentResultUpdatedeleteView.as_view(),name="student_result"),
    path('student_result_detail/<str:id>/',StudentResultDetail.as_view(),name="detail"),
    
]
