from django.urls import path
from . import views
#from .views import ShoeDetailView, ShoeListView
from django.conf import settings
from django.conf.urls import static

urlpatterns = [
    #path('list/', ShoeListView.as_view(), name='list'),
    path('', views.home, name='home_page'),
    path('detail/<int:pk>/', views.shoe_detail, name='shoe_detail'),
    path('shoe/', views.shoe_list, name='shoe_list'),
    path('shoe/create/', views.shoecreate, name='shoecreate'),
    path('search/', views.search_result, name='search_result'),
    path('login/', views.Login, name='login' ),
    path('logout/', views.Logout, name='logout' ),
    path('add_toCart/shoe/<int:pk>', views.add_toCart, name='add_toCart'),
    path('remove_from_cart/<int:cart_item_id>', views.removeproduct, name="removeproduct"),
    path('cart/', views.cartview, name='cart'),
    path('proceed_to_pay/', views.proceed_to_pay, name='proceed_to_pay'),
    path('payment_confirmation/', views.payment_confirmation, name='payment_confirmation'),
    path('register/', views.register, name='register'),
    path('registration_success/', views.registration_success, name='registration_success'),
    path('shoe_edit/<int:shoe_id>', views.shoe_edit, name='shoe_edit'),   
]
