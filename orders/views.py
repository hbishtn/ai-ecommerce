from django.shortcuts import render, redirect
from .models import Order, OrderItem
from products.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def checkout(request):

    cart = request.session.get('cart', {})

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')

        order = Order.objects.create(
            user=request.user,

            name=name,
            email=email,
            address=address,
            city=city

        )

        for product_id, quantity in cart.items():

            product = Product.objects.get(id=product_id)

            OrderItem.objects.create(

                order=order,
                product_name=product.name,
                price=product.price,
                quantity=quantity

            )

        request.session['cart'] = {}

        return redirect('success')

    return render(request, 'orders/checkout.html')

def success(request):

    return render(request, 'orders/success.html')

@login_required
def my_orders(request):

    orders = Order.objects.filter(user=request.user)

    context = {
        'orders': orders
    }

    return render(request, 'orders/my_orders.html', context)