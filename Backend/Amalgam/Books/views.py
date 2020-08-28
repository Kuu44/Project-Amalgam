from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import addBooksForm, commentForm
from .models import Books, Comment
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q
# Create your views here.


# def index(request):
#     books = addBooksForm()
#     if request.method == 'POST':
#         books = addBooksForm(request.POST, request.FILES)
#         if books.is_valid():
#             stock = books.save(commit=False)
#             stock.user = request.user
#             stock.save()
#             return HttpResponse('Hi')
#     context = {
#         'form': books
#     }
#     return render(request, 'Books/index.html', context)
# <form action='{% url 'index' %}' enctype="multipart/form-data" method="post">
#   {%csrf_token%}
# {{form.isbn}}
# <br />
# {{form.book_name}}
# <br />
# {{form.original_price}}
# <br />
# {{form.offered_price}}
# <br />
# {{form.description}}
# <br />
# {{form.category}}
# <br />
# <br />
# <br />
# {{form.image}}
# <br />
# <button type="submit">Submit</button>
# </form>

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
