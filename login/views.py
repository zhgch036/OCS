#coding:utf8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import User
from django.db.models import Q

# Create your views here.
def login(req):
	return render(req,'login/index.html')

def login_test(req):
	username = req.POST['username']
	password = req.POST['password']
	try:
		x = User.objects.get(Q(username=username)|Q(usermail=username))
	except User.DoesNotExist:
		return render(req,'login/error.html',{'error_msg':"用户不存在"})
	else:
		if x.password == password:
			return HttpResponse('<h1>hello welcome to django</h1>')
		else:
			return render(req,'login/error.html',{'error_msg':"用户密码错误"})
		
def register_test(req):
	username = req.POST['username']
	usermail = req.POST['usermail']
	password = req.POST['password']
	passwordc = req.POST['passwordc']
	try:
		x = User.objects.get(Q(username=username)|Q(usermail=usermail))
	except User.DoesNotExist:
		if password == passwordc:
			x = User()
			x.username = username
			x.usermail = usermail
			x.password = password
			x.save()
			return HttpResponse('<h1>hello welcome to django</h1>')
		else:
			return render(req,'login/error.html',{'error_msg':"两次密码输入不一致"})
	else:
		return render(req,'login/error.html',{'error_msg':"用户已存在"})
