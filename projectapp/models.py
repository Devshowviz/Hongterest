from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Project(models.Model):
    image = models.ImageField(upload_to='project/',null=False)
    title = models.CharField(max_length=20,null=False)
    description = models.CharField(max_length=200,null=True)
    writer = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, related_name='project')

    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} : {self.title}'
