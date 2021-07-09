def line(tam=42):
    return "-" * tam


def highlight(txt, color="", tam=42):
    print(f"\n#{'-'*tam}#\n {(color + txt + color_reset()).center(tam)}\n#{'-'*tam}#")


def color_reset():
    return "\033[0;0m"


def color_red():
    return "\033[31m"


def color_green():
    return "\033[32m"


def color_yellow():
    return "\033[33m"


def color_blue():
    return "\033[34m"
