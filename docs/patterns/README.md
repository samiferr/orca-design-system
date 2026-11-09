# ORCA patterns

Generated from `orca/catalogue/` by `python -m orca build`. Do not edit by hand.

Every element below has a **why**, **when**, **when not**, **how**, accessibility notes, the tokens and
classes it uses, the UX principles it applies, and a copy-ready Django template example.
Load the tags with `{% load orca %}` and put `{% orca_head %}` in `<head>`.

## [Page frame](page-frame.md) (11)

The parts every page sits in: headers, top bar, sidebar, footer, page head, messages, drawers and filter panels.

- `site-header` **Header**: The public site header: logo, a few section links and one or two actions, sticky at the top.
- `top-bar` **Top bar**: The application bar: menu button, logo, main sections, search and the user's tools.
- `sidebar` **Sidebar**: The application's side navigation: grouped section links, collapsible to an icon rail, remembered per person.
- `footer` **Footer**: The bottom of public pages: link columns, legal text and version.
- `page-head` **Page head**: The top of a page's content: breadcrumbs or back link, title, subtitle, meta and the page's actions.
- `messages-region` **Messages region**: The place under the page head where results of the last action appear, announced politely.
- `drawer` **Drawer**: A panel that slides over the page from one edge, built on the native dialog.
- `top-actions-header` **Top actions header**: A thin row above a detail or form page: back link on one side, the page's actions on the other.
- `settings-panel` **Settings panel**: Display preferences in groups: theme and density, with a live result. ORCA has one appearance (Tangerine) and brand colours set by the project.
- `filter-panel` **Filter panel**: Filters in labelled groups with the number of results and Clear all: the content of the filter drawer.
- `filter-drawer` **Filter drawer**: Page filters in a right drawer, opened by a Filters button in the page actions, with Show results and Clear all.

## [Grids and collections](grids.md) (5)

Repeating one component in a responsive grid or sequence: products, videos, KPIs, a heat map, an event timeline.

- `product-grid` **Product grid**: Product items in a responsive grid that adapts the number of columns to the screen.
- `video-grid` **Video grid**: Video cards in a grid, pinned videos first, offline videos clearly marked.
- `kpi-grid` **KPI grid**: A row of stat cards summarising the state of things, linking to the detail behind each.
- `capacity-heat-map` **Capacity heat map**: Occupancy by weekday and hour as shaded cells with the value printed, and a legend of the scale.
- `event-timeline` **Event timeline**: Alerts and events grouped by day, newest first, each with its status, time and snapshot.

## [Data and filtering](data-filtering.md) (9)

Tables, panels and the controls that narrow them: filter bars, list headers, summary tiles and record cards.

- `data-table` **Data table**: A table of records with a toolbar, selectable rows, sortable headers, row actions and a pager; rows become cards on phones.
- `accuracy-table` **Accuracy table**: Counted versus reference values per video, with the difference and an accuracy bar coloured by threshold.
- `filter-bar` **Filter bar**: The row above the results that shows the applied filters as removable tags, the result count and Clear all.
- `panel` **Panel**: A bordered section of a page with a header, a body and optional footer actions.
- `tabbed-panel-set` **Tabbed panel set**: One panel whose body switches between related views with tabs.
- `card-list` **Card list**: Records as a vertical list of cards: name, key facts and actions; the phone-friendly alternative to a table.
- `list-header` **List header**: Above a list: its title with the count, a search, the view toggle and, for a list panel inside a page, its create action.
- `summary-tiles` **Summary tiles**: A row of small counts by status that also act as quick filters.
- `autocomplete-results-table` **Autocomplete results table**: Search-as-you-type results shown as a compact table with the matched text highlighted.

## [Forms](pattern-forms.md) (7)

Whole form sections and specialised editors: sections, stacks, sign-in, schedules, zones, properties and rich text.

- `form-section` **Form section**: A titled group of related fields with a short explanation beside them.
- `form-stack` **Form stack**: Fields in one column (the default), or two columns for short, closely related fields.
- `schedule-editor` **Schedule editor**: A weekly schedule made of rows (day, start, end), with presets, add and remove, and overlap checks.
- `zone-editor` **Zone/line editor**: Draw a counting zone on the video image by clicking its corners, with a list of zones beside it.
- `login-card` **Login card**: The sign-in form: logo, title, email, password, remember me, the sign-in button and recovery link.
- `properties-editor` **Properties editor**: A list of key and value rows with add and remove, for free-form metadata.
- `rich-text-editor` **Rich text editor**: A text area with a small formatting toolbar (bold, italic, lists, link) that saves HTML to a field.

