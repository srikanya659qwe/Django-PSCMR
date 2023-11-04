from django.shortcuts import render,redirect
from django.http import HttpResponse
from MyApp.models import Student

# Create your views here.

def ho(request):
	return HttpResponse("<h1>Hello World</h1>")

def he(request):
	return HttpResponse("<h2 style=color:maroon;background-color:blue;font-size:45px><center>welcome to django workshop</center></h2>")


def dynamic(request,a,b):
	return HttpResponse("<h2 style=background-color:skyblue;color:green;font-size:30px><center>My Rollnumber is:{} and My Name is:{}</center></h2>".format(a,b))

def temp(request):
	return render(request,'temp.html',{})

def table(request):
	return render(request,'table.html',{})

def inline(request):
	return render(request,'inline.html',{})

def internal(request):
	return render(request,'internal.html',{})

def external(request):
	if request.method=="POST":
		na=request.POST['uname']
		roll=request.POST['rnm']
		mb=request.POST['mbl']
		e=request.POST['em']
		ps=request.POST['psw']
		cps=request.POST['cpsw']

		return render(request,'details.html',{'n':na,'r':roll,'m':mb,'e':e,'p':ps,
			'cp':cps})

	return render(request,'external.html',{})

def boot(request):
	return render(request,'boot.html',{})

def offline(request):
	return render(request,'offline.html',{})

def insert(request):
	if request.method=="POST":
		na=request.POST['uname']
		roll=request.POST['rnm']
		ag=request.POST['age']
		mb=request.POST['mbl']
		e=request.POST['em']
		add=request.POST['addr']

		Student.objects.create(name=na,rollnum=roll,age=ag,mobile=mb,
			email=e,address=add)

		return redirect('/read')

	return render(request,'insert.html',{})


def read(request):
	data=Student.objects.all()
	return render(request,'read.html',{'info':data})


def update(request,id):
	data=Student.objects.get(id=id)
	if request.method=="POST":
		data.name=request.POST['uname']
		data.rollnum=request.POST['rnm']
		data.age=request.POST['age']
		data.mobile=request.POST['mbl']
		data.email=request.POST['em']
		data.address=request.POST['addr']
		data.save()

		return redirect('/read')
	return render(request,'update.html',{'data':data})

def delete(request,id):
	ob=Student.objects.get(id=id)
	if request.method=="POST":
		ob.delete()
		return redirect('/read')
	return render(request,'delete.html',{'info':ob})