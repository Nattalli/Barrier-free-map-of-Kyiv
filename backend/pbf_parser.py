import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()


import re
from pointer.models import MapPoint, Addition


def parse_binary_data(file_path):
    try:
        with open(file_path, 'rb') as file:
            binary_data = file.read()

        text = binary_data.decode('utf-8', errors='ignore')
        return text
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def parse_location_data(text):
    entries = re.split(r'\n\n+', text)
    parsed_data = []

    for entry in entries:
        name = re.search(r'<b>(.*?)</b>', entry)
        address = re.search(r'<b>Адреса:</b> (.*?)<br>', entry)
        hours = re.search(r'<b>Графік роботи:</b> (.*?)<br>', entry)
        features = re.findall(r'<br>(.*?)<br>', entry)

        if name and name.group(1) != "Джерело" and features:
            try:
                map_point = MapPoint(
                    title=name.group(1),
                    address=address.group(1) if address else 'Unknown',
                    schedule=hours.group(1) if hours else None
                )
                map_point.save()

                for feature in features:
                    addition, created = Addition.objects.get_or_create(title=feature)
                    map_point.addition.add(addition)

                parsed_data.append(map_point)
            except:
                ...

    return parsed_data


file_path = 'parser_data/5525.pbf'
parsed_text = parse_binary_data(file_path)

if parsed_text:
    parsed_data = parse_location_data(parsed_text)

    for item in parsed_data:
        print(item)
