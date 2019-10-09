# Generated by Django 2.2.6 on 2019-10-08 13:59

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_add_social_image_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='featured_people',
            field=wagtail.core.fields.StreamField([('person', wagtail.core.blocks.PageChooserBlock(page_type=['people.Person']))], blank=True, help_text='Optional featured people, max. 3', null=True),
        ),
    ]