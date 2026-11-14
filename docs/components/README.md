# ORCA components

Generated from `orca/catalogue/` by `python -m orca build`. Do not edit by hand.

Every element below has a general description, **when**, **when not**, **how**, accessibility notes, the tokens and
classes it uses, the UX principles it applies, and a copy-ready Django template example.
Load the tags with `{% load orca %}` and put `{% orca_head %}` in `<head>`.

## [Forms](forms.md) (22)

Fields and the small groups around them. A form field holds a label, hint, error and control in a fixed order.

- `form-field` **Form field**: One control with its label, optional marker, help and error, linked together. For text inputs and selects.
- `toggle-field` **Toggle field**: One checkbox or switch with its label, description and error.
- `choice-group` **Choice group**: Radios (one answer) or checkboxes (several answers) in a fieldset with a legend, hint and error.
- `search-field` **Search field**: A labelled search input with magnifier, clear button and a live result count.
- `search-bar` **Search bar**: A search form: optional scope select, search field and a Search button.
- `table-toolbar` **Table toolbar**: The row above a table: search, filters and view options on the left, actions on the right, and a bulk-action bar when rows are selected.
- `multi-picker` **Multi-picker**: A dropdown with a filter and a checkbox list, showing the chosen values as removable tags.
- `language-switcher` **Language switcher**: A select of languages, each named in its own language, posting to Django's set_language view.
- `input-group` **Input group**: An input joined to addons (unit, prefix) or a button that acts on it.
- `filter-button` **Filter button**: A button that opens the filters, showing how many are active.
- `dropdown-select` **Dropdown select (picker)**: A select-style button that opens a listbox whose options can have a description.
- `combobox` **Combobox (autocomplete)**: A text input that suggests matching options as people type. The value must be one of them.
- `auto-suggest` **Auto-suggest input**: A free-text input with browser suggestions from a datalist.
- `otp-input` **OTP input**: A one-time-code field: label, digit boxes, hint, error and a resend link.
- `rating-input` **Rating input**: One to five stars as a radio group, with the chosen value in words.
- `split-date` **Split date input**: Day, month and year as three labelled numeric fields.
- `file-field` **File input field**: A labelled drop zone around a native file input that lists chosen files.
- `form-alert` **Form alert**: A message at the top of a form for errors that belong to no single field.
- `form-actions` **Form actions**: The row of buttons that ends a form: the primary action first, then the alternatives.
- `row-select` **Row selection**: A checkbox per table row and a select-all checkbox in the header.
- `formatting-toolbar` **Formatting toolbar**: A row of toggle icon buttons for bold, italic, lists and links above a text area.
- `applied-filters` **Applied filters**: Active filters as removable tags, with Clear all and the result count.

## [Navigation](navigation.md) (17)

How people move between pages. The current location is marked with aria-current and a shape, not colour alone.

- `primary-navigation` **Primary navigation**: Top-bar links to the product's main sections.
- `utility-navigation` **Utility navigation**: Help, notifications and the user chip at the end of the top bar.
- `sidebar-link` **Sidebar link**: One sidebar destination: icon, label and optional count.
- `breadcrumbs` **Breadcrumbs**: The path from the top level down to the current page.
- `pagination` **Pagination**: Previous, page numbers with gaps, next, and a summary of what is shown.
- `pagination-summary` **Pagination summary**: 'Showing 121–140 of 312 videos': which part of the list is on screen.
- `table-pager` **Table pager**: A compact pager under a table: rows per page, range shown, previous and next.
- `tab-bar` **Tab bar**: Tabs that switch between views of one object, in place or by page.
- `child-tabs` **Child tabs (with counts)**: Page tabs on a parent record, one per kind of child, each with a count.
- `bottom-navigation` **Bottom navigation bar**: 3 to 5 main sections as icon-and-label buttons fixed to the bottom of phone screens.
- `nav-tree` **Nav tree**: Collapsible groups of navigation links for large hierarchies.
- `back-link` **Back link**: A link to the previous level, above the page title.
- `view-toggle` **View toggle (cards, table)**: A segmented control that switches a collection between cards and a table.
- `settings-toggle` **Settings toggle**: An icon button that opens the display settings panel (theme, density).
- `create-button` **Create button (floating on phones)**: The page's create action: a primary button in the page head that floats on phones.
- `skip-navigation` **Skip navigation**: A skip link and the focusable main area it jumps to.
- `link-column` **Link column**: A titled list of links, as in a footer or a site map.

