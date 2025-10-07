from django.contrib import admin
from .models import Watch, WatchType, WatchImage

class WatchImageInline(admin.TabularInline):
    model = WatchImage
    extra = 1  # عدد الصور الإضافية اللي بتظهر تلقائيًا

class WatchAdmin(admin.ModelAdmin):
    inlines = [WatchImageInline]

admin.site.register(WatchType)
admin.site.register(Watch, WatchAdmin)