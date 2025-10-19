from pathlib import Path
from colorama import Fore, Style, init

dir_folder = Path("/Users/elizabethsheremet/python/python_guide")


def tree(path, prefix=""):
    items = list(path.iterdir())  
    count = len(items)


    for index, item in enumerate(items):
        connector = "└──" if index == count - 1 else "├──"
        color = Fore.BLUE if item.is_dir() else Fore.GREEN
        icon = "📂" if item.is_dir() else "📄"

        print(prefix + connector + icon + color + item.name + Fore.RESET)

        if item.is_dir():
            next_prefix = "    " if index == count - 1 else "│   "
            tree(item, prefix + next_prefix)

# tree(Path("/Users/elizabethsheremet/python/python_guide/files"))

tree(dir_folder)