## [Feedback](feedback.md) (12)

Messages that tell people what happened and what to do next: alerts, callouts, toasts, dialogs, empty states and progress.

- `alert` **Alert**: A message about an event, in a box with a coloured side bar, icon, title, text and optional actions.
- `callout` **Callout (info, success, warning, danger)**: A tinted box of guidance that belongs to the page, not to an event.
- `empty-state` **Empty state**: An illustration, title, explanation and next action shown where a list or page is empty.
- `no-data-state` **No-data state**: A compact message in a chart, table or tile with no data for the chosen period.
- `status-light` **Status light**: A dot, a status word and an optional time: 'Offline since 08:14'.
- `dialog` **Dialog**: A modal window with a title, body and actions, built on the native <dialog>.
- `confirm-dialog` **Confirm dialog**: A dialog that names the consequence and action before something irreversible happens.
- `progress-with-counts` **Progress bar with counts**: A labelled progress bar showing the value and the counts behind it.
- `toast` **Toast**: A short message that appears in the bottom corner after an action and goes away on its own; several can stack.
- `flash-message` **Flash message**: Django messages shown as dismissible alerts at the top of the next page.
- `tooltip` **Tooltip**: A short label that appears on hover and keyboard focus, naming an icon-only control.
- `card-skeleton` **Card skeleton**: The grey shape of a card (image, title, two lines) while it loads.

## [Actions](component-actions.md) (6)

Button groups, menus, and the action sets on records and rows.

- `button-group` **Button group**: Related buttons joined into one control, or spaced as a set.
- `dropdown-menu` **Dropdown menu**: A button that opens a list of actions.
- `dropdown-item` **Dropdown item**: One action in a menu: icon, label, optional description or shortcut; danger and disabled variants.
- `copy-button` **Copy button**: A value with a Copy button that confirms 'Copied' in place and for screen readers.
- `record-actions` **Record actions**: On a record's page: one visible main action and a 'More actions' menu for the rest.
- `row-actions` **Row actions**: Small actions at the end of a table row: one or two ghost buttons and an overflow menu.

## [Data display](data-display.md) (29)

Ways to show records and numbers: stat cards, lists, cards, tables, timelines and small charts.

- `stat-card` **Stat card**: One measured value with its label, icon, change and comparison, optionally with a sparkline.
- `key-value-list` **Key/value list**: Properties of a record as label and value pairs.
- `list` **List**: A divided list of items with optional visual, text and end detail.
- `list-item` **List item**: One row of a list: leading visual, title and description, trailing detail; static, link, button or selected.
- `timeline-item` **Timeline item**: One event in a vertical timeline: status dot, title, time and description.
- `sortable-header` **Sortable column header**: A table header that sorts its column and shows the direction with an arrow and aria-sort.
- `legend-item` **Legend item**: A swatch, series name and optional value that key a chart.
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
- `property-row` **Property row**: An editable key and value pair with a remove button, repeated to edit free-form properties.
- `activity-entry` **Activity entry**: One audit-log change: what happened, who did it, when, and the before and after values.
- `carousel` **Carousel**: One slide at a time with previous and next buttons, dots and a count.
- `scroller` **Scroller**: A horizontal row that scrolls and snaps, showing part of the next item.
- `sparkline` **Sparkline**: A tiny trend line without axes, ending with a dot on the latest value.
- `donut-chart` **Donut chart**: A ring of up to about five shares with the total in the middle and a legend with values.
- `chart-frame` **Chart frame**: The frame around every chart: title, subtitle, legend, reserved plot area, source line and a data table.
- `big-number` **Big number**: One large figure with its statement and source.
- `summary-tile` **Summary tile**: A count and status word, as a link that filters the list to that status.
- `heat-row` **Heat-map row**: One labelled row of heat-map cells, each with its value printed.
- `column-header` **Column header**: A board column's title with its card count and, when set, its limit.

