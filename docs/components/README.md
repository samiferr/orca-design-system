# ORCA components

Generated from `orca/catalogue/` by `python -m orca build`. Do not edit by hand.

Every element below has a **why**, **when**, **when not**, **how**, accessibility notes, the tokens and
classes it uses, the UX principles it applies, and a copy-ready Django template example.
Load the tags with `{% load orca %}` and put `{% orca_head %}` in `<head>`.

## [Forms](forms.md) (19)

Fields and the small groups around them. A form field is the unit people complete: label, hint, error and control in a fixed order.

- `form-field` **Form field**: Label, optional marker, help, error and one control, wired together. Text inputs and selects.
- `toggle-field` **Toggle field**: One checkbox or switch with its label, description and error.
- `choice-group` **Choice group**: A fieldset of radios (one answer) or checkboxes (several answers) with a legend, hint and error.
- `search-field` **Search field**: A labelled search input with magnifier, clear button and a live result count.
- `search-bar` **Search bar**: A search form: optional scope select, search field and a Search button.
- `table-toolbar` **Table toolbar**: The row above a table: search, filters and view options on the left, actions on the right, and a bulk-action bar when rows are selected.
- `multi-picker` **Multi-picker**: A dropdown with a filter and a checkbox list, showing the chosen values as removable tags.
- `language-switcher` **Language switcher**: A select of languages, each written in its own language, that posts to Django's set_language view.
- `input-group` **Input group**: An input joined to addons (unit, prefix) or a button that acts on it.
- `filter-button` **Filter button**: A button that opens the filters, showing how many are active.
- `dropdown-select` **Dropdown select (picker)**: A select-like button opening a listbox whose options can carry a description.
- `combobox` **Combobox (autocomplete)**: A text input that suggests matching options as people type; the value must be one of the options.
- `auto-suggest` **Auto-suggest input**: A free-text input with browser suggestions from a datalist.
- `otp-input` **OTP input**: The full one-time-code question: label, digit boxes, hint, error and a resend link.
- `rating-input` **Rating input**: One to five stars as a radio group, with the chosen value in words.
- `split-date` **Split date input**: Day, month and year as three labelled numeric fields.
- `file-field` **File input field**: A labelled drop zone around a native file input, listing the chosen files.
- `form-alert` **Form alert**: A message at the top of a form for errors that belong to no single field.
- `form-actions` **Form actions**: The row of buttons that ends a form: the primary action first, then the alternatives.

## [Navigation](navigation.md) (15)

How people move between places and pages. The current location is always marked with aria-current and a shape, not only colour.

- `primary-navigation` **Primary navigation**: The top-bar links to the main sections of the product.
- `utility-navigation` **Utility navigation**: Help, notifications and the user chip at the end of the top bar.
- `sidebar-link` **Sidebar link**: One destination in the side navigation: icon, label and an optional count.
- `breadcrumbs` **Breadcrumbs**: The path from the top of the hierarchy to the current page.
- `pagination` **Pagination**: Previous, page numbers with gaps, next, and a summary of what is shown.
- `pagination-summary` **Pagination summary**: 'Showing 121–140 of 312 videos': what part of the list is on screen.
- `table-pager` **Table pager**: A compact pager under a table: rows per page, the range shown, previous and next.
- `tab-bar` **Tab bar**: Tabs that switch between views of the same object, in place or by page.
- `child-tabs` **Child tabs (with counts)**: Page tabs on a parent record, one per kind of child, each showing how many there are.
- `bottom-navigation` **Bottom navigation bar**: Three to five main sections as icon-and-label buttons fixed at the bottom of phone screens.
- `nav-tree` **Nav tree**: Collapsible sections of navigation links (tree leaves) for large hierarchies.
- `back-link` **Back link**: A link to the previous level, above the page title.
- `view-toggle` **View toggle (cards, table)**: A segmented control switching a collection between cards and a table.
- `settings-toggle` **Settings toggle**: An icon button that opens the display settings panel (theme, density).
- `create-button` **Create button (floating on phones)**: The page's create action: a primary button in the page head that becomes a floating button on phones.

## [Feedback](feedback.md) (11)

