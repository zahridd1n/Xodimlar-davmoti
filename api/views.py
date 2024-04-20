from django.shortcuts import render
from django.utils import timezone
from main import models
from . import serializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view


@api_view(['GET'])
def worker_list(request):
    """Xodimlar ro'yxati"""
    workers = models.Worker.objects.all()
    serializer_data = serializer.WorkerSerializerList(workers, many=True)
    return Response(serializer_data.data)


@api_view(['POST'])
def attendace_create(request):
    """Davomat yaratilishi va yangilanishi"""
    try:
        worker_id = request.data.get('worker')
        last_attendance = models.Attendance.objects.filter(worker=worker_id).order_by('-id').first()
        if not last_attendance or last_attendance.gone_time:
            # Avvalgi obyekt mavjud emas yoki gone_time qiymati mavjud
            models.Attendance.objects.create(
                worker_id=worker_id,
                come_time=timezone.now(),
                gone_time=None
            )
        else:
            # Avvalgi obyekt mavjud va gone_time qiymati mavjud
            if last_attendance.gone_time is None:
                last_attendance.gone_time = timezone.now()
                last_attendance.save()

        return Response({'success': True})
    except:
        return Response({'success': False})