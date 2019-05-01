from django.shortcuts import render
from .models import MyUser

def create_user(request):
    if request.method == "POST":
        name = request.POST.get('name')
        bdate = request.POST.get('bdate')
        age = request.POST.get('age')
        MyUser.objects.create(name=name,bdate=bdate,age=age)
    return render(request, 'users/create.html')


def user_list(request):
    users = MyUser.objects.all()
    return render(request, 'user/user_list.html', {"users":users})