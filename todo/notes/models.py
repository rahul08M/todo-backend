from django.db import models


class Tasks(models.Model):

    FREQUENCY = (
        ('daily', 'Daily'),
        ('weakly', 'Weakly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    )

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='user_notes', blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    archived = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    color = models.CharField(max_length=10, default="#ffffff")
    is_completed = models.BooleanField(default=False)

    notify = models.BooleanField(default=False)
    notify_on = models.DateTimeField(blank=True, null=True)
    frequency = models.CharField(choices=FREQUENCY, max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title
