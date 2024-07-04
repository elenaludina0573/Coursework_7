from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from habits.models import Habits
from habits.paginators import CustomPagination
from habits.serializers import HabitSerializer


class HabitsCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, )


class HabitsListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (AllowAny, )
    pagination_class = CustomPagination


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, )


class HabitsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, )


class HabitsDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, )

