# Generated by Django 5.0.7 on 2024-07-29 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_rename_note_desc_note_note_descr_alter_note_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='note_descr',
            new_name='notedescr',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='note_title',
            new_name='notetitle',
        ),
    ]
