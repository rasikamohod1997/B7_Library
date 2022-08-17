# exec(open(r'D:\Programs\B7_Django\LibraryProj\app2\db_shell.py').read())


# from django.contrib.auth.models import User

# print(User.objects.all())

# User.objects.create_user(username="Aditi", password="Python@123", email="aditi@gmail.com")



from app2.models import Book

book_obj = Book(name="Book9", price=340, qty=12)
book_obj.save()

