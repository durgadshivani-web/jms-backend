from django.db import models


class Paper(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField()


class Review(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    comment = models.TextField()
