from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from djrichtextfield.models import RichTextField

class Workboard (models.Model):
    SPECIALITIES = [
        ('Plumber', 'Plumber'),
        ('Caterers', 'Caterers'),
        ('Seamstress', 'Seamstress'),
        ('Hairdresser', 'Hairdresser'),
        ('Technical Repairs', 'Technical Repairs'),
        ('Legal', 'Legal'),
        ('Painter', 'Painter'),
        ('Other', 'Other'),
    ]
    user = models.ForeignKey(User, related_name="task_owner", on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=75, null=False, blank=False)
    note = RichTextField(max_length=500, null=False, blank=False)
    slug = models.SlugField(unique=True, blank=True)
    due_date = models.DateField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    speciality = models.CharField(choices=SPECIALITIES, null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    special_requests = models.TextField(null=False, blank=False)


    def __str__(self):
        return f"{self.title} | {self.due_date.strftime('%d/%m/%Y') if self.due_date else 'No due date'}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

        