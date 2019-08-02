from django.http import HttpResponse
from django.db import models
from .models import TaskStatuses, Task


def index(request):
    queryset = Task.objects.filter(created__gte='2019-04-01', created__lt='2019-09-01').annotate(Checked=models.Subquery(TaskStatuses.objects.annotate(max_datetime=models.Max('created')).filter(task_id=models.OuterRef('id'), status_type=3).values('max_datetime'), output_field=models.DateTimeField())).values('created', 'description', 'Checked')
    queryset2 = Task.objects.annotate(task_on_approve=models.Subquery(TaskStatuses.objects.annotate(max_created_date=models.Max('created')).filter(task_id=models.OuterRef('pk'),status_type=3).values('max_created_date'),output_field=models.DateTimeField())).filter(created__gte='2019-04-01', created__lt='2029-05-01').values('created', 'description', 'task_on_approve')
    print(queryset.query)
    print(queryset2.query)
    return HttpResponse(queryset)