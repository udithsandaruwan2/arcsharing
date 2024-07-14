from django.db import models
from django.utils.text import slugify
import uuid

def upload_to(instance, filename):
    return f'{instance.id}/{filename}'

class UploadedFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to=upload_to)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.file)
