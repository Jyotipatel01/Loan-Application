from django.contrib import admin
from .models import loan_application
# Register your models here.

# class courseAdmin(admin.ModelAdmin):
#     search_fields=('name','price')
#     list_display=('name','description','price','duration','rating')
#     list_filter = ('rating', 'duration', 'price')
    
#admin.site.register(course,courseAdmin)
class courseAdmin(admin.ModelAdmin):
    pass
admin.site.register(loan_application,courseAdmin)

    