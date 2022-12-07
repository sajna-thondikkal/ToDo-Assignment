from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,DeleteView,DetailView,UpdateView

from .forms import Todoforms
from . models import task

# Create your views here.
class TaskListView(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'obj1'

class TaskDeleteView(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('covtask')

class TaskDetailView(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'i'
class TaskUpdateView(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'taski'
    fields = ('name','date','priority')
    def get_success_url(self):
        return reverse_lazy('covdetail',kwargs={'pk':self.object.id})



def task_home(request):
    obj1=task.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date= request.POST.get('date')
        obj = task(name=name,date=date,priority=priority)
        obj.save()
    return render(request, 'home.html',{'obj1':obj1})

def delete(request,taskid):
    task1=task.objects.get(id=taskid)
    if request.method=="POST":
        task1.delete()
        return redirect('/')
    return render(request,'delete.html',{'task1':task1})

def update(request,id):
    task2=task.objects.get(id=id)
    form=Todoforms(request.POST or None,instance=task2)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'task2':task2,'form':form})


