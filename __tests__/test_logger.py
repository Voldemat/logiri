import io
import logging
import re
import sys

from logiri import LoggerFactory


def test_logger() -> None:
    factory = LoggerFactory(
        formatter=logging.Formatter(
            "[%(asctime)s][%(levelname)s][%(name)s] %(message)s"
        ),
        prefix="",
        level="DEBUG",
        stream=sys.stderr,
    )
    stream = io.StringIO()
    logger = factory.build("main", stream=stream)
    logger.info("Something")
    assert stream.tell() != 0, "Stream is empty"
    stream.seek(0)
    line = stream.readline()
    assert re.match(
        r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3,}\]"
        r"\[INFO\]\[main\] Something",
        line,
    ), line


def test_sublogger() -> None:
    factory = LoggerFactory(
        formatter=logging.Formatter(
            "[%(asctime)s][%(levelname)s][%(name)s] %(message)s"
        ),
        level="DEBUG",
        stream=sys.stderr,
        prefix="",
    )
    stream = io.StringIO()
    sub_factory = factory.create_subfactory(prefix="module.")
    logger = sub_factory.build("main", stream=stream)
    logger.info("Something")
    assert stream.tell() != 0, "Stream is empty"
    stream.seek(0)
    line = stream.readline()
    assert re.match(
        r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3,}\]"
        r"\[INFO\]\[module\.main\] Something",
        line,
    ), line
