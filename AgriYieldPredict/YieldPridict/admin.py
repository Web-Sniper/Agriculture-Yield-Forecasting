from django.contrib import admin
from .models import Crops,Feedback
class CropsAdmin(admin.ModelAdmin):
    list_display = ['name','description','duration','season']
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'contact', 'feedback']

admin.site.register(Crops,CropsAdmin)
admin.site.register(Feedback,FeedbackAdmin)
