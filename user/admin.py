from django.contrib import admin

# Register your models here.


from .models import Athlete, Article, UserActivity

admin.site.register(Athlete)
admin.site.register(Article)
admin.site.register(UserActivity)
