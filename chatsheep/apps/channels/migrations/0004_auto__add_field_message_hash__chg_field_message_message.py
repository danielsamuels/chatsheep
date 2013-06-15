# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Message.hash'
        db.add_column('channels_message', 'hash',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1000),
                      keep_default=False)


        # Changing field 'Message.message'
        db.alter_column('channels_message', 'message', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # Deleting field 'Message.hash'
        db.delete_column('channels_message', 'hash')


        # Changing field 'Message.message'
        db.alter_column('channels_message', 'message', self.gf('django.db.models.fields.CharField')(max_length=1000))

    models = {
        'channels.channel': {
            'Meta': {'object_name': 'Channel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'channels.message': {
            'Meta': {'object_name': 'Message'},
            'channel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['channels.Channel']"}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'hash': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['channels']