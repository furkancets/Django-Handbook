from django.db import models

"""
5. User nesnesi localhost:8000/admin gittiğimiz yerin databases de defaul oluşturulmuş modelidir.
"""

from django.contrib.auth.models import User

# Create your models here.

"""
3. Category class'ı.
"""

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)

"""
1. Öncelikle MenuItem'ı kurmaya başladım. Burayı kurarken ileride search yapma ihtimalimiz olan yerlere db_index=True dedim ki. Kullanı olarak o search 
querylerine daha hızlı erişelim. Ama tabi indexlerin databases'de alan tutması gibi bir dezavantajı olduğundan dolayı. Gerçekten gerekli yerlerde kullanmaya
çalıştım.

2. En alttaki category ForeignKey ilan etmeden önce Category class'ını oluşturdum.

4. category nesnesini farklı bir class'a referans vererek(ForeignKey) oluştururken on_delete'i model.PROTECT'e çektik. Çünkü herhangi bir ürün 
silinmeye çalışıldığında ona bağlı olan kategorilerin tamamen silinmesini engellemek istiyoruz.
"""

class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(db_index=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT) 
    
"""
6. Beşinci madded açıkladığım User nesnesini burada çağırıyoruz. Bu sefer models.CASCADE yaparak, bir kullanıcı hesabı silinirse, 
o kullanıcıya bağlı olan tüm alışveriş sepeti kayıtları da silinir.
7. bu kod parçasında user ve menuitem alanları birleştirilerek benzersiz birleşim elde edilir. Bu, aynı kullanıcının aynı menü öğesi için yalnızca 
bir kez sipariş vermesine izin verir, ancak farklı menü öğeleri için farklı siparişler verebilir.
"""

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2) 
    
    class Meta:
         unique_together = ('menuitem', 'user')
        
"""
8.on_delete=models.SET_NULL ayarı, bir kullanıcı silindiğinde, delivery_crew alanındaki ilgili kayıtların NULL olarak ayarlanacağı anlamına gelir. 
Yani, delivery_crew alanında bir kullanıcı silinirse, ilişkili kayıtların NULL olarak ayarlanması için bu ayar yapılır.

9. delivery_crew alanını kullandığınızda, User modeline erişmek için delivery_crew.user yerine delivery_crew.delivery_crew kullanılabilir. 
related_name ayarı, bu kullanımı daha uygun hale getirir.
"""
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="delivery_crew", null=True)
    status = models.BooleanField(default=0, db_index=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    date = models.DateField(db_index=True)
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta:
        unique_together = ('order', 'menuitem')
    