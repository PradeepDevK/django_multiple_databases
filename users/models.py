from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        using_db = kwargs.pop('using', 'users_db')
        super().save(*args, using=using_db, **kwargs)
        
    def delete(self, *args, **kwargs):
        using_db = kwargs.pop('using', 'users_db')
        super().save(*args, using=using_db, **kwargs)