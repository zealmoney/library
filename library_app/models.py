from django.db import models

def author_upload_to(instance, filename):
    return 'author/{filename}'.format(filename=filename)

def book_upload_to(instance, filename):
    return 'book{filename}'.format(filename=filename)

class Author(models.Model):
    name = models.CharField(max_length=400, unique=True)
    about = models.TextField()
    author_image = models.ImageField(upload_to=author_upload_to)

    def __str__(self):
        return self.name
    
class Address(models.Model):
    mobileno = models.CharField(max_length=14, unique=True)
    line1 = models.TextField()
    line2 = models.TextField(default='null')
    city = models.TextField()
    state = models.TextField()
    zipcode = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Address'

    def __str__(self):
        return f'{self.city}, {self.state}'
    
class Student(models.Model):
    fullname = models.CharField(max_length=200, unique=True)
    dob = models.DateField()
    address = models.TextField()
    username = models.CharField(max_length=200, default="")
    password = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.fullname
    
class Members(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    member_id = models.CharField(max_length=200)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    
    class Meta:
        verbose_name_plural = 'Members'
    

class Book(models.Model):
    name = models.CharField(max_length=400)
    pub_date = models.DateField()
    no_pages = models.IntegerField()
    book_lang = models.CharField(max_length=400)
    book_dim = models.CharField(max_length=200)
    book_isbn10 = models.CharField(max_length=400, default=0)
    book_isbn13 = models.CharField(max_length=400, default=0)
    book_image = models.ImageField(upload_to=book_upload_to)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, to_field='name')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class BookIssued(models.Model):
    dateissued = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE, to_field='fullname')
    stud_id = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Books Issued'
    
    def __str__(self):
        bk = Book.objects.get(name = self.book.name)
        bk.available = False
        bk.save()
        return self.book.name

class BookReturned(models.Model):
    datereturned = models.DateTimeField(auto_now_add=True)
    book_id = models.IntegerField(default=0)
    book_name = models.CharField(max_length=255, default="")
    student_id = models.IntegerField(default=0)
    student_name = models.CharField(max_length=255, default="")

    class Meta:
        verbose_name_plural = 'Books Returned'
    
    def __str__(self):
        return self.book_name
    
class RequestedBooks(models.Model):
    book_id = models.IntegerField()
    book_name = models.CharField(max_length=400)
    book_image = models.TextField()
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=200)
    request_date = models.DateTimeField(auto_now_add=True)
    request_status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Requested Books'

    def __str__(self):
        return self.book_name
    
class Document(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    overView = models.TextField()
    introduction = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.overView

    
