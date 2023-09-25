from django.contrib import admin
from .models import Author, Address, Student, Members, Book, BookIssued, BookReturned, RequestedBooks, Document, AdminUser

admin.site.register({Author, Address, Student, Members, Book, BookIssued, BookReturned, RequestedBooks, Document, AdminUser})
