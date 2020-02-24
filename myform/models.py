from django.db import models
from django import forms
from django.forms import ModelForm


# Create your models here.
class UserForm(forms.Form):
    name = forms.CharField(label='name', max_length=30)
    age = forms.IntegerField(label='age')


TITLE_CHOICES = [
    ('MR', 'Mr'),
    ('MRS', 'Mrs'),
    ('MS', 'Ms')
]


class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']
