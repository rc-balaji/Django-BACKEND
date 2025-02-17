# Generated by Django 5.0.7 on 2025-01-03 08:08

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_practice_title_alter_practice_title_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practice',
            name='title_id',
            field=models.CharField(default=uuid.uuid4, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='practiceoption',
            name='option_id',
            field=models.CharField(default=uuid.uuid4, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='practicequestion',
            name='question_id',
            field=models.CharField(default=uuid.uuid4, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subtopic',
            name='subtopic_id',
            field=models.CharField(default=uuid.uuid4, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='test',
            name='title_id',
            field=models.CharField(default=uuid.uuid4, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='testhistory',
            name='test_id',
            field=models.CharField(default=uuid.uuid4, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='testoption',
            name='option_id',
            field=models.CharField(default=uuid.uuid4, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='testquestion',
            name='question_id',
            field=models.CharField(default=uuid.uuid4, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='topic',
            name='topic_id',
            field=models.CharField(default=uuid.uuid4, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(default=uuid.uuid4, max_length=255, primary_key=True, serialize=False),
        ),
    ]
