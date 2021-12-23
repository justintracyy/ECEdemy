from django.contrib import admin
from .models import ECEtopic, ECESubject, ECESubtopic,QuizECESubject, QuizECETopics

# Register your models here.
class ECEtopicInline(admin.TabularInline):
    model = ECEtopic
    fields = ('ece_topic',)
    extra = 1


@admin.register(ECESubject)
class ECESubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'ece_subject', 'created_at', 'updated_at' )
    list_per_page = 50
    ordering = ('-ece_subject',)
    search_fields = ('ece_subject',)
    readonly_fields = ('created_at', 'updated_at')
    inlines = (ECEtopicInline,)


class ECESubtopicsInline(admin.TabularInline):
    model = ECESubtopic
    fields = ('ece_subtopic',)
    extra = 1



@admin.register(ECEtopic)
class ECEtopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'ece_topic', 'created_at', 'updated_at' )
    list_per_page = 50
    ordering = ('-ece_topic',)
    search_fields = ('ece_topic',)
    list_filter = ('ece_subject',)
    readonly_fields = ('created_at', 'updated_at', 'ece_subject',)
    inlines = (ECESubtopicsInline,)


admin.site.register(QuizECESubject)


