from django.shortcuts import render,redirect, get_object_or_404
from .models import Product
from django.contrib import messages
#create product
def product_create(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        image_url = request.POST['image_url']
        
        Product.objects.create(
            name=name,
            description=description,
            price=price,
            image_url=image_url
        )
        messages.success(request, "Product added successfully!")
        return redirect('product_list')
    return render(request, 'product_form.html')
#productlist get product list
def product_list(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

# #edit product/update product/ product id 
def product_update(request,pk):
#    object or not found
   product =get_object_or_404(Product, pk=pk)
   if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.image_url = request.POST['image_url']
        product.save()
        messages.success(request, 'Product updated successfully!')
        return redirect('product_list')
   return render(request, 'product_form.html', {'product': product})
#delete product
# DELETE
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, "Product deleted successfully!")
    return redirect("product_list")
#add to cart
def add_to_cart(request,pk):
     product = get_object_or_404(Product, pk=pk)
     cart = request.session.get('cart', {})

    #  check item exist
     if str(pk) in cart:
         cart[str(pk)]['quantity'] += 1
     else:
          # add item
         cart[str(pk)] = {
             'name': product.name,
             'price': str(product.price),
             'quantity': 1}
     request.session['cart'] = cart
     return redirect('cart_detail')

#view cart     
def cart_detail(request):
  cart = request.session.get('cart', {})
  total = sum(float(item['price']) * item['quantity'] for item in cart.values())
  return render(request, 'cart.html', {'cart': cart, 'total': total})
# remove from cart
def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    if str(pk) in cart:
        del cart[str(pk)]
        request.session['cart'] = cart
        return redirect('cart_detail')

# clear cart
def clear_cart(request):
    request.session['cart'] = {}
    return redirect('cart_detail')

# icrement quantity
def increment_quantity(request, pk):
    cart = request.session.get('cart', {})
    if str(pk) in cart:
        # increase by one
        cart[str(pk)]['quantity'] += 1
        # save to cart in session storage
        request.session['cart'] = cart
        return redirect('cart_detail')
    
def decrement_quantity(request, pk):
    cart=request.session.get('cart', {})
    # condotion check item in cart and quantity greater than 1
    if str(pk) in cart and cart[str(pk)]['quantity'] > 1:
        #  decrease by one
        cart[str(pk)]['quantity'] -= 1
        # save to cart in session storage
        request.session['cart'] = cart
        return redirect('cart_detail')
        