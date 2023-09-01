from django.shortcuts import render
from .models import Author, Address, Student, Members, Book, BookIssued, BookReturned, RequestedBooks, Document
from .serializers import AuthorSerializer, AddressSerializer, StudentSerializer, MemberSerializer, BookSerializer, BookIssuedSerializer, BookReturnedSerializer, UserSerializer, RequestedBooksSerializer, DocumentSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 8

class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class MemberView(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookPaginationView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = StandardResultsSetPagination


class BookIssuedView(viewsets.ModelViewSet):
    queryset = BookIssued.objects.all()
    serializer_class = BookIssuedSerializer

class BookReturnedView(viewsets.ModelViewSet):
    queryset = BookReturned.objects.all()
    serializer_class = BookReturnedSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RequestedBooksView(viewsets.ModelViewSet):
    queryset = RequestedBooks.objects.all()
    serializer_class = RequestedBooksSerializer

class DocumentView(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
