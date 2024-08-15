from django.urls import path
from .views import (EducationModulesAPIView, EducationModulesDetailAPIView, EducationModulesCreateAPIView, EducationModulesUpdateAPIView,
                    EducationModulesDestroyAPIView)

app_name = 'education_modules'

urlpatterns = [
    path('models/', EducationModulesAPIView.as_view(), name='models'),
    path('models/<int:pk>/', EducationModulesDetailAPIView.as_view(), name='model'),
    path('models/create/', EducationModulesCreateAPIView.as_view(), name='create'),
    path('models/delete/<int:pk>/', EducationModulesDestroyAPIView.as_view(), name='delete'),
    path('models/update/<int:pk>/', EducationModulesUpdateAPIView.as_view(), name='update'),
]
