from setuptools import setup

setup(
    name="emu",
    version="0.2",
    py_modules=["emu_cli", "helper"],
    install_requires=["Click==7.1.2"],
    entry_points="""
        [console_scripts]
        emu=emu_cli:cli
    """,
)
