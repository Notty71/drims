from django.db import models
from django.contrib.auth.models import User
# Create your models here.


from django.db import models 
from django.contrib.auth.models import AbstractUser 
from django.utils.translation import ugettext_lazy as _ 
from django.conf import settings 
from datetime import date 

TYPE = (('1','Marchent'),('2','Buyer'))

class User(AbstractUser): 
	username = models.CharField(max_length = 50, blank = True, null = True, unique = True) 
	email = models.EmailField(_('email address'), unique = True) 
	native_name = models.CharField(max_length = 5) 
	phone_no = models.CharField(max_length = 10, unique = True) 
	adress = models.ForeignKey('Adress', on_delete=models.PROTECT)
	user_type = models.CharField(choices=TYPE, max_length=20)
	picture = models.ImageField(upload_to='images/%y/%m/%d', blank=True, null=True)
	bio = models.TextField(null=True, blank=True)
	USERNAME_FIELD = 'phone_no'
	REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'adress', 'native_name'] 
	def __str__(self): 
		return "{}".format(self.email)

# class Profile(models.Model):

# 	TYPE = (('1','Marchent'),('2','Buyer'))

# 	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
# 	phone = models.CharField(max_length=15)
# 	adress = models.ForeignKey('Adress', on_delete=models.PROTECT)
# 	user_type = models.CharField(choices=TYPE, max_length=20)
# 	picture = models.ImageField(upload_to='images/%y/%m/%d', blank=True, null=True)
# 	bio = models.TextField(null=True, blank=True)



# 	is_active = models.BooleanField(default=True)
# 	created = models.DateTimeField(auto_now_add=True)
# 	updated = models.DateTimeField(auto_now=True)


# 	def __str__(self):
# 		return self.user.username


class Adress(models.Model):
	adress = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.adress

