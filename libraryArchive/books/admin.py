from django.contrib import admin

from .models import Author, Tag, Book

admin.site.register(Tag)
admin.site.register(Book)
