from django.db import models
from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title

class Gadget(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='gadgets/')
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title

class Latest(models.Model):  # Model nomi 'Latest'
    CATEGORY_CHOICES = [
        ('france', 'France'),
        ('memes', 'Memes'),
        ('tech', 'Technology'),
        ('politics', 'Politics'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='latest_images/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    author = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    box = models.CharField(max_length=50, blank=True)
    descrepti = models.TextField(null=True)
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})  # post_detail - URL nomi
