from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page),
    path('category/<str:pk>', views.get_category),
    path('courses/<str:pk>', views.get_courses),
    path('add_course/<str:pk>', views.add_to_cart),
    path('user_cart', views.get_user_cart),
    path('confirm_order', views.order_confirmation),
    path('user_cabinet', views.get_user_cabinet),
    path('user_courses/<str:pk>', views.get_paid_course)
]