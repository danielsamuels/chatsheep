# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Channel.period'
        db.add_column('channels_channel', 'period',
                      self.gf('django.db.models.fields.IntegerField')(default=30),
                      keep_default=False)

        # Adding field 'Channel.frequency'
        db.add_column('channels_channel', 'frequency',
                      self.gf('django.db.models.fields.IntegerField')(default=5),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Channel.period'
        db.delete_column('channels_channel', 'period')

        # Deleting field 'Channel.frequency'
        db.delete_column('channels_channel', 'frequency')


    models = {
        'channels.channel': {
            'Meta': {'object_name': 'Channel'},
            'frequency': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'period': ('django.db.models.fields.IntegerField', [], {'default': '30'})
        },
        'channels.message': {
            'Meta': {'object_name': 'Message'},
            'channel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['channels.Channel']"}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'hash': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'sender': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        'channels.whitelistedword': {
            'Meta': {'object_name': 'WhitelistedWord'},
            'channel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['channels.Channel']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'word': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['channels']