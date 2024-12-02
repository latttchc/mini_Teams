from django.db import models
from accounts.models import User

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'<{self.user.account_id}>'

class Message(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)  
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message:id {self.id}, {self.title}>'

    class Meta:
        ordering = ('pub_date',)
