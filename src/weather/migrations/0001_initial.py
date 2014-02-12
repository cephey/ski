# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SolarEvent'
        db.create_table(u'weather_solarevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('sunrise', self.gf('django.db.models.fields.DateTimeField')()),
            ('sunset', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'weather', ['SolarEvent'])


    def backwards(self, orm):
        # Deleting model 'SolarEvent'
        db.delete_table(u'weather_solarevent')


    models = {
        u'weather.solarevent': {
            'Meta': {'object_name': 'SolarEvent'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sunrise': ('django.db.models.fields.DateTimeField', [], {}),
            'sunset': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['weather']