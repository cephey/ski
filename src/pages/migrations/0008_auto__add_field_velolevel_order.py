# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'VeloLevel.order'
        db.add_column(u'pages_velolevel', 'order',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'VeloLevel.order'
        db.delete_column(u'pages_velolevel', 'order')


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
            'Meta': {'ordering': "('order',)", 'object_name': 'VeloLevel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        u'pages.veloperoid': {
            'Meta': {'ordering': "('name',)", 'object_name': 'VeloPeroid'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'pages.veloprice': {
            'Meta': {'ordering': "('level', 'price')", 'object_name': 'VeloPrice'},
            'holyday': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'velo_price'", 'to': u"orm['pages.VeloLevel']"}),
            'period': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.VeloPeroid']"}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['pages']