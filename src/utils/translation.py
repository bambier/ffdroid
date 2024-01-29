import gettext
import locale
from pathlib import Path

from flet import Page

from utils.dtypes import LanguagesType

# Codes


BASE_DIR = Path().parent
DOMAIN = "base"
LOCALE_DIR = BASE_DIR / 'locales'


supported_languages = ['fa', 'en']


gettext.bindtextdomain(domain=DOMAIN, localedir=LOCALE_DIR)
gettext.textdomain(domain=DOMAIN)


languages: LanguagesType = {}


for lang in supported_languages:
    translation = gettext.translation(
        domain=DOMAIN,  localedir=LOCALE_DIR, languages=[lang], fallback=True,)
    translation.install(names=['gettext', 'ngettext', 'npgettext', 'pgettext'])
    languages.update({lang: translation})


def set_current_language(page: Page, lang: str = "en") -> None:
    match lang:
        case "en":
            locale.setlocale(category=locale.LC_ALL, locale="en_US.UTF-8")
            page.client_storage.set("lang", "en")
            page.rtl = False
        case "fa":
            locale.setlocale(category=locale.LC_ALL, locale="fa_IR.UTF-8")
            page.client_storage.set("lang", "fa")
            page.rtl = True
        case _:
            locale.setlocale(category=locale.LC_ALL, locale="en_US.UTF-8")
            page.client_storage.set("lang", "en")
            page.rtl = False
            raise Exception(
                "Language is not supported.\n\tSetting language to default en_US.")

    languages[lang].install()


def get_current_language() -> str:
    return locale.getlocale()[0][:2]


def gettext_lazy(message: str) -> str:
    lang = get_current_language()
    _ = languages.get(lang, "en").gettext
    return _(message)
