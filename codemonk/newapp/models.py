from django.db import models


# Create your models here.

# Creating paragraph model
class Paragraphs(models.Model):
    para_id = models.CharField(max_length=20, primary_key=True)
    para_text = models.TextField()


class wordmap(models.Model):
    word = models.CharField(max_length=20)
    para_id = models.ForeignKey(Paragraphs, on_delete=models.CASCADE)
