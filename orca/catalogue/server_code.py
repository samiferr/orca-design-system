"""The Python an element needs on the server: views, forms, mixins, URLs and middleware.

Each element's examples show the template. When an element reads data from the view (charts, calendars, generic
pages), posts data back (formsets, the zone editor, the board) or relies on a Django feature (messages, i18n,
time zones), its ``server`` list holds the code that makes it work, as (title, code) pairs. The documentation
site shows it under "Server code", ``python -m orca show <id>`` prints it, and ``catalogue.json`` carries it.

Snippets use an example app (``videos``) with models such as ``Video``, ``Album``, ``Event`` and ``Task``;
everything imported from ``django`` and ``orca`` is real and checked by the test suite.
"""

from __future__ import annotations

from .registry import set_server

# ============================================================================================ shared snippets

MODEL_FORM_VIEW = '''# videos/forms.py
from django import forms

from .models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["title", "album", "published", "recorded_on"]
        help_texts = {"title": "Shown under the player and in search."}


# videos/views.py
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import VideoForm
from .models import Video


def edit_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    form = VideoForm(request.POST or None, instance=video)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"Video “{video}” saved.")
        return redirect("video-detail", pk=video.pk)
    # Template: {% orca_form_errors form %} then {% orca_field form.title %} for each field.
    return render(request, "videos/edit.html", {"form": form, "video": video})
'''

FORMSET = '''# videos/forms.py
from django import forms

from .models import Chapter, Video

ChapterFormSet = forms.inlineformset_factory(
    Video, Chapter, fields=["title", "starts_at"], extra=0, can_delete=True,
)


# videos/views.py
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ChapterFormSet
from .models import Video


def edit_chapters(request, pk):
    video = get_object_or_404(Video, pk=pk)
    formset = ChapterFormSet(request.POST or None, instance=video, prefix="chapters")
    if request.method == "POST" and formset.is_valid():
        formset.save()
        return redirect("video-detail", pk=video.pk)
    # Template: {{ formset.management_form }}, one [data-orca-row] per form, and a <template id="chapter-row">
    # holding {{ formset.empty_form }} (its names contain __prefix__). The add-row button points at it with
    # data-orca-add-row="chapter-row" and data-orca-total="id_chapters-TOTAL_FORMS".
    return render(request, "videos/chapters.html", {"video": video, "formset": formset})
'''

EVENTS = '''# videos/views.py
import datetime as dt

from django.utils import timezone
from django.views.generic import TemplateView

from .models import Event


class CalendarView(TemplateView):
    template_name = "videos/calendar.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.localdate()
        month = dt.date.fromisoformat(self.request.GET.get("month", today.strftime("%Y-%m")) + "-01")
        # Events are dicts or objects with title, start, end (date or datetime), all_day, color (1–8 or a
        # CSS colour), url, location and status ("tentative", "cancelled"). Aware datetimes are shown in the
        # active time zone.
        ctx["events"] = [
            {"title": e.title, "start": e.starts_at, "end": e.ends_at, "all_day": e.all_day,
             "color": e.calendar.color, "url": e.get_absolute_url(), "location": e.place}
            for e in Event.objects.filter(starts_at__date__lte=month + dt.timedelta(days=42),
                                          ends_at__date__gte=month - dt.timedelta(days=7))
        ]
        ctx["holidays"] = {"2026-11-11": "Armistice Day"}  # date → name
        ctx.update(month=month, today=today, now=timezone.localtime())
        return ctx
'''


def chart(kind_comment: str, build: str) -> list[tuple[str, str]]:
    return [("View: the chart data", f'''# videos/views.py
import datetime as dt

from django.db.models import Count
from django.db.models.functions import ExtractHour, TruncDate
from django.utils import timezone
from django.views.generic import TemplateView

from .models import Visit


class ReportView(TemplateView):
    template_name = "videos/report.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.localdate()
        start = today - dt.timedelta(days=6)
        # {kind_comment}
{build}
        return ctx
''')]


FILTERS = '''# videos/forms.py
from django import forms

from .models import Album, Video


class VideoFilterForm(forms.Form):
    q = forms.CharField(label="Title contains", required=False)
    album = forms.ModelChoiceField(Album.objects.all(), required=False, empty_label="Any album")
    status = forms.MultipleChoiceField(choices=Video.Status.choices, required=False,
                                       widget=forms.CheckboxSelectMultiple)


# videos/views.py
from django.views.generic import ListView

from orca.mixins import OrcaPageMixin

from .forms import VideoFilterForm
from .models import Video


class VideoList(OrcaPageMixin, ListView):
    model = Video
    paginate_by = 25
    template_name = "orca/generic/list.html"   # or "orca/layouts/simple_data.html"
    list_columns = ["title", "album", "status", ("Views today", "views_today")]
    detail_url_name, create_url_name = "video-detail", "video-create"

    def get_queryset(self):
        qs = super().get_queryset()
        self.filter_form = VideoFilterForm(self.request.GET or None)
        if self.filter_form.is_valid():
            data = self.filter_form.cleaned_data
            if data["q"]:
                qs = qs.filter(title__icontains=data["q"])
            if data["album"]:
                qs = qs.filter(album=data["album"])
            if data["status"]:
                qs = qs.filter(status__in=data["status"])
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # The template puts the Filters button in the page actions and the form in the right drawer.
        ctx["filter_form"] = self.filter_form
        data = self.filter_form.cleaned_data if self.filter_form.is_valid() else {}
        ctx["active_filters"] = sum(1 for value in data.values() if value)
        return ctx
'''

