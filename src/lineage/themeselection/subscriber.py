from lineage.themeselection.interfaces import ILineageThemingLayer
from zope.interface import alsoProvides
from zope.interface import Interface

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


def apply_theme(obj, event):
    """Switch to the skin or theme selected for the child site.
    """
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
    obj.changeSkin(theme, event.request)
