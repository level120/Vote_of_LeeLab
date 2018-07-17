from django.contrib import admin
from VoteApp.models import Like, DisLike

# Register your models here.
#admin.site.register(Like)
#admin.site.register(DisLike)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_id']
    list_display_links = ['name_id']


@admin.register(DisLike)
class DisLikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_id']
    list_display_links = ['name_id']