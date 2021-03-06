from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product
# Create your views here.


# Class based view
class ProductListView(ListView):
	queryset = Product.objects.all()
	template_name = "products/list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		print(context)
		return context

# Function based view, same as above
def product_list_view(request):
	#This is like a db query
	queryset = Product.objects.all()
	context = {
		'object_list': queryset
	}
	return render(request, "products/list.html", context)


	# Class based view
class ProductDetailView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"
	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		return context

# Function based view, same as above
def product_detail_view(request, pk=None, *args, **kwargs):
	#instance = Product.objects.get(pk=pk) #id
	instance = get_object_or_404(Product, pk=pk)
	queryset = Product.objects.all()
	context = {
		'object': instance,
	}
	return render(request, "products/detail.html", context)