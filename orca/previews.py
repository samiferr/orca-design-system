"""Placeholder context for the live previews of template-level elements on the documentation site.

A template shows structure, not real content (ORCA guide, level 4), so the records here are neutral placeholders
("Record name 1", "Category A"). Calendars and plans use ``orca.samples`` because they need real dates.
"""

from __future__ import annotations

from django import forms
from django.core.paginator import Paginator
from django.templatetags.static import static

from .samples import SAMPLE


def nav(current: str = "Records") -> list[dict]:
    items = [("Overview", "home", ""), ("Records", "list", 24), ("Calendar", "calendar", ""), ("Reports", "statistics", "")]
    return [
        {"label": "", "items": [{"label": l, "url": "#", "icon": i, "count": c, "current": l == current} for l, i, c in items]},
        {"label": "Admin", "items": [{"label": "Users", "url": "#", "icon": "user", "current": current == "Users"},
                                     {"label": "Settings", "url": "#", "icon": "settings", "current": current == "Settings"}]},
    ]


ROWS = [{"pk": i, "name": f"Record name {i}", "category": "Category A" if i % 3 else "Category B",
         "status": "Active" if i % 4 else "Paused", "amount": 1000 + i * 137, "updated": f"{(i % 27) + 1} Nov 2026",
         "owner": "Person name", "notes": "", "get_absolute_url": "#"} for i in range(1, 25)]
COLUMNS = [{"label": "Name", "name": "name"}, {"label": "Category", "name": "category"}, {"label": "Status", "name": "status"},
           {"label": "Amount", "name": "amount", "numeric": True}, {"label": "Updated", "name": "updated"}]
FIELDS = COLUMNS + [{"label": "Owner", "name": "owner"}, {"label": "Notes", "name": "notes"}]


class RecordForm(forms.Form):
    name = forms.CharField(label="Name", help_text="Shown in lists and reports.", initial="Record name 1")
    category = forms.ChoiceField(label="Category", choices=[("a", "Category A"), ("b", "Category B")])
    amount = forms.IntegerField(label="Amount", initial=1137)
    notes = forms.CharField(label="Notes", required=False, widget=forms.Textarea(attrs={"rows": 3}))
    active = forms.BooleanField(label="Active", required=False, initial=True)


class FilterForm(forms.Form):
    status = forms.MultipleChoiceField(label="Status", required=False, widget=forms.CheckboxSelectMultiple,
                                       choices=[("active", "Active"), ("paused", "Paused")])
    category = forms.ChoiceField(label="Category", required=False, choices=[("", "Any category"), ("a", "Category A"), ("b", "Category B")])


class SignInForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"autocomplete": "username"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}))


class EventForm(forms.Form):
    title = forms.CharField(label="Title", initial="Event title")
    start = forms.DateTimeField(label="Starts", widget=forms.DateTimeInput(attrs={"type": "datetime-local"}), initial="2026-11-06T10:00")
    end = forms.DateTimeField(label="Ends", widget=forms.DateTimeInput(attrs={"type": "datetime-local"}), initial="2026-11-06T11:00")
    location = forms.CharField(label="Location", required=False)
    notes = forms.CharField(label="Notes", required=False, widget=forms.Textarea(attrs={"rows": 3}))


def _list(**extra) -> dict:
    page = Paginator(ROWS, 8).page(1)
    return dict(object_list=page.object_list, page_obj=page, paginator=page.paginator, is_paginated=True,
                columns=COLUMNS, model_name="record", model_name_plural="records", create_url="#",
                detail_url_name="", update_url_name="#", delete_url_name="#", **extra)


RECORD = ROWS[0]
PARENT = {"pk": 1, "name": "Parent record", "category": "Category A", "status": "Active", "amount": 4210,
          "updated": "6 Nov 2026", "owner": "Person name", "notes": ""}


class _Parent(dict):
    def __str__(self):
        return self["name"]


class _Record(dict):
    def __str__(self):
        return self["name"]


def _parent(current: str, **extra) -> dict:
    tabs = [("Overview", None), ("Records", 24), ("People", 3), ("Activity", None)]
    return dict(parent=_Parent(PARENT), parent_update_url="#", subtitle="Short description of the parent record",
                parent_stats=[{"label": "Records", "value": "24", "icon": "list"}, {"label": "Last change", "value": "2 days ago", "icon": "history"}],
                parent_tabs=[{"label": l, "url": "#", "count": c, "current": l == current} for l, c in tabs],
                breadcrumbs=[("Parents", "#"), ("Parent record", "")], fields=FIELDS, **extra)


