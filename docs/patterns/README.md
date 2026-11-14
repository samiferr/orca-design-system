# ORCA patterns

Generated from `orca/catalogue/` by `python -m orca build`. Do not edit by hand.

Every element below has a general description, **when**, **when not**, **how**, accessibility notes, the tokens and
classes it uses, the UX principles it applies, and a copy-ready Django template example.
Load the tags with `{% load orca %}` and put `{% orca_head %}` in `<head>`.

## [Page frame](page-frame.md) (13)

The parts that surround every page: headers, top bar, sidebar, footer, page head, messages, drawers and filter panels.

- `site-header` **Header**: Header of public pages: logo, a few section links and one or two actions, sticky at the top.
- `top-bar` **Top bar**: The application's top bar: menu button, logo, main sections, search and user tools.
- `sidebar` **Sidebar**: Side navigation for an application: grouped section links that collapse to an icon rail, remembered per person.
- `footer` **Footer**: The bottom of public pages: link columns, legal text and version.
- `page-head` **Page head**: The top of a page's content: breadcrumbs or back link, title, subtitle, meta info and page actions.
- `messages-region` **Messages region**: A region under the page head that shows the result of the last action, announced politely.
- `drawer` **Drawer**: A panel that slides in over the page from one edge, built on the native dialog.
- `top-actions-header` **Top actions header**: A thin row above a detail or form page with a back link on one side and page actions on the other.
- `settings-panel` **Settings panel**: Grouped display preferences, theme and density, applied live. ORCA has one appearance; the project sets brand colours.
- `filter-panel` **Filter panel**: Labelled groups of filters with a result count and Clear all: the content of the filter drawer.
- `filter-drawer` **Filter drawer**: Page filters in a right drawer opened by a Filters button in the page actions, with Show results and Clear all.
- `page-landmarks` **Page landmarks**: The regions every page has: skip navigation, the main landmark and a place for dialogs.
- `error-message` **Error message**: What an error page says: the code, what happened in plain words, what to do, and a way back.

## [Grids and collections](grids.md) (7)

One component repeated in a responsive grid or sequence: products, videos, KPIs, a heat map, an event timeline.

- `product-grid` **Product grid**: Product items in a responsive grid whose column count adapts to the screen.
- `video-grid` **Video grid**: Video cards in a grid, pinned videos first, offline videos clearly marked.
- `kpi-grid` **KPI grid**: A row of stat cards that summarise current state, each linking to its detail.
- `capacity-heat-map` **Capacity heat map**: Occupancy by weekday and hour as shaded cells with printed values and a scale legend.
- `event-timeline` **Event timeline**: Alerts and events grouped by day, newest first, each with its status, time and snapshot.
- `card-grid` **Card grid**: Cards for records, products or people in as many equal columns as fit.
- `loading-placeholder` **Loading placeholder**: Placeholder cards shaped like the content while a grid or feed loads, announced to screen readers.

## [Data and filtering](data-filtering.md) (10)

Tables, panels and the controls that narrow them: filter bars, list headers, summary tiles, record cards.

- `data-table` **Data table**: A table of records with a toolbar, selectable rows, sortable headers, row actions and a pager; rows become cards on phones.
- `accuracy-table` **Accuracy table**: Counted and reference values per video, with the difference and an accuracy bar coloured by threshold.
- `filter-bar` **Filter bar**: The row above results showing applied filters as removable tags, the result count and Clear all.
- `panel` **Panel**: A bordered page section with a header, a body and optional footer actions.
- `tabbed-panel-set` **Tabbed panel set**: One panel whose body switches between related views with tabs.
- `card-list` **Card list**: Records as a vertical list of cards with name, key facts and actions; a phone-friendly alternative to a table.
- `list-header` **List header**: The bar above a list: title with count, search, view toggle and, for a list panel in a page, its create action.
- `summary-tiles` **Summary tiles**: A row of small counts by status that also act as quick filters.
- `autocomplete-results-table` **Autocomplete results table**: Search-as-you-type results shown as a compact table with the matched text highlighted.
- `no-results` **No results**: What a list, table or feed shows when empty: the empty state, plus the applied filters when filters hide everything.

## [Forms](pattern-forms.md) (7)

Form sections, stacks and sign-in, plus editors for schedules, zones, properties and rich text.

- `form-section` **Form section**: A titled group of related fields with a short explanation beside them.
- `form-stack` **Form stack**: Fields in one column (the default), or two columns for short, closely related fields.
- `schedule-editor` **Schedule editor**: A weekly schedule of rows (day, start, end) with presets, add and remove, and overlap checks.
- `zone-editor` **Zone/line editor**: Draw a counting zone by clicking its corners on the video image, with the zone list beside it.
- `login-card` **Login card**: The sign-in form: logo, title, email, password, remember me, sign-in button and recovery link.
- `properties-editor` **Properties editor**: A list of key and value rows with add and remove, for free-form metadata.
- `rich-text-editor` **Rich text editor**: A text area with a small formatting toolbar (bold, italic, lists, link) that saves HTML to a field.

