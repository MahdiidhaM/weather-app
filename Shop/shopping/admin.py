from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(User,UserAdmin)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Inside)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Vote)
admin.site.register(Avrage)
