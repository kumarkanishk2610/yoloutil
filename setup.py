from setuptools import setup, find_packages

setup(
    name='yoloutil',
    version='0.1',
    description='Utilities for running YOLO models',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/username/yoloutil',  # Replace with your GitHub URL
    packages=find_packages(),  # This automatically finds the yoloutil package
    install_requires=[
        'matplotlib',
        'opencv-python',
        # List any other dependencies
    ],
)
