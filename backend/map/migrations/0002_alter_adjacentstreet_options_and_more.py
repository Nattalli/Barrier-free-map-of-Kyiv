# Generated by Django 4.1 on 2023-11-11 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("map", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="adjacentstreet",
            options={
                "verbose_name": "Прилегла вулиця",
                "verbose_name_plural": "Прилеглі вулиці",
            },
        ),
        migrations.AlterModelOptions(
            name="commitissue",
            options={
                "verbose_name": "Зафіксована проблема",
                "verbose_name_plural": "Зафіксовані проблеми",
            },
        ),
        migrations.AlterModelOptions(
            name="crosswalk",
            options={
                "verbose_name": "Пішохідний перехід",
                "verbose_name_plural": "Пішохідні переходи",
            },
        ),
        migrations.AlterModelOptions(
            name="crosswalkbenefit",
            options={
                "verbose_name": "Перевага пішохідного переходу",
                "verbose_name_plural": "Переваги пішохідних переходів",
            },
        ),
        migrations.AlterModelOptions(
            name="crosswalkdirection",
            options={
                "verbose_name": "Напрямок пішохідного переходу",
                "verbose_name_plural": "Напрямки пішохідних переходів",
            },
        ),
        migrations.AlterModelOptions(
            name="crosswalkissue",
            options={
                "verbose_name": "Проблема пішохідного переходу",
                "verbose_name_plural": "Проблеми пішохідних переходів",
            },
        ),
        migrations.AlterModelOptions(
            name="sidewalk",
            options={"verbose_name": "Тротуар", "verbose_name_plural": "Тротуари"},
        ),
        migrations.AlterModelOptions(
            name="sidewalkissue",
            options={
                "verbose_name": "Проблема тротуару",
                "verbose_name_plural": "Проблеми тротуарів",
            },
        ),
        migrations.AlterModelOptions(
            name="sidewalkissueborder",
            options={
                "verbose_name": "Проблема кордону тротуару",
                "verbose_name_plural": "Проблеми кордонів тротуарів",
            },
        ),
        migrations.AlterModelOptions(
            name="sidewalkmap",
            options={
                "verbose_name": "Карта тротуарів",
                "verbose_name_plural": "Карти тротуарів",
            },
        ),
        migrations.AlterModelOptions(
            name="street",
            options={"verbose_name": "Вулиця", "verbose_name_plural": "Вулиці"},
        ),
        migrations.AlterField(
            model_name="adjacentstreet",
            name="id",
            field=models.CharField(
                max_length=100, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="adjacentstreet",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Назва"),
        ),
        migrations.AlterField(
            model_name="adjacentstreet",
            name="type",
            field=models.CharField(
                choices=[
                    ("AVENUE", "Проспект"),
                    ("STREET", "Вулиця"),
                    ("BYSTREET", "Бічна вулиця"),
                ],
                max_length=10,
                verbose_name="Тип",
            ),
        ),
        migrations.AlterField(
            model_name="commitissue",
            name="date",
            field=models.DateTimeField(auto_now=True, verbose_name="Дата"),
        ),
        migrations.AlterField(
            model_name="commitissue",
            name="issue",
            field=models.TextField(verbose_name="Проблема"),
        ),
        migrations.AlterField(
            model_name="commitissue",
            name="status",
            field=models.CharField(
                choices=[
                    ("PROCESSED", "Оброблено"),
                    ("INPROCESSING", "В обробці"),
                    ("NEW", "Новий"),
                ],
                max_length=15,
                verbose_name="Статус",
            ),
        ),
        migrations.AlterField(
            model_name="commitissue",
            name="user_email",
            field=models.EmailField(
                max_length=254, verbose_name="Електронна пошта користувача"
            ),
        ),
        migrations.AlterField(
            model_name="commitissue",
            name="username",
            field=models.CharField(max_length=63, verbose_name="Ім'я користувача"),
        ),
        migrations.AlterField(
            model_name="crosswalk",
            name="GPS",
            field=models.CharField(max_length=255, verbose_name="GPS"),
        ),
        migrations.AlterField(
            model_name="crosswalk",
            name="benefits",
            field=models.ManyToManyField(
                related_name="crosswalks",
                to="map.crosswalkbenefit",
                verbose_name="Переваги",
            ),
        ),
        migrations.AlterField(
            model_name="crosswalk",
            name="commit_issues",
            field=models.ManyToManyField(
                related_name="crosswalks",
                to="map.commitissue",
                verbose_name="Зафіксовані проблеми",
            ),
        ),
        migrations.AlterField(
            model_name="crosswalk",
            name="direction",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="map.crosswalkdirection",
                verbose_name="Напрямок",
            ),
        ),
        migrations.AlterField(
            model_name="crosswalk",
            name="issues",
            field=models.ManyToManyField(
                related_name="crosswalks",
                to="map.crosswalkissue",
                verbose_name="Проблеми",
            ),
        ),
        migrations.AlterField(
            model_name="crosswalk",
            name="type",
            field=models.CharField(
                choices=[
                    ("UNDERGROUND", "Підземний"),
                    ("OVERGROUND", "Надземний"),
                    ("BY_ROAD", "Біля дороги"),
                ],
                max_length=15,
                verbose_name="Тип",
            ),
        ),
        migrations.AlterField(
            model_name="crosswalk",
            name="width_in_centimeters",
            field=models.IntegerField(verbose_name="Ширина в сантиметрах"),
        ),
        migrations.AlterField(
            model_name="crosswalkbenefit",
            name="commit_issues",
            field=models.ManyToManyField(
                related_name="benefits",
                to="map.commitissue",
                verbose_name="Зафіксовані проблеми",
            ),
        ),
        migrations.AlterField(
            model_name="crosswalkbenefit",
            name="type",
            field=models.CharField(
                choices=[
                    ("LIFT", "Ліфт"),
                    ("SPECIAL_LIFT", "Спеціальний ліфт"),
                    ("SOCIAL_WORKER", "Соціальний працівник"),
                ],
                max_length=15,
                verbose_name="Тип",
            ),
        ),
        migrations.AlterField(
            model_name="crosswalkdirection",
            name="direction",
            field=models.CharField(
                choices=[
                    ("LEFT", "Ліворуч"),
                    ("RIGHT", "Праворуч"),
                    ("TOP", "Вгору"),
                    ("BOTTOM", "Вниз"),
                ],
                max_length=10,
                verbose_name="Напрямок",
            ),
        ),
        migrations.AlterField(
            model_name="crosswalkdirection",
            name="id",
            field=models.CharField(
                max_length=100, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="crosswalkdirection",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Назва"),
        ),
        migrations.AlterField(
            model_name="crosswalkdirection",
            name="type",
            field=models.CharField(
                choices=[
                    ("AVENUE", "Проспект"),
                    ("STREET", "Вулиця"),
                    ("BYSTREET", "Бічна вулиця"),
                ],
                max_length=10,
                verbose_name="Тип",
            ),
        ),
        migrations.AlterField(
            model_name="crosswalkissue",
            name="border_height_in_centimeters",
            field=models.IntegerField(verbose_name="Висота кордону в сантиметрах"),
        ),
        migrations.AlterField(
            model_name="crosswalkissue",
            name="commit_issues",
            field=models.ManyToManyField(
                related_name="crosswalk_issues",
                to="map.commitissue",
                verbose_name="Зафіксовані проблеми",
            ),
        ),
        migrations.AlterField(
            model_name="sidewalk",
            name="commit_issues",
            field=models.ManyToManyField(
                related_name="sidewalks",
                to="map.commitissue",
                verbose_name="Зафіксовані проблеми",
            ),
        ),
        migrations.AlterField(
            model_name="sidewalk",
            name="crosswalks",
            field=models.ManyToManyField(
                related_name="sidewalks",
                to="map.crosswalk",
                verbose_name="Пішохідні переходи",
            ),
        ),
        migrations.AlterField(
            model_name="sidewalk",
            name="id",
            field=models.CharField(
                max_length=100, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="sidewalk",
            name="issues",
            field=models.ManyToManyField(
                related_name="sidewalks",
                to="map.sidewalkissue",
                verbose_name="Проблеми",
            ),
        ),
        migrations.AlterField(
            model_name="sidewalk",
            name="width_in_centimeters",
            field=models.IntegerField(verbose_name="Ширина в сантиметрах"),
        ),
        migrations.AlterField(
            model_name="sidewalkissue",
            name="borders",
            field=models.ManyToManyField(
                related_name="issues",
                to="map.sidewalkissueborder",
                verbose_name="Кордони",
            ),
        ),
        migrations.AlterField(
            model_name="sidewalkissueborder",
            name="GPS",
            field=models.CharField(max_length=255, verbose_name="GPS"),
        ),
        migrations.AlterField(
            model_name="sidewalkissueborder",
            name="commit_issues",
            field=models.ManyToManyField(
                related_name="borders",
                to="map.commitissue",
                verbose_name="Зафіксовані проблеми",
            ),
        ),
        migrations.AlterField(
            model_name="sidewalkissueborder",
            name="height_in_centimeters",
            field=models.IntegerField(verbose_name="Висота в сантиметрах"),
        ),
        migrations.AlterField(
            model_name="sidewalkmap",
            name="left",
            field=models.ManyToManyField(
                related_name="left_maps", to="map.sidewalk", verbose_name="Лівий"
            ),
        ),
        migrations.AlterField(
            model_name="sidewalkmap",
            name="right",
            field=models.ManyToManyField(
                related_name="right_maps", to="map.sidewalk", verbose_name="Правий"
            ),
        ),
        migrations.AlterField(
            model_name="street",
            name="central_walks",
            field=models.ManyToManyField(
                related_name="central_streets",
                to="map.sidewalk",
                verbose_name="Центральні тротуари",
            ),
        ),
        migrations.AlterField(
            model_name="street",
            name="end_with_names",
            field=models.ManyToManyField(
                related_name="ending_streets",
                to="map.adjacentstreet",
                verbose_name="Кінцеві вулиці",
            ),
        ),
        migrations.AlterField(
            model_name="street",
            name="id",
            field=models.CharField(
                max_length=100, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="street",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Назва"),
        ),
        migrations.AlterField(
            model_name="street",
            name="sidewalks",
            field=models.ManyToManyField(
                related_name="streets", to="map.sidewalkmap", verbose_name="Тротуари"
            ),
        ),
        migrations.AlterField(
            model_name="street",
            name="start_with_names",
            field=models.ManyToManyField(
                related_name="starting_streets",
                to="map.adjacentstreet",
                verbose_name="Початкові вулиці",
            ),
        ),
        migrations.AlterField(
            model_name="street",
            name="type",
            field=models.CharField(
                choices=[
                    ("AVENUE", "Проспект"),
                    ("STREET", "Вулиця"),
                    ("BYSTREET", "Бічна вулиця"),
                ],
                max_length=10,
                verbose_name="Тип",
            ),
        ),
    ]