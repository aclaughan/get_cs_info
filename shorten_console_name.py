import logging


# logging.basicConfig(level=logging.INFO, filename="app.log")


def shorten_console_name(long_name: str) -> str:
    short_name = long_name.replace("RP0_console0", "c0")
    short_name = short_name.replace("RP1_console0", "c1")
    short_name = short_name.replace("RSP0_console0", "c0")
    short_name = short_name.replace("RSP1_console0", "c1")

    logging.info(f"shortened {long_name} to {short_name}")

    return short_name


if __name__ == '__main__':
    shorten_console_name("za-wc-cpt-asw-2-RP0_console0")
