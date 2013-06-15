# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WhitelistedWord'
        db.create_table('channels_whitelistedword', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('channel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['channels.Channel'])),
            ('word', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('channels', ['WhitelistedWord'])

        # Adding field 'Message.sender'
        db.add_column('channels_message', 'sender',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1000),
                      keep_default=False)

        # Adding index on 'Message', fields ['hash']
        db.create_index('channels_message', ['hash'])


    def backwards(self, orm):
        # Removing index on 'Message', fields ['hash']
        db.delete_index('channels_message', ['hash'])

        # Deleting model 'WhitelistedWord'
        db.delete_table('channels_whitelistedword')

        # Deleting field 'Message.sender'
        db.delete_column('channels_message', 'sender')


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