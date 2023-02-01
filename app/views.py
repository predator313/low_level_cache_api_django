from django.shortcuts import render
from django.core.cache import cache

# Create your views here.
def fun(request):
    mv=cache.get_or_set('fees',200,30,version=2)
    return render(request,'app/home.html',{'mv':mv})
    # mv=cache.get('movie','not_available')
    # if mv=='not_available':
    #     cache.set('movie','pathan',30)
    # mv=cache.get('movie')
    # return render(request,'app/home.html',{'mv':mv})
