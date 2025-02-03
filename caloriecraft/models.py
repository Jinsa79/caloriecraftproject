from django.db import models

# Create your models here.
class CalorieCraftPost(models.Model):

    pass

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