How the system tells people what happened and what to do next: alerts, callouts, toasts, dialogs, empty states and progress.

- `alert` **Alert**: An event message in a white box with a coloured side bar: icon, title, text and optional actions.
- `callout` **Callout (info, success, warning, danger)**: A tinted box of guidance that belongs to the page, not to an event.
- `empty-state` **Empty state**: Illustration, title, explanation and the next action, where a list or page has nothing yet.
- `no-data-state` **No-data state**: A compact message inside a chart, table or tile that has no data for the chosen period.
- `status-light` **Status light**: A dot, a status word and an optional time: 'Offline since 08:14'.
- `dialog` **Dialog**: A modal window with a title, a body and actions, built on the native <dialog>.
- `confirm-dialog` **Confirm dialog**: A dialog that names the consequence and the action before something irreversible happens.
- `progress-with-counts` **Progress bar with counts**: A labelled progress bar with the value in words and the counts behind it.
- `toast` **Toast**: A short message that appears at the bottom corner after an action and goes away by itself; several stack.
- `flash-message` **Flash message**: Django messages shown as dismissible alerts at the top of the next page.
- `tooltip` **Tooltip**: A short label that appears on hover and keyboard focus, naming an icon-only control.

## [Actions](component-actions.md) (6)

Groups of actions: button groups, menus and the action sets that sit on records and rows.

- `button-group` **Button group**: Related buttons joined into one control, or spaced as a set.
- `dropdown-menu` **Dropdown menu**: A button that opens a list of actions.
- `dropdown-item` **Dropdown item**: One action in a menu: icon, label, optional description or shortcut; danger and disabled variants.
- `copy-button` **Copy button**: A value with a Copy button that confirms 'Copied' in place and for screen readers.
- `record-actions` **Record actions**: On a record's page: one visible main action and a 'More actions' menu for the rest.
- `row-actions` **Row actions**: Small actions at the end of a table row: one or two ghost buttons and an overflow menu.

## [Data display](data-display.md) (25)

Ways to present records and numbers: stat cards, lists, key/value lists, cards, tables, timelines and small charts.

- `stat-card` **Stat card**: One measured value with its label, change and context, optionally with a sparkline.
- `key-value-list` **Key/value list**: Properties of a record as label and value pairs.
- `list` **List**: A divided list of items with optional visual, text and end detail.
- `list-item` **List item**: One row of a list: leading visual, title and description, trailing detail; static, link, button or selected.
- `timeline-item` **Timeline item**: One event in a vertical timeline: status dot, title, time and description.
- `sortable-header` **Sortable column header**: A table header that sorts the column, showing the direction with an arrow and aria-sort.
- `legend-item` **Legend item**: A swatch, a series name and optionally its value, keying a chart.
- `zone-row` **Zone row**: A counting zone in a list: its swatch, name, type, count and actions.
- `line-count-item` **Line-count item**: A counting line with people in and out, each with a direction arrow.
- `media-object` **Media object**: An image or avatar beside a block of text.
- `card` **Card**: A container for one object: optional media, body and footer. Outlined (default), elevated or filled.
- `card-footer` **Card footer**: The bottom strip of a card for status and actions.
- `linked-card` **Linked card**: A card whose whole area opens the object, built with one real link on the title.
- `accordion` **Accordion**: A stack of sections that open and close, built on details and summary.
- `steps` **Steps**: The steps of a process with done, current and upcoming markers.
- `tree` **Tree**: A hierarchy of items that expand and collapse: sites, buildings, videos.
- `avatar-group` **Avatar group**: Overlapping avatars of the people involved, with '+N' for the rest.
- `table-card` **Table card**: A panel holding a titled table and its pager.
- `property-row` **Property row**: One editable key and value pair with a remove button, repeated to edit free-form properties.
- `activity-entry` **Activity entry**: One change in an audit log: what happened, who did it, when, and the before and after values.
- `carousel` **Carousel**: One slide at a time with previous and next buttons, dots and a count.
- `scroller` **Scroller**: A horizontal row that scrolls and snaps, showing part of the next item.
- `sparkline` **Sparkline**: A tiny trend line without axes, ending with a dot on the latest value.
- `donut-chart` **Donut chart**: A ring of up to about five shares with the total in the middle and a legend with values.
- `chart-frame` **Chart frame**: The frame every chart sits in: title, subtitle, legend, a reserved plot area, a source line and the data as a table.

