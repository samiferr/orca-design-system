# ORCA primitives

Generated from `orca/catalogue/` by `python -m orca build`. Do not edit by hand.

Every element below has a general description, **when**, **when not**, **how**, accessibility notes, the tokens and
classes it uses, the UX principles it applies, and a copy-ready Django template example.
Load the tags with `{% load orca %}` and put `{% orca_head %}` in `<head>`.

## [Base styles](foundations.md) (15)

The tokens all other elements are built from: colour, type, space, shape, elevation, layers, size and motion. Use the names, never raw values. Projects may change only brand tokens.

- `color-palette` **Colour palette**: Raw colours: a 13-step gray scale and eleven hues with nine numbered steps each.
- `semantic-colors` **Semantic colour tokens**: Colours named by their job: text, backgrounds, lines, interaction, status, actions, planning and data.
- `brand-color` **Brand colour and surfaces**: The one brand colour, the fills derived from it, and the page surfaces it sits on.
- `accent-color` **Accent colour**: The single interactive colour: links, checked ticks, radios, switches, progress, selected days.
- `themes` **Themes**: Light, dark and paper share every token name. ORCA has one appearance, named ORCA.
- `typography` **Fonts and type styles**: Ubuntu Sans (variable) for everything, JetBrains Mono for code, on a fixed type scale.
- `spacing` **Spacing scale**: Eleven spacing steps on the 8px unit, named by their pixel value.
- `borders` **Borders**: Three line weights: 1px hairline, 1.5px outline, 3px emphasis bar.
- `radii` **Corner radii**: ORCA is square; only round marks and bar ends are rounded.
- `shadows` **Shadows and elevation**: Three shadows (card, elevated, dragged) and elevation utilities. Only floating things cast a shadow.
- `layers` **Layers (z-index)**: A fixed stacking order from page content to the skip link.
- `control-heights` **Control heights**: Five heights shared by buttons, fields, selects and toggles: sm, dense, md, lg, xl.
- `motion` **Motion**: Four durations and two easings, all under the 400 ms Doherty threshold.
- `aspect-ratio` **Aspect-ratio utilities**: Reserve the space of images and video before they load.
- `scrollbar` **Scrollbar style**: A thin, token-coloured scrollbar for inner scrolling regions.

## [Text](text.md) (22)

Text styles with a fixed role. Choose by what the text is (a page title, a stat value), not by size.

- `heading` **Heading (h1–h6)**: Headings h1 to h6, plus a display style for marketing pages.
- `page-title` **Page title**: The one title that names the page.
- `page-subtitle` **Page subtitle**: One sentence under the page title saying what the page is for.
- `section-title` **Section title**: Title of a section in a page: a group of panels or part of a long form.
- `panel-title` **Panel title**: Title at the top of a panel or card group.
- `alert-title` **Alert title**: Bold first line of an alert, callout or notification, stating what happened.
- `paragraph` **Paragraph**: Running text at 16/24 with a 70-character measure.
- `text-link` **Text link**: An underlined, accent-coloured link in text.
- `muted-text` **Muted text**: Secondary text in `--orca-text-muted` (60% ink, still 4.5:1).
- `small-text` **Small text**: 14/20 detail text for help, meta and timestamps.
- `tabular-number` **Tabular number**: Equal-width digits that line up in columns and do not shift when numbers update.
- `kbd` **Keyboard key**: A key or shortcut the person presses.
- `stat-label` **Stat label**: The name of a measured value, shown above it.
- `stat-value` **Stat value**: The large tabular number a KPI tile exists to show.
- `delta` **Delta (up, down, flat)**: Change against a reference: arrow, signed value, colour, and the reference in words.
- `code-text` **Code text**: Inline code, identifiers, file names and values the person may copy.
- `card-kicker` **Card kicker**: A short uppercase category label above a card title.
- `card-title` **Card title**: The name of the object a card represents.
- `card-meta` **Card meta**: Secondary facts under a card title, separated by middle dots.
- `dialog-title` **Dialog title**: The question or statement a dialog or drawer is about.
- `empty-title` **Empty-state title**: What is missing, said plainly, in an empty region.
- `empty-text` **Empty-state text**: One sentence that says why it is empty and what to do next.

