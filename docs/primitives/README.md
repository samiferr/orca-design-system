# ORCA primitives

Generated from `orca/catalogue/` by `python -m orca build`. Do not edit by hand.

Every element below has a **why**, **when**, **when not**, **how**, accessibility notes, the tokens and
classes it uses, the UX principles it applies, and a copy-ready Django template example.
Load the tags with `{% load orca %}` and put `{% orca_head %}` in `<head>`.

## [Base styles](foundations.md) (15)

Tokens every other element is built from: colour, type, space, shape, elevation, layers, size and motion. Use these names, never raw values. Only brand tokens may be changed by a project.

- `color-palette` **Colour palette**: Raw colours: a 13-step gray scale and eleven hues with nine numbered steps each.
- `semantic-colors` **Semantic colour tokens**: Colours named by their job: text, grounds, lines, interaction, status, actions, planning, data.
- `brand-color` **Brand colour and surfaces**: The one brand colour, the fills derived from it, and the page surfaces it sits on.
- `accent-color` **Accent colour**: The single interactive colour: links, checked ticks, radios, switches, progress, selected days.
- `themes` **Themes**: Light, dark and paper share every token name. ORCA has one appearance: Tangerine.
- `typography` **Fonts and type styles**: Ubuntu Sans (variable) for everything, Ubuntu Sans Mono for code, on a fixed type scale.
- `spacing` **Spacing scale**: Eleven spacing steps on the 8px unit, named by their pixel value.
- `borders` **Borders**: Three line weights: 1px hairline, 1.5px outline, 3px emphasis bar.
- `radii` **Corner radii**: Tangerine is square; only round marks and bar ends are rounded.
- `shadows` **Shadows and elevation**: Three shadows (card, elevated, dragged) and elevation utilities. Only floating things cast a shadow.
- `layers` **Layers (z-index)**: A fixed stacking order from page content to the skip link.
- `control-heights` **Control heights**: Five heights shared by buttons, fields, selects and toggles: sm, dense, md, lg, xl.
- `motion` **Motion**: Four durations and two easings, all under the 400 ms Doherty threshold.
- `aspect-ratio` **Aspect-ratio utilities**: Reserve the space of images and video before they load.
- `scrollbar` **Scrollbar style**: A thin, token-coloured scrollbar for inner scrolling regions.

## [Text](text.md) (22)

Text styles with a fixed role. Choose by what the text is (a page title, a stat value), not by how big you want it.

- `heading` **Heading (h1–h6)**: Document headings from h1 to h6, plus a display style for marketing pages.
- `page-title` **Page title**: The single title naming what this page is.
- `page-subtitle` **Page subtitle**: One sentence under the page title that says what the page is for or about.
- `section-title` **Section title**: Title of a section inside a page (a group of panels or a long form part).
- `panel-title` **Panel title**: Title at the top of a panel or card group of content.
- `alert-title` **Alert title**: Bold first line of an alert, callout or notification that states what happened.
- `paragraph` **Paragraph**: Running text at 16/24 with a 70-character measure.
- `text-link` **Text link**: An underlined, accent-coloured link inside text.
- `muted-text` **Muted text**: Secondary text in `--orca-text-muted` (60% ink, still 4.5:1).
- `small-text` **Small text**: 14/20 detail text for help, meta and timestamps.
- `tabular-number` **Tabular number**: Digits of equal width so numbers line up in columns and do not jitter when they update.
- `kbd` **Keyboard key**: A key or shortcut the person presses.
- `stat-label` **Stat label**: The name of a measured value, shown above it.
- `stat-value` **Stat value**: A large, tabular number that is the point of a KPI tile.
- `delta` **Delta (up, down, flat)**: Change against a reference: arrow, signed value, colour, and the reference in words.
- `code-text` **Code text**: Inline code, identifiers, file names and values the person may copy.
- `card-kicker` **Card kicker**: A short uppercase category label above a card title.
- `card-title` **Card title**: The name of the object a card represents.
- `card-meta` **Card meta**: Secondary facts under a card title, separated by middle dots.
- `dialog-title` **Dialog title**: The question or statement a dialog or drawer is about.
- `empty-title` **Empty-state title**: What is missing, said plainly, in an empty region.
- `empty-text` **Empty-state text**: One sentence that says why it is empty and what to do next.

## [Form text](form-text.md) (6)

The words around a field: its label, requirement marker, help and errors. They decide whether a form is completed.

