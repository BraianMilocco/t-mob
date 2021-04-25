from django.contrib import admin

# Register your models here.
from .models import Redirect

# admin.site.register(Redirect)
@admin.register(Redirect)
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at' )