## [Form text](form-text.md) (6)

The words around a field: label, requirement marker, help and errors. They decide whether people finish a form.

- `label` **Label**: A name that stays visible above every field.
- `required-marker` **Required marker**: The word 'required' or 'optional' after a label.
- `help-text` **Help text**: A hint between label and field that helps people answer correctly.
- `error-text` **Error text**: A message above the field that says what is wrong and how to fix it.
- `help-icon` **Help icon**: A question-mark button that reveals extra explanation in place.
- `error-list` **Error list**: An error summary at the top of a form, linking to each invalid field.

## [Actions](actions.md) (8)

Things people press. One primary action per screen; everything else is quieter.

- `button` **Button**: A command. Variants show importance: primary, secondary (default), ghost, link, plus brand, danger, neutral, elevated and outlines.
- `button-size` **Button sizes**: Size modifiers: sm, dense, default, lg, xl, plus block (full width) and icon-only.
- `link-action` **Link (tertiary action)**: A text-styled button or link for the least important actions.
- `pin-button` **Pin button**: A toggle that pins an item to the top of a list or the dashboard.
- `email-button` **Email button**: A mailto link styled as a button, with the address shown beside it.
- `toggle-button` **Toggle button (pressed)**: A button that stays pressed to show an on state.
- `icon-button` **Icon button**: A square button with one 16px icon and an accessible name. Quiet, outlined, accent and neutral-fill variants.
- `fab` **Floating action button (FAB)**: A large floating button for a phone screen's one create action.

## [Inputs](inputs.md) (13)

Native form controls, styled. They work with keyboards, screen readers, autofill and phones for free.

- `text-input` **Text input**: A single-line field: filled, square, with a 1.5px bottom border.
- `textarea` **Textarea**: A multi-line field that grows vertically.
- `select` **Select (native)**: The browser's dropdown, styled with an ORCA chevron.
- `listbox` **Multiple select (listbox)**: A native `<select multiple>` showing several options at once.
- `search-input` **Search input**: A text field with a magnifier and a clear button.
- `checkbox` **Checkbox**: A square tick for an on/off choice applied when the form is saved, or for one of several choices.
- `radio` **Radio**: A round mark for choosing exactly one of a few visible options.
- `switch` **Switch**: An on/off control that takes effect immediately.
- `number-input` **Number input**: A number field with large minus and plus buttons for small adjustments.
- `color-input` **Colour input**: A native colour picker paired with its hex value.
- `file-input` **File input**: The native file picker with an ORCA-styled button.
- `otp-digit` **OTP digit box**: One box per digit of a one-time code, with auto-advance and paste.
- `input-addon` **Input addon (prefix, suffix)**: A fixed unit, prefix or button joined to an input.

## [Icons](icons.md) (3)

One icon set, 16px, single ink in currentColor. Icons support words and never replace them.

- `icon` **Icon**: An inline SVG glyph from the ORCA set, sized by token and coloured like its text.
- `status-icon` **Status icon**: The four status glyphs (success, warning, error, info), each a distinct shape in its status colour.
- `icon-set` **Icon set**: The named glyphs: 106 from Vanilla (via Tangerine) plus ORCA glyphs for ideas Vanilla lacks.

## [Status marks and labels](status.md) (5)

Small marks that show a condition or categorise an item. Status pairs colour with a word and, where it matters, a shape.

- `status-dot` **Status dot**: A 12px round mark before a word that shows live state.
- `badge` **Badge**: A compact square label with a status or category word, solid or subtle.
- `alert-icon` **Alert icon**: The status glyph at the start of an alert, callout or field message, in its left inset.
- `count-badge` **Count badge**: A small pill with a number: unread items, pending tasks.
- `tag` **Tag**: A label for a keyword or category; static, selectable (filter) or removable (chosen value).

