from django.urls import path
from .views import main_index, main_add_post, main_delete_post, main_view_post

app_name = "main"

urlpatterns = [
    path('', main_index, name='main'),
    path('add-post/', main_add_post, name='add-post'),
    path('delete-post/<int:it>/', main_delete_post, name='delete-post'),
    path('view/<int:id>/', main_view_post, name='view'),
]