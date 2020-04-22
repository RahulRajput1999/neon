from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import TodoList, Category
from login.models import *


@login_required(login_url='/login/')
@user_passes_test(lambda user: not user.is_staff, login_url='/staff/', redirect_field_name=None)
def index(request):  # the index view
    c = {}
    c.update(csrf(request))
    student = Student.objects.filter(student_id=request.user.username)
    todos = TodoList.objects.all()  # quering all todos with the object manager
    categories = Category.objects.all()  # getting all categories with object manager
    if request.method == "POST":  # checking if the request method is a POST
        if "taskAdd" in request.POST:  # checking if there is a request to add a todo
            title = request.POST["description"]  # title
            date = str(request.POST["date"])  # date
            category = request.POST["category_select"]  # category
            content = title + " -- " + date + " " + category  # content
            Todo = TodoList(title=title, content=content, due_date=date,
                            category=Category.objects.get(name=category))
            Todo.save()  # saving the todo
            return redirect("/todoApp")  # reloading the page
        if "taskDelete" in request.POST:  # checking if there is a request to delete a todo
            # checked todos to be deleted
            checkedlist = request.POST["checkedbox"]
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id))  # getting todo id
                todo.delete()  # deleting todo
    c['todos'] = todos
    c['categories'] = categories
    c['student'] = student[0]
    return render(request, "todo.html", c)
