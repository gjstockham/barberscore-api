import os
import csv

from optparse import make_option

from django.core.management.base import (
    BaseCommand,
    CommandError,
)

from convention.models import (
    Contestant,
    Contest,
    Performance,
)


class Command(BaseCommand):
    help = "Command to import scores"
    option_list = BaseCommand.option_list + (
        make_option(
            "-f",
            "--file",
            dest="filename",
            help="specify import file",
            metavar="FILE"
        ),
        make_option(
            "-c",
            "--contest",
            dest="contest",
            help="specify contest by id number",
        ),
        make_option(
            "-r",
            "--rnd",
            dest="rnd",
            help="specify contest round",
        ),
    )

    def handle(self, *args, **options):
        # make sure file option is present
        if options['filename'] is None:
            raise CommandError("Option `--file=...` must be specified.")

        # make sure contest is specified
        if options['contest'] is None:
            raise CommandError("Must specify contest with `--contest=1`.")

        if options['rnd'] is None:
            raise CommandError("Must specify contest round with `--rnd 1`.")

        # make sure file path resolves
        if not os.path.isfile(options['filename']):
            raise CommandError("File does not exist at the specified path.")

        # make certain contest exists
        try:
            contest = Contest.objects.get(pk=options['contest'])
        except:
            raise CommandError("Contest does not exist.")

        rnd = options['rnd']
        # print file
        print "Path: `%s`" % options['filename']

        # open the file
        with open(options['filename']) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:

                try:
                    contestant = Contestant.objects.get(name=row[0])
                    performance = Performance.objects.get(
                        contest=contest,
                        contestant=contestant,
                        contest_round=rnd,
                    )
                    performance.place = row[1]
                    performance.song1 = row[3]
                    performance.mus1 = row[4]
                    performance.prs1 = row[5]
                    performance.sng1 = row[6]
                    performance.song2 = row[7]
                    performance.mus2 = row[8]
                    performance.prs2 = row[9]
                    performance.sng2 = row[10]
                    performance.save()

                except Exception, e:
                    print "Performance {0} could not be updated. {1}".format(
                        row[0], e
                    )
