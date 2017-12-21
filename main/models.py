from django.contrib.auth.models import User
from django.db import models


class Pet(models.Model):
    PET_TYPES = (
        ('1', "Cat"),
        ('2', "Dog"),
    )
    name = models.CharField(max_length=200)
    picture = models.URLField(null=True, blank=True, default=None)
    birthday = models.DateField(null=True)
    type = models.CharField(choices=PET_TYPES, max_length=5)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name + ' - ' + self.get_type_display() + ' - Owner: ' + self.owner.username

