from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(BookReadedChartData)
admin.site.register(SiteVisitedChartData)
admin.site.register(UserBookReadedChart)
admin.site.register(UserSiteVisitedChart)
admin.site.register(AccessBook)
admin.site.register(ReadedBook)