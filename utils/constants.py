"""Defines numerous constants used throughout the project."""

# A unique empty value used when None is a valid value.
EMPTY_VALUE = object()

# The height and width of the macropad display.
DISPLAY_WIDTH = 128
DISPLAY_HEIGHT = 64

# Settings

# The setting name for the previous app setting
PREVIOUS_APP_SETTING = "previous app"

# The setting name and options for the OS setting
OS_SETTING = "OS"
OS_MAC = "MAC"
OS_WINDOWS = "WIN"
OS_LINUX = "LIN"

# Setting name for the pixels disabled setting
PIXELS_DISABLED_SETTING = "pixels disabled"

# Timeout after which the pixels will be disabled
ONE_MINUTE = 60
DISABLE_PIXELS_TIMEOUT = 20 * ONE_MINUTE

# Timer ID for the disabled pixels timer
TIMER_DISABLE_PIXELS = "disable pixels timer"

# Defines a color scheme for the Macropad. You can reference these constants
# for pixel colors to define a consistent color scheme and make it easy to
# update the colors
COLOR_1 = "COLOR_1"
COLOR_2 = "COLOR_2"
COLOR_3 = "COLOR_3"
COLOR_4 = "COLOR_4"
COLOR_5 = "COLOR_5"
COLOR_6 = "COLOR_6"
COLOR_7 = "COLOR_7"
COLOR_8 = "COLOR_8"
COLOR_9 = "COLOR_9"
COLOR_10 = "COLOR_10"

COLOR_APPS = "COLOR_APPS"
COLOR_FUNC = "COLOR_FUNC"
COLOR_MEDIA = "COLOR_MEDIA"
COLOR_NAV = "COLOR_NAV"
COLOR_NUMPAD = "COLOR_NUMPAD"
COLOR_WINMAN = "COLOR_WINMAN"

COLOR_ALERT = "COLOR_ALERT"
COLOR_WARNING = "COLOR_WARNING"
COLOR_GO = "COLOR_GO"

COLOR_BACK = "COLOR_BACK"
COLOR_CLOSE = "COLOR_CLOSE"

COLOR_MAC = "COLOR_MAC"
COLOR_WINDOWS = "COLOR_WINDOWS"
COLOR_LINUX = "COLOR_LINUX"

COLOR_CHROME = "COLOR_CHROME"
COLOR_CODE = "COLOR_CODE"
COLOR_FILES = "COLOR_FILES"
COLOR_NOTION = "COLOR_NOTION"
COLOR_PYCHARM = "COLOR_PYCHARM"
COLOR_SLACK = "COLOR_SLACK"
COLOR_SPOTIFY = "COLOR_SPOTIFY"
COLOR_SUBLIME_MERGE = "COLOR_SUBLIME_MERGE"
COLOR_TERMINAL = "COLOR_TERMINAL"
