# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup


version = '2.0'
short_description = u"Lineage Add-On: Theme Selection on Subsites"
long_description = u'\n\n'.join([
    open('README.rst').read(),
    open('CHANGES.rst').read(),
    open('LICENSE.rst').read(),
])


setup(
    name='lineage.themeselection',
    version=version,
    description=short_description,
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Framework :: Plone :: 4.1',
        'Framework :: Plone :: 4.2',
        'Framework :: Plone :: 4.3',
    ],
    keywords='',
    author='BlueDynamics Alliance',
    author_email='dev@bluedynamics.com',
    url=u'https://github.com/collective/lineage.themeselection',
    license='GNU General Public Licence',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['lineage', ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'collective.lineage',
        'lineage.registry',
        'plone.app.theming',  # for plone 4.2
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
