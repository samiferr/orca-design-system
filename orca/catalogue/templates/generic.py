"""Level 4: generic CRUD and parent-child templates that work with Django's class-based views."""

from ..registry import add
from . import Template
from .layouts import APP_BLOCKS, APP_CONTEXT, C, extend

MIXIN = ("Add `orca.mixins.OrcaPageMixin` to the view: it fills `title`, `model_name`, `model_name_plural`, `columns` "
         "(from `list_columns`), `fields` (from `detail_fields`), the URLs (from `*_url_name`), `cancel_url` and `breadcrumbs`.")
URLS = "`create_url`, `detail_url_name`, `update_url_name`, `delete_url_name` (URL names taking the object's pk), `cancel_url`."
PARENT_CONTEXT = APP_CONTEXT + [
    "`parent`: the parent object (its title heads every tab).",
    "`parent_tabs`: `[{\"label\", \"url\", \"count\", \"current\"}]`, Overview first.",
    "`parent_stats`: optional `[{\"label\", \"value\"}]` shown above the tabs; `parent_update_url`.",
]
PARENT_BLOCKS = APP_BLOCKS + ["parent_summary", "parent_tabs", "detail_actions", "child_content"]


def generic(eid, name, template, summary, why, when, how, laws, uses, guide, blocks, context, avoid=(), classes=(), a11y=()):
    add(Template(eid, name, C, summary, why=why, when=list(when), avoid=list(avoid), how=[extend(template)] + list(how),
                 laws=list(laws), uses=list(uses), guide=list(guide), template=template, preview=eid, blocks=list(blocks),
                 context=list(context), classes=list(classes), a11y=list(a11y), source="ORCA"))


generic("generic-list", "Generic list template", "orca/generic/list.html",
        "A ListView page: title and Add button, optional filter panel, list header with count and search, "
        "a table that becomes cards on phones, pagination and empty states.",
        "Most screens of a business application are lists; one template that is always right (sortable header, row actions, empty and no-match states, "
        "phone cards) removes repeated decisions and keeps every list familiar (Jakob's law, Tesler's law).",
        ["Any ListView: records people find, compare and open."],
        [MIXIN, "Set `template_name = \"orca/generic/list.html\"`, `list_columns` and `paginate_by`; filter the queryset on `request.GET[\"q\"]` for the search box.",
         "Pass a `filter_form` (a GET form) for the filter panel; override `list` to replace the rows, `list_actions` to change the buttons."],
        ["jakob", "tesler", "miller", "L14"], ["app-shell", "list-header", "data-table", "filter-drawer", "no-results"],
        ["Generic list template", "List page"], APP_BLOCKS + ["list_actions", "filter_panel", "list_header", "list"],
        APP_CONTEXT + ["`object_list`, `page_obj`, `paginator` (from ListView).", "`columns`: `[{\"label\", \"name\", \"numeric\"}]`.", URLS,
                       "`filter_form`, `empty_title`, `empty_text`."],
        classes=[".orca-list-layout"])

generic("generic-detail", "Generic detail template", "orca/generic/detail.html",
        "A DetailView page: title, Edit and Delete actions, and the record's fields as a key–value list.",
        "Details read top to bottom as label and value pairs (Practical UI L01); Edit and Delete in the same place on every record make them findable without searching (Jakob's law).",
        ["Any DetailView: one record with its properties."],
        [MIXIN, "Set `detail_fields`; add related lists or history in `detail_extra`, change the buttons in `detail_actions`."],
        ["L01", "jakob", "B08"], ["app-shell", "detail-panel"],
        ["Generic detail template", "Detail page"], APP_BLOCKS + ["detail_actions", "detail", "detail_extra"],
        APP_CONTEXT + ["`object`, `fields`, `update_url`, `delete_url`."])

generic("generic-form", "Generic form template", "orca/generic/form.html",
        "A CreateView or UpdateView page: one column of ORCA fields with an error summary, Save and Cancel.",
        "One column is the fastest form to fill (Practical UI R01); the error summary and inline errors from `orca_form_errors` and `orca_field` "
        "make every form recover the same way (W15).",
        ["Any CreateView or UpdateView; any page whose main job is one form."],
        [MIXIN, "Help text on the model or form field shows under the label. Use `form_fields` to group fields in sections."],
        ["R01", "W15", "R09"], ["app-shell", "narrow-form"],
        ["Generic form template", "Form page"], APP_BLOCKS + ["form_fields", "form_actions"],
        APP_CONTEXT + ["`form`, `object` (when editing), `submit_label`, `cancel_url`."])

generic("generic-confirm-delete", "Generic confirm (delete) template", "orca/generic/confirm_delete.html",
        "A DeleteView confirmation: what will be deleted, what is kept, a danger button and Cancel; "
        "or, if other records still use it, why it cannot be deleted yet.",
        "Deleting is the most costly mistake, so friction scales with it (Practical UI B13): consequences in words, the danger button named after the action. "
        "When related records protect it, saying which ones turns a dead end into a task (W15).",
        ["Any DeleteView; any page confirming a destructive action."],
        [MIXIN + " On a DeleteView it also fills `blocked_by` from protected and restricted foreign keys.",
         "Pass `deleted` (a list) and `kept` (a sentence); `confirm_text` adds a required 'I understand' checkbox for severe deletes."],
        ["B13", "W15", "B10"], ["app-shell", "confirm-action-panel", "delete-blocked-notice"],
        ["Generic confirm (delete) template", "Confirm page"], APP_BLOCKS + ["consequences", "blocked_actions"],
        APP_CONTEXT + ["`object`, `deleted`, `kept`, `confirm_text`, `blocked_by`, `submit_label`, `cancel_url`."])

