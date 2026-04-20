import django.core.validators
import re
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='score',
            field=models.CharField(
                max_length=1024,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile(r'^\d+(?:,\d+)*\Z'),
                        message='Enter only digits separated by commas.',
                        code='invalid',
                    )
                ],
                verbose_name='Score',
            ),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='draft',
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text='If yes, the quiz is not displayed in the quiz list and can only be taken by users who can edit quizzes.',
                verbose_name='Draft',
            ),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='incorrect_questions',
            field=models.CharField(
                blank=True,
                max_length=1024,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile(r'^\d+(?:,\d+)*\Z'),
                        message='Enter only digits separated by commas.',
                        code='invalid',
                    )
                ],
                verbose_name='Incorrect questions',
            ),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='question_list',
            field=models.CharField(
                max_length=1024,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile(r'^\d+(?:,\d+)*\Z'),
                        message='Enter only digits separated by commas.',
                        code='invalid',
                    )
                ],
                verbose_name='Question List',
            ),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='question_order',
            field=models.CharField(
                max_length=1024,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile(r'^\d+(?:,\d+)*\Z'),
                        message='Enter only digits separated by commas.',
                        code='invalid',
                    )
                ],
                verbose_name='Question Order',
            ),
        ),
    ]
