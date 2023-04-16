from django.contrib import admin
from users.models import NewUser
from django.contrib.auth.admin import UserAdmin


# class UserAdminConfig(UserAdmin):
#     model = NewUser
#     search_fields = ('email','user_name','first_name')
#     list_filter = ('email','user_name','first_name','is_active','is_staff')
#     ordering = ('-start_date')
#     list_display = ('email', 'id' ,'user_name','first_name','is_active','is_staff')
#     fieldsets = (
#         (None , {'fields': ('email','user_name','first_name')}),
#         ('permissions', {'fields': ('is_staff','is_active')}),
#     )



admin.site.register(NewUser)