from django.shortcuts import render
def cal(request):
    return render(request,'cal_app/cal.html')