from django.core.management.base import BaseCommand
import json

from inquiries.models import (
    Duty,
    Company,
    Profession,
    ProfessionArea,
    Software,
    SkillRecruiter,
    SocialPackage,
    TaskAdditional,
    TaskRecruiter,
)


array = {
    Company: "data/companies.json",
    Software: "data/programs.json",
    SkillRecruiter: "data/specialSkills.json",
    SocialPackage: "data/socialPackage.json",
    TaskAdditional: "data/additionalTasks.json",
    TaskRecruiter: "data/recruiterTasks.json",
}


class Command(BaseCommand):
    help = "Populates table from json"

    def handle(self, *args, **options):
        for model, add_file in array.items():
            with open(add_file, "r", encoding="utf-8") as file:
                reader = json.load(file)
                for row in reader:
                    model.objects.create(name=row["name"])
            self.stdout.write(
                self.style.SUCCESS(f"Data from {add_file} loaded successfully")
            )

        with open("data/prof.json", "r", encoding="utf-8") as file:
            reader = json.load(file)
            for row in reader:
                prof_area, _ = ProfessionArea.objects.get_or_create(
                    name=row["prof_area"]
                )
                Profession.objects.create(
                    id=row["id"],
                    prof_area=prof_area,
                    prof_name=row["prof_name"]
                )

        self.stdout.write(
            self.style.SUCCESS("Data from data/prof.json loaded successfully")
        )

        with open("data/skill.json", "r", encoding="utf-8") as file:
            reader = json.load(file)
            for row in reader:
                prof_area, _ = ProfessionArea.objects.get_or_create(
                    name=row["prof_area"]
                )
                Duty.objects.create(prof_area=prof_area, name=row["name"])

        self.stdout.write(
            self.style.SUCCESS(
                "Data from data/software.json loaded successfully"
            )
        )
