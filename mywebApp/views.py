from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'footer.html', {'name': 'Logan', 'profileIMG': 'https://picsum.photos/200/300'})
