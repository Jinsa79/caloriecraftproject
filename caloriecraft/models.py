from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=255,null=True)
    author = models.CharField(max_length=100)
    posted_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)
    calories = models.FloatField(blank=True, null=True)
    protein = models.FloatField(blank=True, null=True)
    fat = models.FloatField(blank=True, null=True)
    carbs = models.FloatField(blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)  # カンマ区切りで食材を保存
 
    def __str__(self):
        return self.title

        

class CalorieCraftPost(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=255,null=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
 
    def __str__(self):
        return self.title
    
class Vegetables(models.Model):

    name = models.CharField(max_length=30)
    content = models.TextField(null=True)
    auther = models.CharField(max_length=100)
    posted_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='vegetable_images/', blank=True, null=True)
    protain = models.FloatField(blank=True, null=True)
    fat = models.FloatField(blank=True, null=True)
    carbs = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

'''
class User(models.Model):
    user_id = models.AutoField(verbose_name='ユーザID', primary_key=True)
    user_nickname = models.CharField(verbose_name='ユーザネーム', max_length=50, null=False, unique=True)
    email = models.CharField(verbose_name='メールアドレス', max_length=254, null=False)
    sex = models.IntegerField(verbose_name='性別', null=False)
    birthday = models.DateField(verbose_name='生年月日', null=True)
    password = models.CharField(verbose_name='パスワード', max_length=30, null=False)
    tell_number = models.CharField(verbose_name='電話番号', max_length=21, null=True)

    class Meta:
        db_table = '01_user'  # 明示的にテーブル名を指定



class Recipe(models.Model):
    recipe_name = models.CharField(verbose_name='レシピ名', max_length=25, null=False)
    creator_name = models.ForeignKey('User', verbose_name='レシピ名', on_delete=models.CASCADE)
    step = models.CharField(verbose_name='手順', max_length=255, null=False)
    recipe_id = models.AutoField(verbose_name='レシピID', primary_key=True)

    class Meta:
        db_table = '03_recipes'  # 明示的にテーブル名を指定
'''