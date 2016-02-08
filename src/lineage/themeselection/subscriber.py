# -*- coding: utf-8 -*-
from lineage.themeselection.interfaces import ILineageThemingLayer
from lineage.themeselection.themingcontrolpanel import LineageSubsiteFacade
from zope.component import queryUtility
from zope.interface import alsoProvides
from zope.interface import noLongerProvides
from zope.publisher.interfaces.browser import IBrowserSkinType


def set_theme_specific_layers(request, context, new_skin, current_skin):
    """mark the request with the browserlayer named new_skin
    and remove the one marked with current_skin

    we can't be sure plone.theme.layer.mark_layer is called after our traverser
    so we add the layer manually.
    """
    # check to see the skin has a IBrowserSkinType layer
    skin_iface = queryUtility(IBrowserSkinType, new_skin)
    if skin_iface:
        # remove theme specific layer of the current skin
        current_skin_iface = queryUtility(IBrowserSkinType, name=current_skin)

        if current_skin_iface is not None:
            noLongerProvides(request, current_skin_iface)

        # add the layer interface
        if skin_iface is not None and not skin_iface.providedBy(request):
            alsoProvides(request, skin_iface)


def apply_skin(obj, event):
    """Switch to the skin or theme selected for the child site.
    """
    if event.request.get('editskinswitched', False):
        # don't switch/set skin if collective.editskinswitcher has set
        # the edit skin already
        return

    alsoProvides(event.request, ILineageThemingLayer)
    wrapped_site = LineageSubsiteFacade(obj)
    skin = wrapped_site.default_skin
    if not skin:
        return
    current_skin = obj.getCurrentSkinName()
    obj.changeSkin(skin, event.request)
    set_theme_specific_layers(event.request, obj, skin, current_skin)
