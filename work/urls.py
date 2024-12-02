from django.urls import path
from . import views

app_name = 'work'

urlpatterns = [
    path('<str:account_id>', views.index, name='index'),
    path('<str:account_id>/edit/<int:message_id>', views.edit, name='edit'),
    path('<str:account_id>/<int:message_id>/delete/', views.delete, name='delete'),
    path('<str:account_id>/create', views.create, name='create'),
    path('work/all_index',views.all_index, name='all_index'),
]
