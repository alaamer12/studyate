from setuptools import setup, find_packages

extras_require = {
    'ai': ['torch', 'transformers', 'sentencepiece', 'sacremoses'],
}

setup(
    name="studyate",
    version="0.0.1",
    author="alaamer",
    author_email="",
    description="",
    long_description="",
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['typer', 'tqdm', 'art', 'rich'],
    extras_require=extras_require,
)
