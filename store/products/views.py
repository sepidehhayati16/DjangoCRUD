from django.shortcuts import render
from . import models

def crad(request):
    '''
    products1 = models.Product(name = 'Sunscreen', price = '800', number = '200')
    products1.save()
    '''
    """
    products3 = models.Product.objects.filter(id=3).first()
    products3.name = 'water supply'
    products3.save()
    """
    products2 = models.Product.objects.all()

    products3 = models.Product.objects.filter(id=7).first()
    products3.delete()
    return render(request,'index.html',context={'products2':products2})

# Create your views here.
