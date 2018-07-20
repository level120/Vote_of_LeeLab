from django.contrib import admin
from .models import Like

# Register your models here.
#admin.site.register(Like)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_id', 'name', 'description', 'isVote', 'prize', 'total_likes']
    list_display_links = ['name_id']