## [Media](media.md) (4)

Video players, live streams, photo posts and image galleries.

- `recording-player` **Recording player**: A recorded clip with the native player, a timeline of event marks and a list of events that jump to their moment.
- `live-stream-panel` **Live stream panel**: A live video view with its state, a live flag and the live counts beside it.
- `photo-post` **Photo post**: A shared photo with who posted it and when, the photo, actions and caption.
- `image-gallery` **Image gallery**: A large stage image with a row of thumbnails and a count; thumbnails swap the stage.

## [Record management](records.md) (6)

Showing and changing one record and its children: detail panels, child tabs, activity, protected deletes and confirmations.

- `detail-panel` **Detail panel**: One record's summary: title and status, its actions, and a table of its properties.
- `parent-child-tabs` **Parent record with child tabs**: A parent record's summary followed by tabs, one per kind of child, each with its count.
- `child-list-tab` **Child list tab**: The content of one child tab: a list header scoped to the parent, the children's table and an empty state.
- `activity-feed` **Activity feed**: Changes to a record or a site, grouped by day, each with who, what, when and the before and after values.
- `delete-blocked-notice` **Delete-blocked notice**: Why a record cannot be deleted yet, which records depend on it, and how to proceed.
- `confirm-action-panel` **Confirm action panel**: A full-page confirmation for consequential actions: what will happen, what is kept, and the named action.

## [Charts](pattern-charts.md) (8)

Server-rendered SVG charts in a chart frame, in token colours, each with a text summary and its data as a table. No chart library.

- `bar-chart` **Bar chart**: Bars comparing values across categories; grouped, stacked or horizontal.
- `line-chart` **Line chart**: Lines showing how one or more values change over time.
- `pie-chart` **Pie chart**: A circle split into the shares of one total, with a legend giving each value and percentage.
- `doughnut-chart` **Doughnut chart**: A pie with the total in the middle.
- `scatter-chart` **Scatter chart**: Points placed by two values to show a relationship.
- `bubble-chart` **Bubble chart**: A scatter chart whose point size shows a third value.
- `radar-chart` **Radar chart**: Scores on several axes drawn as a polygon, comparing one or two items.
- `polar-area-chart` **Polar area chart**: Equal-angle segments whose radius shows each value.

## [Marketing and documentation site](marketing-docs.md) (6)

Sections for a product's public pages and its documentation: hero, features, live tokens, code samples and docs navigation.

- `marketing-hero` **Marketing hero**: The full-width opening band of a landing page: headline, lead, actions, proof points and an image, edged with the brand bar.
- `feature-grid` **Feature grid**: Three to six features, each an icon, a short title and one sentence.
- `token-panel` **Live design-token panel**: Controls for the brand tokens beside a live preview, to try a brand before setting it.
- `code-samples` **Code samples block**: The same example in several languages or frameworks as tabs of code blocks.
- `docs-page-header` **Docs page header**: A documentation page's breadcrumb, title, one-paragraph introduction and meta (status, source, version).
- `docs-sidebar` **Docs sidebar tree**: The documentation sidebar: a filter box over grouped, collapsible page links, with the current page open and visible.

## [Process and status](process.md) (1)

Following a long-running job: what is done, what is happening, what failed and what to do.

- `capture-run-progress` **Video export progress**: A running job's progress: overall bar with counts and time left, the steps, and each video's state.

## [Editorial](editorial.md) (2)

Blocks for stories and highlighted facts on news, blog and report pages.

- `story-feature` **Story feature**: A featured article: large image, kicker, headline, lead and meta, side by side on wide screens.
- `factoid` **Factoid**: One striking number with a short statement and its source.

## [Email](email.md) (1)

The frame every transactional email is written in: brand bar, title, text, one action, footer.

- `email-frame` **Email frame**: A table-based, inline-styled email layout in the brand's colours with one action and a copyable link.

## [Calendar views](calendar-views.md) (9)

Whole calendars rendered on the server from a list of events: month, week, day, multi-day, agenda and year, plus the toolbar, sidebar and legend around them.

