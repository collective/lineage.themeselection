# -*- coding: utf-8 -*-
from collective.lineage.interfaces import IChildSite
from Products.Five import BrowserView


class ActionAvailableView(BrowserView):

    def __call__(self):
        return IChildSite.providedBy(self.context)
