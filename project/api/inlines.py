# Django
from django.contrib import admin

# Local
from .models import (
    Appearance,
    Assignment,
    Award,
    Contest,
    Contestant,
    Convention,
    Entry,
    Member,
    Officer,
    Panelist,
    Participant,
    Repertory,
    Round,
    Score,
    Session,
    Slot,
    Song,
)


class AppearanceInline(admin.TabularInline):
    model = Appearance
    fields = [
        'entry',
        'status',
        'num',
        'draw',
    ]
    readonly_fields = [
        'entry',
    ]
    ordering = (
        'num',
    )
    show_change_link = True
    extra = 0


class AssignmentInline(admin.TabularInline):
    model = Assignment
    fields = [
        'nomen',
        'status',
        'category',
        'kind',
        'person',
        'convention',
    ]
    readonly_fields = [
        'nomen',
    ]
    raw_id_fields = [
        'person',
        'convention',
    ]
    extra = 0
    show_change_link = True


class AwardInline(admin.TabularInline):
    model = Award
    fields = [
        'name',
        'kind',
        'rounds',
        'size',
        'is_improved',
        'organization',
    ]
    readonly_fields = [
        'name',
    ]
    extra = 0
    show_change_link = True


class ContestInline(admin.TabularInline):
    model = Contest
    fields = [
        'status',
        'award',
        'session',
        'is_qualifier',
        'kind',
    ]
    raw_id_fields = [
        'award',
    ]
    readonly_fields = [
        'is_qualifier',
    ]
    ordering = (
        'award__kind',
        '-award__is_primary',
        'award__is_improved',
        'award__size',
        'award__scope',
    )
    show_change_link = True
    extra = 0


class ContestantInline(admin.TabularInline):
    model = Contestant
    fields = [
        'nomen',
        'entry',
        'contest',
        'status',
    ]
    readonly_fields = [
        'nomen',
        'status',
    ]
    raw_id_fields = [
        'contest',
    ]
    show_change_link = True
    extra = 0


class ConventionInline(admin.TabularInline):
    model = Convention
    fields = [
        'name',
        'organization',
    ]
    raw_id_fields = [
        'organization',
    ]
    show_change_link = True
    extra = 0


class EntryInline(admin.TabularInline):
    model = Entry
    fields = [
        'nomen',
        'session',
        'group',
        'prelim',
        'seed',
        'status',
    ]
    readonly_fields = [
        'nomen',
        # 'seed',
    ]
    raw_id_fields = [
        'session',
        'group',
    ]
    ordering = [
        'group__nomen',
    ]
    show_change_link = True
    extra = 0


class MemberInline(admin.TabularInline):
    model = Member
    fields = [
        'person',
        'group',
        'part',
        'status',
    ]
    raw_id_fields = [
        'person',
        'group',
    ]
    ordering = (
        'group__kind',
        'group__name',
    )
    show_change_link = True
    extra = 0


class OfficerInline(admin.TabularInline):
    model = Officer
    fields = [
        'office',
        'person',
        'organization',
        'status',
    ]
    raw_id_fields = [
        'office',
        'person',
        'organization',
    ]
    show_change_link = True
    extra = 0


class PanelistInline(admin.TabularInline):
    model = Panelist
    fields = [
        'nomen',
        'status',
        'category',
        'kind',
        'person',
        'round',
        'num',
    ]
    readonly_fields = [
        'nomen',
    ]
    raw_id_fields = [
        'person',
        'round',
    ]
    ordering = (
        'category',
        'kind',
        'person__last_name',
    )
    extra = 0
    show_change_link = True


class ParticipantInline(admin.TabularInline):
    model = Participant
    fields = [
        'member',
        'entry',
        'status',
        'part',
    ]
    raw_id_fields = [
        'member',
        'entry',
    ]
    show_change_link = True
    extra = 0
    classes = [
        'collapse',
    ]


class RepertoryInline(admin.TabularInline):
    model = Repertory
    fields = [
        'chart',
        'group',
    ]
    raw_id_fields = [
        'chart',
        'group',
    ]
    show_change_link = True
    extra = 0


class ScoreInline(admin.TabularInline):
    model = Score
    fields = [
        'song',
        'num',
        'panelist',
        'category',
        'kind',
        'points',
    ]
    raw_id_fields = [
        'song',
    ]
    readonly_fields = [
        'song',
        'category',
        'panelist',
    ]
    ordering = (
        'num',
        'panelist',
    )
    show_change_link = True
    extra = 0


class SongInline(admin.TabularInline):
    model = Song
    fields = [
        'num',
    ]
    ordering = (
        'num',
    )
    show_change_link = True
    extra = 0
    can_delete = False


class SessionInline(admin.TabularInline):
    model = Session
    fields = [
        'convention',
        'kind',
    ]
    raw_id_fields = [
        'convention',
    ]
    show_change_link = True
    extra = 0


class SlotInline(admin.TabularInline):
    model = Slot
    fields = [
        'num',
        'onstage',
        'round',
    ]
    raw_id_fields = [
        'round',
    ]
    show_change_link = True
    extra = 0
    ordering = [
        'num',
    ]


class RoundInline(admin.TabularInline):
    model = Round
    fields = [
        'nomen',
        'session',
        'kind',
        'status',
        'num',
    ]
    ordering = (
        'session',
        'kind',
    )
    readonly_fields = [
        'nomen',
    ]
    show_change_link = True
    extra = 0
