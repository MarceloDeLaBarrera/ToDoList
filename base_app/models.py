from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=220)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    # In this case, class Meta is ordering by complete or not complete the queryset objects 'tasks'. For descending order put "-" before complete.
    class Meta:
        verbose_name = "Task"
        db_table = "task"
        ordering = ['complete']
