from django import forms
from .models import Books, Comment
from django.forms import ModelForm


class addBooksForm(forms.ModelForm):
    isbn = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'ISBN'}),
        required=True, max_length=40)
    book_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Book Name'}),
        required=True, max_length=50)
    original_price = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Original Price'}),
        required=True)
    offered_price = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Offer price'}),
        required=True)
    description = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Description'}),
        required=True, max_length=100)
    image = forms.ImageField(required=True, max_length=100)
    choices = (
        ("1", "Novel"),
        ("2", "Course")
    )
    category = forms.ChoiceField(choices=choices, widget=forms.Select(), required=True)

    class Meta:
        model = Books
        fields = [
            'isbn',
            'book_name',
            'user',
            'original_price',
            'offered_price',
            'description',
            'image',
            'category'
        ]
        ordering = ['book_name']


class commentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'test'}),
        required=True, max_length=100)

    class Meta:
        model = Comment
        fields = [
            'content',
            'book',
        ]
        ordering = ['book']
