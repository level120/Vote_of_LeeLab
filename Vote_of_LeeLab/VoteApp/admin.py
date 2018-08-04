from django.contrib import admin
from .models import Like, VoteDate, VoteResult, Rtsp

# Register your models here.
#admin.site.register(Like)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_id', 'name', 'description', 'isVote', 'prize', 'total_likes']
    list_display_links = ['name_id']


admin.site.register(VoteDate)
admin.site.register(VoteResult)
admin.site.register(Rtsp)