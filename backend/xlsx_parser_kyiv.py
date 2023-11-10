import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()


from pointer.models import MapPoint, Addition, MapPointCategory


new_excel_path = 'parser_data/Київ_Департамент довкілля_Карта інклюзивності.xlsx'
import pandas as pd
df_new = pd.read_excel(new_excel_path)


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


for index, row in df_new.iterrows():
    category_title = row['Категорія']
    category, _ = MapPointCategory.objects.get_or_create(title=category_title)

    map_point, created = MapPoint.objects.get_or_create(
        title=row['Назва'],
        defaults={
            'comment': row['Коментар'],
            'latitude': row['Широта'],
            'longitude': row['Довгота'],
            'schedule': row.get('Графік роботи'),
            'category': category,
            'is_approved': True,
        }
    )

    additions = handle_additions(row, additions_list)
    map_point.addition.set(additions)
    map_point.save()