TILES = '''# videos/views.py (in the list view's get_context_data)
from django.db.models import Count
from django.http import QueryDict

counts = dict(Video.objects.values_list("status").annotate(n=Count("id")))
current = self.request.GET.get("status", "")


def tile_url(status):
    query = self.request.GET.copy()          # keep the other filters
    query.pop("page", None)
    if status:
        query["status"] = status
    else:
        query.pop("status", None)
    return "?" + query.urlencode()


ctx["tiles"] = [{"label": "All videos", "value": sum(counts.values()), "url": tile_url(""), "current": not current}] + [
    {"label": label, "value": counts.get(value, 0), "url": tile_url(value), "current": current == value,
     "tone": {"published": "positive", "draft": "neutral", "failed": "negative"}.get(value, "")}
    for value, label in Video.Status.choices
]
'''

APP_NAV = '''# videos/context_processors.py — add "videos.context_processors.orca" to TEMPLATES["OPTIONS"]["context_processors"]
from django.urls import reverse


def orca(request):
    """The sidebar of the app shell, on every page."""
    path = request.path

    def item(label, name, icon, count=None):
        url = reverse(name)
        return {"label": label, "url": url, "icon": icon, "count": count, "current": path.startswith(url)}

    return {"nav": [
        {"label": "Library", "items": [item("Videos", "video-list", "play"), item("Albums", "album-list", "folder")]},
        {"label": "Admin", "items": [item("Users", "user-list", "user"), item("Settings", "settings", "settings")]},
    ]}


# videos/views.py — any view that renders a template extending orca/layouts/app.html
from django.views.generic import TemplateView


class Overview(TemplateView):
    template_name = "videos/overview.html"   # {% extends "orca/layouts/app.html" %}
    extra_context = {
        "title": "Overview",
        "subtitle": "Everything that happened in your library today.",
        "breadcrumbs": [("Library", "/videos/"), ("Overview", "")],
    }
    # `messages` and `user` come from Django's context processors; ORCA shows them in the shell.
'''

GENERIC_URLS = '''# videos/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("videos/", views.VideoList.as_view(), name="video-list"),
    path("videos/new/", views.VideoCreate.as_view(), name="video-create"),
    path("videos/<int:pk>/", views.VideoDetail.as_view(), name="video-detail"),
    path("videos/<int:pk>/edit/", views.VideoUpdate.as_view(), name="video-update"),
    path("videos/<int:pk>/delete/", views.VideoDelete.as_view(), name="video-delete"),
]
'''

GENERIC_VIEWS = '''# videos/views.py
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from orca.mixins import OrcaPageMixin

from .models import Video


class VideoPages(OrcaPageMixin):
    """What every video page shares: the model and the URL names the templates link to."""

    model = Video
    list_url_name, detail_url_name, create_url_name = "video-list", "video-detail", "video-create"
    update_url_name, delete_url_name = "video-update", "video-delete"


class VideoList(VideoPages, ListView):
    template_name = "orca/generic/list.html"
    paginate_by = 25
    list_columns = ["title", "album", "status", ("Views today", "views_today")]
    extra_context = {"empty_title": "No videos yet", "empty_text": "Add your first video to start your library."}


class VideoDetail(VideoPages, DetailView):
    template_name = "orca/generic/detail.html"
    detail_fields = ["title", "album", "status", "recorded_on", ("Length", "duration_text")]

    def get_title(self, obj=None):
        return str(obj)


class VideoCreate(VideoPages, SuccessMessageMixin, CreateView):
    template_name = "orca/generic/form.html"
    fields = ["title", "album", "recorded_on"]
    title = "New video"
    success_message = "Video “%(title)s” added."
    extra_context = {"submit_label": "Add video"}


class VideoUpdate(VideoPages, SuccessMessageMixin, UpdateView):
    template_name = "orca/generic/form.html"
    fields = ["title", "album", "recorded_on"]
    success_message = "Video “%(title)s” saved."
    extra_context = {"submit_label": "Save video"}

    def get_title(self, obj=None):
        return f"Edit {obj}"


class VideoDelete(VideoPages, DeleteView):
    template_name = "orca/generic/confirm_delete.html"
    success_url = reverse_lazy("video-list")
    # `blocked_by` (protected or restricted related objects) is filled by the mixin.
    extra_context = {"deleted": ["its chapters", "its share links"], "kept": ["the album"], "submit_label": "Delete video"}

    def get_title(self, obj=None):
        return f"Delete {obj}?"

    def form_valid(self, form):
        messages.success(self.request, f"Video “{self.object}” deleted.")
        return super().form_valid(form)
'''

PARENT = '''# videos/views.py
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, ListView

from orca.mixins import OrcaPageMixin

from .models import Album, Video


class AlbumTabs(OrcaPageMixin):
    """The parent (an album) and its tabs, for every page under /albums/<album_pk>/."""

    def get_parent(self):
        return get_object_or_404(Album, pk=self.kwargs["album_pk"])

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        album = ctx["parent"] = self.get_parent()
        here = self.request.path
        tabs = [("Overview", reverse("album-detail", args=[album.pk]), None),
                ("Videos", reverse("album-videos", args=[album.pk]), album.videos.count())]
        ctx["parent_tabs"] = [{"label": label, "url": url, "count": count, "current": here == url} for label, url, count in tabs]
        ctx["parent_stats"] = [{"label": "Videos", "value": album.videos.count(), "icon": "play"},
                               {"label": "Last change", "value": album.updated_at.strftime("%-d %b"), "icon": "history"}]
        ctx["parent_update_url"] = reverse("album-update", args=[album.pk])
        return ctx


class AlbumDetail(AlbumTabs, DetailView):
    model = Album
    pk_url_kwarg = "album_pk"
    template_name = "orca/generic/parent_detail.html"
    detail_fields = ["title", "owner", "created_at"]


class AlbumVideos(AlbumTabs, ListView):
    model = Video
    template_name = "orca/generic/child_list.html"
    paginate_by = 25
    list_columns = ["title", "status", "recorded_on"]
    detail_url_name, create_url_name = "video-detail", "album-video-create"

    def get_queryset(self):
        return super().get_queryset().filter(album_id=self.kwargs["album_pk"])
'''

