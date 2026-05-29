from django.shortcuts import render
from .models import Product, Category, Review
from django.shortcuts import render, get_object_or_404
from django.db.models import Q


def home(request):

    search = request.GET.get('search')
    category = request.GET.get('category')

    products = Product.objects.all()

    categories = Category.objects.all()
    if search:

        products = Product.objects.filter(

            Q(name__icontains=search) |
            Q(description__icontains=search)

        )
    if category:

        products = products.filter(category_id=category)

    context = {

        'products': products,
        'categories': categories
    }

    return render(request, 'products/home.html', context)
# product details

def product_detail(request, id):

    product = Product.objects.get(id=id)

    reviews = Review.objects.filter(product=product)

    if request.method == "POST":

        already_reviewed = Review.objects.filter(

            product=product,

            user=request.user

        ).exists()

        if not already_reviewed:

            comment = request.POST.get("comment")

            rating = request.POST.get("rating")

            Review.objects.create(

                product=product,

                user=request.user,

                comment=comment,

                rating=rating

            )

    total_rating = 0

    for review in reviews:

        total_rating += review.rating

    if reviews.count() > 0:

        average_rating = total_rating / reviews.count()

    else:

        average_rating = 0

    return render(

        request,

        'products/product_detail.html',

        {

            'product': product,

            'reviews': reviews,

            'average_rating': average_rating,

            'user_reviewed': Review.objects.filter(

                product=product,

                user=request.user

            ).exists()
        
        }

    )
    