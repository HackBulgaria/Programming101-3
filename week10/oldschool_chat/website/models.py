from django.db import models
from django.contrib.auth.models import User

class ChatMessage(models.Model):
    message = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return "[{}]: {}: {} from {}".format(self.timestamp, self.id, self.message, self.user)
        
