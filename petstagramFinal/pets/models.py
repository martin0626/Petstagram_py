from django.db import models

from petstagramFinal.accounts.models import UserProfile


class Pet(models.Model):

    TYPE_CHOICE_DOG = 'Dog'
    TYPE_CHOICE_CAT = 'Cat'
    TYPE_CHOICE_PARROT = 'Parrot'

    TYPE_CHOICES = (
        (TYPE_CHOICE_DOG, 'Dog'),
        (TYPE_CHOICE_CAT, "Cat"),
        (TYPE_CHOICE_PARROT, 'Parrot')
    )

    type = models.CharField(
        max_length=6,
        choices=TYPE_CHOICES
    )
    name = models.CharField(max_length=6)
    age = models.PositiveIntegerField()
    description = models.TextField()
    image_url = models.ImageField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)


class Comment(models.Model):
    text = models.TextField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
