from django.contrib import admin
from .models import ToDo
from .models import Books

admin.site.register(ToDo)
admin.site.register(Books)