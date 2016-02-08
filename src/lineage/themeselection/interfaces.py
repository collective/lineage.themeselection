# -*- coding: utf-8 -*-
from plone.app.theming.interfaces import IThemingLayer
from zope import schema
from zope.interface import Interface


REG_KEY_PREFIX = 'lineage.themeselection'


class ILineageThemingLayer(IThemingLayer):
    """Layer indicates that a Lineage Subsite is active"""


class ILineageThemeSelectionSettings(Interface):
    """Theme/Skin settings for Lineage Subsites.
    """
    skin = schema.TextLine(title=u"The skin name for this subsite")
