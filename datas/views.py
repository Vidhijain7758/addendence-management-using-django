

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth import authenticate
from datas.forms import CustomUserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import ie,total
from .forms import LoginForm, ABC1,query
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg, Count, Max, Min, Sum
import datetime
import matplotlib.pyplot as plt
import datetime
from matplotlib.pyplot import figure, title, bar
import numpy as np
import mpld3
from django.views.generic import UpdateView
import matplotlib
from matplotlib import cm


# Create your views here.
def loginpage(request):
    myform = LoginForm(request.POST or None)
    if myform.is_valid():
        status = request.User.last_name
        usern = myform.cleaned_data.get("username")
        passw = myform.cleaned_data.get("password")

        user = authenticate(username=usern, password=passw)
        if user:
            return redirect("/profile")
        else:
            messages.error(request, "Error")



    return render(request, "datas/login.html", {"form": myform})


def register(request):
    if (request.method == 'POST'):
        form = CustomUserCreationForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('/login')
        else:
            messages.error(request, "Error")
    else:
        form = CustomUserCreationForm()

    args = {'form': form}
    return render(request, 'datas/signup.html', args)



def profile(request):
    if (request.method == 'POST'):
        form = ABC1(request.POST)
        if (form.is_valid()):






            day =form.cleaned_data['day']
            month = form.cleaned_data['month']
            year = form.cleaned_data['year']
            b = form.cleaned_data['shift_hours']




            g = ie.objects.all()

            c=0
            v=0
            if(len(g) != 0):
                if g.filter(day = day,month = month,year = year).exists():

                    obj = g.get(day = day, month = month, year = year)
                    obj.shift_hours = b
                    obj.project = form.cleaned_data['project']
                    obj.description = form.cleaned_data['description']

                    obj.save()

                    c= c+1




            if(c==0) :
                obj = ie()

                obj.month = form.cleaned_data['month']
                obj.year = form.cleaned_data['year']

                obj.day = form.cleaned_data['day']

                obj.shift_hours = form.cleaned_data['shift_hours']
                obj.description = form.cleaned_data['description']
                obj.project = form.cleaned_data['project']
                obj.save()
            else:
                c=0




            output = ie.objects.all().filter(month = month,year = year)
            monthly = helper(output)
            f = total.objects.all()
            if(len(f) !=0 ):
                if f.filter(year=year).exists():
                    obj4 = f.get(year=year)


                    if(month =='january'):
                        obj4.january = monthly
                    elif(month == 'febuary'):
                        obj4.feb = monthly
                    elif (month == 'march'):
                        obj4.march = monthly
                    elif (month == 'april'):
                        obj4.april = monthly
                    elif (month == 'may'):
                        obj4.may = monthly
                    elif (month == 'june'):
                        obj4.june = monthly
                    elif (month == 'july'):
                        obj4.july = monthly
                    elif (month == 'august'):
                        obj4.august = monthly
                    elif (month == 'september'):
                        obj4.september = monthly
                    elif (month == 'octuber'):
                        obj4.octuber = monthly
                    elif (month == 'november'):
                        obj4.november = monthly
                    elif (month == 'december'):
                        obj4.december = monthly
                    v= v+1
                    obj4.save()

            if(v==0):
                obj4 = total()
                obj4.year = year
                if (month == 'january'):
                    obj4.january=monthly
                elif (month == 'febuary'):
                    obj4.feb = monthly
                elif (month == 'march'):
                    obj4.march = monthly
                elif (month == 'april'):
                    obj4.april = monthly
                elif (month == 'may'):
                    obj4.may = monthly
                elif (month == 'june'):
                    obj4.june = monthly
                elif (month == 'july'):
                    obj4.july = monthly
                elif (month == 'august'):
                    obj4.august = monthly
                elif (month == 'september'):
                    obj4.september = monthly
                elif (month == 'octuber'):
                    obj4.octuber = monthly
                elif (month == 'november'):
                    obj4.november = monthly
                elif (month == 'december'):
                    obj4.december = monthly
                obj4.save()
            else:
                v=0
            return redirect('/profile/check')






        else:
            messages.error(request, "Error")
    else:
        form = ABC1()
        return render(request, 'datas/profile.html', {'form': form})

    args = {'user': request.user}
    return render(request, 'datas/profile.html', args)

def home(request):
    if request.method == 'POST':
        query_form = query(request.POST)
        if (query_form.is_valid()):
            clean_query = query_form.cleaned_data




            month = clean_query['month']
            year = clean_query['year']

            output = ie.objects.all().filter(month = month,year = year)
            monthly = helper(output)
            a=[]
            for i in output:
                ap = i.day
                a.append(ap)


            performance =[]
            for i in output:
                aq = i.shift_hours
                performance.append(aq)
            mpl_figure = figure(1, figsize=(12, 6))
            index = np.arange(len(a))
            plt.bar(index, performance)
            plt.xlabel('DAY', fontsize=20)
            plt.ylabel('WORKING HOURS', fontsize=20)
            plt.xticks(index, a, fontsize=20, rotation=30)
            plt.title('DAY WISE WORKING HOURS')
            fig_html = mpld3.fig_to_html(mpl_figure)
            plt.clf()
            return render(request,'datas/home1.html',{'output' :output,'monthly' :monthly,'month':month,'year':year,'figure' : fig_html})
            # return redirect('/result')

    else:
        query_form = query()
        return render(request, 'datas/home.html', {'query_form': query_form})


def home1(request):

            output = total.objects.all()


            return render(request,'datas/result.html',{'output' :output})
            # return redirect('/result')

def check(request):

    return render(request, 'datas/check.html')


def helper(output):
    monthly =0.0

    for i in output:
        monthly  = monthly + i.shift_hours

    return monthly
