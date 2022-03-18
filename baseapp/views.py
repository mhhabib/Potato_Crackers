from datetime import datetime
from django.shortcuts import render
from .helpers import get_word, get_date

# Create your views here.
def index(request):
    day=datetime.now().date()
    if request.method=="POST":
        custom_date=request.POST.get('custom-date')
        if custom_date:
            day=datetime.strptime(custom_date, '%Y-%m-%d').date()
        else:
            day= datetime.strptime('16/Jun/2021', '%d/%b/%Y').date()
    return render(request, 'baseapp/index.html',{'date_today':get_date(),'words':get_word(day),'days':day})












