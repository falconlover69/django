from django.contrib import admin

# Register your models here.
from .models import Posts

admin.site.site_header = "Greg`s Social Network Admin Panel"
admin.site.site_title = "Social Network Area"
admin.site.index_title = "Welcome to my Social Network"

class PostsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title','body']}),
        ('Date Info', {'fields': ['created_at'], 'classes': ['collapse']}),
    ]


admin.site.register(Posts,PostsAdmin)
