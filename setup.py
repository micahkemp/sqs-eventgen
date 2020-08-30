from setuptools import setup, find_packages

setup(
    name="sqsgen",
    packages=find_packages(),
    install_requires=[
        "boto3",
        "jinja2",
    ],
    include_package_data=True,
)
