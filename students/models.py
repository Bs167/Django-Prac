from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    # The ForeignKey ensures each note belongs strictly to the logged-in user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title