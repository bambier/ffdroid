#! /usr/bin/env python3
from os import listdir
from pathlib import Path

import flet as ft

from utils.logger import logger
from utils.translation import gettext_lazy as _
from utils.translation import set_current_language
from views.BaseView import BaseView

# Codes


BASE_DIR = Path().parent


class Application(ft.Control):

    def __init__(self, page: ft.Page, *args, **kwargs) -> None:
        logger.info(
            "-----------------Starting Application-----------------")
        super(ft.Control, self).__init__(*args, **kwargs)

        self.page = page
        self.update = self.page.update

        self.page.window_width = 420
        self.page.window_height = 840

        self.page.theme_mode = "light"
        self.page.window_bgcolor = ft.colors.WHITE

        set_current_language(
            lang=self.page.client_storage.get("lang") or "en",
            page=self.page)

        self.page.title = _("My App")

        self.get_views()
        self.page.on_route_change = self.on_route_change
        self.page.go("/")

        self.update()

    def get_views(self):
        self.page.views.clear()
        views_names = filter(lambda x:
                             x.endswith("View.py") and x != "BaseView.py",
                             listdir(BASE_DIR / "views"))

        import importlib
        self.pages_list = {}
        for view_name in views_names:
            view_name = view_name.replace(".py", "")

            module = importlib.import_module(f"views.{view_name}")
            view_class: BaseView = getattr(module, view_name)

            self.page.views.append(
                view_class(page=self.page, route=view_class.route),
            )

        self.update()

    def on_route_change(self, event: ft.RouteChangeEvent, *args, **kwargs):
        self.page.views.clear()
        self.get_views()
        self.update()


if __name__ == "__main__":
    ft.app(
        target=Application,
        view=ft.AppView.FLET_APP,
        assets_dir=BASE_DIR / "assets",
        use_color_emoji=True
    )
