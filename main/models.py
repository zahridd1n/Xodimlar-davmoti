from django.db import models
from django.utils import timezone
from django.db.models import F


class Worker(models.Model):
    """XOdimlar jadvali """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='workers/', null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Attendance(models.Model):
    """Davomat jadvali """
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    come_time = models.DateTimeField(null=True, blank=True)
    gone_time = models.DateTimeField(null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     last_attendance = Attendance.objects.filter(worker=self.worker).order_by('-id').first()
    #     if not last_attendance or last_attendance.gone_time:
    #         self.come_time = timezone.now()
    #         self.gone_time = None
    #     else:
    #
    #         if last_attendance.gone_time is None:
    #             Attendance.objects.filter(id=last_attendance.id).update(gone_time=timezone.now())
    #     super(Attendance, self).save(*args, **kwargs)

    def __str__(self):
        return self.worker.first_name
