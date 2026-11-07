"""The ORCA Design System Guide, level by level and item by item.

Used by the test suite to prove that every primitive the guide lists is covered by an element
of the catalogue (see ``Element.guide``). Text copied verbatim from the guide's headings and bullets.
"""

PRIMITIVES = {
    "Base styles": [
        "Colour palette", "Brand colour and surfaces", "Fonts", "Type scale", "Spacing scale (8 px)", "Borders", "Animation",
        "Themes (light, dark, paper)", "Appearances (Lumen, Tangerine)", "Neutral scale (gray)", "Hue scales (eleven hues, numbered steps)",
        "Semantic colour tokens", "Accent colour", "Type styles (heading, title, body, detail)", "Monospace font",
        "Corner radii (rounding)", "Layers", "Shadows (card, elevated, dragged)", "Control heights (sm, md, lg, xl)", "Motion",
        "Aspect-ratio utilities", "Elevation utilities", "Scrollbar style",
    ],
    "Text": [
        "Heading (h1–h6)", "Page title", "Page subtitle", "Section title", "Panel title", "Alert title", "Paragraph", "Text link",
        "Muted text", "Small text", "Tabular number", "Keyboard key", "Stat label", "Stat value", "Delta (up, down, flat)",
        "Code text", "Card kicker", "Card title", "Card meta", "Dialog title", "Empty-state title", "Empty-state text",
    ],
    "Form text": ["Label", "Required marker", "Help text", "Error text", "Help icon", "Error list"],
    "Actions": [
        "Button (base, positive, negative, brand)", "Button sizes (small, dense, block, icon-only)", "Link", "Pin button",
        "Email button", "Button (primary, brand, secondary, neutral, ghost, elevated, danger)", "Button outlines (accent, neutral, danger)",
        "Button sizes (sm, lg, xl)", "Toggle button (pressed)", "Disabled button", "Icon button (quiet, outlined, accent, neutral fill)",
        "Floating action button (FAB)", "Extended FAB",
    ],
    "Inputs": [
        "Text input", "Dense text input", "Textarea", "Select", "Search input", "Checkbox", "Radio", "Switch", "Number input",
        "Colour input", "File input", "OTP digit box", "Native select", "Multiple select (listbox)", "Small input", "Large input",
        "Fixed-size textarea", "Input addon (prefix, suffix)", "Search clear button",
    ],
    "Icons": [
        "Icon (small, default, large)", "Status icon (four status glyphs)", "Menu (hamburger)", "Notifications", "Snapshot",
        "Statistics", "Plus", "Search (magnifier)", "Play", "Arrows", "Chevrons (left, right, down)", "Close", "Delete", "Archive",
        "Restart", "Location", "Spinner", "Favicon", "Icon sizes (xs, s, m, l, xl)", "Lucide icon set", "Edit (pencil)", "Filter",
        "Star", "More (ellipsis)", "Sort", "Grid", "Chat", "Sliders", "Home", "Help", "Unlock", "Refresh", "Success", "Error", "Settings",
    ],
    "Status marks": [
        "Status dot", "Badge (information, positive, negative, caution)", "Alert icon", "Badge (neutral, grey)", "Badge (accent, brand)",
        "Badge (action, informative)", "Badge (tertiary, purple)", "Count badge",
    ],
    "Labels": ["Tag", "Selected tag", "Removable tag"],
    "Identity": ["Logo", "Avatar (xs, s, l, xl)", "Favicon set", "Avatar (square)", "Avatar initials"],
    "Imagery": [
        "Thumbnail image", "Hero image", "Primary image", "Avatar image", "Snapshot image", "Recording frame",
        "Illustration (empty, search)", "Image (bordered)", "Aspect-ratio frame", "Video frame", "QR code", "Barcode",
    ],
    "Structure marks": [
        "Divider", "Chevron separator", "Screen-reader-only text", "Skip link", "Focus ring", "Divider (medium, large, vertical, labeled)",
        "Accordion chevron", "Step marker", "Carousel dot", "Pagination gap (ellipsis)", "Dialog backdrop", "Drawer backdrop",
    ],
    "Progress": ["Progress track", "Progress fill", "Progress bar (default, large)", "Progress ring (track, indicator)", "Spinner (sm, default, lg)"],
    "Chart and graphic marks": ["Swatch", "Zone swatch", "Dot", "Heat-map cell"],
    "Planning inputs": [
        "Date input", "Time input", "Date-time input", "Duration input", "Timezone select", "Weekday toggle", "Recurrence select", "Reminder select",
    ],
    "Planning text": [
        "Day number", "Weekday name", "Month name", "Year label", "Week number", "Time label", "Date label", "Relative time label",
        "Timezone label", "Duration label", "Countdown label",
    ],
    "Planning marks": [
        "Today marker", "Selected-day marker", "Out-of-month day marker", "Weekend marker", "Holiday marker", "Event dot", "Event bar",
        "All-day bar", "Hour gridline", "Now indicator", "Availability colour (free, busy, tentative)", "Priority marker",
        "Deadline marker", "Overdue marker", "Milestone marker", "Drag handle", "Resize handle",
    ],
    "Planning icons": [
        "Calendar", "Clock", "Repeat", "Bell (reminder)", "Alarm", "Timer", "Hourglass", "Flag", "Pin (date)", "Calendar-plus", "Today (jump to today)",
    ],
}