## [Content blocks](content-blocks.md) (6)

Reusable blocks for products, people, posts, heroes and media.

- `product-item` **Product item**: A product tile: square image, name, price and one action.
- `person-block` **Person block**: Avatar, name and role, optionally with a contact action.
- `post-block` **Block post**: An article teaser: kicker, headline, excerpt, meta and a thumbnail.
- `hero` **Hero**: The opening block of a marketing or landing page: kicker, headline, lead, actions and an image.
- `photo-actions-bar` **Photo-actions bar**: The row under a photo: like, comment and share with counts, and save at the end.
- `video-card` **Video card**: A video's latest snapshot with its status, name, place and actions.

## [Identity and controls](identity-controls.md) (5)

Who is signed in, what a panel is, and the small controls that personalise the interface.

- `user-chip` **User chip**: Avatar, name and role of the signed-in person; opens the account menu.
- `panel-header` **Panel header**: The top of a panel: title, a short description and the panel's actions.
- `pin-control` **Pin control**: A pin toggle with a visible 'Pinned' state and an announcement when it changes.
- `theme-toggle` **Theme toggle**: A segmented choice of Auto, Light, Dark and Paper themes, remembered per browser.
- `email-fallback` **Email button (with fallback link)**: An email button with the address shown and a Copy button, for when no mail app opens.

## [Date and time pickers](pickers.md) (9)

Native date and time inputs, composed with shortcuts, ranges, time zones and a month grid. Native first: every device already knows how to pick a date.

- `date-picker` **Date picker**: A labelled native date input with shortcut buttons for the most common dates.
- `time-picker` **Time picker**: A labelled native time input with a step and its timezone.
- `datetime-picker` **Date-time picker**: A date and a time as two labelled fields in one group, with the timezone.
- `date-range-picker` **Date-range picker**: Start and end dates with presets, kept in order, and the length in days.
- `time-range-input` **Time-range input (start and end)**: Start and end times with the resulting duration, saying when it ends the next day.
- `duration-picker` **Duration picker**: Hours and minutes fields with quick choices for common durations.
- `timezone-selector` **Timezone selector**: A timezone select with a 'Use my timezone' button and the current offset.
- `month-year-switcher` **Month and year switcher**: Previous and next buttons around a month select and a year select.
- `mini-calendar` **Mini calendar**: A server-rendered month grid with today, selected, outside, weekend and holiday days.

## [Planning selectors](planning-selectors.md) (8)

Controls that choose days, repeats, reminders, periods, granularity and calendar views.

- `weekday-selector` **Weekday selector**: Seven weekday toggles with presets for weekdays, every day and clear.
- `recurrence-selector` **Recurrence selector**: A repeat select with common rules and a Custom option that reveals interval, days and end.
- `reminder-selector` **Reminder selector**: One or more reminder offsets, each removable, with an Add reminder button.
- `period-selector` **Period selector**: A segmented choice of Today, This week, This month and Custom, revealing a date range for Custom.
- `granularity-selector` **Granularity selector**: A segmented choice of how data is grouped: hour, day, week or month.
- `calendar-view-switcher` **Calendar view switcher**: Day, Week, Month and Agenda views as a segmented control.
- `preset-buttons` **Preset buttons**: A row of one-tap choices (Today, Weekdays, This week, Next 7 days) that fill a more detailed control.
- `calendar-navigation` **Calendar navigation**: Previous, Today and Next buttons with the visible period's label.

## [Calendar parts](calendar-parts.md) (14)

The pieces month, week, day and agenda views are built from. Each states the date in words for screen readers.

