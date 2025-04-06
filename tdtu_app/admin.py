from django.contrib import admin
from .models import News, Banners, Students, Invites, Department, Statistical
from .telegram_utils import send_news_to_telegram

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        send_news_to_telegram(obj)


admin.site.register(News, NewsAdmin)
admin.site.register(Banners)
admin.site.register(Students)
admin.site.register(Invites)
admin.site.register(Department)
admin.site.register(Statistical)
