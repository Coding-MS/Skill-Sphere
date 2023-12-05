from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from djrichtextfield.models import RichTextField

class workboard (models.Model):
    user = models.ForeignKey(User, related_name="task_owner", on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=75, null=False, blank=False)
    note = RichTextField(max_length=500, null=False, blank=False)
    slug = models.SlugField(unique=True, blank=True)
    due_date = models.DateField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} | {self.due_date.strftime('%d/%m/%Y') if self.due_date else 'No due date'}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

        