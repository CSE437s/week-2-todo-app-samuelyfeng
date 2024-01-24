from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages

# Create your views here.
def todo_list(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()
 
    page = {
        "forms": form,
        "list": item_list,
        "title": "Sam's TODO LIST",
    }
    return render(request, 'todo/todo_list.html', page)

def toggle_completed(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.completed = not item.completed  # Toggle the status
    item.save()
    messages.info(request, "To-do item status has been updated!")
    return redirect('todo')

#removing todo items if needed 
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "To-do item is removed!")
    return redirect('todo')