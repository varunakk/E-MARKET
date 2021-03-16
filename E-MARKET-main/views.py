from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Question, table,seller,verif,farmer,corporate,cart
from django.template import loader
from django.core.mail import send_mail,BadHeaderError
import smtplib
import string
from polls.forms import sellerform

def signupfarm(request):
    if request.GET:
        na=request.GET
        if "cancel" in na:
            return render(request,'polls/signupfarm.html')
        name=na['who']
        pswrd=na['pass']
        phn=na['phn']
        ema=na['email']
        ident=na['ident']
        if len(name)==0 or len(pswrd)==0 or len(ident)==0 or len(phn)!=10:
            return render(request,'polls/signupfarm.html',{'mssg':"enter the details"})

        try:
            obj=verif.objects.get(user_name=name)
        except:
            return render(request,'polls/signupfarm.html',{'mssg':"invalid farmer id"})

        if obj.user_id==ident:
            t=farmer(user_name=name,password=pswrd,email=ema,phn=phn)
            t.save()
            return HttpResponseRedirect('/polls/loginfarm/')
                #render(request,'polls/succsesful.html')
        else:
            return render(request,'polls/signupfarm.html',{'mssg':"invalid farmer id"})
    else:    
        return render(request,'polls/signupfarm.html')

def signup(request):
    # if no data is sent is showing error see that
    #print(name)
    #print(request.POST)
    if request.GET:
        na=request.GET
        if "cancel" in na:
            return render(request,'polls/signup.html')
        name=na['who']
        pswrd=na['pass']
        phn=na['phn']
        ema=na['email']
            #print("entered buyyer email==",ema)
        if len(name)==0 or len(pswrd)==0 or len(ema)==0 or len(phn)!=10:
            #print("in if  ")
            return render(request,'polls/signup.html',{'mssg':"enter the details"})
            #print("out of if")
        t=table(user_name=name,password=pswrd,email=ema,phn=phn)
        t.save()
        return HttpResponseRedirect('/polls/login/')
        #render(request,'polls/succsesful.html')
    else:    
        return render(request,'polls/signup.html')
def buyerbuy(request):
    return render(request,'polls/buyerbuy.html')

def buyAndSell(request):
    #print("hello")
    return render(request,'polls/buyAndSell.html')
  import string

def send_email(request):
    username = "wadgrp2@gmail.com"
    password = "@grp#2$wad"
    smtp_server = "smtp.gmail.com:587"
    email_from = "wadgrp2@gmail.com"
    email_to = "varunakrishna.k19@iiits.in"

    ########## this email body is creating major problem #######

    email_body ="From: "+email_from+"To: "+ email_to+"Subject: This is my subject line sent from django!"+""+"This is my message that can also have a info"+"\r\n"

    #str.join((
    #"From: %s" % email_from,
    #"To: %s" % email_to,
    #"Subject: This is my subject line sent from django!",
    #"",
    #"This is my message that can also have a %s" % ("info"
    #),), "\r\n"
    #)
    
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password,initial_response_ok=True)
    server.sendmail(email_from, email_to, email_body)
    server.quit()
    return render(request,'polls/succsesful.html')

def buyfarm(request):
    if request.GET:
        na=request.GET
        obj=corporate.objects.order_by().values('good_name').distinct()
        #it="crop"
        if 'crop' in na:
            food=na['crop']
            print(food) 
            global it
            it=food
            print(it)
            obj=corporate.objects.filter(good_name=food)
            o=[]
            for i in obj:
                a=corporate.objects.get(company=i)
                o.append(a)
            obj=corporate.objects.order_by().values('good_name').distinct()
            return render(request,'polls/buyfarm.html',{'obj':o,'item':obj,'crop_nm':food})
        else:
            if 'seller' not in na  or 'city' not in na or 'phn' not in na:
                return render(request,'polls/buyfarm.html',{'item':obj,'mssg':"enter the details"})   
            sell=na['seller']
            name=na['who']
            city=na['city']
            phn=na['phn']
            email=na['email']
            #global it
            print(it)
            #print(na['cr'])
            #it=na['cr']
            #it="item"
            if len(sell)==0 or len(city)==0 or len(phn)!=10:
                return render(request,'polls/buyfarm.html',{'item':obj,'mssg':"enter the details"})
            if 'cart' in na:
               
                c=cart(name=name,item=it,seller_name=sell)
                c.save()
                return render(request,'polls/buyfarm.html',{'item':obj,'mssg':"added to cart"})
            #'item':obj,
            return render(request,'polls/feedback.html',{'mssg':"succesful delivery will be there at your home"})
    else:
        obj=corporate.objects.order_by().values('good_name').distinct()
        #print(obj)
        return render(request,'polls/buyfarm.html',{'item':obj})
