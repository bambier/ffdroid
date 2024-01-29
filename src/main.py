#! /usr/bin/env python3
from os import listdir
from pathlib import Path

import flet as ft

from utils.translation import set_current_language, gettext_lazy as _
from views.BaseView import BaseView


# Codes

BASE_DIR = Path().parent


class Application(ft.Control):
    title = _("My App")

    def __init__(self, page: ft.Page, *args, **kwargs) -> None:
        super(ft.Control, self).__init__(*args, **kwargs)
        self.page = page
        print(self.page.fonts)
        self.update = self.page.update
        self.page.window_width = 420
        self.page.window_height = 840
        self.page.theme_mode = "light"
        self.page.window_bgcolor = "#8e4dee"
        set_current_language(
            lang=self.page.client_storage.get("lang") or "en",
            page=self.page)

        self.pages_list = {}

        self.page.title = self.title
        self.get_views_dynamic()

        self.update()

    def get_views_static(self):
        self.page.views.clear()
        pass

    def get_views_dynamic(self):
        self.page.views.clear()
        views_files = filter(lambda x:
                             x.endswith("View.py") and x != "BaseView.py",
                             listdir(BASE_DIR / "views"))
        self.page.on_route_change = self.on_route_change

        import importlib

        for view in views_files:
            view = view.replace(".py", "")
            module = importlib.import_module(f"views.{view}")
            view_class: BaseView = getattr(module, view)
            self.pages_list.update({view_class.route: view_class})

        self.page.go("/")

    def on_route_change(self, route):
        self.page.views.clear()
        page = self.pages_list[self.page.route](page=self.page)
        self.page.views.append(page.view)
        self.update()


if __name__ == "__main__":
    ft.app(target=Application, name=Application.title,
           view=ft.AppView.FLET_APP, assets_dir=BASE_DIR / "assets", use_color_emoji=True)
