from django.db import models

# Create your models here.
class ActiveB(models.Model):
    def get_query(self):
        return super().get_query().filter(is_delete=0)
  

class InActiveB(models.Model):     # Assignment point 
    def get_query(self):
        return super().get_query().filter(is_delete=1)
    

class Book(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    qty = models.IntegerField()
    is_published = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    get_active_books = ActiveB()
    get_inactive_books = InActiveB()
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "book"

    def save(self, *args, **kwargs):
        if self.qty < 12:
            raise ValueError("Minimum qty should be 12")
        print("in overriden save method")
        super(Book, self).save(*args, **kwargs)

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "emp"