import flet as ft

from translation import gettext_lazy as _

AppBar = ft.AppBar(
    leading=ft.Icon(ft.icons.PALETTE),
    leading_width=40,
    title=ft.Text(_("AppBar Example")),
    center_title=False,
    bgcolor=ft.colors.BLUE_GREY_900,
    actions=[
        ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
        ft.IconButton(ft.icons.FILTER_3),
        ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text=_("Item 1")),
                ft.PopupMenuItem(),  # divider
                ft.PopupMenuItem(
                    text=_("Checked item"), checked=False,
                ),
            ]
        ),
    ],
)
