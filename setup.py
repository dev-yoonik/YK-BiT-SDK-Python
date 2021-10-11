from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="yk_bit",
    version="0.0.0",
    description="Python SDK for the YooniK BiometricInThings API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="YooniK",
    author_email="tech@yoonik.me",
    url="https://github.com/dev-yoonik/YK-****-Python",
    license='MIT',
    packages=[
        "yk_bit",
        "yk_bit.models"
    ],
    install_requires=[
        "six",
        "requests",
        "setuptools"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
