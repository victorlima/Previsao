# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ReportDay.date'
        db.add_column('report_reportday', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 10, 27, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ReportDay.date'
        db.delete_column('report_reportday', 'date')


    models = {
        'report.report': {
            'Meta': {'object_name': 'Report'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tideReport': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['report.TideReport']"}),
            'waveReport': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['report.WaveReport']"}),
            'windReport': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['report.WindReport']"})
        },
        'report.reportday': {
            'Meta': {'object_name': 'ReportDay'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'eightAM': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'eightAM_report'", 'to': "orm['report.Report']"}),
            'eightPM': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'eightPM_report'", 'to': "orm['report.Report']"}),
            'elevenAM': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'elevenAM_report'", 'to': "orm['report.Report']"}),
            'fiveAM': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fiveAM_report'", 'to': "orm['report.Report']"}),
            'fivePM': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fivePM_report'", 'to': "orm['report.Report']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'twoPM': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'twoPM_report'", 'to': "orm['report.Report']"})
        },
        'report.tidereport': {
            'Meta': {'object_name': 'TideReport'},
            'height': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'report.wavereport': {
            'Meta': {'object_name': 'WaveReport'},
            'direction': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'report.windreport': {
            'Meta': {'object_name': 'WindReport'},
            'direction': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intensity': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        }
    }

    complete_apps = ['report']