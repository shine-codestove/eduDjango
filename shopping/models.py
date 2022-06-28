from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField()
    size = models.CharField(max_length=100)
    weight = models.IntegerField()
    image_url = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    #
    # def append_hello(self):
    #     return self.question_text + ' Hello'
