from django.shortcuts import render
from django.http import HttpResponse
from .models import Definition
from django.contrib.postgres.search import TrigramSimilarity, SearchQuery, SearchVector
from django.db.models.functions import Cast, Greatest
from django.db import models
from django.db.models import Q, F

# Create your views here.

def index(request):
    return render(request, "search/index.html")

def search(request):
    search_term = request.GET.get("search_term", '')
    search_query = SearchQuery(search_term)
    vector = SearchVector("term") + SearchVector("definition") + SearchVector(Cast("aliases", output_field=models.TextField()))

    results = Definition.objects.annotate(
        search_vector=vector,
        term_similarity=TrigramSimilarity("term", search_term),
        definition_similarity=TrigramSimilarity("definition", search_term),
        aliases_similarity=TrigramSimilarity(Cast("aliases", output_field=models.TextField()), search_term)
    ).filter(
        Q(search_vector=search_query) 
        | Q(term_similarity__gte=0.2)
        | Q(definition_similarity__gte=0.2)
        | Q(aliases_similarity__gte=0.2) 
    ).annotate(
        similarity=(
            Greatest(
                F("term_similarity"),
                F("definition_similarity"),
                F("aliases_similarity")
            )
        )
    ).order_by("-similarity")

    context = {
        "results": results,
    }

    return render(request, "search/search.html", context)