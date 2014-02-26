# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'VeloPrice'
        db.create_table(u'pages_veloprice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('period', self.gf('django.db.models.fields.CharField')(default='1h', max_length=3)),
            ('price', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('holyday', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['VeloPrice'])


    def backwards(self, orm):
        # Deleting model 'VeloPrice'
        db.delete_table(u'pages_veloprice')


    models = {
        u'pages.servicestext': {
            'Meta': {'ordering': "('order',)", 'object_name': 'ServicesText'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'url_path': ('django.db.models.fields.CharField', [], {'default': "'/'", 'max_length': '32'})
        },
        u'pages.veloprice': {
            'Meta': {'ordering': "('level', 'period')", 'object_name': 'VeloPrice'},
            'holyday': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'period': ('django.db.models.fields.CharField', [], {'default': "'1h'", 'max_length': '3'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['pages']