## [Identity](identity.md) (3)

The product's logo and favicon, and people's avatars.

- `logo` **Logo**: The product's logo image, or its name as a wordmark with a brand bar when no logo is set.
- `avatar` **Avatar**: A person's picture or initials in a circle (or square for organisations and devices).
- `favicon` **Favicon set**: The browser-tab and home-screen icons for the product.

## [Imagery](imagery.md) (10)

Images, frames and graphics. Reserve their space, describe them, and keep text readable over them.

- `image` **Image**: A record's main content image, plain or bordered.
- `thumbnail` **Thumbnail image**: A small square preview (48 or 96px) cropped to fill.
- `hero-image` **Hero image**: A wide image (21:9, 4:3 on phones) heading a marketing or landing page.
- `media-frame` **Aspect-ratio frame**: A fixed-ratio box that holds an image, video, map or chart and reserves its space.
- `snapshot-image` **Snapshot image**: A video still in a 16:9 frame, with its source and capture time on a solid caption bar.
- `recording-frame` **Recording frame**: A video or stream frame marked recording or live with a red outline and a worded flag.
- `video-frame` **Video frame**: A native `<video>` with controls inside an aspect-ratio frame.
- `illustration` **Illustration (empty, search, error)**: Simple token-coloured line illustrations for empty, no-result and error states.
- `qr-code` **QR code**: A frame for a server-generated QR code: white quiet zone, black modules, encoded text below.
- `barcode` **Barcode**: A frame for a server-generated 1D barcode with its human-readable digits below.

## [Structure marks](structure.md) (11)

Marks that organise and connect (rules, separators, focus, markers, backdrops), plus the accessibility helpers every page needs.

- `divider` **Divider**: A horizontal or vertical rule: default, muted, medium and large spacing, labelled, highlight and brand.
- `chevron-separator` **Chevron separator**: A small muted chevron between breadcrumb items or path segments.
- `sr-only` **Screen-reader-only text**: Text that assistive technology reads but the screen does not show.
- `skip-link` **Skip link**: The first focusable link on a page; it jumps past the navigation to the main content.
- `focus-ring` **Focus ring**: The 3px keyboard focus outline, drawn inside controls (outside for ticks and switches).
- `chevron` **Accordion chevron**: A chevron that points down when its section is open and sideways when closed.
- `step-marker` **Step marker**: A round marker for one step of a process: to do, current, done or error.
- `carousel-dot` **Carousel dot**: A position marker and button for one slide of a carousel or gallery.
- `pagination-gap` **Pagination gap (ellipsis)**: The ellipsis between page numbers that are not shown.
- `dialog-backdrop` **Dialog backdrop**: The dimmed layer behind a modal dialog, plus the dialog surface itself.
- `drawer-backdrop` **Drawer backdrop**: The scrim behind a side drawer; pressing it closes the drawer.

## [Progress](progress.md) (4)

Feedback while something takes time. Respond within 400 ms; show progress for longer; describe the step past 10 seconds.

- `progress-bar` **Progress bar**: A 3px (or 8px large) track with a fill: determinate with a value, indeterminate without.
- `progress-ring` **Progress ring**: A circular track and indicator with the value in the middle.
- `spinner` **Spinner**: A small rotating ring for short, unknown waits.
- `skeleton` **Skeleton**: Grey placeholder blocks that hold the shape of content while it loads.

## [Chart and graphic marks](charts.md) (4)

The small marks that make up charts, legends, zones and heat maps. Every colour mark has a nearby text label.

- `swatch` **Swatch**: A small colour square that keys a legend entry or shows a chosen colour.
- `zone-swatch` **Zone swatch**: A mark that matches a region drawn on an image or video: coloured outline, light fill, hatched when excluded.
- `chart-dot` **Dot (chart marker)**: A data-point marker: round, square, diamond or ring, coloured by series.
- `heat-cell` **Heat-map cell**: A cell shaded on a 6-step sequential scale, with its value printed inside.

## [Planning inputs](planning-inputs.md) (8)

