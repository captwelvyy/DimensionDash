from django.contrib import admin
from .models import Review, UserScore

admin.site.register(Review)
admin.site.register(UserScore)