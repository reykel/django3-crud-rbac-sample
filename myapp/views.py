from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

from .models import Person, City
from .forms import PersonForm

from django.http import JsonResponse

# Create your views here.
def index (request):
    return render(request,'index.html')

def bookList(request):  
    books = Book.objects.all()  
    return render(request,"book-list.html",{'books':books})  

def bookCreate(request):  
    if request.method == "POST":  
        form = BookForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('book-list')  
            except:  
                pass  
    else:  
        form = BookForm()  
    return render(request,'book-create.html',{'form':form})  

def bookUpdate(request, id):  
    book = Book.objects.get(id=id)
    form = BookForm(initial={'title': book.title, 'description': book.description, 'author': book.author, 'year': book.year})
    if request.method == "POST":  
        form = BookForm(request.POST, instance=book)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/book-list')  
            except Exception as e: 
                pass    
    return render(request,'book-update.html',{'form':form})  

def bookDelete(request, id):
    book = Book.objects.get(id=id)
    try:
        book.delete()
    except:
        pass
    return redirect('book-list')

def personCreate(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person-list')
    return render(request, 'person-create.html', {'form': form})

def personUpdate(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonForm(instance=person)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person-list')
    return render(request, 'person-update.html', {'form': form})

def personDelete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    try:
        person.delete()
    except:
        pass
    return redirect('person-list')    

def personList(request):  
    persons = Person.objects.all()  
    return render(request,"person-list.html",{'persons':persons})

def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})

