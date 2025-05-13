# ~/Documents/lms-bench/apps/lms/setup.py
from setuptools import setup, find_packages

setup(
    name="lms",
    version="0.0.1",
    description="Library Management System",
    author="boora",
    author_email="800raaman@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Keep this empty if you don't have specific dependencies
        # Frappe is already managed by your bench environment
    ],
)
