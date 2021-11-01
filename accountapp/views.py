from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

# 회원가입
def create(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],)
            auth.login(request, user)
            print('회원가입에 성공하였습니다.')
            return redirect('accountapp:login')
        else:
            print('회원가입에 실패하였습니다.')
            return render(request, 'accountapp/create.html')
    return render(request, 'accountapp/create.html')

# 메인
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print('로그인에 성공하였습니다.')
            return redirect('locationapp:main') # 로그인이 성공하였을 경우 PM 위치로 연결
        else:
            print('로그인에 실패하였습니다.')
            return render(request, 'accountapp/main.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accountapp/main.html')

# 로그아웃
@login_required
def logout(request):
    auth.logout(request)
    print('로그아웃 되었습니다.')
    return redirect('accountapp:login')







