from django.contrib import admin
from .models import ECEtopic, ECESubject, ECESubtopic,QuizECESubject, QuizECETopics

# Register your models here.

admin.site.register(ECESubject)
admin.site.register(ECEtopic)
admin.site.register(ECESubtopic)
admin.site.register(QuizECESubject)
admin.site.register(QuizECETopics)


