from django.db import models

class Gender(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'


class Books(models.Model):
    
    name = models.CharField(max_length=255)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    qtd_pages = models.IntegerField()
    cover = models.ImageField(blank=False)
    author = models.CharField(max_length=255)
    qtd_books = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'