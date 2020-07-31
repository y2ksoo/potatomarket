from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    GENDER_MALE = "male"  # male은 DB에 저장되는 값
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),  # Male은 입력값, 웹페이지 표시되는 값
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    trustseller = models.BooleanField(('trust seller'), default=False)

    def __str__(self):
        return self.username