BOARD = '''# tasks/views.py
import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from .models import Task


class Board(TemplateView):
    template_name = "orca/layouts/board.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        tasks = Task.objects.select_related("assignee")
        ctx["board_columns"] = [
            {"key": key, "name": name, "limit": 4 if key == "progress" else None,
             "cards": [{"id": t.pk, "title": t.title, "url": t.get_absolute_url(), "tags": t.tag_names,
                        "due": t.due.strftime("%a %-d %b") if t.due else "", "due_state": t.due_state,
                        "assignee": t.assignee.get_full_name() if t.assignee else ""}
                       for t in tasks if t.status == key]}
            for key, name in Task.Status.choices
        ]
        ctx["title"] = "Board"
        return ctx


@login_required
@require_POST
def move_task(request):
    """Called by the page script when a card is dropped in another column."""
    data = json.loads(request.body)
    task = get_object_or_404(Task, pk=data["id"].removeprefix("card-"))
    task.status = data["to"]
    task.save(update_fields=["status"])
    return JsonResponse({"ok": True})


# The page script (in {% block extra_scripts %}): send each move to the view.
#   document.addEventListener("orca:moved", (e) => fetch("/tasks/move/", {
#     method: "POST", headers: {"X-CSRFToken": csrftoken, "Content-Type": "application/json"},
#     body: JSON.stringify(e.detail),   // {id: "card-12", from: "planned", to: "progress"}
#   }));
'''

EMAIL = '''# videos/notifications.py
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_offline_alert(video, recipients):
    context = {
        "title": f"{video} is offline",
        "preheader": f"No video since {video.last_seen:%H:%M}",
        "paragraphs": [f"{video} has sent nothing since {video.last_seen:%H:%M} today.",
                       "Check the network connection; playback restarts on its own."],
        "action_url": f"https://example.com{video.get_absolute_url()}",
        "action_label": "Open the video",
        "footer": "You get this email because you are on the alert list.",
    }
    html = render_to_string("orca/email/base.html", context)   # colours are inlined: no CSS needed
    message = EmailMultiAlternatives(context["title"], strip_tags(html), to=recipients)
    message.attach_alternative(html, "text/html")
    message.send()
'''

DATE_RANGE = '''# videos/forms.py
from django import forms


class PeriodForm(forms.Form):
    start = forms.DateField(label="From")
    end = forms.DateField(label="To")

    def clean(self):
        data = super().clean()
        if data.get("start") and data.get("end") and data["end"] < data["start"]:
            self.add_error("end", "Choose an end date on or after the start date.")
        return data


# videos/views.py
import datetime as dt

from django.utils import timezone


def period(request):
    """The chosen period from ?start=…&end=…, the last 7 days by default."""
    form = PeriodForm(request.GET or None)
    if form.is_valid():
        return form.cleaned_data["start"], form.cleaned_data["end"]
    today = timezone.localdate()
    return today - dt.timedelta(days=6), today
'''

# ============================================================================================ per element

