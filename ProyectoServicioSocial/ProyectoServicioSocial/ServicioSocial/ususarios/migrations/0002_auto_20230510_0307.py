# Generated by Django 3.2.19 on 2023-05-10 03:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ususarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datospersonales',
            name='ap_materno',
        ),
        migrations.RemoveField(
            model_name='datospersonales',
            name='ap_paterno',
        ),
        migrations.RemoveField(
            model_name='datospersonales',
            name='fecha_nac',
        ),
        migrations.RemoveField(
            model_name='datospersonales',
            name='nombre',
        ),
        migrations.AddField(
            model_name='datospersonales',
            name='rfc',
            field=models.CharField(default=1, max_length=13, validators=[django.core.validators.RegexValidator(code='curp_invalido', message='La CURP no tiene un formato válido.', regex='/^([A-Z][AEIOUX][A-Z]{2}\\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\\d])(\\d)$/')], verbose_name='C.U.R.P.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datospersonales',
            name='telefono',
            field=models.CharField(default=4920000000, max_length=10, verbose_name='Teléfono'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='datospersonales',
            name='foto',
            field=models.ImageField(upload_to='perfil'),
        ),
        migrations.AlterField(
            model_name='datospersonales',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='datos', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
