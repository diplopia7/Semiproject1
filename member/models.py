from datetime import datetime

from django.db import models

# Create your models here.
class Member(models.Model):
    id=models.AutoField(primary_key=True)
    userid=models.CharField(max_length=18,unique=True)
    passwd=models.CharField(max_length=18)
    name=models.CharField(max_length=5)
    email=models.CharField(max_length=100)
    regdate=models.DateTimeField(default=datetime.now)

    class Meta:
        db_table='member'
        ordering=['-regdate']

    def __str__(self):
        return self.userid