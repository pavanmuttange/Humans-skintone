from django.db import models

# Create your models here.
class Image(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to="media")
    def __str__(self):
        # return self.image
        return self.caption



class Questions(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    ques = models.CharField(max_length=100)
    detail = models.TextField(default='Question')