Date, time and schedule inputs. Native pickers come first: people already know them on every device.

- `date-input` **Date input**: A native date field (`type="date"`) with ORCA styling.
- `time-input` **Time input**: A native time field (`type="time"`).
- `datetime-input` **Date-time input**: A native `datetime-local` field for one moment.
- `duration-input` **Duration input**: Hours and minutes as two short numeric fields with their units.
- `timezone-select` **Timezone select**: A native select of IANA timezones, grouped by region, preselected from context.
- `weekday-toggle` **Weekday toggle**: Seven square toggles for picking days of the week.
- `recurrence-select` **Recurrence select**: A select of common repeat rules, with a 'Custom…' option that shows more fields.
- `reminder-select` **Reminder select**: A select of reminder offsets before an event.

## [Planning text](planning-text.md) (11)

How dates, times and durations are written: machine-readable (`<time datetime>`) and formatted for the reader's locale and timezone.

- `day-number` **Day number**: The day of the month in a calendar cell or date badge.
- `weekday-name` **Weekday name**: The day of the week as a short uppercase label or a full word.
- `month-name` **Month name**: The month, with its year, heading a calendar or group of agenda items.
- `year-label` **Year label**: The year, muted, beside a month or in a year view.
- `week-number` **Week number**: The ISO week number, labelled.
- `time-label` **Time label**: A clock time in the reader's 12- or 24-hour convention.
- `date-label` **Date label**: A date written for people: '6 November 2026', 'Fri 6 Nov'.
- `relative-time` **Relative time label**: '2 minutes ago', 'in 3 days', with the exact time on hover and for screen readers.
- `timezone-label` **Timezone label**: A small outlined timezone abbreviation, with the full zone in its title.
- `duration-label` **Duration label**: A length of time: '45 min', '1 h 30 min', '3 d'.
- `countdown-label` **Countdown label**: Time left until a moment, updating live.

## [Planning marks](planning-marks.md) (17)

Marks for calendars, schedules and timelines. Each state pairs colour with a shape, pattern or word.

- `today-marker` **Today marker**: Today's day number outlined in red, bold.
- `selected-day-marker` **Selected-day marker**: The chosen day filled with the accent colour.
- `outside-day-marker` **Out-of-month day marker**: Days of the previous or next month shown muted.
- `weekend-marker` **Weekend marker**: A faint tint behind weekend days and columns.
- `holiday-marker` **Holiday marker**: A purple tint and underline on holidays and closed days, plus the holiday's name.
- `event-dot` **Event dot**: A small dot showing a day has events, or marking an event's calendar.
- `event-bar` **Event bar**: A timed event: a tinted bar with a 3px leading edge in the calendar colour.
- `allday-bar` **All-day bar**: A solid bar for all-day and multi-day events, with arrow ends when it continues.
- `hour-gridline` **Hour gridline**: Hour and half-hour lines with the hour label in the gutter.
- `now-indicator` **Now indicator**: A red line with a dot at the current time across day and week views.
- `availability-color` **Availability colour (free, busy, tentative)**: Free, busy, tentative and off states as filled, solid, hatched and dashed marks.
- `priority-marker` **Priority marker**: Signal bars plus a word: low, medium, high, urgent.
- `deadline-marker` **Deadline marker**: A flag icon with the due date; a caution flag when it is close.
- `overdue-marker` **Overdue marker**: Bold red text with the error glyph and how late it is.
- `milestone-marker` **Milestone marker**: A diamond: filled (reached), outlined (upcoming), red outline (missed), green (done).
- `drag-handle` **Drag handle**: A grip button for moving an item, usable by keyboard too.
- `resize-handle` **Resize handle**: A grip on the edge of an event or panel that changes its length.

## [Planning icons](planning-icons.md) (1)

Time and scheduling icons, on the same 16px grid as the rest of the set.

- `planning-icons` **Planning icons**: calendar, clock, repeat, bell (notifications), alarm, timer, hourglass, flag, pin, calendar-plus, today.
