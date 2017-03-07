from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def mainpage(request):
    page= """
    <html>
    <body>
    Sobres, a PP aplication.
    </body>
    </html>
    """
    return HttpResponse(page)
