from django.contrib import admin
from petstagramFinal.pets.models import Pet, Like, Comment


class PetAdmin(admin.ModelAdmin):
    list_display = ['type', 'name', "age"]


class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'pet_id']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'pet_id']


admin.site.register(Pet, PetAdmin)
admin.site.register(Like, LikeAdmin)
