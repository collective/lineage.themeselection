from Products.Five import BrowserView
from collective.lineage.interfaces import IChildSite

class ActionAvailableView(BrowserView):
    
    def __call__(self):
        return IChildSite.providedBy(self.context)