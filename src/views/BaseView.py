from flet import Container, Page, View

from utils.translation import get_current_language
from utils.translation import gettext_lazy as _
from utils.translation import set_current_language


class BaseView(Container):
    view: View
    name: str
    route: str

    def __init__(self, page: Page, *args, **kwargs) -> None:
        super(Container, self).__init__(*args, **kwargs)
        self.expand = True
        self.page = page
        self.name = self.__class__.__name__[:-4]

    def chlang(self, *args, **kwargs) -> None:
        clang = get_current_language()
        match clang:
            case "en":
                print("en --> fa")
                set_current_language(page=self.page, lang="fa")
            case "fa":
                print("fa --> en")
                set_current_language(page=self.page, lang="en")
            case _:
                print(f"Error language {clang} --> en")
                set_current_language(page=self.page, lang="en")

        self.page.update()