SERVER: dict[str, list[tuple[str, str]]] = {
    # ------------------------------------------------------------------ components: forms
    "form-field": [("Form and view", MODEL_FORM_VIEW)],
    "toggle-field": [("Form", '''# videos/forms.py
from django import forms


class NotificationForm(forms.Form):
    # A checkbox saved with the form: {% orca_field form.weekly_report %}
    weekly_report = forms.BooleanField(label="Send me the weekly report", required=False,
                                       help_text="Every Monday at 07:00.")
    # A setting applied at once: {% orca_field form.autoplay switch=True %} in a form with data-orca-autosubmit,
    # whose view saves it and redirects back.
    autoplay = forms.BooleanField(label="Play videos automatically", required=False)
''')],
    "choice-group": [("Form", '''# videos/forms.py
from django import forms


class ExportForm(forms.Form):
    # One answer: radios. {% orca_field form.format %} renders the fieldset, legend and options.
    format = forms.ChoiceField(choices=[("mp4", "MP4"), ("webm", "WebM"), ("gif", "Animated GIF")],
                               widget=forms.RadioSelect, initial="mp4")
    # Several answers: checkboxes.
    include = forms.MultipleChoiceField(choices=[("captions", "Captions"), ("chapters", "Chapters")],
                                        widget=forms.CheckboxSelectMultiple, required=False)
''')],
    "date-picker": [("Form", '''# videos/forms.py
from django import forms


class PublishForm(forms.Form):
    # orca_field renders a DateField as a native <input type="date"> with its label and help.
    publish_on = forms.DateField(label="Publish on", help_text="The video goes live at 08:00 that day.")
''')],
    "form-alert": [("Form-wide errors", '''# videos/forms.py
from django import forms


class ShareForm(forms.Form):
    email = forms.EmailField()
    expires_on = forms.DateField(required=False)

    def clean(self):
        data = super().clean()
        if not data.get("email", "").endswith("@example.com"):
            # Errors not tied to one field show in the alert: {% orca_form_errors form %}
            raise forms.ValidationError("Videos can only be shared inside your organisation.")
        return data
''')],
    "file-field": [("Form and view", '''# videos/forms.py
from django import forms


class UploadForm(forms.Form):
    file = forms.FileField(label="Video file", help_text="MP4 or WebM, up to 2 GB.")


# videos/views.py
from django.shortcuts import redirect, render


def upload(request):
    # The form needs enctype="multipart/form-data" and the files come in request.FILES.
    form = UploadForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        handle_upload(form.cleaned_data["file"])
        return redirect("video-list")
    return render(request, "videos/upload.html", {"form": form})
''')],
    "language-switcher": [("URLs and settings", '''# project/urls.py — Django's set_language view receives the switcher's form
from django.urls import include, path

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),   # the form posts to {% url 'set_language' %}
]

# project/settings.py
MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",      # after sessions, before common
    "django.middleware.common.CommonMiddleware",
]
LANGUAGES = [("en", "English"), ("fr", "Français"), ("de", "Deutsch")]
''')],
    "month-year-switcher": [("View", '''# videos/views.py — the switcher submits ?month=2026-11 on change
import datetime as dt

from django.utils import timezone


def chosen_month(request):
    value = request.GET.get("month", "")
    try:
        return dt.date.fromisoformat(value + "-01")
    except ValueError:
        return timezone.localdate().replace(day=1)
''')],
    "pagination": [("View", '''# videos/views.py
from django.views.generic import ListView

from .models import Video


class VideoList(ListView):
    model = Video
    paginate_by = 25          # gives the template page_obj
    # Template: {% orca_pagination page_obj noun="videos" %} — the links keep the other query
    # parameters (filters, sort) and the summary says "Showing 26–50 of 312 videos".
''')],
    "flash-message": [("View", '''# videos/views.py — needs django.contrib.messages in INSTALLED_APPS and its middleware
from django.contrib import messages
from django.shortcuts import redirect


def publish(request, pk):
    video = publish_video(pk)
    messages.success(request, f"Video “{video}” published.")      # positive
    # messages.info / warning / error give the information, caution and negative tones.
    return redirect("video-detail", pk=pk)
    # The app shell shows messages under the page head; elsewhere use {% orca_messages %}.
''')],
    "confirm-dialog": [("View", '''# videos/views.py — the dialog only confirms; the delete is a POST the server checks
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .models import Video


@require_POST
def delete_video(request, pk):
    video = get_object_or_404(Video, pk=pk, owner=request.user)
    video.delete()
    messages.success(request, f"Video “{video}” deleted.")
    return redirect("video-list")
''')],
    "timezone-selector": [("Form and middleware", '''# accounts/forms.py — {% orca_field form.timezone %} with the "Use my time zone" button
import zoneinfo

from django import forms


class TimezoneForm(forms.Form):
    timezone = forms.ChoiceField(choices=[(z, z.replace("_", " ")) for z in sorted(zoneinfo.available_timezones())])


# accounts/middleware.py — add "accounts.middleware.TimezoneMiddleware" to MIDDLEWARE
from django.utils import timezone


class TimezoneMiddleware:
    """Show every date and time in the person's own time zone."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        name = request.session.get("timezone")
        if name:
            timezone.activate(zoneinfo.ZoneInfo(name))
        else:
            timezone.deactivate()
        return self.get_response(request)
''')],
    "property-row": [("Formset", FORMSET)],
    "add-row-button": [("Formset", FORMSET)],
    "reminder-selector": [("Formset", FORMSET.replace("Chapter", "Reminder").replace("chapter", "reminder")
                           .replace('fields=["title", "starts_at"]', 'fields=["minutes_before", "method"]'))],
    # ------------------------------------------------------------------ components: data display
    "stat-card": [("View", '''# videos/views.py (get_context_data of the page)
from django.db.models import Count
from django.db.models.functions import ExtractHour
from django.utils import timezone

today = timezone.localdate()
views = Visit.objects.filter(at__date=today)
per_hour = dict(views.annotate(h=ExtractHour("at")).values_list("h").annotate(n=Count("id")))
ctx["views_today"] = views.count()
# Template: {% orca_sparkline hourly "Views per hour today" %}
ctx["hourly"] = [per_hour.get(h, 0) for h in range(8, 20)]
''')],
    "sparkline": [("View", '''# videos/views.py — a list of numbers, oldest first (or a string "12,18,9")
from django.db.models import Count
from django.db.models.functions import TruncDate

daily = (Visit.objects.filter(at__date__gte=start).annotate(day=TruncDate("at"))
         .values("day").annotate(n=Count("id")).order_by("day"))
ctx["trend"] = [row["n"] for row in daily]   # {% orca_sparkline trend "Views per day, last 30 days" %}
''')],
    "donut-chart": [("View", '''# videos/views.py — (label, value) pairs, dicts with label and value, or "A:3, B:1"
from django.db.models import Count

ctx["by_album"] = list(Video.objects.values_list("album__title").annotate(n=Count("id")).order_by("-n")[:5])
# Template: {% orca_donut by_album total_label="Videos" %}
''')],
    "mini-calendar": [("View", '''# videos/views.py
from django.utils import timezone

month = chosen_month(self.request)   # see Month and year switcher
days_with_events = Event.objects.filter(starts_at__year=month.year, starts_at__month=month.month)
ctx.update(
    month=month,
    today=timezone.localdate(),
    event_days=sorted({e.starts_at.date().isoformat() for e in days_with_events}),
)
# Template: {% orca_mini_calendar month selected=day today=today url="/calendar/{date}/" events=event_days %}
''')],
    # ------------------------------------------------------------------ patterns
    "messages-region": [("View", '''# Any view: add a message, then redirect (needs django.contrib.messages)
from django.contrib import messages

messages.success(request, "Report sent to 3 people.")
messages.error(request, "The export failed. Try again in a few minutes.")
# The app shell renders them; in other layouts put {% orca_messages %} at the top of the content.
''')],
    "filter-drawer": [("Filter form and list view", FILTERS)],
    "filter-bar": [("Filter form and list view", FILTERS)],
    "filter-panel": [("Filter form and list view", FILTERS)],
    "list-header": [("Search in the list view", '''# videos/views.py — the list header's search submits ?q=…
from django.db.models import Q
from django.views.generic import ListView


class VideoList(ListView):
    model = Video
    paginate_by = 25

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q", "").strip()
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(album__title__icontains=q))
        return qs
''')],
    "summary-tiles": [("Counts by status", TILES)],
    "data-table": [("Sorting and bulk actions", '''# videos/views.py
from django.contrib import messages
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView

from .models import Video

SORTABLE = {"title", "-title", "recorded_on", "-recorded_on", "views_today", "-views_today"}


class VideoList(ListView):
    model = Video
    paginate_by = 25

    def get_ordering(self):
        sort = self.request.GET.get("sort", "title")     # sortable headers link to ?sort=-recorded_on
        return sort if sort in SORTABLE else "title"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["sort"] = self.get_ordering()                 # the header marks aria-sort from it
        return ctx


@require_POST
def bulk_archive(request):
    """The table is a form; each row checkbox is name="selected" value="{{ video.pk }}"."""
    ids = request.POST.getlist("selected")
    count = Video.objects.filter(pk__in=ids, owner=request.user).update(archived=True)
    messages.success(request, f"{count} videos archived.")
    return redirect("video-list")
''')],
    "kanban-board": [("Board view and move endpoint", BOARD)],
    "zone-editor": [("Form", '''# videos/forms.py — the editor writes the points as JSON into a hidden field
import json

from django import forms


class RegionForm(forms.Form):
    name = forms.CharField()
    points = forms.CharField(widget=forms.HiddenInput)

    def clean_points(self):
        try:
            points = json.loads(self.cleaned_data["points"])
        except ValueError:
            raise forms.ValidationError("Draw the region again: its points could not be read.")
        if len(points) < 3 or not all(len(p) == 2 and all(0 <= v <= 100 for v in p) for p in points):
            raise forms.ValidationError("Draw at least three points inside the image.")
        return points   # [[x, y], …] in percent of the image; store it in a JSONField
''')],
    "rich-text-editor": [("Form", '''# videos/forms.py — the editor syncs its HTML into a hidden field; clean it before saving
import nh3   # pip install nh3

from django import forms

ALLOWED = {"p", "br", "strong", "b", "em", "i", "ul", "ol", "li", "a"}


class DescriptionForm(forms.Form):
    description = forms.CharField(widget=forms.HiddenInput, required=False)

    def clean_description(self):
        return nh3.clean(self.cleaned_data["description"], tags=ALLOWED, link_rel="noopener noreferrer")
''')],
    "schedule-editor": [("Formset", FORMSET.replace("Chapter", "OpeningHours").replace("chapter", "hours")
                         .replace('fields=["title", "starts_at"]', 'fields=["weekday", "opens", "closes"]'))],
    "properties-editor": [("Formset", FORMSET.replace("Chapter", "Property").replace("chapter", "property")
                           .replace('fields=["title", "starts_at"]', 'fields=["key", "value"]'))],
    "weekly-availability-editor": [("Formset", FORMSET.replace("Chapter", "Availability").replace("chapter", "availability")
                                    .replace('fields=["title", "starts_at"]', 'fields=["weekday", "starts", "ends"]'))],
    "time-off-editor": [("Form", DATE_RANGE)],
    "event-editor": [("Form", '''# events/forms.py
from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "starts_at", "ends_at", "all_day", "place", "calendar", "notes"]
        widgets = {"starts_at": forms.DateTimeInput(attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"),
                   "ends_at": forms.DateTimeInput(attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M")}

    def clean(self):
        data = super().clean()
        if data.get("starts_at") and data.get("ends_at") and data["ends_at"] <= data["starts_at"]:
            self.add_error("ends_at", "Choose an end after the start.")
        return data
''')],
    "date-range-filter-bar": [("Form and view helper", DATE_RANGE)],
    "email-frame": [("Sending the email", EMAIL)],
    "tabbed-panel-set": chart("Each tab's chart: labels and one series per line.", '''        ctx["by_day"] = {"labels": ["Mon", "Tue", "Wed"], "series": [{"name": "Views", "values": [120, 180, 150]}]}'''),
    "month-calendar": [("View", EVENTS)],
    "week-view": [("View", EVENTS)],
    "day-view": [("View", EVENTS)],
    "multi-day-view": [("View", EVENTS)],
    "agenda-view": [("View", EVENTS)],
    "year-view": [("View", EVENTS)],
    "mini-calendar-sidebar": [("View", EVENTS)],
}

