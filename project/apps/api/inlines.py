from django.contrib import admin

from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

from super_inlines.admin import SuperInlineModelAdmin


from .models import (
    Arranger,
    Contest,
    Certification,
    Contestant,
    Session,
    Performer,
    Director,
    Group,
    Judge,
    Performance,
    Score,
    Round,
    Singer,
    Song,
)


class ArrangerInline(admin.TabularInline):
    model = Arranger
    fields = (
        # 'song',
        'person',
        'part',
        # 'is_practice',
    )
    ordering = (
        'person',
    )
    extra = 0
    raw_id_fields = (
        'person',
    )
    autocomplete_lookup_fields = {
        'fk': [
            'person',
        ]
    }
    can_delete = True
    show_change_link = True
    classes = ('grp-collapse grp-closed',)


class CertificationInline(admin.TabularInline):
    fields = (
        'name',
        'person',
        'status',
        'category',
    )
    model = Certification
    extra = 0
    raw_id_fields = (
        'person',
    )
    # autocomplete_lookup_fields = {
    #     'fk': [
    #         'person',
    #         'performer',
    #     ]
    # }
    readonly_fields = [
        'name',
    ]
    can_delete = True
    classes = ('grp-collapse grp-closed',)


class ContestInline(admin.TabularInline):
    def link(self, obj):
        return mark_safe(
            "<a href={0}>link</a>".format(
                reverse(
                    'admin:api_contest_change',
                    args=(
                        obj.id.hex,
                    )
                )
            )
        )

    fields = (
        'link',
        'name',
        'status',
        'award',
        'session',
        # 'organization',
        # 'level',
        # 'kind',
        'goal',
        # 'year',
        'rounds',
        'qual_score',
    )
    show_change_link = True

    model = Contest
    extra = 0
    raw_id_fields = (
        'session',
    )
    readonly_fields = [
        'link',
        'name',
    ]

    can_delete = True
    classes = ('grp-collapse grp-closed',)


class ContestantInline(admin.TabularInline):
    def link(self, obj):
        return mark_safe(
            "<a href={0}>link</a>".format(
                reverse(
                    'admin:api_contestant_change',
                    args=(
                        obj.id.hex,
                    )
                )
            )
        )

    fields = (
        'link',
        # 'name',
        'contest',
        'performer',
        'place',
        'total_points',
        'total_score',
    )
    ordering = (
        'place',
    )

    show_change_link = True

    model = Contestant
    extra = 0
    raw_id_fields = (
        'performer',
    )
    # autocomplete_lookup_fields = {
    #     'fk': [
    #         'performer',
    #     ]
    # }
    readonly_fields = [
        'link',
        'name',
        'place',
        'total_score',
        'total_points',
        'performer',
    ]
    can_delete = True
    # classes = ('grp-collapse grp-open',)


class DirectorInline(admin.TabularInline):
    fields = (
        'performer',
        'person',
        'part',
    )
    ordering = (
        'part',
        'performer',
    )
    model = Director
    extra = 0
    raw_id_fields = (
        'person',
        'performer',
    )
    # autocomplete_lookup_fields = {
    #     'fk': [
    #         'person',
    #         'performer',
    #     ]
    # }
    can_delete = True
    classes = ('grp-collapse grp-closed',)


class GroupInline(admin.TabularInline):
    def link(self, obj):
        return mark_safe(
            "<a href={0}>link</a>".format(
                reverse(
                    'admin:api_group_change',
                    args=(
                        obj.id.hex,
                    )
                )
            )
        )

    fields = (
        'link',
        'name',
        'status',
    )
    ordering = (
        'name',
    )
    model = Group
    extra = 0
    readonly_fields = (
        'name',
        'link',
    )
    raw_id_fields = (
        'chapter',
    )
    autocomplete_lookup_fields = {
        'fk': [
            'chapter',
        ]
    }
    can_delete = True
    classes = ('grp-collapse grp-closed',)


class JudgeInline(admin.TabularInline):
    model = Judge
    fields = (
        'person',
        # 'organization',
        'category',
        'slot',
        'kind',
        'round',
    )
    ordering = (
        'round',
        'kind',
        'category',
        'slot',
    )
    extra = 0
    raw_id_fields = (
        'person',
    )
    autocomplete_lookup_fields = {
        'fk': [
            'person',
        ]
    }
    can_delete = True
    show_change_link = True
    classes = ('grp-collapse grp-closed',)


# class PerformancesInline(GrappelliSortableHiddenMixin, admin.TabularInline):
class PerformanceInline(admin.TabularInline):
    def link(self, obj):
        return mark_safe(
            "<a href={0}>link</a>".format(
                reverse(
                    'admin:api_performance_change',
                    args=(
                        obj.id.hex,
                    )
                )
            )
        )

    fields = (
        'link',
        'performer',
        'status',
        'position',
        'draw',
        'scheduled',
        'actual',
    )
    sortable_field_name = "position"

    model = Performance
    extra = 0
    # raw_id_fields = (
    #     'performer',
    # )
    # autocomplete_lookup_fields = {
    #     'fk': [
    #         'performer',
    #     ]
    # }
    readonly_fields = (
        'performer',
        'draw',
        'link',
    )
    classes = ('grp-collapse grp-closed',)


