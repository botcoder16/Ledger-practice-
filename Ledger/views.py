from django.shortcuts import render,HttpResponse,redirect
from Ledger.models import Transaction,Group
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
# make sender also a user
# add,remove user from group
# calculate function
def home(request):
    l=[]
    allTransactions = Transaction.objects.all()
    for transaction in allTransactions:
        if str(request.user)==transaction.sender_name or request.user==transaction.reciever_name:
            l.append(transaction)
    context={'transactions' : l}
    return render(request,'home.html',context)
def history(request):
    l=[]
    allTransactions = Transaction.objects.all()
    for transaction in allTransactions:
        if str(request.user)==transaction.sender_name or request.user==transaction.reciever_name:
            l.append(transaction)
    context={'transactions' : l}
    return render(request,'history.html',context)
def add_transaction(request):
    context={'user':request.user}
    if request.method=="POST":
        Sender_name=request.user
        tempReciever_name=request.POST['lender name']
        Reciever_name=User.objects.get(username=tempReciever_name)
        tempgroupId=request.POST['groupId']
        groupId=Group.objects.get(groupId=tempgroupId)
        amount=request.POST['amount']
        ins=Transaction(sender_name=Sender_name,reciever_name=Reciever_name,amount=amount,groupId=groupId)
        if User.objects.filter(username=Reciever_name).exists():
            if request.user in groupId.users.all() and Reciever_name in groupId.users.all():
                if  amount!=0 and amount!="":
                    ins.save()
                    messages.success(request,"Transaction Added")
                else:
                    messages.error(request,"Amount value not accepted")
            else:
                messages.error(request,"One of the User is not a member of this group")
        else:
            messages.error(request,"User doesn't exist")
    return render(request,'add_transaction.html',context)
def handle_signup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        Cpassword=request.POST['Cpassword']
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists")
            return redirect('home')
        if not username.isalnum():
            messages.error(request,"Username must be alphanumeric")
            return redirect('home')
        if password==Cpassword:
            myuser=User.objects.create_user(username,email,password)
            myuser.first_name=fname
            myuser.last_name=lname
            myuser.save()
            messages.success(request,"USER CREATED")
            return redirect('home')
    else:
        return HttpResponse('404 - NOT FOUND')
def handle_login(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged IN")
            return redirect('home')
        else:
            messages.error(request,"Wrong Username/Password")
            return redirect('home')
    return HttpResponse("login")
def handle_logout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('/')
def group(request):
    context={'users':request.user}
    if request.method=="POST":
        groupName=request.POST['Gname']
        FirstUser=request.user
        SecondUser=request.POST['user2']
        u2=User.objects.get(username=SecondUser)
        g1=Group(groupName=groupName,no_of_users=2)
        if User.objects.filter(username=SecondUser).exists():
            g1.save()
            g1.users.add(FirstUser,u2)
            messages.success(request,"Successfully Created Group")
            return redirect('show_group')
        else:
            messages.error(request,"User doesn't exist")
    return render(request,'group.html',context)
def show_groups(request):
    l=[]
    allgroup=Group.objects.all()
    for group in allgroup:
        if request.user in group.users.all():
            l.append(group)
    context={'groups':l}
    return render(request,'group.html',context)
def group_history(request,slug):
    l=[]
    #if request.method=="POST":
    #no_of_users=request.GET['number']
    allTransactions = Transaction.objects.all()
    for transaction in allTransactions:
        Id=str(transaction.groupId).split(" -> ")
        if str(slug)==Id[0]:
            l.append(transaction)
    context={'transactions' : l}
    return render(request,'group_history.html',context)
def calculate(request):
    if request.method=='POST':
        groupId=request.POST['groupId']
        url='group_history/'+str(groupId)
        allTransactions = Transaction.objects.all()
        def getMin(arr):
            minInd = 0
            for i in range(0,len(arr)):
                if (arr[i] < arr[minInd]):
                    minInd = i
            return minInd

        def getMax(arr):
            MaxInd=0
            for i in range(0,len(arr)):
                if (arr[i]>arr[MaxInd]):
                    MaxInd=i
            return MaxInd

        def minof2(a,b):
            return a if a<b else b

        def minCashFlowRec(amount):
            mxcredit=getMax(amount) 
            mxdebit=getMin(amount)
            if(amount[mxcredit]==0 & amount[mxdebit]==0):
                return
            min=minof2(-amount[mxdebit],amount[mxcredit])
            amount[mxcredit] -=min
            amount[mxdebit] +=min
            
            print("Person ",mxcredit+1," pays ",min," to ",mxdebit+1," person")
            minCashFlowRec(amount)

        def minCashflow(graph):
            amount=[]
            for i in range(0,len(graph)):
                x=0
                for j in range(0,len(graph[0])):
                    x+=(graph[i][j]-graph[j][i])
                amount.append(x)
            minCashFlowRec(amount)
        
        graph=[]
        users={}
        for transaction in allTransactions:
            
            graph=[[0,1000,2000],[0,0,5000],[0,0,0]]
            print("lenght",len(graph)," ",len(graph[0]))
            minCashflow(graph)
        return redirect(url)
    return HttpResponse("group history with minimize")   