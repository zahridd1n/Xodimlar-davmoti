from rest_framework.serializers import ModelSerializer

from main import models


class WorkerSerializerList(ModelSerializer):
    """Xodimlar ro'yxati serizalizeri qiluvchi"""
    class Meta:
        model = models.Worker
        fields = '__all__'


class AttendanceSerializer(ModelSerializer):
    """davomat"""
    class Meta:
        model = models.Attendance
        fields = ['worker']
