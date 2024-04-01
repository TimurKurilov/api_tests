from django.db import models

class UserDataUsername(models.Model):
    username = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.username}'

class Userdata(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.OneToOneField(UserDataUsername, related_name="usernamedata", on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.first_name}, {self.last_name}'