def context(element_id: str) -> dict:
    base = {"nav": nav(), "sample": SAMPLE}
    rec = _Record(RECORD)
    c = {
        "app-shell": dict(title="Page title", subtitle="One sentence about what this page is for.",
                          breadcrumbs=[("Section", "#"), ("Page title", "")], nav=nav("Overview")),
        "auth-layout": dict(title="Sign in", form=SignInForm()),
        "email-layout": dict(title="Email title", preheader="One line shown in the inbox list",
                             paragraphs=["First paragraph: what happened, in one or two sentences.",
                                         "Second paragraph: what the reader can do about it."],
                             action_url="https://example.com/", action_label="Main action",
                             footer="Why the reader gets this email, and how to stop it."),
        "error-layouts": {},
        "homepage-template": dict(title="Good morning, Person", nav=nav("Overview"),
                                  stats=[{"label": "Metric one", "value": "1,234", "foot": "vs last week", "icon": "user"},
                                         {"label": "Metric two", "value": "56", "foot": "of 60", "icon": "clock"},
                                         {"label": "Metric three", "value": "98%", "foot": "last 7 days", "icon": "statistics"}],
                                  shortcuts=[{"label": "Add a record", "url": "#", "icon": "plus"}, {"label": "Open reports", "url": "#", "icon": "statistics"}]),
        "feed-skeleton": dict(title="Feed", nav=nav("Overview"), has_more=True,
                              posts=[{"author": "Person name", "when": "2 hours ago", "image": static("orca/img/sample-street.svg"),
                                      "alt": "Placeholder photo", "text": "Caption of the post, one or two lines."}]),
        "person-block-grid": dict(title="People", nav=nav("Users"),
                                  people=[{"name": f"Person name {i}", "role": "Role, team", "url": "#", "email": "person@example.com"} for i in range(1, 9)]),
        "generic-list": _list(title="Records", filter_form=FilterForm()),
        "generic-detail": dict(object=rec, title="Record name 1", fields=FIELDS, update_url="#", delete_url="#",
                               breadcrumbs=[("Records", "#"), ("Record name 1", "")]),
        "generic-form": dict(form=RecordForm(), object=rec, title="Edit Record name 1", cancel_url="#", breadcrumbs=[("Records", "#"), ("Record name 1", "#"), ("Edit", "")]),
        "generic-confirm-delete": dict(object=rec, deleted=["The record and its 3 notes"], kept="the record's lines in past reports.",
                                       cancel_url="#", submit_label="Delete record", breadcrumbs=[("Records", "#"), ("Record name 1", "#"), ("Delete", "")]),
        "generic-confirm-action": dict(title="Archive Record name 1?", text="Archived records leave every list but stay in reports.",
                                       items=["It stops appearing in searches", "Its owner gets an email"], submit_label="Archive record", cancel_url="#"),
        "parent-base": _parent("Overview"),
        "parent-detail": _parent("Overview"),
        "parent-child-list": dict(_parent("Records"), **_list()),
        "parent-child-detail": dict(_parent("Records"), object=rec, list_url="#", update_url="#", delete_url="#", model_name_plural="records"),
        "parent-child-form": dict(_parent("Records"), form=RecordForm(), model_name="record", cancel_url="#"),
        "parent-child-confirm": dict(_parent("Records"), object=rec, cancel_url="#", submit_label="Delete record"),
        "marketing-layout": dict(site_nav=[{"label": "Product", "url": "#", "current": True}, {"label": "Pricing", "url": "#"}, {"label": "Docs", "url": "#"}],
                                 footer_cols=[{"title": "Product", "links": [{"label": "Features", "url": "#"}, {"label": "Pricing", "url": "#"}]},
                                              {"title": "Help", "links": [{"label": "Documentation", "url": "#"}, {"label": "Contact", "url": "#"}]}]),
        "docs-layout": dict(title="Page title", subtitle="One or two sentences: what this page explains and who it is for.",
                            breadcrumbs=[("Section", "#"), ("Page title", "")],
                            docs_nav=[{"label": "Get started", "open": True, "items": [{"label": "Installation", "url": "#"}, {"label": "Page title", "url": "#", "current": True}]},
                                      {"label": "Reference", "items": [{"label": "Settings", "url": "#"}, {"label": "Template tags", "url": "#"}]}]),
        "dashboard": dict(title="Dashboard", nav=nav("Overview"),
                          periods=[{"label": "Today", "url": "#"}, {"label": "This week", "url": "#", "current": True}, {"label": "This month", "url": "#"}],
                          stats=[{"label": "Metric one", "value": "12,480", "delta": "+8%", "trend": "up", "foot": " vs last week", "url": "#", "icon": "user"},
                                 {"label": "Metric two", "value": "1,204", "foot": "of 1,500", "icon": "home"}, {"label": "Metric three", "value": "96.4%", "foot": "last 7 days", "icon": "statistics"},
                                 {"label": "Metric four", "value": "11 of 12", "icon": "play"}],
                          charts=[{"kind": "bar", "data": SAMPLE["visitors_week"], "title": "Chart title", "subtitle": "Unit and period"},
                                  {"kind": "line", "data": SAMPLE["visitors_hours"], "title": "Chart title", "subtitle": "Unit and period"}]),
        "calendar-page": dict(title="Calendar", nav=nav("Calendar"), create_url="#", view="month", month="2026-11", day="2026-11-06",
                              today=SAMPLE["today"], now=SAMPLE["now"], events=SAMPLE["events"], holidays=SAMPLE["holidays"],
                              period_title="November 2026", prev_url="#", next_url="#", today_url="#", day_url="#{date}", month_url="#{month}",
                              event_days="2026-11-02,2026-11-03,2026-11-04,2026-11-05,2026-11-06,2026-11-10",
                              views=[{"label": l, "url": "#", "current": l == "Month"} for l in ("Day", "Week", "Month", "Agenda")],
                              calendars=[{"key": "a", "label": "Calendar one", "color": 1, "checked": True}, {"key": "b", "label": "Calendar two", "color": 3, "checked": True}]),
        "scheduler-page": dict(title="Schedule", nav=nav("Calendar"), period_title="Friday 6 November 2026", prev_url="#", next_url="#", today_url="#",
                               resources=[{"name": "Resource one", "bookings": [{"title": "Booking", "start": "2026-11-06T10:00", "end": "2026-11-06T11:30", "color": 2},
                                                                                {"title": "Booking", "start": "2026-11-06T14:00", "end": "2026-11-06T15:30", "color": 1}]},
                                          {"name": "Resource two", "bookings": [{"title": "Booking", "start": "2026-11-06T08:00", "end": "2026-11-06T12:00", "color": 5}]},
                                          {"name": "Resource three", "bookings": [{"title": "Away", "start": "2026-11-06", "all_day": True, "color": 8, "status": "tentative"}]},
                                          {"name": "Resource four", "bookings": []}]),
        "planning-board-page": dict(title="Board", nav=nav("Records"), create_url="#", filter_form=FilterForm(),
                                    board_columns=[{"key": "todo", "name": "To do", "cards": [{"id": 1, "title": "Task title", "tags": ["Tag"], "due": "Fri 13 Nov", "assignee": "Person name"}]},
                                                   {"key": "doing", "name": "In progress", "limit": 2, "cards": [{"id": 2, "title": "Task title", "tags": ["Tag"], "due": "Tomorrow", "due_state": "soon", "assignee": "Person name"},
                                                                                                               {"id": 3, "title": "Task title", "due": "Mon 9 Nov", "assignee": "Other person"}]},
                                                   {"key": "done", "name": "Done", "cards": [{"id": 4, "title": "Task title", "due": "2 Nov"}]}]),
        "timeline-page": dict(title="Timeline", nav=nav("Records"), period_title="2 – 15 November 2026", prev_url="#", next_url="#", today_url="#",
                              start="2026-11-02", days=14, today=SAMPLE["today"],
                              rows=[{"label": "Phase one", "start": "2026-11-02", "end": "2026-11-04", "state": "done", "progress": 100},
                                    {"label": "Phase two", "start": "2026-11-05", "end": "2026-11-10", "progress": 40},
                                    {"label": "Phase three", "start": "2026-11-09", "end": "2026-11-12", "state": "late", "milestone": "2026-11-15"}]),
        "booking-flow": dict(title="Book a slot", nav=nav("Calendar"), steps=["Service", "Time", "Confirm"], step=2,
                             summary=[("Service", "Service name, 30 min"), ("With", "Anyone available")]),
        "event-editor-page": dict(form=EventForm(), cancel_url="#", nav=nav("Calendar"), breadcrumbs=[("Calendar", "#"), ("New event", "")],
                                  conflicts=["Overlaps Other event, 10:30–11:00"]),
        "simple-data-page": _list(title="Records", subtitle="Every record, with its status.", filter_form=FilterForm(), active_filters=1,
                                  tiles=[{"label": "All", "value": 24, "url": "#", "current": True}, {"label": "Active", "value": 18, "url": "#", "tone": "positive"},
                                         {"label": "Paused", "value": 6, "url": "#", "tone": "caution"}]),
    }[element_id]
    return {**base, **c}
