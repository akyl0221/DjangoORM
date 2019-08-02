from django.db import models


class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=False)
    cost = models.DecimalField(max_digits=10, decimal_places=1)


class TaskStatuses(models.Model):
    CREATED = 0
    ACCEPTED = 1
    REISSUED = 2
    CHECKED = 3
    FINISHED = 4

    types = (
        (CREATED, 'Created'),
        (ACCEPTED, 'Accepted'),
        (REISSUED, 'Reissued'),
        (CHECKED, 'Checked'),
        (FINISHED, 'Finished'),
    )
    created = models.DateTimeField(auto_now_add=True)
    task_id = models.IntegerField()
    status_type = models.PositiveIntegerField(choices=types, default=CREATED)

