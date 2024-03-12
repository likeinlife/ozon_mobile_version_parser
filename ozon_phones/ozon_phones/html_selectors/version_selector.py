from .mobile_type import MobileType


def system_version_selector(response) -> str | None:
    android = response.xpath(f'//*[dt[span[text() = "Версия {MobileType.ANDROID}"]]]/dd/text()')
    ios = response.xpath(f'//*[dt[span[text() = "Версия {MobileType.IOS}"]]]/dd/text()')
    return android.get() or ios.get()
