from django.db import models

DIRECTIONS = (
    ('N', 'North'),
    ('S', 'South'),
    ('W', 'West'),
    ('E', 'East'),
    ('NE', 'NorthEast'),
    ('NW', 'NorthWest'),
    ('SE', 'SouthEasy'),
    ('SW', 'SouthWest')
)

class ReportDay( models.Model ):
	date = models.DateField()
	fiveAM = models.ForeignKey('Report', related_name='fiveAM_report')
	eightAM = models.ForeignKey('Report', related_name='eightAM_report')
	elevenAM = models.ForeignKey('Report', related_name='elevenAM_report')
	twoPM = models.ForeignKey('Report', related_name='twoPM_report')
	fivePM = models.ForeignKey('Report', related_name='fivePM_report')
	eightPM = models.ForeignKey('Report', related_name='eightPM_report')

class Report( models.Model ):
	waveReport = models.ForeignKey('WaveReport')
	windReport = models.ForeignKey('WindReport')
	tideReport = models.ForeignKey('TideReport')

class WaveReport( models.Model ):
	direction = models.CharField(max_length = 3, choices = DIRECTIONS )
	height = models.CharField( max_length = 3 )
	period = models.CharField( max_length = 3 )

class WindReport( models.Model ):
	direction = models.CharField(max_length = 3, choices = DIRECTIONS )
 	intensity = models.CharField( max_length = 3 )

class TideReport( models.Model ):
	height = models.CharField( max_length = 3 )

