# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Attribute.tag'
        db.alter_column('spektrix_attribute', 'tag', self.gf('django.db.models.fields.SlugField')(max_length=255))


    def backwards(self, orm):
        
        # Changing field 'Attribute.tag'
        db.alter_column('spektrix_attribute', 'tag', self.gf('django.db.models.fields.SlugField')(max_length=50))


    models = {
        'base.audio': {
            'Meta': {'ordering': "['order']", 'object_name': 'Audio'},
            'audio': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'base.file': {
            'Meta': {'ordering': "['order']", 'object_name': 'File'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'base.image': {
            'Meta': {'ordering': "['order']", 'object_name': 'Image'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'base.sponsor': {
            'Meta': {'ordering': "['order']", 'object_name': 'Sponsor'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'base.video': {
            'Meta': {'ordering': "['order']", 'object_name': 'Video'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'provider': ('django.db.models.fields.TextField', [], {'max_length': '10'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'events.event': {
            'Description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Duration': ('django.db.models.fields.IntegerField', [], {}),
            'FirstInstance': ('django.db.models.fields.DateTimeField', [], {}),
            'Html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'ImageUrl': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'LastInstance': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'ordering': "['FirstInstance', 'LastInstance', 'Name']", 'object_name': 'Event'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'OnSaleOnWeb': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ThumbnailUrl': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'WebEventId': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_override': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'featured_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'flickr': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_moderated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'price': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'short_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'spektrix.attribute': {
            'Meta': {'object_name': 'Attribute'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'Value': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'tag': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'spektrix.time': {
            'Capacity': ('django.db.models.fields.IntegerField', [], {}),
            'EventInstanceId': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'Meta': {'ordering': "['Time']", 'object_name': 'Time'},
            'OnSaleOnWeb': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'SeatsAvailable': ('django.db.models.fields.IntegerField', [], {}),
            'SeatsLocked': ('django.db.models.fields.IntegerField', [], {}),
            'SeatsReserved': ('django.db.models.fields.IntegerField', [], {}),
            'SeatsSelected': ('django.db.models.fields.IntegerField', [], {}),
            'SeatsSold': ('django.db.models.fields.IntegerField', [], {}),
            'Time': ('django.db.models.fields.DateTimeField', [], {}),
            'WebInstanceId': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Times'", 'to': "orm['events.Event']"})
        }
    }

    complete_apps = ['spektrix']
