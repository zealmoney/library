from rest_framework import serializers
from .models import Author, Address, Student, Members, Book, BookIssued, BookReturned, RequestedBooks, Document, AdminUser
from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'about', 'author_image')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('mobileno', 'line1', 'line2', 'city', 'state', 'zipcode')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'fullname', 'dob', 'address', 'username', 'password')

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ('firstname', 'lastname', 'member_id', 'address')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'pub_date', 'no_pages', 'book_lang', 'book_dim', 'book_isbn10', 'book_isbn13', 'book_image', 'author', 'available')

class BookIssuedSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookIssued
        fields = ('id', 'dateissued', 'book', 'student', 'stud_id')

class BookReturnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReturned
        fields = ('datereturned', 'book_id', 'book_name', 'student_id', 'student_name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class RequestedBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestedBooks
        fields = ('id', 'book_id', 'book_name', 'book_image', 'student_id', 'student_name', 'request_date', 'request_status')

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('book_id', 'overView', 'introduction', 'content')

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = ('username', 'password')
