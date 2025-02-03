from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Recipe
 
# 修正: きちんと IndexView を定義
class IndexView(TemplateView):
    template_name = 'index.html'
 
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
 
 