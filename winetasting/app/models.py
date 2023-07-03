from django.db import models

class RedTasting(models.Model):
 #外観
    grape = models.TextField(
        verbose_name='ブドウ品種',max_length=30,blank=True,null=True,)
    country = models.TextField(
        verbose_name='国',max_length=30,blank=True,null=True,)
    coolness = models.CharField(
        verbose_name='清涼感',max_length=30,
        choices= (('1.澄んだ','1.澄んだ'),('2.深みのある','2.深みのある'),('3.やや濁った','3.やや濁った'),('4.濁った','4.濁った')),
        blank=True,null=True,)
    shine = models.CharField(
        verbose_name='輝き',max_length=30,
        choices= (('1.輝きのある','1.輝きのある'),('2.艶のある','2.艶のある'),('3.モヤがかった','3.モヤがかった')),
        blank=True, null=True,)
    tone = models.CharField(
        verbose_name='色調', max_length=30,
        choices= (('1.紫がかった','1.紫がかった'),('2.オレンジがかった','2.オレンジがかった'),('3.黒みを帯びた','3.黒みを帯びた'),('4.縁が明るい','4.縁が明るい'),('5.ルビー(ラズベリーレッド)','5.ルビー(ラズベリーレッド)'),('6.ガーネット(ダークチェリーレッド)','6.ガーネット(ダークチェリーレッド)'),('7.トパーズ','7.トパーズ'),('8.マホガニー','8.マホガニー'),('9.レンガ','9.レンガ')),
        blank=True, null=True,) 
    shade = models.CharField(
        verbose_name='濃淡', max_length=30,
        choices= (('1.無色に近い','1.無色に近い'),('2.明るい','2.明るい'),('3.やや明るい','3.やや明るい'),('4.やや濃い','4.やや濃い'),('5.濃い','5.濃い'),('6.非常に濃い','6.非常に濃い')),
        blank = True, null=True,)
    viscosity = models.CharField(
        verbose_name='粘性', max_length=30,
        choices= (('1.さらっとした','1.さらっとした'),('2.やや軽い','2.やや軽い'),('3.やや強い','3.やや強い'),('4.強い','4.強い')),
        blank = True, null=True,)
    freshhness = models.CharField(
        verbose_name='若さ', max_length=30,
        choices= (('1.若々しい','1.若々しい'),('2.若い状態を抜けた','2.若い状態を抜けた'),('3.やや熟成した','3.やや熟成した'),('4.熟成した','4.熟成した'),('5.酸化熟成のニュアンス','5.酸化熟成のニュアンス'),('6.酸化が進んだ','6.酸化が進んだ')),
        blank = True, null=True,)
    Maturity = models.CharField(
        verbose_name='成熟度', max_length=30,
        choices= (('1.軽快な','1.軽快な'),('2.成熟度が高い','2.成熟度が高い'),('3.濃縮感が強い','3.濃縮感が強い')),
        blank = True, null=True,)
    
# #香り
#     firstimpression
#     kazitu
#     hana_shokubutu
#     kousinryou
#     kaorinoinshou
# #味わい
#     attack
#     amami
#     sannmi
#     tannint
#     balance
#     alchool
#     yoin
# #まとめ
#     hyouka
#     tekiseionndo
#     glass
#     decantage
#     year
#     country
#     grape
#command K+C, K+U
 # 管理サイト上の表示設定

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'

