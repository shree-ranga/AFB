from django.db import models
from django.conf import settings


class TrackingModel(models.Model):
    """
    Abstract base model
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# task model
class Task(TrackingModel):
    """
    Task model
    """

    PRIORITY_CHOICES = [("H", "High"), ("M", "Medium"), ("L", "Low")]
    COMPLETED_CHOICES = [("Y", "Yes"), ("N", "No")]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="tasks", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500, blank=True)
    due_date = models.DateField(null=True)
    labels = models.CharField(max_length=30, blank=True)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, blank=True)
    completed = models.CharField(max_length=3, choices=COMPLETED_CHOICES, default="N")

    class Meta:
        # default ordering is reverse chronological order
        ordering = ("-created_at",)

    def __str__(self):
        # String representation of the task by its title.
        return f"Task - {self.title}"
