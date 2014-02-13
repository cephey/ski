# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'SolarEvent'
        db.delete_table(u'weather_solarevent')


    def backwards(self, orm):
        # Adding model 'SolarEvent'
        db.create_table(u'weather_solarevent', (
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('sunset', self.gf('django.db.models.fields.DateTimeField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sunrise', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'weather', ['SolarEvent'])


    models = {
        
    }

    complete_apps = ['weather']