def home(request):
    return render(request,'polls/home.html')



def checkcart(request):
    print(nm)
    #global nm
    #nm="varuna krishna"
    obj=cart.objects.filter(name=nm)
    o=[]
    print(obj,o)       

    for i in obj:
        a=cart.objects.get(name=i)
        o.append(a)
    #obj=cart.objects.order_by().values('item').distinct()
    print(obj,o)       
    for i in o:
        print(i.item)
    return render(request,'polls/choutcart.html',{'name':nm,'obj':o})
 def buy(request):
    if request.GET:
        na=request.GET
        food=na['crop']
        obj=seller.objects.filter(crop_name=food)
        o=[]
        for i in obj:
            a=seller.objects.get(user_name=i)
            o.append(a)
        obj=seller.objects.order_by().values('crop_name').distinct()
        return render(request,'polls/buyer.html',{'obj':o,'item':obj})
    else:
        obj=seller.objects.order_by().values('crop_name').distinct()
        return render(request,'polls/buyer.html',{'item':obj})

it="none"
  
def forgtpswrd(request):
    if request.GET:
        na=request.GET
        if "cancel" in na:
            return render(request,'polls/forgtpswrd.html')
        name=na['who']
        pswrd=na['pass']
        phn=na['phn']
        repass=na['repass']
        if len(name)==0 or len(pswrd)==0 or len(phn)==0 or len(repass)==0 :
            return render(request,'polls/forgtpswrd.html',{'mssg':"enter the details"})
        try:
            obj=table.objects.get(user_name=name)
        except:
            return render(request,'polls/forgtpswrd.html',{'mssg':"invalid user name"})

        if obj.phn==phn:
            if pswrd==repass:
                obj.password=pswrd
                obj.save()
                return HttpResponseRedirect('/polls/login/')
                # render(request,'polls/login.html',{'mssg':"password changed succesfully"})
            else:
                 return render(request,'polls/forgtpswrd.html',{'mssg':"re enter password should be same as new password"})

        else:
            return render(request,'polls/forgtpswrd.html',{'mssg':"phone number not matched"})
    else:
        return render(request,'polls/forgtpswrd.html')
def loginfarm(request):
    if request.GET:
        na=request.GET
        if "cancel" in na:
            return render(request,'polls/loginfarm.html')
        
        name=na['who']
        pswrd=na['pass']
        global nm
        print(nm)
        nm=name
        #nm=name
        print(nm)
        try:
            obj=farmer.objects.get(user_name=name)
        except:
            return render(request,'polls/loginfarm.html',{'mssg':"invalid password or username"})
            
        if obj.password == pswrd:
            return render(request,'polls/buyAndSell.html',{'name':name})
        else:
            return render(request,'polls/loginfarm.html',{'mssg':"invalid password or username"})
    else:
        return render(request,'polls/loginfarm.html')


def login(request):
    if request.GET:
        na=request.GET
        if "cancel" in na:
            return render(request,'polls/login.html')
        
        name=na['who']
        pswrd=na['pass']
        try:
            obj=table.objects.get(user_name=name)
        except:
            return render(request,'polls/login.html',{'mssg':"invalid password or username"})
            
        if obj.password == pswrd:
            return render(request,'polls/buyerbuy.html')
        else:
            return render(request,'polls/login.html',{'mssg':"invalid password or username"})
    else:
        return render(request,'polls/login.html')
