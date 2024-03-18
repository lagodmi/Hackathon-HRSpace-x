from django.core.management.base import BaseCommand
import json

from inquiries.models import(
    City,
    Company,
    Profession,
    ProfessionArea,
    Skill,
    SkillRecruiter,
    SocialPackage,
    TaskAdditional,
    TaskRecruiter,
)


array = {
    Company: 'data/companies.json',
    # Profession: 'data/prof.json',
    Skill: 'data/programs.json',
    SkillRecruiter: 'data/specialSkills.json',
    SocialPackage: 'data/socialPackage.json',
    TaskAdditional: 'data/additionalTasks.json',
    TaskRecruiter: 'data/recruiterTasks.json',
}


class Command(BaseCommand):
    help = 'Populates table from json'

    def handle(self, *args, **options):
        for model, add_file in array.items():
            with open(add_file, 'r', encoding='utf-8') as file:
                reader = json.load(file)
                for row in reader:
                    model.objects.create(
                        name=row['name']
                    )
            self.stdout.write(self.style.SUCCESS(
                'Data from add_file loaded successfully'
            ))

        with open('data/districts.json', 'r', encoding='utf-8') as file:
            reader = json.load(file)
            for row in reader:
                City.objects.create(
                    id = row[id],
                    name=row['name']
                )
        self.stdout.write(self.style.SUCCESS(
            'Data from add_file loaded successfully'
        ))
