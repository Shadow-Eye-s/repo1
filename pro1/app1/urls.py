from django.urls import path
from app1.views import mywish
from app1.views import fresh
from .import views
urlpatterns=[
    path("wish1/",mywish),
    path("age/<int:age>/",fresh),    
]

urlpatterns=[
    path('fresh/', views.fresh, name='fresh')
]