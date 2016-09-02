from django.contrib import admin

from .models import Question

admin.site.register(Question)

admin.site.site_title = 'WeVoice Admin'
admin.site.site_header = 'WeVoice Admin'
