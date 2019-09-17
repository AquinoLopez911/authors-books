from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"Book object: {self.id}: title is {self.title}, {self.description}"

    
class Author(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    notes = models.TextField()
    books = models.ManyToManyField(Book, related_name="publishers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"Author object: {self.id}: {self.f_name} {self.l_name}"