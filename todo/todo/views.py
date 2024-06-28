from asyncio import tasks
from django.shortcuts import render , redirect , get_object_or_404
from .models import TaskModel
from .forms import TaskForm

def index(request ):
    form =  TaskForm(request.GET or None)
    tasks = TaskModel.objects.filter(status = False)
    return render(request, template_name='index.html' , context={'form': form , 'tasks1':tasks })
    
def create_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('/')
def ростов_на_DONу(request, pk):
    obj=get_object_or_404(TaskModel, id=pk)
    obj.status=True
    obj.save()
    return redirect('/')
    
    
    

# Create your views here.
