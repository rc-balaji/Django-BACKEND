# Generated by Django 5.0.7 on 2024-12-30 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practice',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='practice',
            name='title_id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='practiceoption',
            name='option1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='practiceoption',
            name='option2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='practiceoption',
            name='option3',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='practiceoption',
            name='option4',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='practiceoption',
            name='option_id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='practicequestion',
            name='question',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='practicequestion',
            name='question_id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subtopic',
            name='created_at',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='subtopic',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='subtopic',
            name='subtopic_id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='test',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='test',
            name='title_id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='testhistory',
            name='finished_at',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='testhistory',
            name='start_at',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='testhistory',
            name='status',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='testhistory',
            name='test_id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='testhistory',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='testhistory',
            name='type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='testoption',
            name='option1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='testoption',
            name='option2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='testoption',
            name='option3',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='testoption',
            name='option4',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='testoption',
            name='option_id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='testquestion',
            name='question',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='testquestion',
            name='question_id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='topic',
            name='created_at',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='topic',
            name='topic_id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usertopic',
            name='created_at',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='usertopic',
            name='created_by',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='usertopic',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
