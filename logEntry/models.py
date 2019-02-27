from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class Project(models.Model):
    project_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.project_name)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.project_name


LOCATION_CHOICE = (
        ('Inside', 'Inside'),
        ('Outside', 'Outside'),
)


class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_date = models.DateField()
    location = models.CharField(max_length=100,
                                choices=LOCATION_CHOICE,
                                default='Inside')
    detail = models.TextField()
    working_hour = models.FloatField(max_length=20)
    is_cod = models.BooleanField(default=False)
    note = models.TextField()
    # slug = models.SlugField(unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('entry:entry-detail', kwargs={'pk': self.pk})

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = slugify(self.user.username)
    #     super(Entry, self).save(*args, **kwargs)

    def __str__(self):
        return self.project.project_name
