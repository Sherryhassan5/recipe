from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class recipe(models.Model):
    recipe_title = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_img = models.ImageField(upload_to='data/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.recipe_title