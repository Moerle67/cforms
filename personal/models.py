from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField("Name", max_length=50)
    vorname = models.CharField("Vorname", max_length=50)
    eintritt = models.DateField("Eintritt", auto_now=False, auto_now_add=True)
    update = models.DateField("Update", auto_now=True, auto_now_add=False)
    comment = models.TextField("Kommentar", blank=True, null=True)
    wertung = models.IntegerField("Wertung")
    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Personen"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Person_detail", kwargs={"pk": self.pk})

