from django.shortcuts import render, redirect
from .. import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate


@login_required(login_url='dashboard:login')
def index(request):
    """Admin oynaning bosh sahifasi"""
    context = {
        'workers': models.Worker.objects.all(),
        'attendance': models.Attendance.objects.all(),
        'post': models.Attendance.objects.all().order_by('-gone_time')[0],
    }

    return render(request, 'dashboard/index.html', context)


# --------------Workers crude ------------------------
@login_required(login_url='dashboard:login')
def worker_create(request):
    """admin oynada xodim yaratish"""
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        tel = request.POST.get('tel')
        position = request.POST.get('position')
        image = request.FILES.get('image')
        worker = models.Worker.objects.create(
            first_name=first_name,
            last_name=last_name,
            tel=tel,
            position=position,
            image=image,
        )

    return render(request, 'dashboard/worker/create.html')


@login_required(login_url='dashboard:login')
def worker_list(request):
    """xodimlar ro'yxati"""
    worker = models.Worker.objects.all()
    return render(request, 'dashboard/worker/list.html', {'workers': worker})


@login_required(login_url='dashboard:login')
def worker_edit(request, id):
    """Xodimlarni tahririlash """
    worker = models.Worker.objects.get(id=id)
    if request.method == 'POST':
        worker.first_name = request.POST.get('first_name')
        worker.last_name = request.POST.get('last_name')
        worker.tel = request.POST.get('tel')
        worker.position = request.POST.get('position')
        if request.FILES.get('image'):
            worker.image = request.FILES.get('image')
        worker.save()
        messages.success(request, 'Muvafaqiyatli o\'zgartirildi')

    return render(request, 'dashboard/worker/edit.html', {'worker': worker})


@login_required(login_url='dashboard:login')
def worker_delete(request, id):
    """xodimni uchirish"""
    worker = models.Worker.objects.get(id=id)
    worker.delete()
    messages.success(request, 'hodim muvafaqiyatli o\'chirildi')
    return redirect('dashboard:worker_list')


@login_required(login_url='dashboard:login')
def attendance_list(request):
    """davomatlar ro'yxati"""
    workers = models.Worker.objects.all()
    worker_id = request.GET.get('worker_id')
    if worker_id:
        filter_items = {}
        for key, value in request.GET.items():
            if value and not value == '0':
                if key == 'start_date':
                    key = 'come_time__gte'
                elif key == 'end_date':
                    key = 'come_time__lte'
                filter_items[key] = value
        attendance = models.Attendance.objects.filter(**filter_items)
    else:
        attendance = models.Attendance.objects.all()
    context = {
        'attendance': attendance,
        'workers': workers,
    }
    return render(request, 'dashboard/attendance/list.html', context)


# -------------Profile update-----------------------
@login_required(login_url='dashboard:login')
def profile_update(request):
    """profilnni tahrirlash"""
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        if request.POST.get('email'):
            user.email = request.POST.get('email')
        user.save()
        messages.success(request, 'Muvafaqiyatli o\'zgartirildi')
    return render(request, 'dashboard/profile.html')


@login_required(login_url='dashboard:login')
def edit_password(request):
    """parolni uzgartirish"""
    user = request.user
    password = request.POST.get('password')
    password_new = request.POST.get('password_new')
    password_conf = request.POST.get('password_conf')
    if user.check_password(password) and password_new == password_conf:
        user.set_password(password_new)
        user.save()
        return redirect('dashboard:profile_update')


# -------------Authendication------------------------
def log_in(request):
    """royxatdan o'tish"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user and user.is_staff:
            login(request, user)
            messages.success(request, 'Muvafaqiyatli kirildi !')
            return redirect('dashboard:index')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('dashboard:login')

    return render(request, 'dashboard/auth/login.html')


def log_out(request):
    """chiqish"""
    if request.method == "POST":
        logout(request)
        messages.success(request, 'logout succsessful')
        return redirect('dashboard:logout_page')


def logout_page(request):
    """logout page"""
    return render(request, 'dashboard/auth/logout.html')
