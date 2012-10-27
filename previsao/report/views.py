from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from models import ReportDay

def home(request):
	rd = ReportDay.objects.all()[0]
	waves = make_wave_report_string( rd )
	winds = make_wind_report_string( rd )
	return render(request, 'report/chart.html', {"data_waves" : waves, "data_winds" : winds } )


def make_wave_report_string( rd ):
	return "data : [[ new Date(%s, %s, %s, %s, 0, 0), %s], [ new Date(%s, %s, %s, %s, 0, 0), %s], [ new Date(%s, %s, %s, %s, 0, 0), %s], [ new Date(%s, %s, %s, %s, 0, 0), %s], [ new Date(%s, %s, %s, %s, 0, 0), %s]]" % (rd.date.year, rd.date.month, rd.date.day, '5', rd.fiveAM.waveReport.height, rd.date.year, rd.date.month, rd.date.day, '8', rd.eightAM.waveReport.height, rd.date.year, rd.date.month, rd.date.day, '11', rd.elevenAM.waveReport.height, rd.date.year, rd.date.month, rd.date.day, '14', rd.twoPM.waveReport.height, rd.date.year, rd.date.month, rd.date.day, '17', rd.fivePM.waveReport.height)

def make_wind_report_string( rd ):
	return "data : [[ new Date(%s, %s, %s, %s, 0, 0), %s], [ new Date(%s, %s, %s, %s, 0, 0), %s], [ new Date(%s, %s, %s, %s, 0, 0), %s], [ new Date(%s, %s, %s, %s, 0, 0), %s], [ new Date(%s, %s, %s, %s, 0, 0), %s]]" % (rd.date.year, rd.date.month, rd.date.day, '5', rd.fiveAM.windReport.intensity, rd.date.year, rd.date.month, rd.date.day, '8', rd.eightAM.windReport.intensity, rd.date.year, rd.date.month, rd.date.day, '11', rd.elevenAM.windReport.intensity, rd.date.year, rd.date.month, rd.date.day, '14', rd.twoPM.windReport.intensity, rd.date.year, rd.date.month, rd.date.day, '17', rd.fivePM.windReport.intensity)
