from django.core.management.base import (
    BaseCommand,
)

from apps.api.models import (
    Convention,
)

from apps.api.utils import (
    import_convention,
    extract_sessions,
    extract_rounds,
    extract_panel,
    extract_performers,
)

from django.core.files import File


class Command(BaseCommand):
    help = "Command to rebuild from stix files."

    def handle(self, *args, **options):

        vs = Convention.objects.filter(year=2015)
        vs.delete()

        self.stdout.write("Database Flushed")

        i = 11
        while i <= 27:
            path = "stix/fall000{0}.txt".format(i)
            convention = import_convention(path, kind='fall')
            convention.save()
            filename = convention.id.hex + '.txt'
            convention.stix_file.save(
                filename,
                File(open(path, 'r')),
                save=True,
            )
            i += 1
            self.stdout.write("{0}".format(convention))

        i = 11
        while i <= 21:
            path = "stix/spring000{0}.txt".format(i)
            convention = import_convention(path, kind='spring')
            convention.save()
            filename = convention.id.hex + '.txt'
            convention.stix_file.save(
                filename,
                File(open(path, 'r')),
                save=True,
            )
            i += 1
            self.stdout.write("{0}".format(convention))

        i = 11
        while i <= 25:
            path = "stix/combo000{0}.txt".format(i)
            convention = import_convention(path, kind='spring', division=True)
            convention.save()
            filename = convention.id.hex + '.txt'
            convention.stix_file.save(
                filename,
                File(open(path, 'r')),
                save=True,
            )
            i += 1
            self.stdout.write("{0}".format(convention))

        international = [
            'international.txt',
        ]

        for f in international:
            path = "stix/{0}".format(f)
            convention = import_convention(path, kind='international')
            convention.save()
            filename = convention.id.hex + '.txt'
            convention.stix_file.save(
                filename,
                File(open(path, 'r')),
                save=True,
            )
            self.stdout.write("{0}".format(convention))

        midwinter = [
            'midwinter.txt',
        ]

        for f in midwinter:
            path = "stix/{0}".format(f)
            convention = import_convention(path, kind='midwinter')
            convention.save()
            filename = convention.id.hex + '.txt'
            convention.stix_file.save(
                filename,
                File(open(path, 'r')),
                save=True,
            )
            self.stdout.write("{0}".format(convention))

        self.stdout.write("Conventions Loaded")

        vs = Convention.objects.filter(year=2015)

        for v in vs:
            extract_sessions(v)
        self.stdout.write("Sessions Extracted")

        for v in vs:
            extract_rounds(v)
        self.stdout.write("Rounds Extracted")

        for v in vs:
            extract_panel(v)
        self.stdout.write("Panel Extracted")

        for v in vs:
            extract_performers(v)
        self.stdout.write("Performers Extracted")

        return "Rebuild Complete"
