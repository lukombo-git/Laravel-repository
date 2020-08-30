from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Candidates)
admin.site.register(Vagas)
admin.site.register(DownloadFile)
admin.site.register(Curriculums)