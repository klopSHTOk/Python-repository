import uuid
from django.urls import reverse
from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter genre')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, help_text='Enter title')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1500, help_text='Enter summary')
    isbn = models.CharField('ISBN', max_length=13)
    genre = models.ManyToManyField(Genre, help_text='Choose your genre')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class BookInstance(models.Model):

    LOAN_STATUS = ( 
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m')

    class Meta:
        ordering = ["due_back"]
    
    def __str__(self):
        return '%s (%s)' % (self.id, self.book.title)

class Author(models.Model):
    fname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def get_absolute_id(self):
        return reverse('author-detail', args=[str(self.id)] )

    def __str__(self):
        return "%s, %s" % (self.surname, self.fname)