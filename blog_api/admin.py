from django.contrib import admin

class PersonAdmin(admin.ModelAdmin):
    search_fields = ('username',)