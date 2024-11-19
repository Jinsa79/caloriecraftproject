from django.shortcuts import render

# Create your views here.
# django.views.generic.baseからTemplateViewをインポート
from django.views.generic import TemplateView

class IndexView(TemplateView):
    '''トップページのビュー
    
    テンプレートのレンダリングに特化したTemplateViewを継承

    Attributes:
        template_name: レンダリングするテンプレート
    '''
    # index.htmlをレンダリングする
    template_name = 'index.html'
    #object_listキーの別名を設定
#    context_object_name = 'orderby_records'
    #モデルBlogPostのオブジェクトにorder_by()を適用して
    #BlogPostのレコードを投稿日時の降順で並べ替える
#    queryset = CalorieCraftPost.objects.order_by('-posted_at')