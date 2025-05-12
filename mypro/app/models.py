from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    task_name=models.CharField(max_length=40)
    description=models.TextField(default='')
    created_date=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    assigned_to=models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True)
    def __str__(self,):
        return f"Task -{self.id}-{self.task_name}"
