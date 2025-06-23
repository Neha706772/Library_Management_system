from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
class Booklist_view(ListView):
    model = Book
    template_name = "library/list.html"
    context_object_name = 'list_object'

class BookDetails_view(DetailView):
    model = Book
    template_name = 'library/details.html'
    context_object_name = 'book'



class BookCreate_view(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/creates.html'
    context_object_name = 'home'
    success_url = reverse_lazy('home')


class BookUpdate_view(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'library/update.html'
    context_object_name = 'books'
    success_url = reverse_lazy('home')

class BookDelete_view(DeleteView):
    model = Book
    template_name = 'library/delete.html'
    success_url = reverse_lazy('home')
