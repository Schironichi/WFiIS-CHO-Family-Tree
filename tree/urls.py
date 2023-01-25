from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tree-home'),
    path('person/<uid>/', views.person, name='person'),
    path('person/<uid>/delete/', views.delPerson, name='del-person'),
    path('new/', views.newPerson, name='new-person'),
    path('relation/', views.newRelation, name='new-relation'),
]