from django.shortcuts import render
from django.http import HttpResponse
from .models import Definition
from django.contrib.postgres.search import TrigramSimilarity, SearchVector

# Create your views here.

def index(request):
    return HttpResponse("Hello, World")

def search(request):
    search_term = request.GET.get("search_term", '')
    term = Definition.objects.annotate(
        similarity=TrigramSimilarity("term", search_term)).filter(
            similarity__gt=0.2
        ).order_by("-similarity")

    definition = Definition.objects.annotate(
        similarity=TrigramSimilarity("definition", search_term)).filter(
            similarity__gt=0.2
    ).order_by("-similarity")

    aliases = Definition.objects.filter(aliases__icontains=search_term)

    results = (term | definition | aliases).distinct()

    context = {
        "results": results,
    }

    return render(request, "search/search.html", context)