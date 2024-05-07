from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.ItemView, name='item_view'),
    path("<int:pk>/", views.Detail, name="detail"),
    path('new_item/', views.New_Item, name="new_item"),
    path('<int:pk>/delete/', views.Delete, name='delete'), 
    path('<int:pk>/edit/', views.Edit_Item, name='edit'),
]