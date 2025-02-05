from django.forms import ModelForm
from .models import Recipe

class RecipePostForm(ModelForm):

    class Meta:

        model = Recipe
        fields = ['title', 'content','image', 'calories', 'protein', 'fat', 'carbs', 'ingredients']