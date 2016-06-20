
History
=======


2.0 (2016-06-20)
----------------

.. warning:: Upgrade Warning!
    After installing this release, you need to run the provided upgrade steps.

New:

- Set the childsite skin on a ``lineage.registry`` based local registry instead of an ``lineage_theme`` attribute on an ``IChildSite`` object.
  Includes an upgrade step.
  [thet]

- Allow setting of ``lineage_theme`` skin setting through the ``@@theming-controlpanel`` and remove the customized controlpanel template, Archetypes schemaextender and Dexterity behavior.
  This works for ``plone.app.theming`` ``1.1.x`` and ``1.2.x``.
  Includes an upgrade step.
  [thet]

Fixes:

- Install ``lineage.registry`` when installing this addon.
  [thet]


1.4.1 (2016-02-08)
------------------

Fixes:

- Only remove the current ``IBrowserSkinType`` browser layer and add the new one, if a new one can be found.
  [thet]

- Fix a bug in the ``apply_theme`` event subscriber, which prevented it from correctly set the skin.
  [thet]


1.4 (2014-11-20)
----------------

- Also set the browserlayer registered under the skin name if it exists and
  remove the one set by the "old" skin.
  [fRiSi]

- Play well with collective.editskinswitcher. If edit skin is active, do
  not set/activate any other skin. This allows to use a specific skin (eg.
  Sunburst) for CMS-mode even for Subsites which define a different theme.
  [fRiSi]

- Add support for Dexterity.
  [thet]


1.3 (2013-12-04)
----------------

- Add GenericSetup config to properly register the Browser Layer.
  [thet. 2013-10-15]

- Let lineage.themeselection work with Plone 4.3, where plone.app.theming has a
  combined Diazo and Skins control panel. Setting the skin through this
  controlpanel doesn't work at the moment, so these settings are hidden for
  now. Please set the skin in the settings tab of the @@edit page of the
  lineage subsite.
  [thet, 2013-10-14]


1.2
---

- added Diazo Theme Support
  [jensens, 2012-01-01]


1.1
---

- added manifest file [jensens]

- cleanup [thet]


1.0
---

* Make it work. [jensens, 2011-06-06]
