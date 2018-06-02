from django.contrib import admin
from tag.models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    pass
class ProjectAdmin(admin.ModelAdmin):
    pass
class RepositoriesAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin )
admin.site.register(Project, ProjectAdmin )
admin.site.register(Repository, RepositoriesAdmin )