## [Content blocks](content-blocks.md) (14)

Reusable blocks for products, people, posts, heroes and media.

- `product-item` **Product item**: A product tile: square image, name, price and one action.
- `person-block` **Person block**: Avatar, name and role, optionally with a contact action.
- `post-block` **Block post**: An article teaser: kicker, headline, excerpt, meta and a thumbnail.
- `hero` **Hero**: The opening block of a marketing or landing page: kicker, headline, lead, actions and an image.
- `photo-actions-bar` **Photo-actions bar**: The row under a photo: like, comment and share with counts, and save at the end.
- `video-card` **Video card**: A video's latest snapshot with its status, name, place and actions.
- `page-heading` **Page heading**: The page title, a one-sentence subtitle and an optional line of facts and status badges.
- `section-heading` **Section heading**: A section title with an optional short introduction.
- `feature-item` **Feature item**: One feature: an icon, a short title and one sentence.
- `captioned-media` **Captioned media**: An image or video in a fixed-ratio frame, with a caption or flag on a solid bar.
- `thumbnail-strip` **Thumbnail strip**: A row of thumbnail buttons that pick the image shown and mark the current one.
- `video-player` **Video player**: A native video with a live or recording flag and the current time.
- `call-to-action` **Call to action**: The one or two actions a section asks for: a primary button and an optional quieter one.
- `fine-print` **Fine print**: Small legal and version text on one line, with policy links.

## [Identity and controls](identity-controls.md) (7)

Who is signed in, panel headers, and small controls that personalise the interface.

- `user-chip` **User chip**: Avatar, name and role of the signed-in person; opens the account menu.
- `panel-header` **Panel header**: A panel's top: title, short description and actions.
- `pin-control` **Pin control**: A pin toggle that shows 'Pinned' in words and announces changes.
- `theme-toggle` **Theme toggle**: A segmented choice of Auto, Light, Dark and Paper themes, remembered per browser.
- `email-fallback` **Email button (with fallback link)**: An email button with the address shown and a Copy button, for when no mail app opens.
- `logo-link` **Logo link**: The product logo as a link to the home page.
- `collapse-toggle` **Collapse toggle**: An icon button that collapses or expands a region and remembers the choice. Its label says what a press will do.

## [Date and time pickers](pickers.md) (9)

Native date and time inputs plus shortcuts, ranges, time zones and a month grid. Native comes first: every device already knows how to pick a date.

- `date-picker` **Date picker**: A native date input with shortcut buttons for common dates.
- `time-picker` **Time picker**: A labelled native time input with a step and its timezone.
- `datetime-picker` **Date-time picker**: A date field and a time field in one group, with the timezone.
- `date-range-picker` **Date-range picker**: Start and end dates with presets, always in order, and the length in days.
- `time-range-input` **Time-range input (start and end)**: Start and end times with the duration, noting when it ends the next day.
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

The building blocks of month, week, day and agenda views. Each gives screen readers the date in words.

