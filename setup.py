from setuptools import setup

setup (
    name="PowerUpMoonRobot",

    version="0.1.0",

    packages=["moonrobot"],

    include_package_data=True,
    install_requires=[
        "pytest",
        "mock"
    ],
    
)