COMPONENTS = {
    'Forms': ['Form field (text)', 'Form field (select)', 'Form field (checkbox)', 'Form field (switch)', 'Form field (radio group)', 'Form field (checkbox group)', 'Search form', 'Table toolbar', 'Multi-picker', 'Language switcher', 'Input group (addon + input)', 'Search field (icon + input + clear)', 'Search bar', 'Filter button', 'Dropdown select (picker)', 'Combobox (input + suggestions)', 'Autocomplete input', 'Auto-suggest input', 'OTP input', 'Rating input', 'Split date input (day, month, year)', 'File input field', 'Form alert (non-field errors)', 'Form actions'],
    'Navigation': ['Primary navigation', 'Utility navigation', 'Sidebar link', 'Breadcrumbs', 'Pagination', 'Table pager', 'Tab bar', 'Bottom navigation bar', 'Nav tree (collapsible sections)', 'Tree leaf', 'Child tabs (with counts)', 'Back link', 'Pagination summary', 'Pagination link', 'View toggle (cards, table)', 'Settings toggle', 'Create button (floating on phones)'],
    'Feedback': ['Alert', 'Empty state', 'Status light', 'Confirm dialog', 'Progress bar with counts', 'Callout (info, success, warning, danger)', 'Toast', 'Toast stack', 'Flash message', 'Tooltip', 'No-data state', 'Dialog'],
    'Actions': ['Button group', 'Dropdown menu', 'Dropdown item', 'Copy button (copied confirmation)', 'Record actions (one button + overflow menu)', 'Row actions'],
    'Data display': ['Stat card', 'Key/value list', 'List', 'List item', 'Timeline item', 'Sortable column header', 'Legend item', 'Zone row', 'Line-count item', 'Media object', 'Card', 'Accordion', 'Steps', 'Tree', 'Avatar group', 'Card (outlined, elevated, filled)', 'Table card', 'Card footer', 'Linked card', 'Property row (key, value, remove)', 'Activity entry (badge, actor, time, before and after)', 'Carousel', 'Scroller (scroll-snap region)', 'Sparkline', 'Donut chart', 'Chart frame'],
    'Content blocks': ['Product item', 'Person block', 'Block post (thumbnail + headline + excerpt)', 'Hero', 'Photo-actions bar', 'Camera card'],
    'Identity and controls': ['User chip', 'Panel header', 'Pin control', 'Theme toggle', 'Email button (with fallback link)'],
    'Date and time pickers': ['Date picker', 'Time picker', 'Date-time picker', 'Date-range picker', 'Time-range input (start and end)', 'Duration picker', 'Timezone selector', 'Month and year switcher', 'Mini calendar'],
    'Planning selectors': ['Weekday selector', 'Recurrence selector', 'Reminder selector', 'Period selector', 'Granularity selector', 'Calendar view switcher (day, week, month, agenda)', 'Preset buttons (Today, Weekdays, This week, Next 7 days)', 'Calendar navigation (previous, today, next)'],
    'Calendar parts': ['Day cell', 'Week header', 'Weekday header', 'Week row', 'Hour row', 'Time slot', 'All-day row', 'Event chip', 'Event card', 'Agenda item', 'Date badge', 'Holiday label', 'More-events link ("+3 more")', 'Calendar header (month label + navigation)'],
    'Schedule parts': ['Schedule row (day, start, end)', 'Add-row button', 'Remove-row button', 'Availability legend', 'Exception entry (date override)', 'Time-off entry', 'Booking slot', 'Conflict warning', 'Overlap warning', 'Working-hours label'],
    'Plan items': ['Task item', 'Subtask item', 'Milestone item', 'Deadline item', 'Reminder item', 'Assignee chip', 'Due-date chip', 'Status chip (planned, in progress, done, overdue)', 'Priority chip', 'Progress chip', 'Gantt bar', 'Plan card', 'Board card', 'Resource row'],
    'Documentation site': ['Live example (preview and code tabs)', 'Code block', 'Docs navigation tree'],
}


LEVELS = {"primitive": PRIMITIVES, "component": COMPONENTS}


def all_items(level: str = "primitive") -> list[tuple[str, str]]:
    return [(section, item) for section, items in LEVELS[level].items() for item in items]
