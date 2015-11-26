from django.core.management.base import (
    BaseCommand,
    CommandError,
)

from apps.api.factories import (
    score_performance,
)

from apps.api.models import (
    Session,
)


class Command(BaseCommand):
    help = "Create sample panel."

    def add_arguments(self, parser):
        parser.add_argument(
            'slug',
            nargs='+',
        )

    def handle(self, *args, **options):
        for slug in options['slug']:
            try:
                session = Session.objects.get(
                    slug=slug,
                )
            except Session.DoesNotExist:
                raise CommandError("Session does not exist.")
            performances = session.performances.filter(
                status=session.performances.model.STATUS.new,
            ).order_by('position')
            for performance in performances:
                performance.start()
                performance.save()
                score_performance(performance)
                performance.finish()
                performance.save()
            self.stdout.write("Filled Session")