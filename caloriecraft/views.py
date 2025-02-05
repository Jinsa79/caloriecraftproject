from django.shortcuts import render
<<<<<<< HEAD
from django.views.generic import TemplateView, ListView
=======
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RecipePostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

>>>>>>> 5b3b715beff2855dbed9caa28d57928fa14d8448
from .models import Recipe
from .models import PhotoPost
# 修正: きちんと IndexView を定義
class IndexView(TemplateView):
    template_name = 'index.html'

@method_decorator(login_required, name='dispatch')

class CreateRecipeView(CreateView):

    form_class = RecipePostForm
    template_name = "post_recipe.html"
    success_url = reverse_lazy('recipe:post_done')

    def form_valid(self, form):

        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)
 
def search(request):
    query = request.GET.get('q', '').strip()
    print(f"検索クエリ: {query}")  # コンソールに出力
 
    if not query:
        return render(request, 'caloriecraft/index.html', {'error': '検索クエリを入力してください。'})
 
    # タイトルに検索クエリを含むレシピを取得
    results = Recipe.objects.filter(title__icontains=query)
    print(f"検索結果数: {results.count()}")  # 結果数を出力
 
    for result in results:
        print(f"見つかったレシピ: {result.title}")  # 各結果のタイトルを出力
 
    return render(request, 'caloriecraft/search_results.html', {
        'query': query,
        'results': results
    })
 
class IndexView(ListView):
    template_name = 'index.html'
    queryset = PhotoPost.objects.order_by('-posted_at')
    paginate_by = 9
