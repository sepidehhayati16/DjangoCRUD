from django.shortcuts import render,redirect
from . import models

def crud(request):
    '''
    products1 = models.Product(name = 'Sunscreen', price = '800', number = '200')
    products1.save()
    '''
    """
    products3 = models.Product.objects.filter(id=3).first()
    products3.name = 'water supply'
    products3.save()
    """
    """
    products3 = models.Product.objects.filter(id=7).first()
    products3.delete()
    """
    products2 = models.Product.objects.all()


    return render(request,'index.html',context={'products2':products2})

# Create your views here.
def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        number = request.POST.get('number')
        product = models.Product(name=name, price=price, number=number)
        product.save()
        return redirect('store')