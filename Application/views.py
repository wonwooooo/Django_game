from django.shortcuts import render
from .models import Game, Phone
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse, Http404
import json

# Create your views here.

def home(request):
    return render(request, 'Application/index.html', locals())

def test(request):
    return render(request, 'Application/2048.html', locals())


def create(request):
    if request.method == "POST":
        nom = request.POST.get('nom').capitalize()
        prenom = request.POST.get('prenom').capitalize()
        mail = request.POST.get('mail').lower()
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        username = f"{nom}.{prenom}"

        if len(User.objects.filter(email=mail)) == 1:
            return HttpResponse("Vous avez déjà un compte")

        usr = User(username=username, password=password, email=mail, first_name=nom, last_name=prenom)
        usr.set_password(password)
        usr.save()

        usr_phone = Phone(username=usr, phone=phone)
        usr_phone.save()
        
        return HttpResponse(1)
    raise Http404("Chemin Non Trouvé")


def connect(request):
    if request.method == "POST":
        mail = request.POST.get("mail")
        password = request.POST.get("password")

        try:
            usr = User.objects.get(email=mail)
        except:
            return HttpResponse("Adresse Mail Incorrecte")
        
        if not usr.check_password(password):
            return HttpResponse("Mot de passe Incorecte")
        
        usr_phone = Phone.objects.get(username=usr)
        return HttpResponse(usr_phone.phone)
    
    raise Http404("Chemin non Trouvé")


def get_game(request):
    if request.method == "POST":
        game_list = []
        game = Game.objects.all()

        for g in game:
            game_list.append([
                g.id,
                g.titre,
                g.couverture,
                g.categorie,
                g.gameplay,
                g.prix
            ])

        return JsonResponse([game_list], safe=False)

    
    raise Http404("Chemin non Trouvé")
