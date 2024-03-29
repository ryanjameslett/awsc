from setuptools import setup, find_packages

setup(
    name='awsc',
    version='0.3',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'awsc = awsc.cmds:cli'
        ]
    }
)
