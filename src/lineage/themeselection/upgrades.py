# -*- coding: utf-8 -*-
from collective.lineage.interfaces import IChildSite
from lineage.themeselection.themingcontrolpanel import LineageSubsiteFacade
from plone.dexterity.interfaces import IDexterityFTI
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode

import logging


logger = logging.getLogger('lineage.themeselection upgrade')


def remove_behavior(context):
    """Remove the lineage.themeselection behavior from portal_types types.
    """
    key = 'lineage.themeselection.behaviors.IThemeSelection'
    types_tool = getToolByName(context, 'portal_types')
    for item in types_tool.values():
        if IDexterityFTI.providedBy(item):
            if key in getattr(item, 'behaviors', ''):
                item.behaviors = tuple(
                    it for it in types_tool.Folder.behaviors if it not in key
                )
                logger.info("Removed {0} from {1}".format(key, item.id))


def migrate_to_registry(context):
    """Remove all ``lineage_theme`` properties from IChildSite objects and
    migrate it to the plone.registry under the key
    ``lineage.themeselection.skin``.
    """
    cat = getToolByName(context, 'portal_catalog')
    items = cat.searchResults(object_provides=IChildSite.__identifier__)

    for it in items:
        ob = it.getObject()
        skin = getattr(ob, 'lineage_theme', None)
        if skin:
            skin = safe_unicode(skin)
            wrapped_site = LineageSubsiteFacade(ob)
            wrapped_site.default_skin = skin
            del ob.lineage_theme
            logger.info("Migrated skin setting {0} for {1}".format(
                skin, '/'.join(ob.getPhysicalPath()))
            )
