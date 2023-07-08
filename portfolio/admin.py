from django.contrib import admin
# Importing classes from models.py
from .models import Projects, Social, MyInfo,Skills

admin.site.register(Projects)
admin.site.register(Social)
admin.site.register(MyInfo)
admin.site.register(Skills)

