from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import addBooksForm, commentForm
from .models import Books, Comment
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.


def add(request):
    books = addBooksForm()
    if request.method == 'POST':
        books = addBooksForm(request.POST, request.FILES)
        if books.is_valid():
            stock = books.save(commit=False)
            stock.user = request.user
            stock.save()
            return HttpResponseRedirect(reverse('show_book',args=[stock.id]))
    context = {
        'form': books
    }
    return render(request, 'Books/add.html', context)


@login_required
def show_book(request, pk):
    book = Books.objects.get(id=pk)
    try:
        comments = Comment.objects.filter(book=book)
    except Comment.DoesNotExist:
        comments = None
    commentform = commentForm()
    if request.method == 'POST':
        comment = commentForm(request.POST)
        if comment.is_valid():
            book = Books.objects.get(id=pk)
            temp = comment.save(commit=False)
            temp.book = book
            temp.user = request.user
            temp.save()
    context = {
        'book': book,
        'comments': comments,
        'commentform': commentform
    }
    return render(request, 'Books/view.html', context)


@login_required
def index(request):
    books = Books.objects.all()
    if request.method == 'POST':
        search = request.POST['search']
        filter_books = Books.objects.filter(Q(book_name__icontains=search))
        novel = []
        course = []
        for item in filter_books:
            if item.category == "1":
                novel.append(item)
            else:
                course.append(item)

        context = {
            'filter_books': {
                'novel': novel,
                'course': course
            },
            'books': books
        }
        return render(request, 'Books/searchresults.html', context)
    context = {
        'books': books
    }
    return render(request, 'Books/index.html', context)


@login_required
def home(request):
    return render(request, 'Books/home.html')
