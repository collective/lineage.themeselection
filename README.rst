This package provides theme selection for Lineage subsites. It adds a
schema-extender and a subscriber to the before traverse event for theme
switching, both on the ``IChildSite``.

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

Source Code
===========

The sources are in a GIT DVCS with its main branches at
`github <http://github.com/collective/lineage.themeselection>`_.

We'd be happy to see many pushes, forks and pull-requests to make it better.

Contributors
============

* Jens Klein <jens@bluedynamics.com>

* thanks to Maurits van Rees for showing with collective.editskinswitcher how
  this can be implemented and to the Weblion-team for the same with
  themetweaker.themeswitcher.

License
=======

GPL 2

Changes
=======

1.1
---

- added manifest file [jensens]

- cleanup [thet]

1.0
---

* Make it work. [jensens, 2011-06-06]
