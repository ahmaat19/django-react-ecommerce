from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(
            name = "admin",
            email = "ahmaat19@gmail.com",
            is_staff = True,
            is_superuser = True,
            phone = "615301507",
            gender = "Male"
        )

        user.set_password("admin1234")
        user.save()

    dependencies = [
    
    ]   

    operations = [
        migrations.RunPython(seed_data),
    ]