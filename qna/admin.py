from django.contrib import admin

from qna.models import Answer, Question

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)