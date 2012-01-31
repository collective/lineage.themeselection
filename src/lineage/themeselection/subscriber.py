from zope.interface import alsoProvides
from .interfaces import ILineageThemingLayer
 
def apply_theme(obj, event):
    """Switch to the skin or theme selected for the child site.
    """
    # this works:
    alsoProvides(event.request, ILineageThemingLayer)
    #return
    field = obj.Schema().get('lineage_theme', None)
    if field is None:
        return
    theme = field.get(obj)
    if not theme:
        return
    obj.changeSkin(theme, event.request)
    
    
