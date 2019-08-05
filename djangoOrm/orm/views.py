from django.http import HttpResponse
from django.db import models
from datetime import date
from .models import TaskStatuses, Task


def index(request):
    start_date = date(2019, 4, 2)
    end_date = date(2019, 9, 2)
    sub_queryset = TaskStatuses.objects.annotate(max_datetime=models.Max('created'))\
        .filter(task_id=models.OuterRef('id'), status_type=3)\
        .values('max_datetime')
    queryset = Task.objects.filter(created__range=(start_date, end_date))\
        .annotate(Checked=models.Subquery(
            sub_queryset, output_field=models.DateTimeField()))\
        .values('created', 'description', 'Checked')
    print(queryset.query)
    return HttpResponse(queryset)
