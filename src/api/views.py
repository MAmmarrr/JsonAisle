from django.shortcuts import render, HttpResponseRedirect
from .forms import ProductForm
from .models import Product
# Create your views here.
def product_view(request):
    if request.method=='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("product")
    form = ProductForm()
    objects = Product.objects.all()
    context = {
        "form": form,
        "Product": objects
    }
    return render(request,'product.html',context)
