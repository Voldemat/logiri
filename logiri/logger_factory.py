from __future__ import annotations

import logging
from typing import IO


class LoggerFactory:
    def __init__(
        self,
        formatter: logging.Formatter,
        prefix: str,
        level: str,
        stream: IO[str],
    ) -> None:
        self.prefix = prefix
        self.level = level
        self.stream = stream
        self.formatter = formatter

    def build(
        self,
        name: str,
        level: str | None = None,
        stream: IO[str] | None = None,
    ) -> logging.Logger:
        if level is None:
            level = self.level
        if stream is None:
            stream = self.stream
        logger = logging.getLogger(self.build_logger_fullname(name))
        logger.propagate = False
        logger.setLevel(level)
        logger.addHandler(self.build_stream_handler(level, stream))
        return logger

    def build_stream_handler(
        self, level: str, stream: IO[str]
    ) -> logging.StreamHandler:  # type: ignore [type-arg]
        handler = logging.StreamHandler(stream)
        handler.setLevel(level)
        handler.setFormatter(self.formatter)
        return handler

    def build_logger_fullname(self, name: str) -> str:
        return self.prefix + name

    def create_subfactory(
        self,
        prefix: str,
        formatter: logging.Formatter | None = None,
        level: str | None = None,
        stream: IO[str] | None = None,
    ) -> LoggerFactory:
        if formatter is None:
            formatter = self.formatter
        if level is None:
            level = self.level
        if stream is None:
            stream = self.stream
        return LoggerFactory(
            formatter=formatter,
            prefix=prefix,
            level=level,
            stream=stream,
        )
