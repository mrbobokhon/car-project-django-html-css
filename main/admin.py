from main.models import Post
from django.contrib import admin

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = [
        'id'
    ]
    fields = [       
        'subject_ru',
        'subject_uz',
        'content_uz',
        'content_ru' 
        'image'        
    ]