- `label` **Label**: A visible, persistent name above every field.
- `required-marker` **Required marker**: The word 'required' or 'optional' after a label.
- `help-text` **Help text**: A hint between the label and the field that helps people answer correctly.
- `error-text` **Error text**: A message above the field that says what is wrong and how to fix it.
- `help-icon` **Help icon**: A question-mark button that reveals optional, extra explanation in place.
- `error-list` **Error list**: An error summary at the top of a form, linking to each invalid field.

## [Actions](actions.md) (8)

Things people press. One primary action per screen; everything else is quieter.

- `button` **Button**: A command. Variants express importance: primary, secondary (default), ghost, link, plus brand, danger, neutral, elevated and outlines.
- `button-size` **Button sizes**: Size modifiers: sm, dense, default, lg, xl, plus block (full width) and icon-only.
- `link-action` **Link (tertiary action)**: A text-styled button or link for the least important actions.
- `pin-button` **Pin button**: A toggle that pins an item to the top of a list or to the dashboard.
- `email-button` **Email button**: A mailto link styled as a button, with the address shown as a fallback.
- `toggle-button` **Toggle button (pressed)**: A button that stays pressed to show an on state.
- `icon-button` **Icon button**: A square button with a single 16px icon and an accessible name. Quiet, outlined, accent and neutral-fill variants.
- `fab` **Floating action button (FAB)**: A large floating button for the one creation action of a phone screen.

## [Inputs](inputs.md) (13)

Native form controls styled by ORCA. Native first: they work with keyboards, screen readers, autofill and phones for free.

- `text-input` **Text input**: A single-line field: filled, square, with a 1.5px bottom border.
- `textarea` **Textarea**: A multi-line field that grows vertically.
- `select` **Select (native)**: The browser's dropdown, styled with an ORCA chevron.
- `listbox` **Multiple select (listbox)**: A native `<select multiple>` showing several options at once.
- `search-input` **Search input**: A text field with a magnifier and a clear button.
- `checkbox` **Checkbox**: A square tick for an on/off choice that takes effect when the form is saved, or one of several choices.
- `radio` **Radio**: A round mark for choosing exactly one option from a small visible set.
- `switch` **Switch**: An on/off control that takes effect immediately.
- `number-input` **Number input**: A numeric field with large minus and plus buttons for small adjustments.
- `color-input` **Colour input**: A native colour picker paired with its hex value.
- `file-input` **File input**: The native file picker with an ORCA-styled button.
- `otp-digit` **OTP digit box**: One box per digit of a one-time code, with auto-advance and paste.
- `input-addon` **Input addon (prefix, suffix)**: A fixed unit, prefix or button joined to an input.

## [Icons](icons.md) (3)

One icon set, 16px, single ink in currentColor. Icons support words; they never replace them.

- `icon` **Icon**: An inline SVG glyph from the ORCA set, sized by token and coloured by its text.
- `status-icon` **Status icon**: The four status glyphs (success, warning, error, info), each a distinct shape in its status colour.
- `icon-set` **Icon set**: The named glyphs: 106 from Vanilla (via Tangerine) plus ORCA glyphs for ideas Vanilla lacks.

## [Status marks and labels](status.md) (5)

Small marks that state a condition or categorise an item. Status always pairs colour with a word and, where it matters, a shape.

- `status-dot` **Status dot**: A 12px round mark before a word, showing the live state of a thing.
- `badge` **Badge**: A compact square label with a status or category word, solid or subtle.
- `alert-icon` **Alert icon**: The status glyph that leads an alert, callout or field message, placed in the alert's left inset.
- `count-badge` **Count badge**: A small pill with a number: unread items, pending tasks.
- `tag` **Tag**: A label for a keyword or category; static, selectable (filter) or removable (chosen value).

## [Identity](identity.md) (3)

Who and what: the product's logo and favicon, and people's avatars.

- `logo` **Logo**: The product's logo image, or its name as a wordmark with a brand bar when no logo is set.
- `avatar` **Avatar**: A person's picture or initials in a circle (or square for organisations and devices).
- `favicon` **Favicon set**: The browser-tab and home-screen icons for the product.

## [Imagery](imagery.md) (10)

Images, frames and graphics. Reserve their space, describe them, and keep text readable over them.

- `image` **Image**: A content image (the primary image of a record), plain or bordered.
- `thumbnail` **Thumbnail image**: A small square preview (48 or 96px) cropped to fill.
- `hero-image` **Hero image**: A wide image (21:9, 4:3 on phones) heading a marketing or landing page.
- `media-frame` **Aspect-ratio frame**: A box with a fixed aspect ratio that holds an image, video, map or chart and reserves its space.
- `snapshot-image` **Snapshot image**: A still image taken from a video, in a 16:9 frame with its source and capture time on a solid caption bar.
- `recording-frame` **Recording frame**: A video or stream frame marked as recording or live with a red outline and a worded flag.
- `video-frame` **Video frame**: A native `<video>` with controls inside an aspect-ratio frame.
- `illustration` **Illustration (empty, search, error)**: Simple token-coloured line illustrations for empty, no-result and error states.
- `qr-code` **QR code**: A frame for a server-generated QR code: white quiet zone, black modules, and the encoded text below.
- `barcode` **Barcode**: A frame for a server-generated 1D barcode with its human-readable digits below.

