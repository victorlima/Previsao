from django.contrib import admin
from report.models import ReportDay, Report, WaveReport, WindReport, TideReport

class ReportDayAdmin( admin.ModelAdmin ):
	pass

class ReportAdmin( admin.ModelAdmin ):
	pass

class WaveReportAdmin( admin.ModelAdmin ):
	pass

class WindReportAdmin( admin.ModelAdmin ):
	pass

class TideReportAdmin( admin.ModelAdmin ):
	pass


admin.site.register(ReportDay, ReportDayAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(WaveReport, WaveReportAdmin)
admin.site.register(WindReport, WindReportAdmin)
admin.site.register(TideReport, TideReportAdmin)