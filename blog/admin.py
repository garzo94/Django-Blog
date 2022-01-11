from django.contrib import admin
from .models import Post
# In this class, you can include information about how to display the model in the site and how to
#interact with it.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
 list_display = ('title', 'slug', 'author', 'publish', 'status')
 list_filter = ('status', 'created', 'publish', 'author')
 search_fields = ('title', 'body')
 prepopulated_fields = {'slug': ('title',)} #fill the slug field automatically when you write your tile down (When creating blog (POST))
 raw_id_fields = ('author',) #display a lookup, very usefull when you a tons of user
 date_hierarchy = 'publish'  #Just below the search bar, there are navigation links to navigate through a date hierarchy; this has been defined by the date_hierarchy attribute
 ordering = ('status', 'publish')



