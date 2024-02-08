from django.test import TestCase

# Create your tests here.
    # with open
import os 
file_path = os.path.abspath(__file__)

file_name = os.path.basename(file_path)

with open('C:\\Users\\User\\Desktop\\New folder (3)\\project\\app\\urls.py','w') as e:
    e.write('A')
    e.close()

print('hello')







from django.shortcuts import render,redirect
from .forms import PytjaForm  # Ensure the correct form is being imported
from .models import *


def Kontakti(request):
    if request.method == 'POST':
        form = PytjaForm(request.POST)
        if form.is_valid():
            form.save()  # If this form is a ModelForm
            # Process valid form data here if needed
        return redirect('/')
    else:
        form = PytjaForm()
    return render(request, 'index2.html', {'form': form})


def index(request):
    data = Njoftime.objects.all()[::-1]
    # with open
    import os 
    # file_path = os.path.abspath(__file__)

# Extract the file name from the file path
# file_name = os.path.basename(file_path)
    return render(request, 'index.html', {'data': data,})


