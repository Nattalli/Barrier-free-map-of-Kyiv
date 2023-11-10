import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()


from pointer.models import MapPoint, Addition, MapPointCategory
import pandas as pd
from django.db.utils import IntegrityError

excel_path = 'parser_data/Київ_Оболонський_Карта інклюзивності.xlsx'
df = pd.read_excel(excel_path)


def handle_additions(row, additions_list):
    additions = []
    for addition in additions_list:
        if row.get(addition) == 'так':
            obj, created = Addition.objects.get_or_create(title=addition)
            additions.append(obj)
    return additions


additions_list = ['Пандус', 'Понижений бордюр', 'Тактильне маркування',
                  'Світлофор зі звуковим сигналом', 'Вбиральня для людей з інвалідністю',
                  'Вхід в рівень з тротуаром', 'Ліфт', 'Підйомник',
                  'Простір для сповинання дітей', 'Парковка для людей з інвалідністю']


for index, row in df.iterrows():
    category_title = row['Категорія']
    category, _ = MapPointCategory.objects.get_or_create(title=category_title)

    try:
        map_point, created = MapPoint.objects.update_or_create(
            address=row['Адреса '],
            defaults={
                'title': row['Назва'],
                'comment': row['Коментар'],
                'latitude': row['Широта'],
                'longitude': row['Довгота'],
                'schedule': row.get('Графік роботи (у форматі Пн-Нд: 9:00 - 21:00)'),
                'category': category,
                'is_approved': True,
            }
        )
    except IntegrityError:
        continue

    additions = handle_additions(row, additions_list)
    map_point.addition.set(additions)
