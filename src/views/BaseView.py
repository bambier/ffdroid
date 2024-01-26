from flet import Page, View

from translation import change_language, get_current_language
from translation import gettext_lazy as _


class BaseView:
    view: View

    def __init__(self, *args, **kwargs) -> None:
        self.page: Page = kwargs["page"]

    def chlang(self, *args, **kwargs) -> None:
        clang = get_current_language()
        match clang:
            case "en":
                print("en --> fa")
                change_language("fa")
                self.page.rtl = True
            case "fa":
                print("fa --> en")
                change_language("en")
                self.page.rtl = False
            case _:
                print(f"Error language {clang} --> en")
                change_language("en")
                self.page.rtl = False

        self.page.update()
