from setuptools import setup, find_packages
import sys, os

version = '1.1'
shortdesc ="Theme Selection on Lineage Subsites"
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(name='lineage.themeselection',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python', 
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',        
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
          'archetypes.schemaextender',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
