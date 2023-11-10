import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()


from pointer.models import MapPoint, Addition, MapPointCategory
import pandas as pd


excel_path = 'parser_data/мапа доступності.xlsx'


def parse_address(row):
    parts = [str(row['Тип вулиці']), str(row['Назва вулиці']), str(row['номер будинку']), str(row.get('Номер корпусу', ''))]
    return ', '.join(part for part in parts if part not in ['nan', ''])


additions_list = ["спеціальні місця для паркування", 'вхідна група', 'засоби невізуальної орієнтації',
                  'засоби неакустичної орієнтаціїзасоби неакустичної орієнтації', 'наявність спеціального ліфту',
                  'Санітарно-гігєнічні приміщення', 'Адаптовані пристрої оповіщення', 'Перекладач з жестової мови',
                  'Укриття', 'Wi-Fi', 'Пеленальний столик', 'Дитяча кімната', 'Супроводжуюча людина',
                  'наявність тактильного маршруту']


def handle_additions_new(row):
    additions = []
    for addition in additions_list:
        if row.get(addition) == 'так':
            obj, created = Addition.objects.get_or_create(title=addition)
            additions.append(obj)
    return additions


def parse_excel(file_path):
    df = pd.read_excel(file_path)

    for index, row in df.iterrows():
        category_title = row['тип закладу']
        category, _ = MapPointCategory.objects.get_or_create(title=category_title)

        address = parse_address(row)

        try:
            map_point, created = MapPoint.objects.update_or_create(
                address=address,
                defaults={
                    'title': row['назва закладу'],
                    'latitude': row['Latitude'],
                    'longitude': row['Longitude'],
                    'schedule': row.get('Графік роботи', ''),
                    'category': category,
                    'is_approved': True,
                }
            )
        except:
            continue

        additions = handle_additions_new(row)
        map_point.addition.set(additions)


parse_excel(excel_path)
