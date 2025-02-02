# created by santhu
# created on: 2-2-2025

import os
import importlib
from rich.console import Console
from rich.table import Table
from userbot.logger import LOGGER

console = Console()

MODULES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ""))

def load_modules():
    if not os.path.exists(MODULES_DIR):
        LOGGER.error(f"Modules directory not found: {MODULES_DIR}")
        raise FileNotFoundError(f"Modules directory not found: {MODULES_DIR}")
    LOGGER.info("Loading modules...")
    table = Table(title="Loaded Modules", show_lines=True)
    table.add_column("Sno", justify="right", style="bold cyan")
    table.add_column("Module Name", justify="left", style="bold green")
    table.add_column("Status", justify="center", style="bold magenta")

    module_count = 1

    for filename in os.listdir(MODULES_DIR):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"userbot.modules.{filename[:-3]}"
            try:
                importlib.import_module(module_name)
                LOGGER.info(f"Successfully loaded module: {module_name}")
                table.add_row(str(module_count), filename, "✅ Loaded")
                module_count += 1
            except Exception as e:
                LOGGER.error(f"Failed to load module {module_name}: {e}")
                table.add_row(str(module_count), filename, f"❌ Failed: {e}")
                module_count += 1
    
    console.print(table) 
load_modules()