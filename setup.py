from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
        name='hr',
        version='1.0.0',
        author='David Gnamus',
        author_email='david.gnamus@protonmail.com',
        description='Tool for exporting user information in CSV or JSON',
        long_description=readme,
        long_description_content_type='text/markdown',
        url='https://github.com/dgnamus/hr',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        install_requires=[],
        python_requires='>=3.7',
        entry_points={
            'console_scripts': 'hr=hr.cli:main',
            }

    )