- `day-cell` **Day cell**: One day of a month view: day number, up to three events and a '+N more' link.
- `week-header` **Week header**: The week number and its date range, heading a week view.
- `weekday-header` **Weekday header**: The row of weekday names above a month or week grid.
- `week-row` **Week row**: One row of a month grid: the week number and seven day cells.
- `hour-row` **Hour row**: One hour of a day or week view: the hour label and two half-hour slots.
- `time-slot` **Time slot**: An empty half-hour in a day view that creates an event when chosen; free, busy or selected.
- `all-day-row` **All-day row**: The strip above a week view's hours that holds all-day and multi-day bars.
- `event-chip` **Event chip**: A one-line event in a month cell: colour dot, time and title.
- `event-card` **Event card**: An event block in a day or week view: title, time, place and its calendar colour edge.
- `agenda-item` **Agenda item**: One event in a list view: time column, colour dot, title and details.
- `date-badge` **Date badge**: A small calendar-page box with month, day number and weekday.
- `holiday-label` **Holiday label**: The holiday's name on a purple tint with a diamond mark.
- `more-events-link` **More-events link**: '+3 more' at the bottom of a crowded day cell; opens that day's full list.
- `calendar-header` **Calendar header**: The month or period title with navigation and the view switcher.

## [Schedule parts](schedule-parts.md) (10)

Rows and messages for opening hours, availability, exceptions, time off and bookings.

- `schedule-row` **Schedule row**: One line of a weekly schedule: day, start time, end time and a remove button.
- `add-row-button` **Add-row button**: A ghost button that adds a row to a repeating group and focuses it.
- `remove-row-button` **Remove-row button**: An icon button that removes its row; named after the row and announced when used.
- `availability-legend` **Availability legend**: The key to the availability marks: free, busy, tentative, not working.
- `exception-entry` **Exception entry**: A one-day override of the usual schedule: date, new hours or Closed, and the reason.
- `time-off-entry` **Time-off entry**: A person's absence: who, dates, type and approval status.
- `booking-slot` **Booking slot**: A bookable time as a large button: free, limited ('2 left'), full or chosen.
- `conflict-warning` **Conflict warning**: A caution message naming what the plan conflicts with and how to fix it.
- `overlap-warning` **Overlap warning**: An inline message under a schedule row that overlaps another row.
- `working-hours-label` **Working-hours label**: 'Open now, closes at 18:00' or 'Closed, opens Monday 08:00', with a status dot.

## [Plan items](plan-items.md) (14)

Tasks, milestones, deadlines and reminders, with chips for assignee, due date, status, priority and progress.

- `task-item` **Task item**: A task row with a checkbox, a title, and chips for assignee, due date and priority.
- `subtask-item` **Subtask item**: A smaller indented task under its parent, joined by a line.
- `milestone-item` **Milestone item**: A milestone row: diamond marker, name, date and state in words.
- `deadline-item` **Deadline item**: A deadline row: flag, name, due date and time left or overdue.
- `reminder-item` **Reminder item**: A reminder that has come due: bell, text, time and Snooze or Done.
- `assignee-chip` **Assignee chip**: A small avatar and name showing who owns the item.
- `due-date-chip` **Due-date chip**: A calendar icon and the due date, amber when close, red and bold when overdue.
- `status-chip` **Status chip (planned, in progress, done, overdue)**: A plan item's state, each with its own shape: empty circle, half circle, full circle, square.
- `priority-chip` **Priority chip**: A priority marker in chip form, to sit beside other chips.
- `progress-chip` **Progress chip**: A tiny bar and a count ('3/5') of finished sub-items.
- `gantt-bar` **Gantt bar**: A task drawn as a bar on a time grid, with a progress line and milestone diamonds.
- `plan-card` **Plan card**: A plan summary: name, period, progress and counts of open, done and late items.
- `board-card` **Board card**: A card on a kanban board: title, labels, due date, assignee and a drag handle.
- `resource-row` **Resource row**: A person or resource with their workload and a row of day cells showing availability.

## [Documentation site](docs-site.md) (3)

Components for documenting a design system or API: live examples, code blocks and a navigation tree.

- `live-example` **Live example**: A rendered example and its source as two tabs.
- `code-block` **Code block**: Multi-line code with its language and a Copy button.
- `docs-nav-tree` **Docs navigation tree**: A documentation sidebar: an optional filter box and an optional Collapse all button above a tree of sections and pages.
