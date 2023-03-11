import os
from pathlib import Path

from setuptools import setup  # type: ignore [import]


setup(
    name="logiri",
    version=os.environ["GITHUB_REF_NAME"],
    description="Package for logging",
    author="Vladimir Vojtenko",
    author_email="vladimirdev635@gmail.com",
    license="MIT",
    packages=["logiri"],
    package_data={"logiri": ["py.typed"]},
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
)
