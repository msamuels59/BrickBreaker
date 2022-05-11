from django.db import models

# Create your models here
class Score(models.Model):
    points = models.IntegerField()
    player = models.CharField(max_length=5, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.player} SCORE: {self.points} @ {self.timestamp}'

    @property
    def calculate_high_score(self):
        pass