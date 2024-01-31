import flet as ft
from utils.logger import logger
from utils.translation import gettext_lazy as _


class AppBar(ft.AppBar):

    def __init__(self, page: ft.Page, *args, **kwargs):
        super(AppBar, self).__init__(*args, **kwargs)
        # self.page = page
        self.leading = ft.Icon(ft.icons.PALETTE)
        self.leading_width = 40
        self.title = ft.Text(_("AppBar Example"), color=ft.colors.WHITE)
        self.center_title = False
        self.bgcolor = ft.colors.BLUE_GREY_900
        self.actions = [
            ft.IconButton(
                ft.icons.WB_SUNNY_OUTLINED,
                icon_color=ft.colors.WHITE,
                on_click=self.go_to_route
            ),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text=_("Item 1")),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text=_("Checked item"), checked=False,
                    ),
                ],
                tooltip=_("Checked item")
            ),
        ]

    def go_to_route(self, evnet, *args, **kwargs):
        logger.debug("Click button to go to /loging")
        self.page.go("/login")
