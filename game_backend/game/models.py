from django.contrib.auth.models import AbstractUser
from django.db import models

class Player(AbstractUser):
    # Add custom fields for your game
    score = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    coins = models.IntegerField(default=0)
    avatar = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.username