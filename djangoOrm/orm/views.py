from django.http import HttpResponse
from django.db import models
from .models import TaskStatuses, Task


def index(request):
    queryset = Task.objects.filter(created__gte='2019-04-01', created__lt='2019-09-01').annotate(Checked=models.Subquery(TaskStatuses.objects.annotate(max_datetime=models.Max('created')).filter(task_id=models.OuterRef('id'), status_type=3).values('max_datetime'), output_field=models.DateTimeField())).values('created', 'description', 'Checked')
    print(queryset.query)
    return HttpResponse(queryset)
