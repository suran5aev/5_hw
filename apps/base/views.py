from django.shortcuts import render
from apps.base.models import Base, Popular_category,Our_chef,News
from apps.telegram.models import Telegram
# Create your views here.

def index(request):
    base = Base.objects.latest('id')
    category = Popular_category.objects.all()
    chef = Our_chef.objects.all().order_by('?')[:3]
    news = News.objects.all().order_by('?')[:2]
    return render(request, 'base/index-dark.html', locals())



def telegram(request):
    base = Base.objects.latest('id')
    if request.method == "POST":
        phone = request.POST.get('phone')
        persone = request.POST.get("persone")
        date = request.POST.get("date")
        time = request.POST.get("time")
        Telegram.objects.create(phone=phone, persone=persone, date=date, time=time)
        

        

           


