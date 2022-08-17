
##############################################################################

import sre_constants
import traceback

from django.http import HttpResponse
from django.shortcuts import redirect, render

from app2.models import Book, Employee

# Create your views here.

# request.POST.getlist("books")  # ["book1", ]

# function based view / class based view

def homepage(request):              # request -- HTTPRequest -- 
    # print(request.method)
    # print(request.POST, type(request.POST))
    # print(request.POST)
    name = request.POST.get("bname")
    price = request.POST.get("bprice")
    qty = request.POST.get("bqty")

    if request.method == "POST":
        if not request.POST.get("bid"):  
            book_name = name
            book_price = price
            book_qty = qty
            # print(book_name, book_qty, book_price)
            Book.objects.create(name=book_name, price=book_price, qty=book_qty)  # create book
            return redirect("homepage")
        else:
            bid = request.POST.get("bid")
            try:
                book_obj = Book.objects.get(id=bid)
            except Book.DoesNotExist as err_msg:
                print(err_msg)
            book_obj.name = name
            book_obj.price = price
            book_obj.qty = qty
            book_obj.save()
            return redirect("show_all_books")

    # print(request.build_absolute_uri())
    # statements -- 
    # a = [1,2,3,4]
    # print(a)
    elif request.method == "GET":
        all_books = Book.objects.all()
        data = {"books": all_books}
        # return render(request, "home.html", context=data)
        return render(request, template_name="home.html")
    # return HttpResponse("<h3>Hi Hello</h3><h5>Good Evening..!</h5>")

# HTTP Status Codes --  200 -- info -- 

# http://127.0.0.1:8000/home/  -- Base URL --  

def show_all_books(request):
    all_books = Book.objects.all()
    data = {"books": all_books}
    return render(request, "show_books.html", context=data)

def edit_data(request, id):
    book = Book.objects.get(id=id)
    return render(request, template_name="home1.html", context={"single_book": book})

def delete_data(request, id):
    print(request.method)
    if request.method == "POST":
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist as err_msg:
            traceback.print_exc()  # detailed exception msg
            return HttpResponse(f"Book Does not exist for ID:- {id}")
        else:
            book.delete()
        return redirect("show_all_books")
    else:
        return HttpResponse(f"Request method: {request.method} Not allowed..! Only POST method is allowed")



from app2.forms import AddressForm, BookForm
from django.contrib import messages
# Create your views here.   ---- 

def form_home(request):  # Funcion Based View
    if request.method == "POST":
        print(request.POST)
        print("in POST request")
        form  = BookForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data["name"])
            form.save()
            messages.success(request, 'Data Saved successfully!')  # <-
            messages.info(request, 'Redirecting to home page')
        else:
            messages.error(request, 'Invalid Data..!')
        return redirect("form_home")

    elif request.method == "GET":
        print("in get request")
        context = {"form": BookForm()}
        return render(request, "form_home.html", context=context)
    else:
        return HttpResponse("Invalid HTTP Method", status=405)


# HTTP Methods-- GET, POST, PUT, DELETE, PATCH


# class ABCD(View):
#     def get(request):   #   by default -- get
#         pass

#     def post():    # 
#         pass
    
from django.views import View

class HomePage(View):
    # Name = None
    def get(self, request):
        print("in get request")
        # print(self.Name)
        return HttpResponse("In GET")

    def post(self, request):
        # print(dir(request))
        # print(request.build_absolute_uri())
        # print(request.user)
        print(request.POST)
        # print("in post request", request.body.decode("utf-8")) 
        return HttpResponse("In POST")

    def delete(self, request):
        print("in delete request")
        return HttpResponse("In DELETE", status=204)

    def put(self, request):
        print("in put request")
        return HttpResponse("In PUT")

    def patch(self, request):
        print("in patch request")
        return HttpResponse("In PATCH")

# - idempotent -- 
# - non-idempotent --

from django.views.generic.base import TemplateView, RedirectView

class CBVTemplateView(TemplateView):    
    # extra_context = {"form" : BookForm()}
    # template_name = "form_home.html"
    extra_context = {"Course_Name" : "Python"}
    template_name = "about_us.html"

class CBVRedirectView(RedirectView):
    url = "https://money.rediff.com/gainers/bse/monthly/groupz"


from django.urls import reverse, reverse_lazy  

from django.views.generic import CreateView, ListView, DetailView, UpdateView

# # generic views

class EmployeeCreate(CreateView):    # employee_form.html
    model = Employee  
    fields = '__all__'  
    success_url = "http://127.0.0.1:8000/emp-gcreate/"
    # return render(request, "employee_form.html", {"form": EmployeeForm})


class EmployeeRetrieve(ListView):    # Listview -- sara data fetch kar ke deta hai
    model = Employee  
    # return render(request, "employee_list.html", {"object_list": data})
    


class EmployeeDetail(DetailView):   # for fetching single data 
    model = Employee  
    # return render(request, "employee_detail.html", {"object": data})        

class EmployeeUpdate(UpdateView):  
    model = Employee  
    fields = '__all__'  
    success_url = "http://127.0.0.1:8000/emp-retr/"
