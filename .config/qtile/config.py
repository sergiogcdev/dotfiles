###################################################
#  mmmm  m   ""#                     m"" "        #
# m"  "mm#mmmm #  mmm    mmm mmmm mmm#mmmm  mmmm  #
# #    # #   # # #"     #"  #" "#"  ##   # #" "#  #
# #    # #   # # #"""   #   #   #   ##   # #   #  #
#  #mm#" "mmm#m"m"#mm   "#mm"#m##   ## mm#m"#m"#  #
#     #                                     m  #  #
#                                            ""   #
#   By: B34n5                                     # 
###################################################

from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, EzKey
from libqtile.lazy import lazy
import subprocess

sticky_windows = []

def stick_win(qtile):
    global sticky_windows
    sticky_windows.append(qtile.current_window)
def unstick_win(qtile):
    global sticky_windows
    if qtile.current_window in sticky_windows:
        sticky_windows.remove(qtile.current_window)

mod = "mod1"
terminal = "kitty"
groups = [Group(i) for i in [ " www ", " dev ", " sys ", " mus ", " chat ", " doc ", " vid ", " vbox ", " gfx " ]]
# ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "] ]

keys = [
    EzKey("A-j", lazy.layout.left(), desc="Move focus to left"),
    EzKey("A-k", lazy.layout.right(), desc="Move focus to right"),
    EzKey("A-<Tab>", lazy.layout.next(), desc="Move window focus to other window"),
    EzKey("A-S-j", lazy.layout.shuffle_left(), desc="Move window to the left"),
    EzKey("A-S-k", lazy.layout.shuffle_right(), desc="Move window to the right"),
    EzKey("A-S-h", lazy.layout.shuffle_down(), desc="Move window down"),
    EzKey("A-S-l", lazy.layout.shuffle_up(), desc="Move window up"),
    EzKey("A-h", lazy.layout.grow_left(), desc="Grow window to the left"),
    EzKey("A-l", lazy.layout.grow_right(), desc="Grow window to the right"),
    EzKey("A-t", lazy.layout.normalize(), desc="Reset all window sizes"),
    EzKey("A-<Space>", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    EzKey("A-S-<Return>", lazy.spawn(terminal), desc="Launch terminal"),
    EzKey("A-<Space>", lazy.next_layout(), desc="Toggle between layouts"),
    EzKey("A-S-c", lazy.window.kill(), desc="Kill focused window"),
    EzKey("C-A-f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    EzKey("C-A-z", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    EzKey("A-r", lazy.spawn("killall loop_wp.py"), desc="Kill loop_wp.py process"),
    EzKey("A-q", lazy.reload_config(), desc="Reload the config"),
    EzKey("A-S-q", lazy.shutdown(), desc="Shutdown Qtile"),
    # MonadTall specific ##############
    EzKey("A-l", lazy.layout.grow(), desc="Grow window"),
    EzKey("A-h", lazy.layout.shrink(), desc="Shrink window"),
    EzKey("A-S-j", lazy.layout.swap_left(), desc="Move window to the left"),
    EzKey("A-S-k", lazy.layout.swap_right(), desc="Move window to the right"),
    EzKey("A-t", lazy.layout.reset(), desc="Reset all window sizes"),
    ###################################
    # Programs
    EzKey("A-r", lazy.spawn("pkill loop_wp.py"), desc="Stop looping wallpapers"),
    EzKey("A-x", lazy.spawn("mouseless"), desc="Mouse management with keyboard"),
    EzKey("A-v", lazy.spawn("pamixer -i 5"), desc="Increase volume"),
    EzKey("A-S-v", lazy.spawn("pamixer -d 5"), desc="Decrease volume"),
    EzKey("A-f", lazy.spawn("firefox"), desc="Launch firefox"),
    EzKey("A-s", lazy.spawn("scrot /home/sergio/pictures/screenshots/scrot_%y-%m-%d_%H%M%S.png"), desc="Take screenshot"),
    EzKey("A-C-s", lazy.spawn("scrot -s /home/sergio/pictures/screenshots/scrot_%y-%m-%d_%H%M%S.png"), desc="Take a selected screenshot"),
    EzKey("A-y", lazy.spawn("/home/sergio/scripts/dmenu_youtube"), desc="Youtube search prompt"),
    EzKey("A-C-p", lazy.spawn("/home/sergio/scripts/playYoutube"), desc="Play YT video in mpv player"),
    ###################################
    # lazy custom function
    EzKey("C-A-c", lazy.function(stick_win), desc="Stick window"),
    EzKey("C-A-S-c", lazy.function(unstick_win), desc="Unstick window"),
    ###################################
    # Scripts
    EzKey("M-q", lazy.spawn("/home/sergio/scripts/switch-qtile"), desc=".xinitrc symlink points to qtilerc"),
    EzKey("M-m", lazy.spawn("/home/sergio/scripts/switch-xmonad"), desc=".xinitrc symlink points to xmonadrc"),
    ###################################
    # Workspaces
    EzKey("A-p", lazy.spawn("dmenu_run -fn 'JetBrains Mono-14'"), desc="Spawn a command using a prompt widget"),
    EzKey("A-1", lazy.group[" www "].toscreen(), desc="Switch to www workspace"),
    EzKey("A-2", lazy.group[" dev "].toscreen(), desc="Switch to dev workspace"),
    EzKey("A-3", lazy.group[" sys "].toscreen(), desc="Switch to sys workspace"),
    EzKey("A-4", lazy.group[" mus "].toscreen(), desc="Switch to mus workspace"),
    EzKey("A-5", lazy.group[" chat "].toscreen(), desc="Switch to chat workspace"),
    EzKey("A-6", lazy.group[" doc "].toscreen(), desc="Switch to doc workspace"),
    EzKey("A-7", lazy.group[" vid "].toscreen(), desc="Switch to vid workspace"),
    EzKey("A-8", lazy.group[" vbox "].toscreen(), desc="Switch to vbox workspace"),
    EzKey("A-9", lazy.group[" gfx "].toscreen(), desc="Switch to gfx workspace"),
    EzKey("A-S-1", lazy.window.togroup(" www ", switch_group=False), desc="Move focused window to www workspace"),
    EzKey("A-S-2", lazy.window.togroup(" dev ", switch_group=False), desc="Move focused window to dev workspace"),
    EzKey("A-S-3", lazy.window.togroup(" sys ", switch_group=False), desc="Move focused window to sys workspace"),
    EzKey("A-S-4", lazy.window.togroup(" mus ", switch_group=False), desc="Move focused window to mus workspace"),
    EzKey("A-S-5", lazy.window.togroup(" chat ", switch_group=False), desc="Move focused window to chat workspace"),
    EzKey("A-S-6", lazy.window.togroup(" doc ", switch_group=False), desc="Move focused window to doc workspace"),
    EzKey("A-S-7", lazy.window.togroup(" vid ", switch_group=False), desc="Move focused window to vid workspace"),
    EzKey("A-S-8", lazy.window.togroup(" vbox ", switch_group=False), desc="Move focused window to vbox workspace"),
    EzKey("A-S-9", lazy.window.togroup(" gfx ", switch_group=False), desc="Move focused window to gfx workspace"),
    ###################################
]

layouts = [
    layout.MonadTall(align=0, border_focus="#00e673", border_normal="#ff0000", margin=5),
    layout.Max(border_focus="#00e673", border_normal="#ff0000", margin=5)
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrains Mono",
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

colors = [["#292d3e", "#292d3e"],
          ["#434758", "#434758"],
          ["#ffffff", "#ffffff"],
          ["#ff5555", "#ff5555"],
          ["#8d62a9", "#8d62a9"],
          ["#668bd7", "#668bd7"],
          ["#e1acff", "#e1acff"]]

colors_two = {
    "black":		["#2B303B", "#2B303B"],
    "grey":		["#40444D", "#424A5B"],
    "white":		["#C0C5CE", "#C0C5CE"],
    "red":		["#BF616A", "#BF616A"],
    "magenta":		["#B48EAD", "#B48EAD"],
    "green":		["#A3BE8C", "#A3BE8C"],
    "darkgreen":	["#859900", "#859900"],
    "blue":		["#8FA1B3", "#8FA1B3"],
    "darkblue":		["#65737E", "#65737E"],
    "orange":		["#EBCB8B", "#EBCB8B"]
}


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active = colors[3],
                    inactive = colors[2],
                    rounded = False,
                    highlight_method = "line",
                    highlight_color = colors[1],
                    this_current_screen_border = colors[3],
                    foreground = colors[2],
                    background = colors[0]
                ),
                widget.Sep(background=colors[0], foreground=colors[2], padding=10),
                widget.CurrentLayout(foreground=colors[2], background=colors[0]),
                widget.Sep(background=colors[0], foreground=colors[2], padding=10),
                widget.WindowName(foreground=colors[2], background=colors[0]),
                widget.Image(
                    scale = True,
                    filename = "~/.config/qtile/icons/bar06.png",
                    background = colors_two["red"]
                ),
                widget.Image(
                    scale = True,
                    filename = "~/.config/qtile/icons/bar02-b.png",
                    background = colors_two["red"]
                ),
                widget.TextBox(
                    font="Font Awesome 6 Free",
                    text="",
                    background = colors_two["red"],
                    foreground = colors_two["black"]
                ),
                widget.TextBox(
                    text="b34n5 ",
                    background = colors_two["red"],
                    foreground = colors_two["black"]
                ),
                widget.Image(
                    scale = True,
                    filename = "~/.config/qtile/icons/bar03.png",
                    background = colors_two["magenta"]
                ),
                widget.Clock(
                    foreground = colors_two["black"],
                    background = colors_two["magenta"],
                    format='%d-%m-%Y %a %H:%M %p'
                ),
                widget.Image(
                    scale = True,
                    filename = "~/.config/qtile/icons/bar04.png",
                    background = colors_two["green"]
                ),
		widget.PulseVolume(
		    foreground = colors_two["black"],
		    background = colors_two["green"],
                    limit_max_volume = True,
                    volume_app = "pamixer"
		),
                widget.Image(
        	    scale = True,
        	    filename = "~/.config/qtile/icons/bar05.png",
        	    background = colors_two["blue"]
        	),
                widget.Memory(
                    background = colors_two["blue"],
                    foreground = colors_two["black"]
                ),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# Hooks

@hook.subscribe.setgroup
def move_sticky_windows():
    for window in sticky_windows:
        window.togroup(qtile.current_group.name)

@hook.subscribe.client_killed
def remove_sticky_windows(window):
    if window in sticky_windows:
        sticky_windows.remove(window)

@hook.subscribe.client_managed
def auto_sticky_windows(window):
    info = window.info()
    if (info['wm_class'] == ['guvcview', 'guvcview']):
        sticky_windows.append(window)

@hook.subscribe.client_new
def floating_mpv(window):
    info = window.info()
    if (info['wm_class'] == ['gl', 'mpv']):
        window.toggle_floating()
        window.set_size_floating(1680, 1024)
        window.center()

@hook.subscribe.startup_once
def autostart():
    subprocess.Popen(["/usr/bin/python3", "/home/sergio/scripts/loop_wp.py"])
    subprocess.Popen(["/usr/bin/picom", "-b"])
