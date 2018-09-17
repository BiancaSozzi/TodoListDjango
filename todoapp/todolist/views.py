from django.shortcuts import render, redirect
from .models import TodoList, Priority, State


def index(request):  # the index view
    todos = TodoList.objects.all()  # quering all todos with the object manager
    priorities = Priority.objects.all()
    states = State.objects.all()
    if request.method == "POST":  # checking if the request method is a POST
        if "taskAdd" in request.POST:  # checking if there is a request to add a todo
            title = request.POST["title"]
            description = request.POST["description"]  # title
            priority = request.POST["priority_select"]  # category
            Todo = TodoList(title=title, content=description,
                            priority=Priority.objects.get(name=priority),
                            state=State.objects.get(name="Pending"))
            Todo.save()  # saving the todo
            return redirect("/")  # reloading the page
        if "taskDelete" in request.POST:  # checking if there is a request to delete a todo
            # checked todos to be deleted
            checkedlist = request.POST["checkedbox"]
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id))  # getting todo id
                todo.delete()  # deleting todo
    return render(request, "index.html", {"todos": todos, "priorities": priorities, "states": states})