class RankingInline(admin.TabularInline):
    def link(self, obj):
        return mark_safe(
            "<a href={0}>link</a>".format(
                reverse(
                    'admin:api_performance_change',
                    args=(
                        obj.id.hex,
                    )
                )
            )
        )

    fields = (
        'link',
        'performer',
        'status',
        'place',
        'total_points',
        'total_score',
    )
    extra = 0

    model = Performance
    readonly_fields = (
        'performer',
        'status',
        'place',
        'total_points',
        'total_score',
        'link',
    )
    ordering = (
        'place',
    )

    classes = ('grp-collapse grp-closed',)


class PerformerInline(admin.TabularInline):
    def link(self, obj):
        return mark_safe(
            "<a href={0}>link</a>".format(
                reverse(
                    'admin:api_performer_change',
                    args=(
                        obj.id.hex,
                    )
                )
            )
        )

    fields = (
        'link',
        'session',
        'group',
        'organization',
        # 'seed',
        # 'prelim',
        # 'total_score',
        'men',
    )
    ordering = (
        'group__kind',
        'group',
    )

    show_change_link = True

    model = Performer
    extra = 0
    raw_id_fields = (
        'group',
    )
    readonly_fields = [
        'total_score',
        'link',
        # 'organization',
        'seed',
        'prelim',
    ]

    autocomplete_lookup_fields = {
        'fk': [
            'group',
        ]
    }
    can_delete = True
    classes = ('grp-collapse grp-closed',)


class ScoreInline(admin.TabularInline):
    model = Score
    fields = (
        'song',
        'judge',
        'category',
        'points',
        'dixon_test',
    )
    ordering = (
        'judge',
    )
    extra = 0
    raw_id_fields = (
        'song',
    )
    readonly_fields = [
        'song',
        'category',
        'judge',
        'dixon_test',
    ]

    # autocomplete_lookup_fields = {
    #     'fk': [
    #         'song',
    #     ]
    # }
    can_delete = True
    show_change_link = True
    classes = ('grp-collapse grp-open',)


class SessionInline(admin.TabularInline):
    def link(self, obj):
        return mark_safe(
            "<a href={0}>link</a>".format(
                reverse(
                    'admin:api_session_change',
                    args=(
                        obj.id.hex,
                    )
                )
            )
        )

    fields = (
        'link',
        'name',
        'status',
        'convention',
        'kind',
        # 'size',
        # 'num_rounds',
    )
    show_change_link = True

    model = Session
    extra = 0
    raw_id_fields = (
        'convention',
    )
    readonly_fields = [
        'link',
        'name',
    ]

    can_delete = True
    classes = ('grp-collapse grp-open',)


class SingerInline(admin.TabularInline):
    model = Singer
    fields = (
        'performer',
        'person',
        'part',
    )
    ordering = (
        'part',
        'performer',
    )
    extra = 0
    raw_id_fields = (
        'person',
        'performer',
    )
    # autocomplete_lookup_fields = {
    #     'fk': [
    #         'person',
    #         # 'performer',
    #     ]
    # }
    can_delete = True
    show_change_link = True
    classes = ('grp-collapse grp-closed',)


class RoundInline(admin.TabularInline):
    def link(self, obj):
        return mark_safe(
            "<a href={0}>link</a>".format(
                reverse(
                    'admin:api_round_change',
                    args=(
                        obj.id.hex,
                    )
                )
            )
        )

    fields = (
        'link',
        'name',
        'session',
        'kind',
        'status',
        'num',
        'slots',
    )
    ordering = (
        'session',
        'kind',
    )

    model = Round
    extra = 0
    # raw_id_fields = (
    #     'contest',
    # )
    # autocomplete_lookup_fields = {
    #     'fk': [
    #         'contest',
    #     ]
    # }
    classes = ('grp-collapse grp-closed',)
    readonly_fields = [
        'link',
        'name',
    ]


class PerformerStackedInline(SuperInlineModelAdmin, admin.StackedInline):
    def link(self, obj):
        return mark_safe(
            "<a href={0}>link</a>".format(
                reverse(
                    'admin:api_performer_change',
                    args=(
                        obj.id.hex,
                    )
                )
            )
        )

    fields = (
        'link',
        'session',
        'group',
        'men',
        'organization',
        ('seed', 'prelim',),
    )
    ordering = (
        'group__kind',
        'group',
    )

    show_change_link = True

    model = Performer
    extra = 0
    raw_id_fields = (
        'group',
    )
    readonly_fields = [
        'link',
        'organization',
        'seed',
        'prelim',
    ]

    inlines = [
        ContestantInline,
    ]

    autocomplete_lookup_fields = {
        'fk': [
            'group',
        ]
    }
    can_delete = True
    # classes = ('grp-collapse grp-open',)


class SongStackedInline(SuperInlineModelAdmin, admin.StackedInline):
    fields = (
        'performance',
        'order',
        # 'status',
        'title',
        # 'tune',
        ('mus_points', 'prs_points', 'sng_points',),
    )
    ordering = (
        'performance',
        'order',
    )
    model = Song
    extra = 0
    raw_id_fields = (
        'tune',
    )
    autocomplete_lookup_fields = {
        'fk': [
            'tune',
        ]
    }
    inlines = (
        ScoreInline,
    )
    readonly_fields = [
        'mus_points',
        'prs_points',
        'sng_points',
    ]
    show_change_link = True
    # classes = ('grp-collapse grp-open',)
