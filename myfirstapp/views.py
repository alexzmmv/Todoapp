from django.shortcuts import render,redirect
from .models import ToDOItem
from .forms import todoaddform

def todo(request):
    if request.method == 'POST':
        form = todoaddform(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            user_input_description = form.cleaned_data['user_input_description']
            # Save the user input to the database
            #if the object with the title is already in the database dont add it
            if not ToDOItem.objects.filter(title=user_input).exists():
                ToDOItem.objects.create(title=user_input, description=user_input_description)
            # After saving the form data, you may want to clear the form for the next input
            form = todoaddform()
    else:
        form = todoaddform()
    return render(request, 'todo.html', {'form': form, 'todos': ToDOItem.objects.all(),})

def delete_todo(request, todo_id):
    todo = ToDOItem.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo')

def status_todo(request, todo_id):
    todo = ToDOItem.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo')