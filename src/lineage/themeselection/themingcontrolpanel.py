# -*- coding: utf-8 -*-
from collective.lineage.interfaces import IChildSite
from collective.lineage.utils import parent_site
from lineage.themeselection.interfaces import ILineageThemeSelectionSettings
from lineage.themeselection.interfaces import REG_KEY_PREFIX
from plone.app.layout.viewlets.common import ViewletBase
from plone.app.theming.browser.controlpanel import ThemingControlpanel
from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces import IPloneSiteRoot
from zope.component import getUtility


class LineageSubsiteFacade(object):

    def __init__(self, subsite):
        self.subsite = subsite

    # plone.app.theming >= 1.2

    @property
    def default_skin(self):
        registry = getUtility(IRegistry, context=self.subsite)
        settings = registry.forInterface(
            ILineageThemeSelectionSettings, check=False, prefix=REG_KEY_PREFIX
        )
        return settings.skin

    @default_skin.setter
    def default_skin(self, value):
        registry = getUtility(IRegistry, context=self.subsite)
        try:
            registry.records['{0}.skin'.format(REG_KEY_PREFIX)]
        except KeyError:
            registry.registerInterface(
                interface=ILineageThemeSelectionSettings, prefix=REG_KEY_PREFIX
            )
        finally:
            settings = registry.forInterface(
                ILineageThemeSelectionSettings, prefix=REG_KEY_PREFIX
            )
            settings.skin = value

    def getDefaultSkin(self):
        parent = parent_site()
        parent_skin = None
        if IChildSite.providedBy(parent):
            # Wrap with this class to use this convenient API
            parent_wrapped = LineageSubsiteFacade(parent)
            parent_skin = getattr(parent_wrapped, 'default_skin', None)
            if not parent_skin:
                # This one eventually iterates up to where no getDefaultSkin is
                # defined on parent anymore... (e.g. the IPloneSiteRoot)
                parent_skin = getattr(parent_wrapped, 'getDefaultSkin', None)
        elif IPloneSiteRoot.providedBy(parent):
            pskin = getToolByName(self.context, 'portal_skins')
            parent_skin = pskin.getDefaultSkin()
        return parent_skin

    # plone.app.theming < 1.2

    @property
    def theme(self):
        return self.default_skin

    @theme.setter
    def theme(self, value):
        self.default_skin = value

    # These cannot be set for plone.app.theming < 1.2
    @property
    def mark_special_links(self):
        return None

    @mark_special_links.setter
    def mark_special_links(self, value):
        pass

    @property
    def ext_links_open_new_window(self):
        return None

    @ext_links_open_new_window.setter
    def ext_links_open_new_window(self, value):
        pass

    @property
    def use_popups(self):
        return None

    @use_popups.setter
    def use_popups(self, value):
        pass

    @property
    def icon_visibility(self):
        return None

    @icon_visibility.setter
    def icon_visibility(self, value):
        pass


class LineageThemingControlpanel(ThemingControlpanel):

    _subsite_facade = None

    # plone.app.theming >= 1.2

    @property
    def pskin(self):
        if not self._subsite_facade:
            self._subsite_facade = LineageSubsiteFacade(self.context)
        return self._subsite_facade

    @pskin.setter
    def pskin(self, value):
        # don't let pskin to be set
        return

    # plone.app.theming < 1.2

    @property
    def skinsSettings(self):
        return self.pskin

    @skinsSettings.setter
    def skinsSettings(self, value):
        # don't let skinsSettings to be set
        return


class ControlPanelStyleViewlet(ViewletBase):
    """Hide all but "Theme base" settings from the "Theme base" tab.
    """

    def index(self):
        return u"""
<style type="text/css">
    body.template-theming-controlpanel:not(.portaltype-plone-site) #fieldset-advanced fieldset:nth-of-type(2) div { display:none; }
    body.template-theming-controlpanel:not(.portaltype-plone-site) #fieldset-advanced fieldset:nth-of-type(2) div:nth-of-type(1) { display:block; }
</style>
"""