from django.shortcuts import render, get_object_or_404
from .models import Supplier, Product, Purchase, PriceChange, Category


def index(request):
    num_products = Product.objects.all().count()

    return render(
        request,
        'index.html'
    )


def catalog_view(request):
    products = Product.objects.all()
    products = products.order_by('name')
    categories = Category.objects.all()
    current_category = None

    query = request.GET.get('product-name', '')
    articul_search = request.GET.get('articul-search', False)

    if query:
        if articul_search:
            products = products.filter(article_number__icontains=query)
        else:
            products = products.filter(name__icontains=query)

    sorting_option = 'sort-name'

    if request.method == 'POST':
        sorting_option = request.POST.get('sorting_option')

        if sorting_option == 'price_asc':
            products = products.order_by('price')
        elif sorting_option == 'price_desc':
            products = products.order_by('-price')

    return render(
        request,
        'catalog.html',
        context=
        {'products': products,
         'query': query,
         'articul_search': articul_search,
         'sorting_option': sorting_option,
         'categories': categories,
         'current_category': current_category, }
    )


def product_list_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()

    return render(request,
                  'catalog.html',
                  {'category': category,
                   'products': products,
                   'categories': categories,
                   'current_category': category.name, }
                  )
