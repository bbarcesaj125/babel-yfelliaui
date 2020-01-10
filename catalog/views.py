import json
from django.shortcuts import render
from django.conf import settings
from .models import Dewey

# Create your views here.
CONTEXT_GLOBAL = {
    "mediatheque_name": "Bibliothèque de St Pons",
    "mediatheque_adr": "Villeneuve les Avignon",
    "dev_name": "Youssef FELLIAUI",
    "dev_github": "https://github.com/bbarcesaj125/babel-yfelliaui",
    "dev_cadre": "Formation Django/Python FORMEXT",
}


def publication(request):
    record = Dewey.objects.get(number="200")

    context_local = {
        "title": "Liste de publications",
        "description": "Ouvrage et leurs classifications",
    }
    context_page = {
        "global": CONTEXT_GLOBAL,
        "local": context_local,
        "dewey_object": record,
    }
    return render(request, "catalog/index.html", context=context_page)


def home(request):
    context_local = {
        "title": "Page d'accueil de Babel",
        "description": "Bienvenue sur cette page en cours de réalisation",
    }
    context_page = {"global": CONTEXT_GLOBAL, "local": context_local}
    return render(request, "catalog/index.html", context=context_page)


def about(request):
    context_local = {
        "title": "A propos de Babel",
        "description": "Vous trouverez tous les détails de spécifications ici.",
    }
    context_page = {"global": CONTEXT_GLOBAL, "local": context_local}
    return render(request, "catalog/about.html", context=context_page)


def newsroom(request):
    basedir = settings.BASE_DIR
    filename = basedir + "/json_file.json"
    try:
        with open(filename, "r") as f:
            dict_checkurl = json.load(f)
    except Exception as e:
        dict_checkurl = {"error": str(e)}

    context_local = {
        "title": "Salle de presse",
        "description": "Voici une liste de quotidiens internationaux",
    }

    context_page = {
        "checkurl": dict_checkurl,
        "local": context_local,
        "global": CONTEXT_GLOBAL,
    }

    return render(request, "catalog/newsroom.html", context=context_page)
