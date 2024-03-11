def android_version_selector(response) -> str | None:
    android = response.xpath('//*[span[text() = "Версия Android"]]/dd/text()')
    return android.get()
