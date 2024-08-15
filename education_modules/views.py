from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from education_modules.models import EducationModules
from education_modules.pagination import MyPagination
from education_modules.permissions import IsAdmin
from education_modules.serializers import EducationSerializer


class EducationModulesAPIView(ListAPIView):
    queryset = EducationModules.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [AllowAny]
    pagination_class = MyPagination


class EducationModulesDetailAPIView(RetrieveAPIView):
    queryset = EducationModules.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [AllowAny]


class EducationModulesCreateAPIView(CreateAPIView):
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]


class EducationModulesUpdateAPIView(UpdateAPIView):
    queryset = EducationModules.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]


class EducationModulesDestroyAPIView(DestroyAPIView):
    queryset = EducationModules.objects.all()
    permission_classes = [IsAdmin]
