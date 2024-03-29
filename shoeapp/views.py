import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .models import Shoe, Cart, CartItems
from .forms import ShoeForm, SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


#views for registration form
def register(request): #
    if request.method == "POST":
        form = UserCreationForm(request.POST) #
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username') #
            raw_password=form.cleaned_data.get('password1') #
            user=authenticate(username=username, password=raw_password)#
            login(request,user) #
            return redirect('home')
        
    else:
        form = UserCreationForm() #
    
    return render(request, 'register.html', {'form':form})

def registration_success(request):
    return render(request, 'registration_success.html')

#views for home.html
def home(request):
    return render(request, 'shoeapp/home.html')

# views for search_result.html   
def search_result(request):
    search_query = request.GET.get('search', '')
    shoe = Shoe.objects.filter(Q(brand__icontains = search_query))
    return render(request, 'shoeapp/search_result.html', {'shoe' : shoe, 'search_query' : search_query})

#views for shoe_list.html
def shoe_list(request):
    shoe = Shoe.objects.all()
    return render (request, 'shoeapp/shoe_list.html', {'shoe' : shoe})

# Create your views here.
def shoe_detail(request, pk):
    #pets = Pet.objects.get(pk=pk)
    shoe = get_object_or_404(Shoe, pk=pk)
    return render(request, 'shoeapp/detail.html', {'shoe': shoe})

#create view for cart
def cartview(request):
    cart_items = CartItems.objects.filter(cart__user=request.user)
    return render(request, 'shoeapp/cart.html',{'cart_items':cart_items})

#Create View for add to cart items :
def add_toCart(request, pk):
    if request.method == 'POST':
        shoe = get_object_or_404(Shoe, pk=pk)
        quantity = int(request.POST.get('quantity', 1))
        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItems.objects.get_or_create(cart=cart, shoe=shoe, defaults={'quantity': quantity})
        # the cart quantity intially empty
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart_item.quantity = quantity
            cart_item.save()
        return redirect('cart')

#create view for remove items from cart
def removeproduct(request, cart_item_id):
    cart_item = get_object_or_404(CartItems, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')

def proceed_to_pay(request):
    cart_items = CartItems.objects.filter(cart__user=request.user)
    total_amount = sum(item.shoe.price * item.quantity for item in cart_items)
    return render(request, 'shoeapp/proceed_to_pay.html', {'total_amount': total_amount})

@csrf_exempt
def payment_confirmation(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItems.objects.filter(cart=cart)
    order_amount = 0

    total_amount = sum(item.shoe.price * item.quantity for item in cart_items)
    client = razorpay.Client(auth=(settings.RAZORPAY_TEST_KEY_ID, settings.RAZORPAY_TEST_KEY_SECRET))

    order_amount = (order_amount + total_amount) * 100
    order_currency = 'INR'
    
    order = client.order.create({'amount':order_amount, 'currency':order_currency})

    context = {'order_amount': order_amount, 'order': order, 'razorpay_key_id': settings.RAZORPAY_TEST_KEY_ID}
    return render(request, 'shoeapp/payment_confirmation.html', context)

#views for shoe edit option
def shoe_edit(request, id):
    shoe = get_object_or_404(Shoe, id=id)
    if request.method == 'POST':
        form = ShoeForm(request.POST, instance=shoe)
        if form.is_valid():
            form.save()
            return redirect('shoe_list')
    else:
        form = ShoeForm(instance=shoe)
    return render(request, 'shoeapp/shoe_edit.html', {'form': form}) 

#views for shoecreate.html
def shoecreate(request):
    if request.method == 'POST':
        form = ShoeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shoe_list')
    else:
        form = ShoeForm()
    return render(request, 'shoeapp/shoecreate.html', {'form': form})

#views for Login.html
def Login(request):  
    if request.method == 'POST':  
        username = request.POST['username']  
        password = request.POST['password']  
        user = authenticate(request, username=username, password=password) 
        
        if user is not None:  # the password checked out  
            login(request,user)                     
            return redirect('shoe_list')               
        else:
            pass
    return render(request,'shoeapp/login.html')    

#views for logout.html
def Logout(request):
    logout(request)
    return redirect('login')



