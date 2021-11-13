from django.http.response import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from base_app.models import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.


class Login_View(LoginView):
    """From model LoginView, take all the fields for login an user, autogenerate a class_form, render it on login, access to them 
    and when submit the form and method is POST, the user will login and redirect (success_url) to tasklist.html (alias= tasks)"""

    fields = '__all__'
    template_name = "accounts/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("tasks")


class Register_View(FormView):
    """From model UserCreationForm, take all the fields for register an user, autogenerate a class_form, render it on register, access to them 
    and when submit the form and method is POST, the user will register and redirect (success_url) to tasklist.html (alias= tasks)"""

    template_name = "accounts/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        """It is necessary for save the user in database with the POST data of the UserCreationForm, so if the user is not none, then 
        make the login of he"""

        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register_View, self).form_valid(form)

    def get(self, *args, **kwargs):
        """Witouth this method, if user is autenticathed can access to register page, so with the method redirect to homepage when is autenthicated """

        if self.request.user.is_authenticated:
            # return redirect("tasks")
            return HttpResponse('<p>You already have an account. <a href="/">Go home</a></p>')
        return super(Register_View, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    """From model Task, get all the Tasks, render on tasklist, access to them 
    with a for loop on object_list or context object name 'tasks' """

    model = Task
    template_name = "tasklist.html"
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context["tasks"] = context["tasks"].filter(user=self.request.user)
        context["count"] = context["tasks"].filter(complete=False).count()

        if self.request.GET.get("searched-task"):
            searched_task = self.request.GET["searched-task"]
            context["tasks"] = context["tasks"].filter(
                title__icontains=searched_task)
            context["searched_task"] = searched_task

        return context

    def get_queryset(self):
        """Filter and shows only the task where the user if equals to the user request."""
        return Task.objects.filter(user=self.request.user)


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "view_task.html"
    context_object_name = "task"


class TaskCreate(LoginRequiredMixin, CreateView):
    """From model Task, take all the fields, autogenerate a class_form, render it on create_task, 
    and when submit the form and method is POST, redirect to tasklist.html (alias= tasks)"""

    model = Task
    fields = ["title", "description", "complete"]
    template_name = "create_task.html"
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    """From model Task, take all the fields, autogenerate a class_form, render it on update_task/id based on the create_task form, 
    and when submit the form and method is POST, update the task and redirect to tasklist.html (alias= tasks)"""
    model = Task
    fields = ["title", "description", "complete"]
    template_name = "create_task.html"
    success_url = reverse_lazy("tasks")

    def get_object(self, queryset=None):
        task = super(TaskUpdate, self).get_object(queryset)
        if task.user != self.request.user:
            raise Http404(("Permission Denied"))
        return task


class TaskDelete(LoginRequiredMixin, DeleteView):
    """From model Task, takes a id=pk and the object and render it on create_task, 
    and when submit the form and method is POST, delete the task and redirect to tasklist.html (alias= tasks)"""
    model = Task
    context_object_name = "task"
    template_name = "delete_task.html"
    success_url = reverse_lazy("tasks")

    def get_object(self, queryset=None):
        task = super(TaskDelete, self).get_object(queryset)
        if task.user != self.request.user:
            raise Http404(("Permission Denied"))
        return task
