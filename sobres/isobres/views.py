from django.contrib.auth.models import User
from django.http import Http404,HttpResponse
from django.shortcuts import render,render_to_response
from django.template.loader import get_template
from django.template import Context



# Create your views here.
def mainpage(request):
    render_to_response('principal.html',{
        'appname':"electrosobres",
        'titlepage':'sobres',
        'author':"Luis Barcenas"

    })
    #template=get_template('principal.html')
    #variables=Context({
        #'appname':"electrosobres",
        #'titlepage':'sobres',
        #'author':"Luis Barcenas"

    

    page= template.render(variables)#Fa la subsitucio de les variables dins del html
    return HttpResponse(page)

def dashboard(request,usuari):
    try:
        user=User.objects.get(username=usuari)#Busca el objecte User amb aquest parametre
        #retorna error si no existeix el usuari
    except:
        #Pagina 404
        raise Http404("L'usuari no hi es, collons")
    sobres=user.sobre_set.all()
    template=get_template('dashboard.html')
    variables=Context({
        'username':usuari,
        'author':'Luis Barcenas',
        'sobres':sobres
    })
    page=template.render(variables)
    return HttpResponse(page)
