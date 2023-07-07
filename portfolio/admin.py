from django.contrib import admin
# Importing classes from models.py
from .models import Works, Social, MyInfo,Skills

admin.site.register(Works)
admin.site.register(Social)
admin.site.register(MyInfo)
admin.site.register(Skills)

