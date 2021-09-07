from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()                                 #declaration of a router
router.register('cats', AllCatView, basename='cats')

urlpatterns = [
    path('add/', AddCatView.as_view()),                 #URL to add new cats
    path('', include(router.urls)),                     #this router contains all the URLs required to show, edit or remove cats
]