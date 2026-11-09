# ORCA templates

Generated from `orca/catalogue/` by `python -m orca build`. Do not edit by hand.

Every element below has a **why**, **when**, **when not**, **how**, accessibility notes, the tokens and
classes it uses, the UX principles it applies, and a copy-ready Django template example.
Load the tags with `{% load orca %}` and put `{% orca_head %}` in `<head>`.

## [Layouts](template-layouts.md) (21)

Whole-page Django templates you extend. They place patterns in a fixed structure and leave named blocks for your content. Every page of an ORCA project starts from one of these.

- `base-layout` **Base layout**: The root every ORCA page extends: the html element with language, theme and density, the head with ORCA's styles and theme bootstrap, the skip link, and slots for body, modal and scripts.
- `app-shell` **App shell**: The application frame: top bar with brand, sidebar navigation that collapses to a rail (a drawer on phones), and a main column with breadcrumbs, page title, subtitle, actions, messages and content.
- `auth-layout` **Auth layout**: A centred card on the alternate ground for sign-in, password reset and other pages before an account is open.
- `email-layout` **Email layout**: The page frame of every transactional email: brand bar, title, paragraphs, one action with its link printed, and footer, with colours written inline.
- `error-layouts` **Error layouts**: 403, 404 and 500 pages: logo, illustration, error code, what happened in plain words and what to do next.
- `homepage-template` **Homepage template**: The page people land on after signing in: a greeting, a stat grid, a main column for what changed and an aside with shortcuts.
- `feed-skeleton` **Feed skeleton**: A centred column of posts with skeleton posts while more load, and an empty state when there are none.
- `person-block-grid` **Person-block grid**: A grid of people cards: avatar, name, role and a contact action.
- `marketing-layout` **Marketing page layout**: The public site frame: site header with navigation and actions, full-width sections, and a footer with link columns.
- `docs-layout` **Docs page layout**: Documentation frame: top bar, a sidebar with a filter and a page tree, and a reading column with breadcrumbs, title and introduction.
- `generic-list` **Generic list template**: A list page from a ListView: title and Add button, optional filter panel, list header with count and search, a table that becomes cards on phones, pagination and the right empty state.
- `generic-detail` **Generic detail template**: A record page from a DetailView: title, Edit and Delete actions, and the record's fields as a key–value list.
- `generic-form` **Generic form template**: A create or edit page from a CreateView or UpdateView: one column of ORCA fields with the error summary and Save and Cancel.
- `generic-confirm-delete` **Generic confirm (delete) template**: The delete confirmation from a DeleteView: what will be deleted, what is kept, a danger button and Cancel; or, when other records still use it, why it cannot be deleted yet.
- `generic-confirm-action` **Generic confirm-action template**: A confirmation page for any consequential action that is not a delete: archive, send, disable, run.
- `parent-base` **Parent base template**: The frame shared by every page of a parent record: its title and actions, optional summary stats, and tabs for the overview and each child list.
- `parent-detail` **Parent detail template**: The parent's Overview tab: its fields as a key–value list, with room for more overview panels.
- `parent-child-list` **Parent-child list template**: A child list inside a parent tab: header with count and 'Add … to parent', the table, pagination and an empty state naming the parent.
- `parent-child-detail` **Parent-child detail template**: One child record inside its parent's tab: a back link to the list, Edit and Delete, and the record's fields.
- `parent-child-form` **Parent-child form template**: Create or edit a child inside its parent's tab, with a heading that names the parent.
- `parent-child-confirm` **Parent-child confirm template**: Confirm removing a child from its parent, or explain what blocks it.

## [Page-type skeletons](page-types.md) (8)

The app shell set up for one kind of screen: dashboard, calendar, scheduler, board, timeline, booking, event editor and simple data page. Pass data in the context; override a block only to change a region.

