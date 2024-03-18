from django.core.management.base import BaseCommand
import json

from inquiries.models import(

)


array = {
    
}


class Command(BaseCommand):
    help = 'Populates table from json'

    def handle(self, *args, **options):
        with open('data/ingredients.json', 'r', encoding='utf-8') as file:
            reader = json.load(file)
            for row in reader:
                Ingredient.objects.create(
                    name=row['name'],
                    measurement_unit=row['measurement_unit'],
                )
        self.stdout.write(self.style.SUCCESS(
            'Data from json loaded successfully'
        ))