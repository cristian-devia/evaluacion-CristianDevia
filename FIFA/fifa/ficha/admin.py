from django.contrib import admin
from .models import Team,Player, PlayingPosition, Coach

#admin.site.register(Team)
#admin.site.register(Player)
#admin.site.register(PlayingPosition)
#admin.site.register(Coach)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','flag_image','shield_image',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name','last_name','birth_date','position','number','is_starting','team','show_photo',)

@admin.register(PlayingPosition)
class PlayingPositionAdmin(admin.ModelAdmin):
    list_display = ('name','description',)

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('name','last_name','birth_date','nationality','role',)

# Register your models here.
