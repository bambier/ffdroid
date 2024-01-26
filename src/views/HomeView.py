import flet as ft

from components.AppBar import AppBar
from components.BottomAppBar import BottomAppBar
from translation import gettext_lazy as _
from views.BaseView import BaseView

# Code


class HomeView(BaseView):

    def __init__(self, *args, **kwargs) -> None:
        super(HomeView, self).__init__(*args, **kwargs)

        self.view = ft.View(
            route="/",
            controls=[
                ft.OutlinedButton(text=_("Hello"), on_click=self.chlang)
            ],
            bottom_appbar=BottomAppBar,
            appbar=AppBar
        )
