from django.db import models
from django.contrib.auth.models import User

class Peoplesdata(models.Model):
    radif = models.CharField(max_length = 100)
    fullname = models.CharField(max_length = 100 , default='name')
    groupnumber = models.IntegerField()
    tedadhesab = models.IntegerField()
    mandeghabli = models.IntegerField()
    mablaghghest = models.IntegerField()
    pardakhti = models.IntegerField()

    ozviyat = models.IntegerField(default=0)
    moavagemahiyane = models.IntegerField(default=0)
    mandesincemahegabl = models.IntegerField(default=0)
    
    Tozihat = models.CharField(max_length = 100 , default='empty')
    kodemeli = models.IntegerField()
    # slug = models.SlugField()

    # author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    def __str__(self):
        return self.fullname