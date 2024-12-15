from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=100) 
    recipient = models.CharField(max_length=100)  
    message = models.TextField()  

    def __str__(self):
        return f"From {self.sender} to {self.recipient}"

