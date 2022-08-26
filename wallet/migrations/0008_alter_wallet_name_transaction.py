# Generated by Django 4.1 on 2022-08-26 11:53

from django.db import migrations, models
import django.db.models.deletion
import wallet.models


class Migration(migrations.Migration):

    dependencies = [
        ("wallet", "0007_alter_wallet_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wallet",
            name="name",
            field=models.CharField(
                default=wallet.models.get_uuid,
                editable=False,
                max_length=8,
                unique=True,
            ),
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "transfer_amount",
                    models.DecimalField(decimal_places=2, max_digits=14),
                ),
                ("commission", models.DecimalField(decimal_places=2, max_digits=14)),
                (
                    "status",
                    models.CharField(
                        choices=[("PAID", "Paid"), ("FAILED", "Failed")], max_length=6
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "receiver",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="reciever",
                        to="wallet.wallet",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="sender",
                        to="wallet.wallet",
                    ),
                ),
            ],
        ),
    ]