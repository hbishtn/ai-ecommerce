from django.shortcuts import redirect
from products.models import Product
from django.shortcuts import render


def add_to_cart(request, product_id):

    product = Product.objects.get(id=product_id)

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:

        cart[product_id] += 1

    else:

        cart[product_id] = 1

    request.session['cart'] = cart

    return redirect('home')

# cart detail view

def cart_detail(request):

    cart = request.session.get('cart', {})

    cart_items = []

    total = 0

    for product_id, quantity in cart.items():

        product = Product.objects.get(id=product_id)

        subtotal = product.price * quantity

        total += subtotal

        cart_items.append({

            'product': product,
            'quantity': quantity,
            'subtotal': subtotal

        })

    context = {

        'cart_items': cart_items,
        'total': total

    }

    return render(request, 'cart/cart.html', context)

# for increasing & decreasing quantity of a product in cart
def increase_quantity(request, product_id):

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:

        cart[product_id] += 1

    request.session['cart'] = cart

    return redirect('cart_detail')

def decrease_quantity(request, product_id):

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:

        cart[product_id] -= 1

        if cart[product_id] <= 0:

            del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart_detail')

def remove_from_cart(request, product_id):

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:

        del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart_detail')