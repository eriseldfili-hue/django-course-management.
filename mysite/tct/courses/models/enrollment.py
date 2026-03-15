from django.db import models


class Enrollment(models.Model):

    STATUS_CHOICES = [
        ("active", "Active"),
        ("completed", "Completed"),
        ("dropped", "Dropped"),
        ("draft", "Draft"),
    ]
