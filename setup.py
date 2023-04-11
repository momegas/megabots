from setuptools import setup, find_packages

setup(
    name="qnabot",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        # List your package's dependencies here, e.g.,
        # "numpy>=1.18",
    ],
    author="Megaklis Vasilakis",
    author_email="megaklis.vasilakis@gmail.com",
    description="Create a question answering over docs bot with one line of code.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/momegas/qnabot",
    classifiers=[
        # Choose appropriate classifiers from
        # https://pypi.org/classifiers/
        "Development Status :: 4 - Beta"
    ],
)