## [Media](media.md) (4)

Video players, live streams, photo posts and image galleries.

- `recording-player` **Recording player**: A recorded clip with the native player, a timeline of event marks and an event list that jumps to each moment.
- `live-stream-panel` **Live stream panel**: A live video view with its state, a live flag and live counts beside it.
- `photo-post` **Photo post**: A shared photo with its poster, time, actions and caption.
- `image-gallery` **Image gallery**: A large main image with a row of thumbnails and a count; clicking a thumbnail swaps the image.

## [Record management](records.md) (6)

Showing and changing one record and its children: detail panels, child tabs, activity, blocked deletes and confirmations.

- `detail-panel` **Detail panel**: A record's title, status, actions and a table of its properties.
- `parent-child-tabs` **Parent record with child tabs**: A parent record's summary above tabs, one per kind of child, each with its count.
- `child-list-tab` **Child list tab**: One child tab's content: a list header for the parent, the children's table and an empty state.
- `activity-feed` **Activity feed**: Changes to a record or site, grouped by day, each showing who, what, when and the before and after values.
- `delete-blocked-notice` **Delete-blocked notice**: Why a record cannot be deleted yet, what depends on it and what to do next.
- `confirm-action-panel` **Confirm action panel**: A full-page confirmation for serious actions: what will happen, what is kept and a button naming the action.

## [Charts](pattern-charts.md) (8)

Charts drawn by Chart.js in a chart frame, in token colours, each with a text summary and a data table. One template tag, no chart code.

- `bar-chart` **Bar chart**: Bars comparing values across categories; grouped, stacked or horizontal.
- `line-chart` **Line chart**: Lines showing how one or more values change over time.
- `pie-chart` **Pie chart**: A circle split into shares of one total, with a legend showing each value and percentage.
- `doughnut-chart` **Doughnut chart**: A pie with the total in the middle.
- `scatter-chart` **Scatter chart**: Points placed by two values to show a relationship.
- `bubble-chart` **Bubble chart**: A scatter chart whose point size shows a third value.
- `radar-chart` **Radar chart**: Scores on several axes drawn as a polygon, comparing one or two items.
- `polar-area-chart` **Polar area chart**: Equal-angle segments whose radius shows each value.

## [Marketing and documentation site](marketing-docs.md) (7)

Sections for a product's public pages and its documentation: hero, features, live tokens, code samples and docs navigation.

- `marketing-hero` **Marketing hero**: The full-width opening band of a landing page: headline, lead, actions, proof points and image, edged with the brand bar.
- `feature-grid` **Feature grid**: Three to six features, each an icon, a short title and one sentence.
- `token-panel` **Live design-token panel**: Brand token controls beside a live preview, for trying a brand before setting it.
- `code-samples` **Code samples block**: One example in several languages or frameworks, as tabs of code blocks.
- `docs-page-header` **Docs page header**: A documentation page's breadcrumb, title, short introduction and meta (status, source, version).
- `docs-sidebar` **Docs sidebar tree**: The documentation sidebar: an optional filter box and an optional Collapse all button over grouped, collapsible page links, with the current page open.
- `table-of-contents` **Table of contents**: An "On this page" list of a long page's sections, marking the one being read.

## [Process and status](process.md) (1)

Following a long-running job: what is done, what is happening, what failed and what to do next.

- `capture-run-progress` **Video export progress**: A running job's progress: overall bar with counts and time left, the steps, and each video's state.

## [Editorial](editorial.md) (2)

Blocks for stories and highlighted facts on news, blog and report pages.

- `story-feature` **Story feature**: A featured article: large image, kicker, headline, lead and meta, side by side on wide screens.
- `factoid` **Factoid**: One striking number with a short statement and its source.

## [Email](email.md) (1)

The layout for every transactional email: brand bar, title, text, one action, footer.

- `email-frame` **Email frame**: A table-based email layout with inline styles in the brand's colours, one action and a copyable link.

## [Calendar views](calendar-views.md) (9)

Server-rendered calendars built from a list of events: month, week, day, multi-day, agenda and year, plus the toolbar, sidebar and legend.

