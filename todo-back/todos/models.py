from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.


# 유저는 커스텀 유저를 사용(default 유저를 사용하더라도 장고에서는 커스텀 유저를 사용하라고 권장.)
# 디폴트를 사용하더라도 커스텀 유저를 사용하는 번거로움이 있음.
class User(AbstractUser):
    pass

class Todo(models.Model):
    # user.todo_set.all()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title