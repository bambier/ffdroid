#! /usr/bin/env python3
from gettext import gettext as _
from os import listdir
from pathlib import Path

import flet as ft

# Codes

BASE_DIR = Path().parent


class Application:
    title = _("My App")

    def __init__(self, page: ft.Page) -> None:
        """Initilizing application in class
        """
        self.page = page
        self.update = self.page.update
        self.page.window_width = 420
        self.page.window_height = 840
        self.page.window_bgcolor = "#8e4dee"
        self.lang = "en"

        self.page.title = self.title
        self.get_views()

        self.update()

    def get_views(self):
        self.page.views.pop()
        self.page.views.clear()
        views_files = filter(lambda x:
                             x.endswith("View.py") and x != "BaseView.py",
                             listdir(BASE_DIR / "views"))
        import importlib

        for view in views_files:
            view = view.replace(".py", "")
            module = importlib.import_module(f"views.{view}")
            view_class = getattr(module, view)
            self.page.views.append(view_class(page=self.page).view)

        self.update()


if __name__ == "__main__":
    ft.app(Application)
