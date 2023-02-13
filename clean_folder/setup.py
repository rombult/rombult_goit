from setuptools import setup, find_namespace_packages

setup(
    name='Clean Folder',
    version='1.0.0',
    description='Clean folder',
    author='Oleksandr Rombult',
    author_email='',
    license='MIT',
    url='',
    packages=find_namespace_packages(),
    include_package_data=True,
    entry_points={'console_scripts': [
        'clean-folder=clean_folder.sort_files:main']}
    )

        