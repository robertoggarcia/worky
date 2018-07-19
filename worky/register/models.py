from django.db import models


# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    token = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = "register"
        unique_together = ("name", "description")

    def __str__(self):
        return self.name