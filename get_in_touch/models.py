from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Bio(models.Model):
    """
    Model for the bio of the website.
    """
    description = models.TextField(null=True,  blank=True)
    title = models.CharField(max_length=255)
    image = CloudinaryField('image', null=True, blank=True,
                            default='placeholder')
    last_update = models.DateField(null=True, auto_now_add=True,  blank=True)

    @property
    def image_url(self):
        if self.image:
            return self.image.build_url(secure=True)
        return None

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    """
    Model for collaboration requests.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
