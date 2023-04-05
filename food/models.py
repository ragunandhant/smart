from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_image',blank = True,null=True)
    class Meta:
        verbose_name_plural = 'categories'
    def __str__(self) -> str:
        return self.name
class Item(models.Model):
    def __str__(self):
        return self.name
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    description = models.TextField(blank=True,null=True)
    price= models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='item_image',blank = True,null=True)
