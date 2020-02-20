# Generated by Django 3.0.3 on 2020-02-20 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac_scraper', '0002_facdocument_audit'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facdocument',
            options={'ordering': ('dbkey', 'audit_year', '-version', 'file_type')},
        ),
        migrations.AddIndex(
            model_name='facdocument',
            index=models.Index(fields=['dbkey', 'audit_year'], name='fac_scraper_dbkey_61fe0c_idx'),
        ),
    ]
