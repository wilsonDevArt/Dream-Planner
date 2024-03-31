from django.shortcuts import render, redirect
from .models import List_of_Dream, Steps_to_Concretize
from django.http import HttpResponseRedirect
from .forms import AddDreamForm, AddStepForm
from django.db.models import Sum
import datetime

from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
          form = UserCreationForm()  
          
    return render(request, 'dream_list/register_page.html',{'form':form})
    

def login_page(request): 
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
                
    context = {}
    return render(request, 'dream_list/login_page.html', context)


def logout_page(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login_page')    
def home(request):
    username = request.user.username 

    userid = User.objects.get(username=username)   
    list_dream = List_of_Dream.objects.filter(user=userid)
    return render(request, "dream_list/home.html", {'list_dream':list_dream})


@login_required(login_url='login_page')
def list_of_steps(request,foo):
    add_step = List_of_Dream.objects.get(dream=foo)
    list_steps= Steps_to_Concretize.objects.filter(dream=add_step)
    try:

        ##sum all steps schedule
        the_time = Steps_to_Concretize.objects.filter(dream=add_step).aggregate(the_time=Sum('time_line'))
        add_step.schedule = the_time["the_time"]
        add_step.save()
        
        return render(request, "dream_list/list_of_steps.html", {'add_step':add_step, 'list_steps': list_steps})
    except:
        add_step.schedule = datetime.timedelta(seconds=0)
        add_step.save()        
        return render(request, "dream_list/list_of_steps.html", {'add_step':add_step, 'list_steps': list_steps})
   
    
@login_required(login_url='login_page')    
def delete_step(request,pk):
    delete_it = Steps_to_Concretize.objects.get(id=pk)    
    delete_it.delete()
    
    # redirect one page back in Django
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


@login_required(login_url='login_page')
def delete_dream(request,pk):
    delete_it = List_of_Dream.objects.get(id=pk)
    delete_it.delete()
      
    # redirect one page back in Django
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


@login_required(login_url='login_page')
def add_new_dream(request): 

    username = request.user.username 
    userid = User.objects.get(username=username)
    userid = str(userid.id)

    submitted = False
    if request.method == "POST":
        form = AddDreamForm(request.POST, initial={'user': userid})
        
        if form.is_valid():
            form.save()
            s = request.POST.get("dream")
                                 
            url = reverse('list_of_steps', kwargs={'foo':s})
            return HttpResponseRedirect(url)

    else:
        form = AddDreamForm(request.POST or None, initial={ 'user':userid})
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'dream_list/add_new_dream.html', {'form':form, 'submitted': submitted})


@login_required(login_url='login_page')
def add_step(request,foo): 
    add_step = List_of_Dream.objects.get(dream=foo)    
    dream_name=str(add_step.dream)
    
    
    username = request.user.username
    #sum all steps schedule
    submitted = False 
    form = AddStepForm(request.POST or None, initial={ 'dream':add_step})
    if request.method == "POST":
        if form.is_valid():
            form.save()  
            url = reverse('list_of_steps', kwargs={'foo':dream_name})
            return HttpResponseRedirect(url)

    else:
        form = AddStepForm(request.POST or None, initial={ 'dream':add_step})
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'dream_list/add_step.html', {'form':form, 'submitted': submitted})


@login_required(login_url='login_page')    
def edit_step(request,pk):    
    update_it = Steps_to_Concretize.objects.get(id=pk)
    
    #take de dream model name
    dream_name=str(update_it.dream)
    form = AddStepForm(request.POST or None, instance = update_it)
    if form.is_valid():
        form.save()
        
        # go to list of steps path
        url = reverse('list_of_steps', kwargs={'foo':dream_name})
        return HttpResponseRedirect(url) 
    return render(request, 'dream_list/edit_step.html', {'update_it': update_it,'form':form})


@login_required(login_url='login_page')
def edit_dream(request,pk):
    
    update_it = List_of_Dream.objects.get(id=pk)
    
    form = AddDreamForm(request.POST or None, instance = update_it)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'dream_list/edit_dream.html', {'update_it': update_it,'form':form})

