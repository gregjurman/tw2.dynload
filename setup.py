from setuptools import setup, find_packages

# Ridiculous as it may seem, we need to import multiprocessing and
# logging here in order to get tests to pass smoothly on python 2.7.
# Thanks RJ!
import multiprocessing
import logging

setup(
    name='tw2.dynload',
    version='2.0b1',
    description='Allow loading of TW2 widgets into already loaded DOM.',
    author='Greg Jurman',
    author_email='gdj2214@rit.edu',
    url='https://github.com/gregjurman/tw2.dynload',
    install_requires=[
        "tw2.core",
        "tw2.jquery",
        ## Add other requirements here
        "mako",
        ],
    packages=find_packages(exclude=['ez_setup', 'tests']),
    namespace_packages = ['tw2'],
    zip_safe=False,
    include_package_data=True,
    test_suite = 'nose.collector',
    tests_require = [
        'nose',
        'BeautifulSoup',
        'Genshi',
        'mako',
        # formencode isn't actually needed, but is just here to patch up
        'tw2.forms',
        'tw2.dyntext',
        'formencode',
        'strainer',
        'WebTest'
    ],
    entry_points="""
        [tw2.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        widgets = tw2.dynload
    """,
    keywords = [
        'toscawidgets.widgets',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
