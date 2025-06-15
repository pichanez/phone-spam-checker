from typing import Iterable, cast

from .logging_config import configure_logging
from .registry import register_default_checkers, load_checker_module
from .config import settings


def initialize() -> None:
    """Configure logging and register available phone checkers."""
    configure_logging(
        level=settings.log_level,
        fmt=settings.log_format,
        log_file=settings.log_file,
        json_format=settings.log_json,
        max_bytes=settings.log_max_bytes,
        backup_count=settings.log_backup_count,
        remote_host=settings.log_remote_host or None,
        remote_port=int(settings.log_remote_port) if settings.log_remote_host else 0,
    )
    register_default_checkers()
    modules = cast(Iterable[str], filter(None, getattr(settings, "checker_modules", [])))
    for mod_name in modules:
        load_checker_module(str(mod_name))
