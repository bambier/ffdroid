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

        self.set_theme()

        set_current_language(
            lang=self.page.client_storage.get("lang") or "en",
            page=self.page,
        )

        self.page.title = _("My App")

        self.page.on_route_change = self.on_route_change
        self.get_views()
        self.page.go("/")

        self.update()

    def get_views(self) -> None:
        """Get views dynamically and put them in `page.views`
        """
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

            self.pages_list.update({
                view_class.route:
                    view_class(page=self.page, route=view_class.route)
            })

    def set_theme(self) -> None:
        """Set theme, page size and define fonts
        """
        self.page.fonts = {
            "Vazirmatn-Thin": "assets/fonts/Vazirmatn/Vazirmatn-RD-UI-Thin.ttf",
            "Vazirmatn-SemiBold": "assets/fonts/Vazirmatn/Vazirmatn-RD-UI-SemiBold.ttf",
            "Vazirmatn-Regular": "assets/fonts/Vazirmatn/Vazirmatn-RD-UI-Regular.ttf",
            "Vazirmatn-Medium": "assets/fonts/Vazirmatn/Vazirmatn-RD-UI-Medium.ttf",
            "Vazirmatn-Light": "assets/fonts/Vazirmatn/Vazirmatn-RD-UI-Light.ttf",
            "Vazirmatn-ExtraLight": "assets/fonts/Vazirmatn/Vazirmatn-RD-UI-ExtraLight.ttf",
            "Vazirmatn-ExtraBold": "assets/fonts/Vazirmatn/Vazirmatn-RD-UI-ExtraBold.ttf",
            "Vazirmatn-Bold": "assets/fonts/Vazirmatn/Vazirmatn-RD-UI-Bold.ttf",
            "Vazirmatn-Black": "assets/fonts/Vazirmatn/Vazirmatn-RD-UI-Black.ttf",
        }
        self.page.theme = ft.Theme(
            font_family="Vazirmatn-Regular",
            use_material3=True,
        )

        self.page.window_width = 420
        self.page.window_height = 840

        self.page.padding = 0

        self.page.theme_mode = "light"
        self.page.window_bgcolor = ft.colors.WHITE

    def on_route_change(self, event: ft.RouteChangeEvent, *args, **kwargs):
        """Gets new route and changes page to given route
        """
        logger.debug("Changing route to %s" % event.route)
        self.page.views.clear()
        view: BaseView = self.pages_list.get(event.route)
        self.page.views.append(view)
        self.update()


if __name__ == "__main__":
    ft.app(
        target=Application,
        view=ft.AppView.FLET_APP,
        assets_dir=BASE_DIR / "assets",
        use_color_emoji=True
    )
