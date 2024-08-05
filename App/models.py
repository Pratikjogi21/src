from django.db import models
from datetime import datetime

class Note(models.Model):
    notetitle = models.CharField(max_length=25)
    notedescr = models.CharField(max_length=500)
    date = models.DateField(default=datetime.now().date())

    class Meta:
        db_table= "NOTE"