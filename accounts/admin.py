from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    
    # 2. Clicking these columns will open the detail page
    list_display_links = ('email', 'first_name', 'last_name')
    
    # 3. Fields that are completely read-only on the detail page
    readonly_fields = ('last_login', 'date_joined')
    
    # 4. Ordering the list (newest users first)
    ordering = ('-date_joined',)

    # 5. CRUCIAL: Overriding these tells Django NOT to look for default groups/permissions
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Register your models here.
admin.site.register(Account,AccountAdmin) 