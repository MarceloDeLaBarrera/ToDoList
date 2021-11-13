from django.urls import path
from django.views.generic.edit import FormView
from base_app.views import Login_View, TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, Register_View
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('accounts/register/', Register_View.as_view(), name='register'),
    path('accounts/login/', Login_View.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page="login"), name='logout'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create_task/', TaskCreate.as_view(), name='task_create'),
    path('update_task/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('delete_task/<int:pk>/', TaskDelete.as_view(), name='task_delete'), ]
