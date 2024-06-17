from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        using_db = kwargs.pop('using', 'books_db')
        super().save(*args, using=using_db, **kwargs)
        
    def delete(self, *args, **kwargs):
        using_db = kwargs.pop('using', 'books_db')
        super().delete(*args, using=using_db, **kwargs)