generic("generic-confirm-action", "Generic confirm-action template", "orca/generic/confirm_action.html",
        "A confirmation page for a consequential action other than delete: archive, send, disable, run.",
        "A separate page with the consequences listed gives people a moment to check (Practical UI B13) without the alarm of a danger colour when nothing is lost.",
        ["Actions with wide effects that need a second look: send to everyone, disable a site, start a long run."],
        ["Pass `title` (a question), `text`, `items` and `submit_label` (the verb); set `danger=True` only when something is lost.",
         "Add a `form` for an optional reason or choice."],
        ["B13", "B10", "W04"], ["app-shell", "confirm-action-panel"],
        ["Generic confirm-action template"], APP_BLOCKS + ["consequences"],
        APP_CONTEXT + ["`title`, `text`, `items`, `form`, `danger`, `submit_label`, `cancel_url`."])

generic("parent-base", "Parent base template", "orca/generic/parent_base.html",
        "The frame shared by a parent record's pages: title and actions, optional summary stats, and tabs for the overview and each child list.",
        "Keeping the parent's header and tabs fixed while the tab content changes tells people where they are and what else the record holds (Practical UI L05, Jakob's law).",
        ["Records that own other records: a site and its videos, a project and its tasks."],
        ["Extend it for each tab and fill `child_content`; mark the current tab in `parent_tabs`.",
         "Each tab has its own URL and view, so it can be linked, bookmarked and refreshed."],
        ["L05", "jakob", "miller"], ["parent-child-tabs"],
        ["Parent base template"], PARENT_BLOCKS, PARENT_CONTEXT, classes=[".orca-parent__panel"])

generic("parent-detail", "Parent detail template", "orca/generic/parent_detail.html",
        "The parent's Overview tab: its fields as a key–value list, with room for more overview panels.",
        "The overview answers 'what is this record' before any child list (Practical UI W04), so the first tab is always the parent itself.",
        ["The first tab of a parent record."],
        ["Pass `fields` (or use OrcaPageMixin's `detail_fields`); add panels in `overview_extra`."],
        ["W04", "L01"], ["parent-base", "detail-panel"],
        ["Parent detail template (tabbed)", "Parent detail page (overview + child tabs)"], PARENT_BLOCKS + ["overview", "overview_extra"],
        PARENT_CONTEXT + ["`fields`."])

generic("parent-child-list", "Parent-child list template", "orca/generic/child_list.html",
        "A child list inside a parent tab: header with count and 'Add … to parent', the table, pagination and an empty state naming the parent.",
        "Naming the parent in the add button and the empty state ('No videos for North building') removes any doubt about where a new record goes (Practical UI W04, B10).",
        ["Each child tab of a parent record. The four parent-child templates (list, detail, form, confirm) make up its pages."],
        [MIXIN, "Filter the queryset by the parent from the URL; pass `parent` and `parent_tabs` with this tab current."],
        ["W04", "B10", "jakob"], ["parent-base", "child-list-tab"],
        ["Parent-child list template", "Parent-child pages (list, detail, form, confirm)"], PARENT_BLOCKS + ["list_actions", "list"],
        PARENT_CONTEXT + ["`object_list`, `page_obj`, `columns`.", URLS])

generic("parent-child-detail", "Parent-child detail template", "orca/generic/child_detail.html",
        "One child record inside its parent's tab: a back link to the list, Edit and Delete, and the record's fields.",
        "The back link and the parent's header keep the path home visible (Jakob's law); the child's own actions sit next to its title (Practical UI L14).",
        ["Opening a child record without leaving its parent."],
        [MIXIN, "Pass `list_url` for the back link; `detail` overrides the field list."],
        ["jakob", "L14"], ["parent-base", "top-actions-header", "detail-panel"],
        ["Parent-child detail template"], PARENT_BLOCKS + ["detail_actions", "detail"], PARENT_CONTEXT + ["`object`, `fields`, `list_url`, `update_url`, `delete_url`."])

generic("parent-child-form", "Parent-child form template", "orca/generic/child_form.html",
        "Create or edit a child inside its parent's tab, with a heading that names the parent.",
        "A form that says 'Add video to North building' cannot be misread (Practical UI W04), and the parent's tabs stay one click away.",
        ["Adding and editing child records."],
        [MIXIN, "Set the parent on the new object in `form_valid` (do not show the parent as a field)."],
        ["W04", "R01", "R02"], ["parent-base", "form-stack"],
        ["Parent-child form template"], PARENT_BLOCKS + ["form_fields"], PARENT_CONTEXT + ["`form`, `object`, `model_name`, `cancel_url`."])

generic("parent-child-confirm", "Parent-child confirm template", "orca/generic/child_confirm.html",
        "Confirm removing a child from its parent, or explain what blocks it.",
        "The question names both records ('Remove Gate 1 from Warehouse?') so the consequence is clear (Practical UI B13, W04).",
        ["Deleting a child record from inside its parent."],
        [MIXIN, "Pass `deleted` to list what goes with it; `blocked_by` is filled by the mixin on a DeleteView."],
        ["B13", "W04"], ["parent-base", "confirm-action-panel", "delete-blocked-notice"],
        ["Parent-child confirm template"], PARENT_BLOCKS + ["consequences"], PARENT_CONTEXT + ["`object`, `deleted`, `blocked_by`, `submit_label`, `cancel_url`."])
