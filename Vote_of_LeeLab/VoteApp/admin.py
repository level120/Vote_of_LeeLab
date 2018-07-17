from django.contrib import admin
from VoteApp.models import Like

# Register your models here.
#admin.site.register(Like)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_id']
    list_display_links = ['name_id']

