# Generated by Django 2.2.14 on 2020-07-13 12:00

from django.db import migrations

ABOUT_PAGE_SLUG = "about"


def forwards(apps, schema_editor):
    ContentPage = apps.get_model("content", "ContentPage")

    ContentPage.objects.filter(slug=ABOUT_PAGE_SLUG).update(show_in_menus=False)


def backwards(apps, schema_editor):
    ContentPage = apps.get_model("content", "ContentPage")
    ContentPage.objects.filter(slug=ABOUT_PAGE_SLUG).update(show_in_menus=True)


class Migration(migrations.Migration):

    dependencies = [("content", "0013_make_sidebar_optional")]

    operations = [migrations.RunPython(forwards, backwards)]
