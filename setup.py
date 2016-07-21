from setuptools import setup
from pip.req import parse_requirements


setup(
    name='subscriber',
    version='1.0',
    description='Async redis subscriber for some channel',
    url='https://github.com/AHAPX/subscriber',
    author='anarchy',
    author_email='anarchy.b@gmail.com',
    license='MIT',
    keywords='redis subscribe async',
    packages=['subscriber'],
    package_dir={'subscriber': 'src'},
    install_requires=[
        'asyncio',
        'asyncio_redis',
    ],
)