# ------------------------------------------------------------------ charts: the data shape each kind expects
_BAR = '''        rows = (Visit.objects.filter(at__date__gte=start).annotate(day=TruncDate("at"))
                .values_list("day", "entrance").annotate(n=Count("id")))
        counts = {(day, entrance): n for day, entrance, n in rows}
        days = [start + dt.timedelta(days=i) for i in range(7)]
        entrances = sorted({entrance for _, entrance, _ in rows})
        ctx["visits"] = {"labels": [d.strftime("%a") for d in days],
                         "series": [{"name": e, "values": [counts.get((d, e), 0) for d in days]} for e in entrances]}
        # Template: {% orca_chart "bar" visits title="Visitors per day" subtitle="This week" %}'''
_LINE = '''        hours = range(8, 20)
        last_friday = today - dt.timedelta(days=(today.weekday() - 4) % 7 or 7)

        def per_hour(day):
            counts = dict(Visit.objects.filter(at__date=day).annotate(h=ExtractHour("at"))
                          .values_list("h").annotate(n=Count("id")))
            return [counts.get(h, 0) for h in hours]
        ctx["visits"] = {"labels": [f"{h:02}" for h in hours],
                         "series": [{"name": "Today", "values": per_hour(today)},
                                    {"name": "Last Friday", "values": per_hour(last_friday)}]}
        # Template: {% orca_chart "line" visits title="Visitors per hour" %} ("area" for one series)'''
