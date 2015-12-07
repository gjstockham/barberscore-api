from django.core.management.base import (
    BaseCommand,
)

from apps.api.models import (
    Performer,
    Performance,
    Song,
)


class Command(BaseCommand):
    help = "Command to denormailze data."

    def handle(self, *args, **options):
        ps = Song.objects.all()
        for p in ps:
            p.save()
        as_ = Performance.objects.all()
        for a in as_:
            a.save()
        cs = Performer.objects.all()
        for c in cs:
            c.save()
        return "Done"
