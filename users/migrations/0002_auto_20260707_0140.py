from django.db import migrations


def update_names(apps, schema_editor):
    DummyUser = apps.get_model("users", "DummyUser")

    for user in DummyUser.objects.all():
        user.name = f"User - {user.name}"
        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(update_names),
    ]