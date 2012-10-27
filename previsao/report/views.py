from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from models import ReportDay

def home(request):
	waves = make_wave_report_string()
	winds = make_wind_report_string()
	return render(request, 'report/chart.html', {"data_waves" : waves, "data_winds" : winds } )


def make_wave_report_string( ):
	str = "data : [ "
	for rd in ReportDay.objects.all():
		for x in range(0, 5):
			if x == 0:
				str = str + "%s," % make_wave_report( rd.date, '05', rd.fiveAM.waveReport)
			elif x == 1:
				str = str + "%s," % make_wave_report( rd.date, '08', rd.eightAM.waveReport)
			elif x == 2:
				str = str + "%s," % make_wave_report( rd.date, '11', rd.elevenAM.waveReport)
			elif x == 3:
				str = str + "%s," % make_wave_report( rd.date, '14', rd.twoPM.waveReport)
			elif x == 4:
				str = str + "%s," % make_wave_report( rd.date, '17', rd.fivePM.waveReport)
			elif x == 5:
				str = str + "%s," % make_wave_report( rd.date, '20', rd.eightPM.waveReport)

	return str + " ]"

def make_wind_report_string( ):
	str = "data : [ "
	for rd in ReportDay.objects.all():
		for x in range(0, 5):
			if x == 0:
				str = str + "%s," % make_wind_report( rd.date, '05', rd.fiveAM.windReport)
			elif x == 1:
				str = str + "%s," % make_wind_report( rd.date, '08', rd.eightAM.windReport)
			elif x == 2:
				str = str + "%s," % make_wind_report( rd.date, '11', rd.elevenAM.windReport)
			elif x == 3:
				str = str + "%s," % make_wind_report( rd.date, '14', rd.twoPM.windReport)
			elif x == 4:
				str = str + "%s," % make_wind_report( rd.date, '17', rd.fivePM.windReport)
			elif x == 5:
				str = str + "%s," % make_wind_report( rd.date, '20', rd.eightPM.windReport)

	return str + " ]"

def make_wave_report( report_date, report_hour, waveReport ):
	return "[ new Date(%s, %s, %s, %s, 0, 0), %s]" % (report_date.year, report_date.month, report_date.day, report_hour, waveReport.height)

def make_wind_report( report_date, report_hour, windReport ):	
	return "[ new Date(%s, %s, %s, %s, 0, 0), %s]" %  (report_date.year, report_date.month, report_date.day, report_hour, windReport.intensity)
