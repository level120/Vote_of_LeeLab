from django.contrib import admin
from VoteApp.models import Like, DisLike

# Register your models here.
admin.site.register(Like)
admin.site.register(DisLike)
#@admin.register(Like)
#class PostAdmin(admin.ModelAdmin):
#    list_display = ['name_id', 'like', 'dislike']
#    list_display_links = ['name_id']