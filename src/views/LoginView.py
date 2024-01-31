import flet as ft

from utils.logger import logger
from utils.translation import gettext_lazy as _
from views.BaseView import BaseView

# Code


class LoginView(BaseView):
    route = "/login"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.controls.append(
            ft.Container(
                ft.OutlinedButton(text=_("Hello"), on_click=self.chlang)
            )
        )
