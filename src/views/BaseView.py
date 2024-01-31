import flet as ft

from utils.logger import logger
from utils.translation import get_current_language, set_current_language
import os
import sys


class BaseView(ft.View):
    page: ft.Page

    def __init__(self, page: ft.Page, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.page = page

    def chlang(self, event: ft.ControlEvent, lang=None, *args, **kwargs) -> None:
        clang = get_current_language()
        if lang is not None:
            set_current_language(page=self.page, lang=lang)
        else:
            match clang:
                case "en":
                    logger.debug("")
                    set_current_language(page=self.page, lang="fa")
                case "fa":
                    set_current_language(page=self.page, lang="en")
                case _:
                    logger.error(f"Error in changing language {clang} --> en")
                    set_current_language(page=self.page, lang="en")
            self.restart_app()

    @classmethod
    def __repr__(cls):
        return str(f'<{cls.name}View route="{cls.route}" lang="{get_current_language()}">')

    @classmethod
    def __str__(cls):
        return str(cls.__class__.__name__)

    @property
    def name(self) -> str:
        return str(self.__class__.__name__[:-4])

    def restart_app(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)
