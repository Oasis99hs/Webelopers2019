from django.db import models

# Create your models here.

# class User(models.Model):
#     first_name = models.CharField(max_length=25)
#     last_name = models.CharField(max_length=25)
#     username = models.CharField(max_length=25)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)
#
#     def __init__(self, first_name, last_name, username, email, password, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.first_name = first_name
#         self.last_name = last_name
#         self.username = username
#         self.email = email
#         self.password = password


class Course(models.Model):
    DAY_OF_THE_WEEK = (
        (0, 'Saturday'),
        (1, 'Sunday'),
        (2, 'Monday'),
        (3, 'Tuesday'),
        (4, 'Wednesday'),
    )

    department = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    course_number = models.IntegerField()
    group_number = models.IntegerField()
    teacher = models.CharField(max_length=25)
    start_time = models.TimeField()
    end_time = models.TimeField()
    first_day = models.IntegerField(choices=DAY_OF_THE_WEEK)
    second_day = models.IntegerField(choices=DAY_OF_THE_WEEK, null=True, blank=True)


