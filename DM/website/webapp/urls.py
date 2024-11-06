from django.urls import path
from . import views,constructeur_views

urlpatterns = [
    path('', views.home),
    path('Mobile/', views.home),
    path('Mobile/show/<int:id>/', views.show_Mobile),
    path('Mobile/add/', views.add_Mobile),
    path('Mobile/processing/', views.processing),
    path('Mobile/update/<int:id>/', views.update_Mobile),
    path('Mobile/processing_update/<int:id>/', views.processing_update),
    path('Mobile/delete/<int:id>/', views.delete_Mobile),
    path('Constructeur/', constructeur_views.home),
    path('Constructeur/add/', constructeur_views.add_Constructeur),
    path('Constructeur/processing/', constructeur_views.processing),
    path('Constructeur/show/<int:id>/', constructeur_views.show_Constructeur),
    path('Constructeur/update/<int:id>/', constructeur_views.update_Constructeur),
    path('Constructeur/processing_update/<int:id>/', constructeur_views.processing_update),
    path('Constructeur/delete/<int:id>/', constructeur_views.delete_Constructeur),
]