- `day-cell` **Day cell**: One day of a month view: day number, up to three events and a '+N more' link.
- `week-header` **Week header**: The week number and its date range, heading a week view.
- `weekday-header` **Weekday header**: The row of weekday names above a month or week grid.
- `week-row` **Week row**: One row of a month grid: the week number and seven day cells.
- `hour-row` **Hour row**: One hour of a day or week view: the hour label and two half-hour slots.
- `time-slot` **Time slot**: An empty half-hour in a day view that creates an event when chosen; free, busy or selected.
- `all-day-row` **All-day row**: The strip above the hours of a week view holding all-day and multi-day bars.
- `event-chip` **Event chip**: A one-line event in a month cell: colour dot, time and title.
- `event-card` **Event card**: An event block in a day or week view: title, time, place and its calendar colour edge.
- `agenda-item` **Agenda item**: One event in a list view: time column, colour dot, title and details.
- `date-badge` **Date badge**: A small calendar-page box with month, day number and weekday.
- `holiday-label` **Holiday label**: The holiday's name on a purple tint with a diamond mark.
- `more-events-link` **More-events link**: '+3 more' at the bottom of a crowded day cell, opening the full list of that day.
- `calendar-header` **Calendar header**: The month or period title with navigation and the view switcher.

## [Schedule parts](schedule-parts.md) (10)

Rows and messages for opening hours, availability, exceptions, time off and bookings.

- `schedule-row` **Schedule row**: One line of a weekly schedule: day, start time, end time and a remove button.
- `add-row-button` **Add-row button**: A ghost button that adds one more row to a repeating group and focuses it.
- `remove-row-button` **Remove-row button**: An icon button that removes its row, named after what it removes, with the removal announced.
- `availability-legend` **Availability legend**: The key to availability marks: free, busy, tentative and not working.
- `exception-entry` **Exception entry**: A one-day override of the usual schedule: date, new hours or Closed, and the reason.
- `time-off-entry` **Time-off entry**: A person's absence: who, dates, type and approval status.
- `booking-slot` **Booking slot**: A bookable time as a large button: free, limited ('2 left'), full or chosen.
- `conflict-warning` **Conflict warning**: A caution message saying what this plan conflicts with and how to resolve it.
- `overlap-warning` **Overlap warning**: An inline message under a schedule row whose times overlap another row.
- `working-hours-label` **Working-hours label**: 'Open now, closes at 18:00' or 'Closed, opens Monday 08:00', with a status dot.

## [Plan items](plan-items.md) (14)

Tasks, milestones, deadlines and reminders, and the chips that describe them: assignee, due date, status, priority, progress.

- `task-item` **Task item**: A task row: completion checkbox, title and chips for assignee, due date and priority.
- `subtask-item` **Subtask item**: A smaller, indented task under its parent with a connecting line.
- `milestone-item` **Milestone item**: A milestone row: diamond marker, name, date and state in words.
- `deadline-item` **Deadline item**: A deadline row: flag, name, due date and how long is left or how late it is.
- `reminder-item` **Reminder item**: A reminder that has come due: bell, text, time and Snooze or Done.
- `assignee-chip` **Assignee chip**: A small avatar and name showing who is responsible.
- `due-date-chip` **Due-date chip**: A calendar icon and the due date, amber when close, red and bold when overdue.
- `status-chip` **Status chip (planned, in progress, done, overdue)**: A plan item's state with a distinct shape per state: empty circle, half circle, full circle, square.
- `priority-chip` **Priority chip**: The priority marker in a chip, for use among other chips.
- `progress-chip` **Progress chip**: A tiny bar and a count ('3/5') of completed sub-items.
- `gantt-bar` **Gantt bar**: A task as a bar positioned on a time grid, with a progress line and milestones as diamonds.
- `plan-card` **Plan card**: A plan's summary: name, period, progress and counts of open, done and late items.
- `board-card` **Board card**: A card on a kanban board: title, labels, due date, assignee and a drag handle.
- `resource-row` **Resource row**: A person or resource with their load and a row of day cells showing availability.

## [Documentation site](docs-site.md) (3)

Components for documenting a design system or an API: live examples, code blocks and the navigation tree.

- `live-example` **Live example**: A rendered example and its source as two tabs.
- `code-block` **Code block**: Multi-line code with its language and a Copy button.
- `docs-nav-tree` **Docs navigation tree**: A documentation sidebar: a filter box above a nav tree of sections and pages.
