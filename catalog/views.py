import json
from django.shortcuts import render
from django.conf import settings


def index(request):
    """ A simple home page. """
    basedir = settings.BASE_DIR
    # filename = basedir + "/checkurl/checkurl.json"
    filename = basedir + "/json_file.json"

    try:
        with open(filename, "r") as f:
            dict_checkurl = json.load(f)
    except Exception as exc:
        dict_checkurl = {"error": str(exc)}

    dic_context = {
        "jumbotron_title": "Welcome to Django Bango!!!",
        "jumbotron_p": "This is amazing xD!",
        "checkurl": dict_checkurl,
    }
    return render(request, "index.html", context=dic_context)
