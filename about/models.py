from django.db import models

# Create your models here.
class Bio(models.Model):
    description = models.TextField(null=True,  blank=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='about/bio_images', null=True,  blank=True)
    last_update = models.DateField(null=True, auto_now_add=True,  blank=True)
    
    def __str__(self):
        return self.title

class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"