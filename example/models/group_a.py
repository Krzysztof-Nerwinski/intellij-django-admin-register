from django.db import models

# Create your models here.
class MyModel(models.Model):
    string_field = models.CharField(max_length=255)
    integer_field = models.IntegerField()
    boolean_field = models.BooleanField()
    date_field = models.DateField()

    class Meta:
        verbose_name = "My Model"
        verbose_name_plural = "My Models"