from django.db import models

class Car(models.Model):
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.brand} ({self.year})"

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)  # Cambiado de TextField a CharField
    birth_date = models.DateField()

    def __str__(self):  # Faltaba espacio entre def y __str__
        return self.name

class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    website = models.URLField()
    biography = models.TextField(max_length=500)   

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name="books")  # related_name más descriptivo

    def __str__(self):
        return self.title