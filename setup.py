from setuptools import setup, find_packages
import sys, os

version = '1.2'
shortdesc ="Lineage Addon: Theme Selection on Subsites"
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'HISTORY.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()

setup(name='lineage.themeselection',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Web Environment',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python', 
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Framework :: Plone :: 4.1',
            'Framework :: Plone :: 4.2',
      ],
      keywords='',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      url=u'https://github.com/collective/lineage.themeselection',
      license='GNU General Public Licence',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['lineage',],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.lineage',
          'lineage.registry',
          'archetypes.schemaextender',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