- `dashboard` **Dashboard**: An overview page: a period switch, a stat grid, charts in two columns and room for lists below.
- `calendar-page` **Calendar page**: A full calendar: toolbar (previous, Today, next, period, view switch), a side panel with a mini calendar and calendars legend, and the month, week, day or agenda view.
- `scheduler-page` **Scheduler page**: Resources by time for one day: a date toolbar, a row per person, room or vehicle with bookings placed by time, and the legend.
- `planning-board-page` **Planning board page**: A kanban board page: filters on top and columns of cards that move by drag and drop.
- `timeline-page` **Timeline page**: A Gantt timeline: period toolbar, task bars on a day scale with progress, milestones and a today line.
- `booking-flow` **Booking flow**: A step-by-step booking page: steps on top, the current step's choices, and a summary of the booking so far beside it.
- `event-editor-page` **Event editor page**: Create or edit an event on its own page: the form on the left, conflicts and attendees on the right, Delete apart from Save.
- `simple-data-page` **Simple data page**: A data page with everything in one place: title bar, summary tiles that filter, search, a filter drawer and the table.

## [Structural layouts](structural-layouts.md) (8)

Layout classes that arrange sections inside a page: stacks, grids and splits. They hold patterns and never style them.

- `vertical-stack` **Vertical stack**: Sections one under another with one spacing step between them; tight and loose variants.
- `stat-grid` **Stat grid**: Stat cards in equal columns that wrap, each at least 12rem wide.
- `card-grid-layout` **Card grid**: Cards in as many equal columns as fit, at least 15rem wide.
- `two-column-grid` **Two-column grid**: Two equal columns from 1036px, one column below.
- `split-layout` **Split (main + aside)**: A main column and a 20rem aside (end by default, start or wider as variants); the aside drops below on narrow screens.
- `camera-split` **Camera split**: The live picture in two thirds, details and actions in one third; the picture stays in view while the details scroll.
- `form-grid` **Form grid**: Short fields side by side in as many 16rem columns as fit; long fields span the full width.
- `narrow-form` **Narrow form**: One column of fields at most 36rem wide.

## [Template slots](template-slots.md) (23)

The named blocks of ORCA's layouts. A page fills slots instead of rewriting layouts, so every page keeps the same structure. Each slot below says which layouts have it and what belongs in it.

- `slot-title` **Title**: The text of the browser tab, before ` · Brand`.
- `slot-page-title` **Page title**: The page's one h1, in the page head.
- `slot-page-subtitle` **Page subtitle**: One sentence under the title saying what the page is for or its scope.
- `slot-page-actions` **Page actions**: The page's buttons, at the end of the page head: one primary action and few others.
- `slot-breadcrumbs` **Breadcrumbs**: The trail of parent pages above the title.
- `slot-content` **Content**: The page's own content, inside the main landmark.
- `slot-scripts` **Scripts**: Script tags at the end of the body, for a project-wide script loaded on every page.
- `slot-head` **Head**: ORCA's stylesheets, brand values, favicon and script (`orca_head`).
- `slot-body-class` **Body class**: Classes on the body element, for page-wide styling hooks.
- `slot-sidebar` **Sidebar**: The whole sidebar element: navigation, extra content and the collapse toggle.
- `slot-top-bar` **Top bar**: The bar at the top of the page: menu button, brand, top navigation and the user's controls.
- `slot-brand` **Brand**: The logo or wordmark, from `settings.ORCA['BRAND']`.
- `slot-sidebar-extra` **Sidebar extra**: Content under the navigation in the sidebar: a site switcher, a plan meter, a help link.
- `slot-sidebar-nav` **Sidebar navigation**: The navigation sections of the sidebar.
- `slot-filter-panel` **Filter panel**: Where filters go: a side panel on the generic list, a bar on the board, a drawer on the simple data page.
- `slot-body` **Body**: Everything inside the body element except the skip link, modal and scripts.
- `slot-modal` **Modal**: Dialogs and drawers, placed after the page so they open above everything.
- `slot-footer` **Footer**: The end of the page: legal and help links on public pages, a version line in applications.
- `slot-extra-head` **Extra head**: Page-specific additions to the head: a stylesheet, meta tags, preloads.
- `slot-extra-scripts` **Extra scripts**: One page's scripts, after the site-wide ones.
- `slot-theme-bootstrap` **Theme bootstrap**: The inline script that applies the reader's saved theme before the page paints.
- `slot-list-actions` **List actions**: The buttons of a list page: Add first, then exports or bulk tools.
- `slot-detail-actions` **Detail actions**: The buttons of a record: Edit, then other actions, Delete last and quieter.
