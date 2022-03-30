from django.db import models


class Atleta(models.Model):
    SEX = (('F', 'feminino'), ('M', 'masculino'))
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=1, choices=SEX, null=True, blank=True)
    team = models.CharField(max_length=255, null=True, blank=True)
    noc = models.CharField(max_length=3, null=True, blank=True)
    sport = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Evento(models.Model):
    MEDAL = (('Gold', 'Gold'), ('Silver', 'Silver'), ('Bronze', 'Bronze'))
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    games = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    season = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    event = models.CharField(max_length=255, null=True, blank=True)
    medal = models.CharField(max_length=6, choices=MEDAL, null=True, blank=True)

    def __str__(self):
        return self.event