from django.db import models

# Create your models here.


class FrontUser(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return f"<FrontUser:({self.id},{self.username},{self.userextension})>"


class UserExtension(models.Model):
    school = models.CharField(max_length=100)
    user = models.OneToOneField("FrontUser", on_delete=models.CASCADE,
                                related_name="extension")

    def __str__(self):
        return f"<UserExtension:({self.id},{self.school},{self.user.id})>"
