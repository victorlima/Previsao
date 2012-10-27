# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WaveReport'
        db.create_table('report_wavereport', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('direction', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('height', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('period', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('report', ['WaveReport'])

        # Adding model 'WindReport'
        db.create_table('report_windreport', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('direction', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('intensity', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('report', ['WindReport'])

        # Adding model 'TideReport'
        db.create_table('report_tidereport', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('height', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('report', ['TideReport'])

        # Adding model 'ReportDay'
        db.create_table('report_reportday', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fiveAM', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fiveAM_report', to=orm['report.Report'])),
            ('eightAM', self.gf('django.db.models.fields.related.ForeignKey')(related_name='eightAM_report', to=orm['report.Report'])),
            ('elevenAM', self.gf('django.db.models.fields.related.ForeignKey')(related_name='elevenAM_report', to=orm['report.Report'])),
            ('twoPM', self.gf('django.db.models.fields.related.ForeignKey')(related_name='twoPM_report', to=orm['report.Report'])),
            ('fivePM', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fivePM_report', to=orm['report.Report'])),
            ('eightPM', self.gf('django.db.models.fields.related.ForeignKey')(related_name='eightPM_report', to=orm['report.Report'])),
        ))
        db.send_create_signal('report', ['ReportDay'])

        # Adding model 'Report'
        db.create_table('report_report', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('waveReport', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['report.WaveReport'])),
            ('windReport', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['report.WindReport'])),
            ('tideReport', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['report.TideReport'])),
        ))
        db.send_create_signal('report', ['Report'])


    def backwards(self, orm):
        # Deleting model 'WaveReport'
        db.delete_table('report_wavereport')

        # Deleting model 'WindReport'
        db.delete_table('report_windreport')

        # Deleting model 'TideReport'
        db.delete_table('report_tidereport')

        # Deleting model 'ReportDay'
        db.delete_table('report_reportday')

        # Deleting model 'Report'
        db.delete_table('report_report')


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