- `month-calendar` **Month calendar**: Weeks of day cells showing each day's events, with '+N more' when a day overflows and a count dot on phones.
- `week-view` **Week view**: Seven day columns on an hour grid with events positioned by time, an all-day row and a line at the current time.
- `day-view` **Day view**: One day on the hour grid: the full detail of a single day, and the phone default.
- `agenda-view` **Agenda view**: Upcoming events listed by day, with times, colours and places: the most readable calendar on any screen.
- `year-view` **Year view**: Twelve small months with event days marked, to see a year's rhythm and jump to any day.
- `multi-day-view` **Multi-day view**: Three (or any number of) days on the hour grid, between the day and week views.
- `calendar-toolbar` **Calendar toolbar**: The bar above any calendar view: previous, Today, next, the period title, the view switcher and a create button.
- `mini-calendar-sidebar` **Mini-calendar sidebar**: A sidebar beside the main calendar: create button, mini calendar to jump to any date, and the calendars legend.
- `calendar-legend` **Calendar legend**: The list of calendars, each a checkbox in its colour, to show or hide its events.

## [Scheduler](scheduler.md) (10)

Editing when things and people are available, and booking time against that availability.

- `weekly-availability-editor` **Weekly availability editor**: Each day of the week with an open switch and one or more time spans, to set when something is open or someone is available.
- `working-hours-editor` **Working-hours editor**: A compact editor for regular hours: the working days, one start and end time, a break and the timezone.
- `recurrence-editor` **Recurrence editor**: Repeat rules for an event or task: frequency, interval, days, end condition and a plain-language summary.
- `exception-editor` **Exception and holiday editor**: The list of dates that differ from the regular hours (closed days, short days) with a form to add one.
- `time-off-editor` **Time-off editor**: A request form for time off (type, dates, half days, note) beside the person's balance and their existing requests.
- `resource-scheduler` **Resource scheduler**: Resources (people, rooms, videos) as rows against a time scale, with bookings as bars on each row.
- `shift-planner` **Shift planner**: A roster table of people by days with shifts in each cell, weekly totals and over-hours highlighted.
- `booking-slot-picker` **Booking slot picker**: A strip of dates and the free slots on the chosen date, grouped by part of day, for booking a fixed-length slot.
- `appointment-picker` **Appointment picker**: Booking in steps: choose the service and person, then the date and time, then confirm, with a running summary.
- `conflict-resolver` **Conflict resolver**: When two bookings clash: both side by side with what conflicts, and clear choices to resolve it.

## [Event editing](event-editing.md) (7)

Creating, viewing and answering events: full editor, popover, panel, quick add, reminders, attendees and RSVP.

- `event-editor` **Event editor**: The full form for an event: title, date and time (or all day), repeat, place, people, reminders, calendar and notes.
- `event-popover` **Event detail popover**: A small card that opens over the calendar when an event is clicked: title, time, place, people and quick actions.
- `event-detail-panel` **Event detail panel**: All of an event's details in a panel or page: title, status, time, place, description, attendees and actions.
- `quick-add-event` **Quick-add event**: One text field that creates an event from a sentence ('Audit Friday 10:00 at North building'), showing what it understood before saving.
- `reminder-manager` **Reminder manager**: The list of upcoming reminders with Snooze and Done, and the defaults for new events.
- `attendee-list` **Attendee list**: People invited to an event with their answers, a summary count and controls to add or remove.
- `invitation-response-bar` **Invitation response bar**: A bar on an invitation asking 'Going?' with Yes, Maybe and No, showing the current answer.

## [Planning boards and timelines](planning-boards.md) (11)

Seeing and steering work over time: task lists, boards, Gantt charts, roadmaps, milestones, capacity, deadlines and plan summaries.

- `task-list` **Task list**: Tasks grouped by status or due date, each with a checkbox, assignee, due chip and status, plus an inline add row.
- `kanban-board` **Kanban board**: Columns of cards by status; cards move between columns by drag and drop or a 'Move to' menu, with work-in-progress limits.
- `gantt-chart` **Gantt chart**: Tasks as bars on a time scale with progress, dependencies in order, milestones and a today line.
- `roadmap` **Roadmap**: Themes or teams as lanes across quarters or months, with items placed in the period they are planned for.
- `milestone-timeline` **Milestone timeline**: Key dates on one horizontal line: reached, next and upcoming milestones with their dates.
- `period-overview` **Sprint or period overview**: A period's dashboard: dates and days left, goal, progress, the plan summary and the open work.
- `capacity-planner` **Capacity planner**: People as rows with their booked hours per day against capacity, totals and over-allocation flagged.
- `deadline-list` **Deadline list**: Upcoming deadlines grouped into Overdue, This week and Later, each with its date and time left.
- `planning-summary` **Planning summary**: Planned against done for each team, person or category as paired bars with the numbers.
- `plan-filter-bar` **Plan filter bar**: Above a plan: the period shown, the applied assignee and status filters as removable chips, and the number of results.
- `date-range-filter-bar` **Date-range filter bar**: A period filter for reports and plans: quick presets plus a custom from–to range, showing the chosen dates.
