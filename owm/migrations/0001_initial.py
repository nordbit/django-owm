# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Weather'
        db.create_table(u'owm_weather', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, db_index=True, blank=True)),
            ('values', self.gf('jsonfield.fields.JSONField')(default={})),
        ))
        db.send_create_signal(u'owm', ['Weather'])

        # Adding model 'Forecast'
        db.create_table(u'owm_forecast', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, db_index=True, blank=True)),
            ('values', self.gf('jsonfield.fields.JSONField')(default={})),
        ))
        db.send_create_signal(u'owm', ['Forecast'])


    def backwards(self, orm):
        # Deleting model 'Weather'
        db.delete_table(u'owm_weather')

        # Deleting model 'Forecast'
        db.delete_table(u'owm_forecast')


    models = {
        u'owm.forecast': {
            'Meta': {'object_name': 'Forecast'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'values': ('jsonfield.fields.JSONField', [], {'default': '{}'})
        },
        u'owm.weather': {
            'Meta': {'object_name': 'Weather'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'values': ('jsonfield.fields.JSONField', [], {'default': '{}'})
        }
    }

    complete_apps = ['owm']