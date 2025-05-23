from django.db import models

# portfolio/models.py

from django.db import models

class About(models.Model):
    content = models.TextField()

class TechStack(models.Model):
    category = models.CharField(max_length=50)  # e.g., Frontend, Backend
    stack = models.TextField()  # list or description

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    live_demo = models.URLField(blank=True, null=True)
    tech_used = models.CharField(max_length=255)

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

class SocialLink(models.Model):
    platform = models.CharField(max_length=50)  # e.g., "LinkedIn", "GitHub"
    url = models.URLField()
    icon = models.CharField(max_length=50, blank=True)  # Optional: e.g., "fa-linkedin"

    def __str__(self):
        return f"{self.platform}: {self.url}"