- `month-calendar` **Month calendar**: Weeks of day cells showing each day's events, '+N more' when a day overflows, and a count dot on phones.
- `week-view` **Week view**: Seven day columns on an hour grid, with events placed by time, an all-day row and a current-time line.
- `day-view` **Day view**: One day on the hour grid, with full detail; the phone default.
- `agenda-view` **Agenda view**: Upcoming events listed by day with times, colours and places; readable on any screen.
- `year-view` **Year view**: Twelve small months with event days marked, to see the year at a glance and jump to any day.
- `multi-day-view` **Multi-day view**: A chosen number of days (such as three) on the hour grid, between the day and week views.
- `calendar-toolbar` **Calendar toolbar**: The bar above a calendar view: previous, Today, next, period title, view switcher and create button.
- `mini-calendar-sidebar` **Mini-calendar sidebar**: A calendar sidebar with a create button, a mini calendar to jump to any date, and the legend.
- `calendar-legend` **Calendar legend**: A list of calendars, each a coloured checkbox that shows or hides its events.

## [Scheduler](scheduler.md) (10)

Setting when people and things are available, and booking time within that.

- `weekly-availability-editor` **Weekly availability editor**: Each weekday with an open switch and one or more time spans, to set opening hours or availability.
- `working-hours-editor` **Working-hours editor**: A compact editor for regular hours: working days, one start and end time, a break and the timezone.
- `recurrence-editor` **Recurrence editor**: Repeat rules for an event or task: frequency, interval, days, end and a plain-language summary.
- `exception-editor` **Exception and holiday editor**: A list of dates that differ from regular hours (closed or short days), with a form to add one.
- `time-off-editor` **Time-off editor**: A time-off request form (type, dates, half days, note) beside the person's balance and existing requests.
- `resource-scheduler` **Resource scheduler**: Resources (people, rooms, videos) as rows on a time scale, with bookings as bars.
- `shift-planner` **Shift planner**: A roster table of people by day, with shifts in each cell, weekly totals and over-hours highlighted.
- `booking-slot-picker` **Booking slot picker**: A date strip and the free slots on the chosen date, grouped by part of day.
- `appointment-picker` **Appointment picker**: Booking in steps: service and person, then date and time, then confirm, with a running summary.
- `conflict-resolver` **Conflict resolver**: Shows two clashing bookings side by side, with what conflicts and clear choices to resolve it.

## [Event editing](event-editing.md) (7)

Creating, viewing and answering events: editor, popover, panel, quick add, reminders, attendees and RSVP.

- `event-editor` **Event editor**: The full event form: title, date and time (or all day), repeat, place, people, reminders, calendar and notes.
- `event-popover` **Event detail popover**: A small card over the calendar when an event is clicked, showing title, time, place, people and quick actions.
- `event-detail-panel` **Event detail panel**: An event's full details in a panel or page: title, status, time, place, description, attendees and actions.
- `quick-add-event` **Quick-add event**: One text field that creates an event from a sentence ('Audit Friday 10:00 at North building') and shows what it understood before saving.
- `reminder-manager` **Reminder manager**: The list of upcoming reminders with Snooze and Done, and the defaults for new events.
- `attendee-list` **Attendee list**: Invitees with their answers, a summary count and controls to add or remove people.
- `invitation-response-bar` **Invitation response bar**: A bar on an invitation asking 'Going?' with Yes, Maybe and No buttons, showing the current answer.

## [Planning boards and timelines](planning-boards.md) (11)

Show and manage work over time: task lists, boards, Gantt charts, roadmaps, milestones, capacity, deadlines and plan summaries.

- `task-list` **Task list**: Tasks grouped by status or due date, each with checkbox, assignee, due date and status, plus a row to add more.
- `kanban-board` **Kanban board**: Status columns of cards that move by drag and drop or a 'Move to' menu, with work-in-progress limits.
- `gantt-chart` **Gantt chart**: Task bars on a time scale, showing progress, dependencies, milestones and a today line.
- `roadmap` **Roadmap**: Lanes of themes or teams across quarters or months, with each item in its planned period.
- `milestone-timeline` **Milestone timeline**: Key dates on one line: reached, next and upcoming milestones with their dates.
- `period-overview` **Sprint or period overview**: A sprint or period at a glance: dates, days left, goal, progress, plan summary and open work.
- `capacity-planner` **Capacity planner**: One row per person showing booked hours per day against capacity, with totals and over-allocation flagged.
- `deadline-list` **Deadline list**: Deadlines grouped as Overdue, This week and Later, each with its date and time left.
- `planning-summary` **Planning summary**: Paired bars comparing planned with done for each team, person or category, with the numbers.
- `plan-filter-bar` **Plan filter bar**: A bar above a plan showing the period, applied assignee and status filters as removable chips, and the result count.
- `date-range-filter-bar` **Date-range filter bar**: A period filter for reports and plans: quick presets or a custom from–to range, with the chosen dates shown.
