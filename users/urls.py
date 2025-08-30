from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('private_page_1/', views.private_page_1, name='private_page_1'),
    path('private_page_2/', views.private_page_2, name='private_page_2')
]