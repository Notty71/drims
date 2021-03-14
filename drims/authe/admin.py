from django.contrib import admin
from .models import Adress
# Register your models here.

from django.contrib import admin 
from django.utils.translation import ugettext_lazy as _ 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 
from django.contrib.auth import get_user_model 
from django.contrib.auth.admin import UserAdmin 
from .models import User 
from django.contrib.auth.forms import UserChangeForm
class UserAdmin(BaseUserAdmin): 
	form = UserChangeForm
	fieldsets = ( 
	(None, {'fields': ('phone_no', 'password', )}), 
	(_('Personal info'), {'fields': ('email','adress','user_type')}), 
	(_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }), 
	(_('Important dates'), {'fields': ('last_login', 'date_joined')}), 
	(_('user_info'), {'fields': ('native_name', 'phone_no', 'adress','user_type','picture')}), 
	) 
	add_fieldsets = ( 
	(None, { 
	'classes': ('wide', ), 
	'fields': ('phone_no','password1', 'password2'), 
	}), 
	) 
	list_display = ['email', 'first_name', 'last_name', 'is_staff', "native_name", "phone_no"] 
	search_fields = ('email', 'first_name', 'last_name') 
	ordering = ('email', ) 
	admin.site.register(User, UserAdmin) 



# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
# 	list_disply = ['user','phone','user_type','adress','is_active']# Register your models here.
@admin.register(Adress)
class AdressAdmin(admin.ModelAdmin):
	list_disply = ['adress']

