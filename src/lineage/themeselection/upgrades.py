# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from plone.dexterity.interfaces import IDexterityFTI

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
