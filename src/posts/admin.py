from django.contrib import admin
from .models import Post, Category

# Register your models here.


class AdminCategory(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)
    
    class Meta:
        model = Category
        

class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'publishing_date',)
    list_filter = ('publishing_date',)
    search_fields = ('title', 'content')
    
    class Meta:
        model = Post

admin.site.register(Category, AdminCategory)
admin.site.register(Post, AdminPost)