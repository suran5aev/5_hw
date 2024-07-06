from django.shortcuts import render
from apps.base.models import Our_chef
# Create your views here.

def about(request):
    chef = Our_chef.objects.all().order_by('?')[:3]
    return render(request, 'base/about.html', locals())

