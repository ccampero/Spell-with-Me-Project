from django.contrib import admin
from .models import Speller, Study, Word

# Register your models here.
admin.site.register(Speller)
admin.site.register(Study)
admin.site.register(Word)
