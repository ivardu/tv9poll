from django.contrib import admin
from .models import Question, Answer

# Register your models here.

class AnswersInline(admin.TabularInline):
    model = Answer
    fields = ['yes','no']
    extra = 0 #will remove the extra empty rows from django-admin page

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question','pub_date', 'get_question_id')
    list_filter = ('pub_date',)
    search_fields = ('question',)
    fieldsets = [
        (None, {'fields':['question']}),
        ('Published Date', {'fields':['pub_date']})
    ]
    inlines = [AnswersInline]
    


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Answer)
admin.AdminSite.site_header = 'Tv9 Polls Admin Page'
admin.AdminSite.site_title = 'Tv9 Polls Admin Page'