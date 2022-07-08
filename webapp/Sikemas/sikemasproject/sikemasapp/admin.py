from django.contrib import admin


from sikemasapp.models import Opd, People, Responden, Service, SikemasappQuestionnaire, Staff

admin.site.site_header = ('DATABASE_SIKEMAS')


class opd(admin.ModelAdmin):
    list_display = ('opd_id', 'opd_name', 'opd_province',
                    'opd_city', 'opd_address')
    search_fields = ('opd_name', 'opd_id')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    site_title = ("LIST_OPD")

class responden(admin.ModelAdmin):
    list_display = ('people_id', 'question_id', 'answer')
    search_fields = ('people_id', 'question_id', 'answer')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    site_title = ("LIST_Responden")
    
# Register your models here.
admin.site.register(Opd,opd)
admin.site.register(Responden)
