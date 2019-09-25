from setuptools import setup, find_packages

setup(
    name='awsc',
    version='0.2',
    packages=['awsc', 'awsc.cmds'],
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
