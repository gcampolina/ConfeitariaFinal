# Generated by Django 4.2.6 on 2023-11-23 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_loja', '0005_remove_pedido_usuario_pedido_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='data_entrega',
            new_name='data_de_entrega',
        ),
    ]
