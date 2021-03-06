# Generated by Django 3.0.2 on 2020-01-23 18:50

import compositefk.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_cfda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finding',
            fields=[
                ('elec_audit_findings_id', models.IntegerField(help_text='C system generated sequence number for finding', primary_key=True, serialize=False)),
                ('dbkey', models.CharField(help_text='Audit Year and DBKEY (database key) combined make up the primary key.', max_length=6)),
                ('audit_year', models.DecimalField(decimal_places=0, help_text='Audit Year and DBKEY (database key) combined make up the primary key.', max_digits=4)),
                ('finding_ref_nums', models.CharField(help_text='Findings Reference Numbers', max_length=100)),
                ('type_requirement', models.CharField(blank=True, help_text='Type Requirement Failure', max_length=256, null=True)),
                ('modified_opinion', models.BooleanField(help_text='Modified Opinion finding', null=True)),
                ('other_noncompliance', models.BooleanField(help_text='Other Noncompliance finding', null=True)),
                ('material_weakness', models.BooleanField(help_text='Material Weakness finding', null=True)),
                ('significant_deficiency', models.BooleanField(help_text='Significant Deficiency finding', null=True)),
                ('other_findings', models.BooleanField(help_text='Other findings', null=True)),
                ('questioned_costs', models.BooleanField(help_text='Questioned Costs', null=True)),
                ('repeat_finding', models.BooleanField(help_text='Indicates whether or not the audit finding was a repeat of an audit finding in the immediate prior audit', null=True)),
                ('prior_finding_ref_nums', models.CharField(blank=True, help_text='Audit finding reference numbers from the immediate prior audit', max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='assistancelisting',
            name='id',
        ),
        migrations.RemoveField(
            model_name='cfda',
            name='id',
        ),
        migrations.AddField(
            model_name='audit',
            name='cfda',
            field=compositefk.fields.CompositeForeignKey(default=None, null_if_equal=[], on_delete=django.db.models.deletion.DO_NOTHING, to='data.CFDA', to_fields={'audit_year': compositefk.fields.LocalFieldValue('audit_year'), 'dbkey': compositefk.fields.LocalFieldValue('dbkey')}),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assistancelisting',
            name='program_number',
            field=models.CharField(help_text='Program Number', max_length=6, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cfda',
            name='cfda',
            field=models.ForeignKey(db_constraint=False, help_text='Federal Agency Prefix and Extension', max_length=52, on_delete=django.db.models.deletion.DO_NOTHING, to='data.AssistanceListing'),
        ),
        migrations.AlterField(
            model_name='cfda',
            name='elec_audits_id',
            field=models.IntegerField(help_text='FAC system generated sequence number used to link to Findings data between CFDA Info and Findings', primary_key=True, serialize=False),
        ),
        migrations.AddIndex(
            model_name='audit',
            index=models.Index(fields=['audit_year', 'dbkey'], name='data_audit_audit_y_b55533_idx'),
        ),
        migrations.AddIndex(
            model_name='audit',
            index=models.Index(fields=['fac_accepted_date'], name='data_audit_fac_acc_b554be_idx'),
        ),
        migrations.AddIndex(
            model_name='audit',
            index=models.Index(fields=['audit_year'], name='data_audit_audit_y_2d4cd9_idx'),
        ),
        migrations.AddIndex(
            model_name='audit',
            index=models.Index(fields=['dbkey'], name='data_audit_dbkey_1f6a2c_idx'),
        ),
        migrations.AddIndex(
            model_name='cfda',
            index=models.Index(fields=['audit_year', 'dbkey'], name='data_cfda_audit_y_17c884_idx'),
        ),
        migrations.AddField(
            model_name='finding',
            name='elec_audits',
            field=models.ForeignKey(db_constraint=False, help_text='FAC system generated sequence number used to link to Findings data between CFDA Info and Findings', on_delete=django.db.models.deletion.DO_NOTHING, to='data.CFDA'),
        ),
        migrations.AddIndex(
            model_name='finding',
            index=models.Index(fields=['audit_year', 'dbkey'], name='data_findin_audit_y_556a85_idx'),
        ),
        migrations.AddIndex(
            model_name='finding',
            index=models.Index(fields=['elec_audits_id'], name='data_findin_elec_au_8cb44d_idx'),
        ),
    ]
