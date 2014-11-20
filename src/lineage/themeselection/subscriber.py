from lineage.themeselection.interfaces import ILineageThemingLayer
from zope.component import queryUtility
from zope.interface import alsoProvides
from zope.interface import noLongerProvides
from zope.interface import Interface
from zope.publisher.interfaces.browser import IBrowserSkinType


try:
    from Products.Archetypes.interfaces import IBaseObject
except ImportError:
    class IBaseObject(Interface):
        pass
try:
    from plone.dexterity.interfaces import IDexterityContent
except ImportError:
    class IDexterityContent(Interface):
        pass


def set_theme_specific_layers(request, context, new_skin, current_skin):
    """mark the request with the browserlayer named new_skin
    and remove the one marked with current_skin

    we can't be sure plone.theme.layer.mark_layer is called after our traverser
    so we add the layer manually.
    """

    # remove theme specific layer of the current skin
    current_skin_iface = queryUtility(IBrowserSkinType, name=current_skin)
    if current_skin_iface is not None:
        noLongerProvides(request, current_skin_iface)
    # check to see the skin has a BrowserSkinType and add it.
    skin_iface = queryUtility(IBrowserSkinType, new_skin)
    if skin_iface is not None and not skin_iface.providedBy(request):
        alsoProvides(request, skin_iface)


def apply_theme(obj, event):
    """Switch to the skin or theme selected for the child site.
    """

    if event.request.get('editskinswitched', 'None'):
        # don't switch/set skin if collective.editskinswitcher has set
        # the edit skin already
        return

    alsoProvides(event.request, ILineageThemingLayer)
    theme = None
    if IBaseObject.providedBy(obj):
        field = obj.Schema().get('lineage_theme', None)
        if field is None:
            return
        theme = field.get(obj)
    elif IDexterityContent.providedBy(obj):
        theme = getattr(obj, 'lineage_theme', None)
    if not theme:
        return
    current_skin = obj.getCurrentSkinName()
    obj.changeSkin(theme, event.request)
    set_theme_specific_layers(event.request, obj, theme,
                              current_skin)
