init offset = -2

init python:
    gui.init(1280, 720)

define config.check_conflicting_properties = True

## COLORS - Meridian-7 Interface Theme
define gui.accent_color = '#27f3ff'
define gui.warning_color = '#ff4f64'
define gui.idle_color = '#9fc1c9'
define gui.idle_small_color = '#6c8d97'
define gui.hover_color = '#ffffff'
define gui.selected_color = '#ffffff'
define gui.insensitive_color = '#49616a7f'
define gui.muted_color = '#06151c'
define gui.hover_muted_color = '#0d2d38'
define gui.text_color = '#e8fbff'
define gui.interface_text_color = '#d8f3f8'

## FONTS
define gui.text_font = "DejaVuSans.ttf"
define gui.name_text_font = "DejaVuSans.ttf"
define gui.interface_text_font = "DejaVuSans.ttf"

## SIZES
define gui.text_size = 24
define gui.name_text_size = 28
define gui.interface_text_size = 22
define gui.label_text_size = 26
define gui.notify_text_size = 16
define gui.title_text_size = 66

## MENU BACKGROUNDS
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"

## TEXTBOX
define gui.textbox_height = 210
define gui.textbox_yalign = 1.0

## NAME POSITION
define gui.name_xpos = 94
define gui.name_ypos = 10
define gui.name_xalign = 0.0
define gui.namebox_width = None
define gui.namebox_height = None
define gui.namebox_borders = Borders(28, 10, 28, 10)
define gui.namebox_tile = False

## DIALOGUE POSITION
define gui.dialogue_xpos = 96
define gui.dialogue_ypos = 76
define gui.dialogue_width = 1088
define gui.dialogue_text_xalign = 0.0

## BUTTONS
define gui.button_width = 250
define gui.button_height = 46
define gui.button_borders = Borders(18, 8, 18, 8)
define gui.button_tile = False
define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size
define gui.button_text_idle_color = '#a6c7cf'
define gui.button_text_hover_color = '#ffffff'
define gui.button_text_selected_color = '#ffffff'
define gui.button_text_insensitive_color = '#49616a7f'
define gui.button_text_xalign = 0.0

define gui.radio_button_borders = Borders(34, 8, 16, 8)
define gui.check_button_borders = Borders(34, 8, 16, 8)
define gui.confirm_button_text_xalign = 0.5
define gui.page_button_borders = Borders(14, 6, 14, 6)
define gui.quick_button_borders = Borders(12, 5, 12, 5)
define gui.quick_button_text_size = 13
define gui.quick_button_text_idle_color = '#89aab3'
define gui.quick_button_text_selected_color = '#27f3ff'

## CHOICE BUTTONS
define gui.choice_button_width = 900
define gui.choice_button_height = 58
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(40, 12, 40, 12)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#d8f3f8'
define gui.choice_button_text_hover_color = '#ffffff'
define gui.choice_button_text_insensitive_color = '#49616a7f'

## FILE SLOTS
define gui.slot_button_width = 292
define gui.slot_button_height = 214
define gui.slot_button_borders = Borders(16, 16, 16, 16)
define gui.slot_button_text_size = 13
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = '#7a9aaa'
define gui.slot_button_text_selected_idle_color = '#ffffff'
define gui.slot_button_text_selected_hover_color = '#00e5ff'

define config.thumbnail_width = 256
define config.thumbnail_height = 144

define gui.file_slot_cols = 3
define gui.file_slot_rows = 2

## SPACING
define gui.navigation_xpos = 44
define gui.skip_ypos = 10
define gui.notify_ypos = 45
define gui.choice_spacing = 14
define gui.navigation_spacing = 9
define gui.pref_spacing = 16
define gui.pref_button_spacing = 6
define gui.page_spacing = 4
define gui.slot_spacing = 14
define gui.main_menu_text_xalign = 1.0

## FRAMES
define gui.frame_borders = Borders(18, 18, 18, 18)
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)
define gui.skip_frame_borders = Borders(18, 8, 42, 8)
define gui.notify_frame_borders = Borders(18, 8, 42, 8)
define gui.frame_tile = False

## BARS
define gui.bar_size = 24
define gui.scrollbar_size = 10
define gui.slider_size = 24
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False
define gui.bar_borders = Borders(10, 10, 10, 10)
define gui.scrollbar_borders = Borders(5, 5, 5, 5)
define gui.slider_borders = Borders(10, 10, 10, 10)
define gui.vbar_borders = Borders(10, 10, 10, 10)
define gui.vscrollbar_borders = Borders(5, 5, 5, 5)
define gui.vslider_borders = Borders(10, 10, 10, 10)
define gui.unscrollable = "hide"

## HISTORY
define config.history_length = 250
define gui.history_height = 132
define gui.history_spacing = 8
define gui.history_name_xpos = 120
define gui.history_name_ypos = 0
define gui.history_name_width = 155
define gui.history_name_xalign = 1.0
define gui.history_text_xpos = 300
define gui.history_text_ypos = 2
define gui.history_text_width = 760
define gui.history_text_xalign = 0.0

## NVL
define gui.nvl_borders = Borders(0, 10, 0, 20)
define gui.nvl_list_length = 6
define gui.nvl_height = 115
define gui.nvl_spacing = 10
define gui.nvl_name_xpos = 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 150
define gui.nvl_name_xalign = 1.0
define gui.nvl_text_xpos = 450
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = 620
define gui.nvl_text_xalign = 0.0
define gui.nvl_thought_xpos = 240
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 780
define gui.nvl_thought_xalign = 0.0
define gui.nvl_button_xpos = 450
define gui.nvl_button_xalign = 0.0

define gui.language = "unicode"

init python:
    @gui.variant
    def touch():
        gui.quick_button_borders = Borders(40, 14, 40, 0)

    @gui.variant
    def small():
        gui.text_size = 30
        gui.name_text_size = 36
        gui.notify_text_size = 25
        gui.interface_text_size = 30
        gui.button_text_size = 30
        gui.label_text_size = 34
        gui.textbox_height = 240
        gui.name_xpos = 68
        gui.dialogue_xpos = 90
        gui.dialogue_width = 1100
        gui.slider_size = 36
        gui.choice_button_width = 1160
        gui.choice_button_text_size = 30
        gui.navigation_spacing = 20
        gui.pref_button_spacing = 10
        gui.history_height = 190
        gui.history_text_width = 690
        gui.quick_button_text_size = 20
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2
        gui.nvl_height = 170
        gui.nvl_name_width = 305
        gui.nvl_name_xpos = 325
        gui.nvl_text_width = 915
        gui.nvl_text_xpos = 345
        gui.nvl_text_ypos = 5
        gui.nvl_thought_width = 1240
        gui.nvl_thought_xpos = 20
        gui.nvl_button_width = 1240
        gui.nvl_button_xpos = 20
