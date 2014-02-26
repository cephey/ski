# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'VeloPrice.image'
        db.delete_column(u'pages_veloprice', 'image')


    def backwards(self, orm):
        # Adding field 'VeloPrice.image'
        db.add_column(u'pages_veloprice', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


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
        u'pages.velolevel': {
            'Meta': {'ordering': "('name',)", 'object_name': 'VeloLevel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'pages.veloprice': {
            'Meta': {'ordering': "('level', 'price')", 'object_name': 'VeloPrice'},
            'holyday': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.VeloLevel']"}),
            'period': ('django.db.models.fields.CharField', [], {'default': "'1h'", 'max_length': '3'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['pages']