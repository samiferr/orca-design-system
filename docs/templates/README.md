# ORCA templates

Generated from `orca/catalogue/` by `python -m orca build`. Do not edit by hand.

Every element below has a general description, **when**, **when not**, **how**, accessibility notes, the tokens and
classes it uses, the UX principles it applies, and a copy-ready Django template example.
Load the tags with `{% load orca %}` and put `{% orca_head %}` in `<head>`.

## [Layouts](template-layouts.md) (22)

Whole-page Django templates you extend. Each places patterns in a fixed structure and leaves named blocks for your content. Every ORCA page starts from one of them.

- `base-layout` **Base layout**: The root every ORCA page extends: the html element (language, theme, density), the head with styles and theme setup, the skip link, and slots for body, modal and scripts.
- `app-shell` **App shell**: The application frame: top bar with brand, sidebar that collapses to a rail (a drawer on phones), and a main column with breadcrumbs, title, subtitle, actions, messages and content.
- `auth-layout` **Auth layout**: A centred card for sign-in, password reset and other pages shown before sign-in.
- `email-layout` **Email layout**: The frame of every transactional email: brand bar, title, paragraphs, one action with its link printed, and footer, with inline colours.
- `error-layouts` **Error layouts**: 403, 404 and 500 pages: logo, illustration, error code, a plain explanation and a next step.
- `homepage-template` **Homepage template**: The page after sign-in: a greeting, a stat grid, a main column for what changed and an aside of shortcuts.
- `feed-skeleton` **Feed skeleton**: A centred column of posts, with skeleton posts while more load and an empty state when there are none.
- `person-block-grid` **Person-block grid**: A grid of people cards: avatar, name, role and a contact action.
- `marketing-layout` **Marketing page layout**: The public site frame: site header with navigation and actions, full-width sections, and a footer with link columns.
- `blog-layout` **Blog page layout**: A long-form reading page: breadcrumbs, title, introduction, version and last update, sections in a measured reading column, and an "On this page" column on the right.
- `docs-layout` **Docs page layout**: The Blog page with a documentation sidebar: a filter and a page tree on the left, the reading column and "On this page" on the right.
- `generic-list` **Generic list template**: A ListView page: title and Add button, optional filter panel, list header with count and search, a table that becomes cards on phones, pagination and empty states.
- `generic-detail` **Generic detail template**: A DetailView page: title, Edit and Delete actions, and the record's fields as a key–value list.
- `generic-form` **Generic form template**: A CreateView or UpdateView page: one column of ORCA fields with an error summary, Save and Cancel.
- `generic-confirm-delete` **Generic confirm (delete) template**: A DeleteView confirmation: what will be deleted, what is kept, a danger button and Cancel; or, if other records still use it, why it cannot be deleted yet.
- `generic-confirm-action` **Generic confirm-action template**: A confirmation page for a consequential action other than delete: archive, send, disable, run.
- `parent-base` **Parent base template**: The frame shared by a parent record's pages: title and actions, optional summary stats, and tabs for the overview and each child list.
- `parent-detail` **Parent detail template**: The parent's Overview tab: its fields as a key–value list, with room for more overview panels.
- `parent-child-list` **Parent-child list template**: A child list inside a parent tab: header with count and 'Add … to parent', the table, pagination and an empty state naming the parent.
- `parent-child-detail` **Parent-child detail template**: One child record inside its parent's tab: a back link to the list, Edit and Delete, and the record's fields.
- `parent-child-form` **Parent-child form template**: Create or edit a child inside its parent's tab, with a heading that names the parent.
- `parent-child-confirm` **Parent-child confirm template**: Confirm removing a child from its parent, or explain what blocks it.

## [Page-type skeletons](page-types.md) (8)

App-shell setups for one kind of screen: dashboard, calendar, scheduler, board, timeline, booking, event editor and simple data page. Pass data in the context; override a block only to change a region.

