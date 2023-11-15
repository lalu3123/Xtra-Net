from django.contrib import admin

from user.models import Support_Engineer_tab,Issue_Tab,Status_Tab,ESCALATION_Tab,data_Tab

# Register your models here.
admin.site.register(Support_Engineer_tab)
admin.site.register(Issue_Tab)
admin.site.register(Status_Tab)
admin.site.register(ESCALATION_Tab)
admin.site.register(data_Tab)
