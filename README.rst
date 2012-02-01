This package provides theme selection for Lineage subsites. 

In Plone we have ``plone.app.theming`` (aka Diazo theming) and the old CMF skins.
Both are almost independent. 

lineage.themeselection adds a `lineage.registry <http://pypi.python.org/pypi/lineage.themeselection>`_ 
local component containing the settings for the ``plone.app.theming`` based theme. 
An object tab appears for site-managers to configure the subsite theme.

Additionally it adds a schema-extender to the ChildSite Folder adding a CMFSkin 
selection dropown to the settings tab under edit.

On traversal skin is switched and a plone.browserlayer marker is put on the request.

Installation
============

* add the egg to your buildouts ``eggs``-section.
* apply the GS-profile to your Plone site.

Usage
=====

After installation click on edit at the child site folder and go to settings.
There you can select one of the installed skins.

Restrictions
============

The child site object has to be Archetypes based.

Installation
============

Just depend in your buildout on the egg ``lineage.themeselection``. ZCML is
loaded automagically with z3c.autoinclude.

Install it as an addon in Plone control-panel or portal_setup.

This package is written for Plone 4.1 or later.

Source Code and Contributions
=============================

If you want to help with the development (improvement, update, bug-fixing, ...)
of ``lineage.themeselection`` this is a great idea!

The code is located in the
`github collective <https://github.com/collective/lineage.themeselection>`_.

You can clone it or `get access to the github-collective
<http://collective.github.com/>`_ and work directly on the project.

Maintainer is Jens Klein and the BlueDynamics Alliance developer team. We
appreciate any contribution and if a release is needed to be done on pypi,
please just contact one of us
`dev@bluedynamics dot com <mailto:dev@bluedynamics.com>`_


Contributors
============

* Jens Klein <jens@bluedynamics.com>

* thanks to Maurits van Rees for showing with collective.editskinswitcher how
  this can be implemented and to the Weblion-team for the same with
  themetweaker.themeswitcher.

