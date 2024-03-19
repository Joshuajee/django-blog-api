from django.contrib import admin
from .models import User
# Register your models here.


admin.site.register(User)

class PersonAdmin(admin.ModelAdmin):
    search_fields = ('username',)