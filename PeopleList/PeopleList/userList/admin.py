from django.contrib import admin
from .models import User, Skill
# Register your models here.



class UserAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
    filter_horizontal = ('user_skills',)



class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


admin.site.register(Skill, SkillAdmin)
admin.site.register(User, UserAdmin)





#
# admin.site.register(User)
# admin.site.register(Skill)
