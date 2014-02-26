# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'VeloPeroid'
        db.create_table(u'pages_veloperoid', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'pages', ['VeloPeroid'])


        # Renaming column for 'VeloPrice.period' to match new field type.
        db.rename_column(u'pages_veloprice', 'period', 'period_id')
        # Changing field 'VeloPrice.period'
        db.alter_column(u'pages_veloprice', 'period_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.VeloPeroid']))
        # Adding index on 'VeloPrice', fields ['period']
        db.create_index(u'pages_veloprice', ['period_id'])


    def backwards(self, orm):
        # Removing index on 'VeloPrice', fields ['period']
        db.delete_index(u'pages_veloprice', ['period_id'])

        # Deleting model 'VeloPeroid'
        db.delete_table(u'pages_veloperoid')


        # Renaming column for 'VeloPrice.period' to match new field type.
        db.rename_column(u'pages_veloprice', 'period_id', 'period')
        # Changing field 'VeloPrice.period'
        db.alter_column(u'pages_veloprice', 'period', self.gf('django.db.models.fields.CharField')(max_length=3))

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