_PART = '''        rows = Visit.objects.filter(at__date=today).values_list("entrance").annotate(n=Count("id")).order_by("-n")
        ctx["share"] = {"labels": [name for name, _ in rows], "series": [{"name": "Visitors", "values": [n for _, n in rows]}]}
        # Template: {% orca_chart "KIND" share title="Visitors by entrance" %} — one series; 2 to 5 parts read best'''
_POINTS = '''        # Points are (x, y) pairs; bubbles add a size: (x, y, size).
        ctx["points"] = {"labels": [], "series": [
            {"name": "Weekdays", "values": [(s.avg_dwell, s.visits) for s in weekday_stats]},
            {"name": "Weekends", "values": [(s.avg_dwell, s.visits) for s in weekend_stats]},
        ]}
        # Template: {% orca_chart "KIND" points title="Dwell time and visits" subtitle="x: minutes, y: visits per hour" %}'''
_RADAR = '''        axes = ["Accuracy", "Uptime", "Coverage", "Freshness", "Calibration"]
        ctx["scores"] = {"labels": axes, "series": [{"name": site.name, "values": [site.score(a) for a in axes]}
                                                    for site in sites]}
        # Template: {% orca_chart "radar" scores title="Site health" unit="" %}'''
for _id, _kind, _body, _note in [
    ("bar-chart", "bar", _BAR, "Categories as labels, one series per bar colour; stacked=True or horizontal=True."),
    ("line-chart", "line", _LINE, "Time points as labels, one series per line."),
    ("pie-chart", "pie", _PART.replace("KIND", "pie"), "Parts of a whole: labels and one series."),
    ("doughnut-chart", "doughnut", _PART.replace("KIND", "doughnut"), "Parts of a whole: labels and one series."),
    ("polar-area-chart", "polar", _PART.replace("KIND", "polar"), "Categories as labels and one series."),
    ("scatter-chart", "scatter", _POINTS.replace("KIND", "scatter"), "No labels; each series is a list of (x, y)."),
    ("bubble-chart", "bubble", _POINTS.replace("KIND", "bubble").replace("(s.avg_dwell, s.visits)", "(s.avg_dwell, s.visits, s.sites)"),
     "No labels; each series is a list of (x, y, size)."),
    ("radar-chart", "radar", _RADAR, "Axes as labels, one series per shape."),
]:
    SERVER[_id] = chart(_note, _body)

