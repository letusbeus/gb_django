from django.db import models


class GameModel(models.Model):
    result = models.CharField(max_length=10)
    played = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Result: {self.result}, played at: {self.played}'

