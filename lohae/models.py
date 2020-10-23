from django.db import models


<<<<<<< HEAD
# Create your models here.
=======
class Message(models.Model):
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
>>>>>>> ae62cd8ed675f11efd14b1300dc62b3fdc507ab0
