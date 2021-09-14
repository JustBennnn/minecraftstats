from setuptools import setup

setup(
    name="minecraftstats",
    version="1.0.2",
    author="JustBen",
    author_email="justben009@gmail.com",
    description="A python library allowing the user to get stats from Hypixel in Minecraft.",
    keywords="minecraft api-wrapper".split(),
    python_requires=">=3.7",
    packages=["minecraftstats"],
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JustBennnn/minecraftstats",
    project_urls={
        "Issue Tracker": "https://github.com/JustBennnn/minecraftstats/issues",
    },
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)