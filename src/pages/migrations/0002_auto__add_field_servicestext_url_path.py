# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ServicesText.url_path'
        db.add_column(u'pages_servicestext', 'url_path',
                      self.gf('django.db.models.fields.CharField')(default='/', max_length=32),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ServicesText.url_path'
        db.delete_column(u'pages_servicestext', 'url_path')


    models = {
        u'pages.servicestext': {
            'Meta': {'ordering': "('order',)", 'object_name': 'ServicesText'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'url_path': ('django.db.models.fields.CharField', [], {'default': "'/'", 'max_length': '32'})
        }
    }

    complete_apps = ['pages']