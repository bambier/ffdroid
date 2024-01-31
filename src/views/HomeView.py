import flet as ft

from components.AppBar import AppBar
from components.BottomAppBar import BottomAppBar
from utils.logger import logger
from utils.translation import gettext_lazy as _
from views.BaseView import BaseView

# Code


class HomeView(BaseView):
    route = "/"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.bottom_appbar = BottomAppBar()
        self.appbar = AppBar(page=self.page)

        self.controls.append(
            ft.OutlinedButton(text=_("Hello"), on_click=self.chlang)
        )
