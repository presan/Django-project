
from django.urls import path
from myapp import views

urlpatterns = [
    path('post',views.post,name='post'),
    path('post/<int:pk>',views.hello,name='hello'),
    path('',views.navb,name='navb'),
    path('ga',views.ga, name='ga'),
    path('co',views.co, name='co'),
]

