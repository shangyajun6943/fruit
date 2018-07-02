from django.db import models

class goodsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(isDelete=0) 
class Goods(models.Model):
    goodsname=models.CharField(max_length=40,unique=True)
    price=models.DecimalField(max_digits=7,decimal_places=3)
    goods_status=models.IntegerField(default=1)
    goods_type=models.IntegerField()
    goods_introduce=models.CharField(max_length=255)
    goods_volume=models.IntegerField()
    goods_num=models.IntegerField()
    img1=models.URLField()
    img2=models.URLField()
    shopping_state=models.IntegerField(default=0)
    isDelete=models.IntegerField(default=0)
    goods=goodsManager()

    def __str__(self):
            return self.goodsname
    class Meta:
        db_table='goods'