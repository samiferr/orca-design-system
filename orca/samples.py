"""Realistic sample data for the documentation examples (and for your own prototypes).

Every pattern example on the documentation site renders with ``sample`` in its context, so an example shows
both the markup and how to pass data to the template tags. The data describes a people-counting product:
sites, entrances, cameras, events, staff and plans, in the week of 2 November 2026 ("today" is Friday 6 November).
"""

TODAY = "2026-11-06"
NOW = "2026-11-06T10:40"

EVENTS = [
    {"title": "Trade fair", "start": "2026-11-04", "end": "2026-11-09", "all_day": True, "color": 4},
    {"title": "Inventory day", "start": "2026-11-02", "all_day": True, "color": 7},
    {"title": "Delivery window", "start": "2026-11-02T09:00", "end": "2026-11-02T10:30", "color": 1, "location": "Loading dock"},
    {"title": "Weekly review", "start": "2026-11-03T14:00", "end": "2026-11-03T15:00", "color": 3, "location": "Room 2"},
    {"title": "Camera install, Gate 1", "start": "2026-11-04T08:00", "end": "2026-11-04T12:00", "color": 2, "location": "Warehouse"},
    {"title": "Delivery window", "start": "2026-11-05T09:00", "end": "2026-11-05T10:30", "color": 1, "location": "Loading dock"},
    {"title": "Audit", "start": "2026-11-06T10:00", "end": "2026-11-06T11:30", "color": 2, "location": "North building", "status": "tentative"},
    {"title": "Supplier call", "start": "2026-11-06T10:30", "end": "2026-11-06T11:00", "color": 3},
    {"title": "Training", "start": "2026-11-06T14:00", "end": "2026-11-06T15:30", "color": 1, "status": "cancelled"},
    {"title": "Zone check", "start": "2026-11-06T16:00", "end": "2026-11-06T16:30", "color": 5},
    {"title": "Night count audit", "start": "2026-11-06T17:00", "end": "2026-11-06T18:00", "color": 6},
    {"title": "Weekly review", "start": "2026-11-10T14:00", "end": "2026-11-10T15:00", "color": 3, "location": "Room 2"},
    {"title": "Go-live rehearsal", "start": "2026-11-18T09:00", "end": "2026-11-18T12:00", "color": 2},
    {"title": "Weekly review", "start": "2026-11-17T14:00", "end": "2026-11-17T15:00", "color": 3},
    {"title": "Weekly review", "start": "2026-11-24T14:00", "end": "2026-11-24T15:00", "color": 3},
]
HOLIDAYS = {"2026-11-11": "Armistice Day"}

VISITORS_WEEK = {"labels": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
                 "series": [{"name": "Entrance A", "values": [4120, 3980, 4310, 4480, 5210, 6120, 2890]},
                            {"name": "Entrance B", "values": [2210, 2140, 2380, 2290, 2860, 3410, 1520]}]}
VISITORS_HOURS = {"labels": ["08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"],
                  "series": [{"name": "Today", "values": [180, 420, 610, 720, 980, 1010, 760, 690, 720, 910, 640, 310]},
                             {"name": "Last Friday", "values": [160, 380, 590, 700, 900, 960, 740, 700, 680, 860, 600, 280]}]}
BY_ENTRANCE = {"labels": ["Entrance A", "Gate 1", "Entrance B", "Car park"], "series": [{"name": "Visitors", "values": [4812, 2140, 1980, 640]}]}
DWELL_VS_VISITS = {"labels": [], "series": [{"name": "Weekdays", "values": [(12, 340), (14, 410), (18, 520), (21, 610), (24, 580)]},
                                             {"name": "Weekends", "values": [(26, 820), (31, 940), (35, 1010)]}]}
SITES_BUBBLE = {"labels": [], "series": [{"name": "Sites", "values": [(12, 340, 12), (20, 610, 4), (8, 180, 2), (30, 940, 7)]}]}
SITE_SCORES = {"labels": ["Accuracy", "Uptime", "Coverage", "Freshness", "Calibration"],
               "series": [{"name": "North building", "values": [96, 99, 84, 92, 88]}, {"name": "Warehouse", "values": [88, 94, 70, 97, 76]}]}
ALERTS_BY_TYPE = {"labels": ["Offline", "Over capacity", "Low accuracy", "Disk", "Tamper"], "series": [{"name": "Alerts", "values": [12, 7, 5, 3, 1]}]}

CAMERAS = [
    {"name": "Entrance A", "site": "North building", "status": "positive", "status_text": "Online", "today": 4812, "accuracy": 97.8, "last": "2 min ago"},
    {"name": "Entrance B", "site": "North building", "status": "positive", "status_text": "Online", "today": 1980, "accuracy": 95.1, "last": "5 min ago"},
    {"name": "Gate 1", "site": "Warehouse", "status": "caution", "status_text": "Degraded", "today": 2140, "accuracy": 91.4, "last": "1 min ago"},
    {"name": "Loading dock", "site": "Warehouse", "status": "negative", "status_text": "Offline", "today": 0, "accuracy": None, "last": "08:14"},
    {"name": "Car park", "site": "Car park", "status": "positive", "status_text": "Online", "today": 640, "accuracy": 93.0, "last": "3 min ago"},
]

PEOPLE = [
    {"name": "Ada Lovelace", "initials": "AL", "role": "Site manager", "hours": 32, "capacity": 40, "days": [8, 8, 0, 8, 8]},
    {"name": "Grace Hopper", "initials": "GH", "role": "Operator", "hours": 44, "capacity": 40, "days": [9, 9, 9, 9, 8]},
    {"name": "Alan Turing", "initials": "AT", "role": "Installer", "hours": 16, "capacity": 40, "days": [0, 8, 8, 0, 0]},
]

TASKS = [
    {"title": "Recalibrate Entrance A camera", "assignee": "AL", "due": "Tomorrow", "due_state": "soon", "priority": "high", "status": "progress"},
    {"title": "Draw zones for Gate 1", "assignee": "GH", "due": "Fri 13 Nov", "due_state": "", "priority": "medium", "status": "planned"},
    {"title": "Replace Loading dock camera", "assignee": "AT", "due": "Overdue, 4 Nov", "due_state": "overdue", "priority": "urgent", "status": "blocked"},
    {"title": "Mount Gate 1 bracket", "assignee": "AT", "due": "2 Nov", "due_state": "", "priority": "low", "status": "done"},
]

EMAIL_PARAGRAPHS = [
    "The Loading dock camera at Warehouse has sent no video since 08:14 today, so visitors there are not being counted.",
    "Check that the camera has power and a network connection. Counting restarts on its own when the stream is back.",
]

SAMPLE = {
    "today": TODAY, "now": NOW, "events": EVENTS, "holidays": HOLIDAYS, "visitors_week": VISITORS_WEEK,
    "visitors_hours": VISITORS_HOURS, "by_entrance": BY_ENTRANCE, "dwell_vs_visits": DWELL_VS_VISITS,
    "sites_bubble": SITES_BUBBLE, "site_scores": SITE_SCORES, "alerts_by_type": ALERTS_BY_TYPE,
    "cameras": CAMERAS, "people": PEOPLE, "tasks": TASKS, "email_paragraphs": EMAIL_PARAGRAPHS,
}
