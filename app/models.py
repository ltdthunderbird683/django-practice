from django.db import models

# Create your models here.
from django.contrib.auth.models import User 

class List(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Card(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


"""
models.Modelの__str__()関数により、管理画面に表示されるモデル内のデータを判別するための名前の定義ができる
https://office54.net/python/django/model-str-self
"""