## [Structure marks](structure.md) (11)

Marks that organise and connect: rules, separators, focus, markers and backdrops. Plus the accessibility helpers every page needs.

- `divider` **Divider**: A horizontal or vertical rule: default, muted, medium and large spacing, labelled, highlight and brand.
- `chevron-separator` **Chevron separator**: A small muted chevron between breadcrumb items or path segments.
- `sr-only` **Screen-reader-only text**: Text that is read by assistive technology but not shown.
- `skip-link` **Skip link**: The first focusable link on every page, jumping past navigation to the main content.
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

The small marks charts, legends, zones and heat maps are made of. Every colour mark has a text label nearby.

- `swatch` **Swatch**: A small square of colour that keys a legend entry or shows a chosen colour.
- `zone-swatch` **Zone swatch**: A mark matching how a region is drawn on an image or video: coloured outline with a light fill, hatched when excluded.
- `chart-dot` **Dot (chart marker)**: A data-point marker: round, square, diamond or ring, coloured by series.
- `heat-cell` **Heat-map cell**: A cell shaded on a 6-step sequential scale, with its value printed in it.

## [Planning inputs](planning-inputs.md) (8)

Date, time and schedule inputs. Native pickers first: they are what people already know, on every device.

- `date-input` **Date input**: A native date field (`type="date"`) with ORCA styling.
- `time-input` **Time input**: A native time field (`type="time"`).
- `datetime-input` **Date-time input**: A native `datetime-local` field for one moment.
- `duration-input` **Duration input**: Hours and minutes as two short numeric fields with their units.
- `timezone-select` **Timezone select**: A native select of IANA timezones, grouped by region, preselected from context.
- `weekday-toggle` **Weekday toggle**: Seven square toggles for picking days of the week.
- `recurrence-select` **Recurrence select**: A select of common repeat rules with a 'Custom…' option that reveals more fields.
- `reminder-select` **Reminder select**: A select of reminder offsets before an event.

## [Planning text](planning-text.md) (11)

How dates, times and durations are written. Always machine-readable (`<time datetime>`) and formatted for the reader's locale and timezone.

- `day-number` **Day number**: The day of the month in a calendar cell or date badge.
- `weekday-name` **Weekday name**: The day of the week as a short uppercase label or a full word.
- `month-name` **Month name**: The month (and year) heading a calendar or a group of agenda items.
- `year-label` **Year label**: The year, muted, beside a month or in a year view.
- `week-number` **Week number**: The ISO week number, labelled.
- `time-label` **Time label**: A clock time in the reader's 12- or 24-hour convention.
- `date-label` **Date label**: A date written for people: '6 November 2026', 'Fri 6 Nov'.
- `relative-time` **Relative time label**: '2 minutes ago', 'in 3 days', with the exact time on hover and for screen readers.
- `timezone-label` **Timezone label**: A small outlined abbreviation of the timezone, with the full zone in its title.
- `duration-label` **Duration label**: A length of time: '45 min', '1 h 30 min', '3 d'.
- `countdown-label` **Countdown label**: Time left until a moment, updating live.

## [Planning marks](planning-marks.md) (17)

Marks drawn on calendars, schedules and timelines. Each state pairs colour with a shape, a pattern or a word.

- `today-marker` **Today marker**: Today's day number outlined in red, bold.
- `selected-day-marker` **Selected-day marker**: The chosen day filled with the accent colour.
- `outside-day-marker` **Out-of-month day marker**: Days of the previous or next month shown muted.
- `weekend-marker` **Weekend marker**: A faint tint behind weekend days and columns.
- `holiday-marker` **Holiday marker**: A purple tint and underline mark on holidays and closed days, with the holiday's name.
- `event-dot` **Event dot**: A small dot that says 'there are events here' or keys an event's calendar.
- `event-bar` **Event bar**: A timed event in a day: tinted bar with a 3px leading edge in the calendar colour.
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

Icons for time and scheduling ideas, drawn by ORCA on the same 16px grid as the rest of the set.

- `planning-icons` **Planning icons**: calendar, clock, repeat, bell (notifications), alarm, timer, hourglass, flag, pin, calendar-plus, today.