- `dashboard` **Dashboard**: An overview page: period switch, stat grid, two columns of charts and room for lists below.
- `calendar-page` **Calendar page**: A full calendar: toolbar (previous, Today, next, period, view switch), a side panel with a mini calendar and legend, and a month, week, day or agenda view.
- `scheduler-page` **Scheduler page**: One day by resource: a date toolbar, a row per person, room or vehicle with bookings placed by time, and a legend.
- `planning-board-page` **Planning board page**: A kanban board: filters on top and columns of cards you drag between stages.
- `timeline-page` **Timeline page**: A Gantt timeline: period toolbar, task bars on a day scale with progress, milestones and a today line.
- `booking-flow` **Booking flow**: A step-by-step booking page: steps on top, the current step's choices, and a booking summary beside them.
- `event-editor-page` **Event editor page**: A full page to create or edit an event: form on the left, conflicts and attendees on the right, Delete apart from Save.
- `simple-data-page` **Simple data page**: A data page with title bar, summary tiles that filter, search, a filter drawer and the table.

## [Structural layouts](structural-layouts.md) (8)

Layout classes for arranging sections in a page: stacks, grids and splits. They hold patterns, never style them.

- `vertical-stack` **Vertical stack**: Sections stacked with one spacing step between them, in tight and loose variants.
- `stat-grid` **Stat grid**: Stat cards in equal columns that wrap, each at least 12rem wide.
- `card-grid-layout` **Card grid**: Cards in as many equal columns as fit, at least 15rem wide.
- `two-column-grid` **Two-column grid**: Two equal columns from 1036px, one column below.
- `split-layout` **Split (main + aside)**: A main column and a 20rem aside (at the end by default; start and wider variants) that drops below on narrow screens.
- `media-split` **Media split**: The live picture in two thirds, details and actions in one third; the picture stays in view as the details scroll.
- `form-grid` **Form grid**: Short fields side by side in as many 16rem columns as fit; long fields span the full width.
- `narrow-form` **Narrow form**: One column of fields at most 36rem wide.

## [Template slots](template-slots.md) (23)

The named blocks that ORCA's layouts offer. A page fills slots instead of rewriting the layout. Each slot lists the layouts that have it and what goes in it.

- `slot-title` **Title**: The text of the browser tab, before ` · Brand`.
- `slot-page-title` **Page title**: The page's one h1, in the page head.
- `slot-page-subtitle` **Page subtitle**: One sentence under the title: what the page is for or covers.
- `slot-page-actions` **Page actions**: The page's buttons at the end of the page head: one primary action, few others.
- `slot-breadcrumbs` **Breadcrumbs**: The trail of parent pages above the title.
- `slot-content` **Content**: The page's own content, inside the main landmark.
- `slot-scripts` **Scripts**: Script tags at the end of the body, for scripts loaded on every page.
- `slot-head` **Head**: ORCA's stylesheets, brand values, favicon and script (`orca_head`).
- `slot-body-class` **Body class**: Classes on the body element, for page-wide styling.
- `slot-sidebar` **Sidebar**: The whole sidebar: navigation, extra content and the collapse toggle.
- `slot-top-bar` **Top bar**: The bar at the top of the page: menu button, brand, top navigation and the user's controls.
- `slot-brand` **Brand**: The logo or wordmark, from `settings.ORCA['BRAND']`.
- `slot-sidebar-extra` **Sidebar extra**: Content under the sidebar navigation: a site switcher, plan meter or help link.
- `slot-sidebar-nav` **Sidebar navigation**: The navigation sections of the sidebar.
- `slot-filter-panel` **Filter panel**: A right drawer for filters, opened by the Filters button in the page actions.
- `slot-body` **Body**: Everything inside the body element except the skip link, modal and scripts.
- `slot-modal` **Modal**: Dialogs and drawers, placed after the page so they open above it.
- `slot-footer` **Footer**: Legal and help links on public pages, a version line in applications.
- `slot-extra-head` **Extra head**: Page-specific head content: a stylesheet, meta tags, preloads.
- `slot-extra-scripts` **Extra scripts**: One page's scripts, after the site-wide ones.
- `slot-theme-bootstrap` **Theme bootstrap**: The inline script that applies the reader's saved theme before the page paints.
- `slot-list-actions` **List actions**: The buttons of a list page: Add first, then exports or bulk tools.
- `slot-detail-actions` **Detail actions**: The buttons of a record: Edit, then other actions, Delete last and quieter.
