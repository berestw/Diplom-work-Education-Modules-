from django.urls import path
from .views import (
    EducationModulesListAPIView,
    EducationModulesCreateAPIView,
    EducationModulesUpdateAPIView,
    EducationModulesDestroyAPIView,
    EducationModulesRetrieveAPIView,
)

app_name = "education_modules"

urlpatterns = [
    path("", EducationModulesListAPIView.as_view(), name="list"),
    path("create/", EducationModulesCreateAPIView.as_view(), name="create"),
    path("delete/<int:pk>/", EducationModulesDestroyAPIView.as_view(), name="delete"),
    path("update/<int:pk>/", EducationModulesUpdateAPIView.as_view(), name="update"),
    path(
        "retrieve/<int:pk>/", EducationModulesRetrieveAPIView.as_view(), name="retrieve"
    ),
]
