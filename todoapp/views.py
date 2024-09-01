from django.shortcuts import render, redirect
from .models import Todo
from datetime import datetime
# Create your views here.

def index(request):
    if request.method == 'POST':
        text = request.POST.get("text").strip()
        if text:
            Todo.objects.create(text=text)
        return redirect('/')
    todo=Todo.objects.all()
    d = datetime.now()
    context={
        'todo': todo,
        'dt': d,
    }
    return render(request, 'todoapp/index.html', context)

def deleteTodo(request, id):
    Todo.objects.get(id=id).delete()
    return redirect('/')

def home(request):
    return render(request, 'todoapp/home.html')
def about(request):
    d = datetime.now()
    return render(request, 'todoapp/about.html', {'dt':d})
def footer(request):
    d = datetime.now()
    return render(request, 'todoapp/components/footer.html', {'dt':d})
