# Generated by Django 2.2.2 on 2019-07-31 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=1, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='TaskStatuses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status_type', models.PositiveIntegerField(choices=[(0, 'Created'), (1, 'Accepted'), (2, 'Reissued'), (3, 'Checked'), (4, 'Finished')], default=0)),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orm.Task')),
            ],
        ),
    ]
