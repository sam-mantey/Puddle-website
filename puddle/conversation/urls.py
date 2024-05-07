from . import views
from django.urls import path

app_name = 'conversation'

urlpatterns = [
    path('', views.Inbox, name='inbox'),
    path('<int:pk>/', views.MessageDetail, name='detail'),
    path('new/<int:item_pk>/', views.NewConversation, name='new'),
]