# ------------------------------------------------------------------ templates
SERVER.update({
    "base-layout": [("View", '''# videos/views.py
from django.utils.translation import get_language
from django.views.generic import TemplateView


class Landing(TemplateView):
    template_name = "videos/landing.html"   # {% extends "orca/layouts/base.html" %}

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(title="Welcome", lang=get_language())   # <html lang="…"> and the <title>
        return ctx
''')],
    "app-shell": [("Context processor and view", APP_NAV)],
    "auth-layout": [("URLs", '''# accounts/urls.py — Django's auth views with the ORCA layout
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(
        template_name="orca/layouts/auth.html",
        extra_context={"title": "Sign in", "subtitle": "Use your work email.", "submit_label": "Sign in"},
    ), name="login"),
    path("password-reset/", auth_views.PasswordResetView.as_view(
        template_name="orca/layouts/auth.html",
        extra_context={"title": "Reset your password", "submit_label": "Send the reset link"},
    ), name="password_reset"),
]
''')],
    "email-layout": [("Sending the email", EMAIL)],
    "homepage-template": [("View", '''# videos/views.py
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "orca/layouts/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = self.request.user
        ctx["title"] = f"Good morning, {user.first_name}"
        ctx["stats"] = [
            {"label": "Views today", "value": f"{views_today():,}", "icon": "show", "url": "/reports/"},
            {"label": "Videos", "value": Video.objects.count(), "icon": "play", "foot": "3 processing"},
        ]
        ctx["shortcuts"] = [{"label": "Add a video", "url": "/videos/new/", "icon": "plus"},
                            {"label": "Open reports", "url": "/reports/", "icon": "statistics"}]
        return ctx
''')],
    "feed-skeleton": [("View", '''# videos/views.py
from django.views.generic import TemplateView


class Feed(TemplateView):
    template_name = "orca/layouts/feed.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        posts = Post.objects.select_related("author").order_by("-created_at")[:20]
        ctx["posts"] = [{"author": p.author.get_full_name(), "when": p.created_at, "text": p.text,
                         "image": p.image.url if p.image else "", "alt": p.image_alt} for p in posts]
        ctx.update(title="Feed", has_more=Post.objects.count() > 20,
                   empty_title="No posts yet", empty_text="Share the first clip with your team.")
        return ctx
''')],
    "person-block-grid": [("View", '''# people/views.py
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView


class Team(TemplateView):
    template_name = "orca/layouts/people.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        users = get_user_model().objects.filter(is_active=True).order_by("first_name")
        ctx["people"] = [{"name": u.get_full_name(), "role": u.profile.role, "email": u.email,
                          "url": f"/people/{u.pk}/"} for u in users]
        ctx.update(title="Team", empty_title="No one here yet")
        return ctx
''')],
    "marketing-layout": [("View", '''# site/views.py
from django.views.generic import TemplateView


class Pricing(TemplateView):
    template_name = "site/pricing.html"   # {% extends "orca/layouts/marketing.html" %}
    extra_context = {
        "title": "Pricing",
        "site_nav": [{"label": "Product", "url": "/"}, {"label": "Pricing", "url": "/pricing/", "current": True},
                     {"label": "Docs", "url": "/docs/"}],
        "footer_cols": [{"title": "Product", "links": [{"label": "Features", "url": "/"}, {"label": "Pricing", "url": "/pricing/"}]},
                        {"title": "Help", "links": [{"label": "Documentation", "url": "/docs/"}]}],
    }
''')],
    "blog-layout": [("View", '''# blog/views.py
from datetime import date

from django.views.generic import TemplateView


class PostDetail(TemplateView):
    template_name = "blog/post.html"   # {% extends "orca/layouts/blog.html" %}, sections in {% block blog_body %}

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(title="How we count visitors", kicker="Case study",
                   subtitle="Two sentences that say what this page covers and who it is for.",
                   version="1.2.0", updated=date(2026, 11, 6), author="Person name", reading_time=4,
                   breadcrumbs=[("Blog", "/blog/"), ("How we count visitors", "")])
        return ctx
''')],
    "docs-layout": [("View", '''# docs/views.py
from datetime import date

from django.views.generic import TemplateView


class DocsPage(TemplateView):
    template_name = "docs/page.html"   # {% extends "orca/layouts/docs.html" %}, sections in {% block blog_body %}

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        here = self.request.path
        sections = {"Get started": ("book", [("Installation", "/docs/install/"), ("Usage", "/docs/usage/")]),
                    "Guides": ("repository", [("Uploads", "/docs/uploads/"), ("Sharing", "/docs/sharing/")])}
        ctx["docs_nav"] = [{"label": label, "icon": icon, "open": any(url == here for _, url in items),
                            "items": [{"label": t, "url": url, "current": url == here} for t, url in items]}
                           for label, (icon, items) in sections.items()]
        ctx.update(title="Uploads", subtitle="Add videos one by one or in bulk.", version="1.2.0", updated=date(2026, 11, 6),
                   breadcrumbs=[("Docs", "/docs/"), ("Uploads", "")])
        return ctx
''')],
    "generic-list": [("Views", GENERIC_VIEWS), ("URLs", GENERIC_URLS), ("Filters (optional)", FILTERS)],
    "generic-detail": [("Views", GENERIC_VIEWS), ("URLs", GENERIC_URLS)],
    "generic-form": [("Views", GENERIC_VIEWS), ("URLs", GENERIC_URLS)],
    "generic-confirm-delete": [("Views", GENERIC_VIEWS), ("URLs", GENERIC_URLS)],
    "generic-confirm-action": [("View", '''# videos/views.py
from django import forms
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import FormView

from .models import Album


class ArchiveForm(forms.Form):
    reason = forms.CharField(required=False, label="Reason (optional)")


class ArchiveAlbum(FormView):
    template_name = "orca/generic/confirm_action.html"
    form_class = ArchiveForm

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        album = get_object_or_404(Album, pk=self.kwargs["pk"])
        ctx.update(title=f"Archive {album}?", text="Its videos stay available by link but leave the library.",
                   items=[str(v) for v in album.videos.all()[:10]], danger=False,
                   submit_label="Archive album", cancel_url=album.get_absolute_url())
        return ctx

    def form_valid(self, form):
        album = get_object_or_404(Album, pk=self.kwargs["pk"])
        album.archive(reason=form.cleaned_data["reason"])
        messages.success(self.request, f"Album “{album}” archived.")
        return redirect("album-list")
''')],
    "parent-base": [("Parent mixin and views", PARENT)],
    "parent-detail": [("Parent mixin and views", PARENT)],
    "parent-child-list": [("Parent mixin and views", PARENT)],
    "parent-child-detail": [("Parent mixin and views", PARENT)],
    "parent-child-form": [("Parent mixin and views", PARENT)],
    "parent-child-confirm": [("Parent mixin and views", PARENT)],
    "dashboard": [("View", '''# reports/views.py
from django.views.generic import TemplateView


class Dashboard(TemplateView):
    template_name = "orca/layouts/dashboard.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        period = self.request.GET.get("period", "week")
        ctx["periods"] = [{"label": label, "url": f"?period={key}", "current": key == period}
                          for key, label in [("day", "Today"), ("week", "This week"), ("month", "This month")]]
        ctx["stats"] = [
            {"label": "Views", "value": "12,480", "icon": "show", "delta": "+8%", "trend": "up", "foot": " vs last week", "url": "/reports/views/"},
            {"label": "Videos published", "value": 36, "icon": "play", "foot": "of 40 planned"},
        ]
        # Each chart: kind, data (labels and series, as for {% orca_chart %}), title and subtitle.
        ctx["charts"] = [{"kind": "bar", "data": views_per_day(period), "title": "Views per day", "subtitle": "People"},
                         {"kind": "line", "data": views_per_hour(), "title": "Views per hour", "subtitle": "Today and last Friday"}]
        ctx["title"] = "Dashboard"
        return ctx
''')],
    "calendar-page": [("View", '''# events/views.py
import datetime as dt

from django.urls import reverse
from django.utils import timezone
from django.views.generic import TemplateView

from .models import Calendar, Event


class CalendarPage(TemplateView):
    template_name = "orca/layouts/calendar.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.localdate()
        view = self.request.GET.get("view", "month")                  # month, week, day or agenda
        day = dt.date.fromisoformat(self.request.GET.get("day", today.isoformat()))
        month = day.replace(day=1)
        step = {"month": dt.timedelta(days=31), "week": dt.timedelta(days=7)}.get(view, dt.timedelta(days=1))
        url = lambda d, v=view: f"?view={v}&day={d.isoformat()}"
        ctx.update(
            title="Calendar", view=view, day=day, month=month, today=today, now=timezone.localtime(),
            # Events: dicts (or objects) with title, start, end, all_day, color, url, location, status.
            events=[{"title": e.title, "start": e.starts_at, "end": e.ends_at, "all_day": e.all_day,
                     "color": e.calendar.color, "url": e.get_absolute_url(), "location": e.place}
                    for e in Event.objects.filter(starts_at__date__gte=month - dt.timedelta(days=7),
                                                  starts_at__date__lte=month + dt.timedelta(days=42))],
            holidays={"2026-11-11": "Armistice Day"},
            period_title=day.strftime("%B %Y") if view == "month" else day.strftime("%-d %B %Y"),
            prev_url=url(day - step), next_url=url(day + step), today_url=url(today),
            day_url="?view=day&day={date}", month_url="?view=month&day={month}-01",
            views=[{"label": v.title(), "url": url(day, v), "current": v == view} for v in ("month", "week", "day", "agenda")],
            calendars=[{"key": c.slug, "label": c.name, "color": c.color, "checked": True} for c in Calendar.objects.all()],
            create_url=reverse("event-create"),
        )
        return ctx
''')],
    "scheduler-page": [("View", '''# bookings/views.py
import datetime as dt

from django.utils import timezone
from django.views.generic import TemplateView

from .models import Booking, Room


class Scheduler(TemplateView):
    template_name = "orca/layouts/scheduler.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.localdate()
        day = dt.date.fromisoformat(self.request.GET.get("day", today.isoformat()))
        bookings = Booking.objects.filter(starts_at__date=day)
        # One row per resource; its bookings are events (title, start, end, status, url).
        ctx["resources"] = [{"name": room.name, "url": room.get_absolute_url(),
                             "bookings": [{"title": b.title, "start": b.starts_at, "end": b.ends_at, "status": b.status}
                                          for b in bookings if b.room_id == room.pk]}
                            for room in Room.objects.all()]
        ctx.update(title="Rooms", start_hour=8, end_hour=18, period_title=day.strftime("%A %-d %B"),
                   prev_url=f"?day={day - dt.timedelta(days=1)}", next_url=f"?day={day + dt.timedelta(days=1)}",
                   today_url=f"?day={today}")
        return ctx
''')],
    "planning-board-page": [("Board view and move endpoint", BOARD)],
    "timeline-page": [("View", '''# projects/views.py
import datetime as dt

from django.utils import timezone
from django.views.generic import TemplateView

from .models import Task


class Timeline(TemplateView):
    template_name = "orca/layouts/timeline.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        today = timezone.localdate()
        start = dt.date.fromisoformat(self.request.GET.get("start", (today - dt.timedelta(days=today.weekday())).isoformat()))
        # Rows: label, start, end (dates, end included), progress 0–100, state "done" or "late", url, milestone.
        ctx["rows"] = [{"label": t.title, "start": t.starts_on, "end": t.due_on, "progress": t.progress,
                        "state": "done" if t.done else ("late" if t.due_on < today else ""), "url": t.get_absolute_url()}
                       for t in Task.objects.filter(due_on__gte=start)]
        ctx.update(title="Timeline", start=start, days=14, today=today,
                   period_title=f"{start:%-d %b} – {start + dt.timedelta(days=13):%-d %b %Y}",
                   prev_url=f"?start={start - dt.timedelta(days=14)}", next_url=f"?start={start + dt.timedelta(days=14)}",
                   today_url="?")
        return ctx
''')],
    "booking-flow": [("View", '''# bookings/views.py — one view per step, sharing what was chosen in the session
from django.shortcuts import redirect, render

STEPS = ["Service", "Date and time", "Your details", "Confirm"]


def book_time(request):
    chosen = request.session.setdefault("booking", {})
    form = SlotForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        chosen["slot"] = form.cleaned_data["slot"].isoformat()
        request.session.modified = True
        return redirect("book-details")
    summary = [("Service", chosen.get("service", "")), ("Time", chosen.get("slot", ""))]
    return render(request, "bookings/time.html", {      # extends "orca/layouts/booking.html"
        "title": "Choose a time", "steps": STEPS, "step": 2, "summary": [s for s in summary if s[1]], "form": form,
    })
''')],
    "event-editor-page": [("View", '''# events/views.py
from django.urls import reverse
from django.views.generic import UpdateView

from orca.mixins import OrcaPageMixin

from .forms import EventForm
from .models import Event


class EventEdit(OrcaPageMixin, UpdateView):
    model = Event
    form_class = EventForm                     # see Event editor
    template_name = "orca/layouts/event_editor.html"
    list_url_name = "calendar"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        event = self.object
        # Bookings that overlap this one, shown as conflict warnings above the form.
        ctx["conflicts"] = [str(e) for e in Event.objects.filter(place=event.place, starts_at__lt=event.ends_at,
                                                                  ends_at__gt=event.starts_at).exclude(pk=event.pk)]
        ctx.update(title=f"Edit {event}", submit_label="Save event",
                   delete_url=reverse("event-delete", args=[event.pk]), cancel_url=reverse("calendar"))
        return ctx
''')],
    "simple-data-page": [("View", FILTERS.replace('template_name = "orca/generic/list.html"   # or "orca/layouts/simple_data.html"',
                                                  'template_name = "orca/layouts/simple_data.html"')),
                         ("Summary tiles", TILES)],
})


def attach() -> None:
    for element_id, items in SERVER.items():
        set_server(element_id, items)
