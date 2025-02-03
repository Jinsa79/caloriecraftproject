from django.contrib import admin

# Register your models here.
from .models import CalorieCraftPost
from .models import Recipe



admin.site.register(CalorieCraftPost)
 
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'calories', 'protein', 'fat', 'carbs', 'image')
    search_fields = ('title', 'author')
    list_filter = ('category',)
    ordering = ('-posted_at',)
 
admin.site.register(Recipe, RecipeAdmin)