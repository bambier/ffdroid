import flet as ft

from translation import gettext_lazy as _

BottomAppBar = ft.BottomAppBar(
    bgcolor=ft.colors.INDIGO_500,
    shape=ft.NotchShape.CIRCULAR,
    content=ft.Row(
        controls=[
            ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),
            ft.Container(expand=True),
            ft.IconButton(icon=ft.icons.SEARCH,
                          icon_color=ft.colors.WHITE),
            ft.IconButton(icon=ft.icons.FAVORITE,
                          icon_color=ft.colors.WHITE),
        ]
    ),
)
