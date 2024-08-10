from django.shortcuts import render, redirect, get_object_or_404
from .models import Xodimlar, Davomat, Profile
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout 
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            error = "Foydalanuvchi nomi yoki parol noto'g'ri."
            return render(request, 'login.html', {'error': error})
    return render(request, 'login.html')


def logout_view(request):
    auth_logout(request)
    return redirect('login')


def is_admin(user):
    return user.is_authenticated and user.is_staff


def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if is_admin(request.user):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrapper

@login_required
@admin_required
def index(request):
    return render(request, 'index.html')


@login_required
@admin_required
def header_page(request):
    return render(request, 'header.html')


@login_required(login_url='login')
@admin_required
def xodim_list(request):
    xodimlar = Xodimlar.objects.all()
    return render(request, 'xodim_list.html', {'xodimlar': xodimlar})


@login_required(login_url='login')
@admin_required
def xodim_detail(request, pk):
    xodim = get_object_or_404(Xodimlar, pk=pk)
    return render(request, 'xodim_detail.html', {'xodim': xodim})


@login_required(login_url='login')
@admin_required
def xodim_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        lavozim = request.POST.get('lavozim')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        email = request.POST.get('email')
        
        Xodimlar.objects.create(
            first_name=first_name,
            last_name=last_name,
            age=age,
            lavozim=lavozim,
            phone=phone,
            address=address,
            email=email
        )
        return redirect('xodim_list')
    return render(request, 'xodim_create.html')


@login_required(login_url='login')
@admin_required
def xodim_update(request, pk):
    xodim = get_object_or_404(Xodimlar, pk=pk)
    if request.method == 'POST':
        xodim.first_name = request.POST.get('first_name')
        xodim.last_name = request.POST.get('last_name')
        xodim.age = request.POST.get('age')
        xodim.lavozim = request.POST.get('lavozim')
        xodim.phone = request.POST.get('phone')
        xodim.address = request.POST.get('address')
        xodim.email = request.POST.get('email')
        xodim.save()
        return redirect('xodim_detail', pk=xodim.pk)
    return render(request, 'xodim_update.html', {'xodim': xodim})


@login_required(login_url='login')
@admin_required
def xodim_delete(request, pk):
    xodim = get_object_or_404(Xodimlar, pk=pk)
    if request.method == 'POST':
        xodim.delete()
        return redirect('xodim_list')
    return render(request, 'xodim_delete.html', {'xodim': xodim})


@login_required(login_url='login')
@admin_required
def davomat(request):
    if request.method == 'POST':
        xodim_id = request.POST.get('xodim_id')
        if xodim_id:
            xodim = Xodimlar.objects.get(pk=xodim_id)
            Davomat.objects.create(xodim=xodim)
            xodim.save()
    davomats = Davomat.objects.all()
    xodimlar = Xodimlar.objects.all()
    return render(request, 'davomat.html', {'kelgan_xodimlar': xodimlar, 'davomats':davomats})


@login_required(login_url='login')
@admin_required
def profile(request):
    return render(request, 'profile.html')


@login_required(login_url='login')
@admin_required
def profile_update(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.phone = phone
        user.address = address
        user.username = username
        if password:
            user.set_password(password)
        user.save()
        profile, created = Profile.objects.get_or_create(user=user)
        profile.phone = phone
        profile.address = address
        profile.save()
        
        return redirect('login')
    return render(request, 'profil_update.html')

