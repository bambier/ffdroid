import flet as ft

from utils.translation import gettext_lazy as _


class BottomAppBar(ft.BottomAppBar):
    """Buttom navigation menu
    """

    def __init__(self, *args, **kwargs):
        super(BottomAppBar, self).__init__(*args, **kwargs)
        self.bgcolor = "#8F0FFF"
        self.shape = ft.NotchShape.CIRCULAR
        self.content = ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.icons.SEARCH,
                              icon_color=ft.colors.WHITE),
                ft.IconButton(icon=ft.icons.FAVORITE,
                              icon_color=ft.colors.RED),
            ]
        )
