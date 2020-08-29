from django.conf import settings
from django.db import models

# Create your models here.


class Books(models.Model):
    isbn = models.CharField(max_length=40)
    book_name = models.CharField(max_length=50)
    date_time = models.DateField(auto_now_add=True)
    original_price = models.IntegerField()
    offered_price = models.IntegerField()
    description = models.CharField(max_length=500)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='media', height_field=None,
                              width_field=None, max_length=100)
    choices = (
        ("1", "Novel"),
        ("2", "Course")
    )
    category = models.CharField(choices=choices, max_length=20, default=None)

    class Meta:
        ordering = ['book_name']

    def __str__(self):
        return f'{self.book_name}->{self.user}'

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
            super().save_model(request, obj, form, change)


class Comment(models.Model):
    book = models.ForeignKey(Books, null=True, blank=True, on_delete=models.SET_NULL)
    content = models.TextField(blank=True)
    date_time = models.DateField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.content}'

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
            super().save_model(request, obj, form, change)
