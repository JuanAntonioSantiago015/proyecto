# Generated by Django 4.2.6 on 2023-10-11 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presentations', '0001_initial'),
        ('suppliers', '0001_initial'),
        ('medicines', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorialMedicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('brand', models.CharField(blank=True, max_length=150, null=True)),
                ('medication_code', models.CharField(blank=True, max_length=25, null=True)),
                ('expiration_date', models.DateField()),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicines.medicamento')),
                ('presentation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='presentations.presentacion')),
                ('supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.proveedor')),
            ],
        ),
    ]
