from django.shortcuts import render
from django.template import RequestContext
from . models import Portofolio, Hero, About


def view404(request, *args, **argv):
    response = render('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

# Create your views here.
def home(request):
    portofolios = Portofolio.objects.all()
    hero = Hero.objects.first()
    about = About.objects.first()
    return render(request, 'index.html', {
        'portofolios': portofolios,
        'hero': hero,
        'about': about
        })
