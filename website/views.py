from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import HomePage, Page
# Create your views here.
def index(request):
    """View function for home page of site."""
    homePage = HomePage.objects.all()
    context = {
        'title_text': homePage[0].Title_Text,
        'subtitle_text': homePage[0].Subtitle_Text,
        'cover_photo': homePage[0].Cover_Photo,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def book(request):
    """View function for home page of site."""
    pages = Page.objects.all()
    first_research_pagenum = 0
    for page in pages:
        if page.Category == "researches":
            first_research_pagenum = page.id
            break
    first_meet_research_pagenum = 0
    for page in pages:
        if page.Category == "meet_research":
            first_meet_research_pagenum = page.id
            break
    first_meet_team_pagenum = 0
    for page in pages:
        if page.Category == "meet_team":
            first_meet_team_pagenum = page.id
            break
    
    context = {"pages": pages,
               "first_research_pagenum": first_research_pagenum,
               "first_meet_research_pagenum": first_meet_research_pagenum,
               "first_meet_team_pagenum": first_meet_team_pagenum}

    # Render the HTML template book.html with the data in the context variable
    return render(request, 'book.html', context=context)

@csrf_exempt
def getResearch(request: WSGIRequest):
    if request.method == 'GET':
        pages = Page.objects.all()
        reqpage = ""
        for page in pages:
            if page.id == int(request.headers["id"]):
                reqpage = page
                break
        return HttpResponse(reqpage.Content)
    else:
        return HttpResponse(status=405, content=request.method + " method is not accepted on this endpoint")