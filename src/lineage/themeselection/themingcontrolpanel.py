from plone.app.theming.browser.controlpanel import ThemingControlpanel


class LineageSubsiteFacade(object):

    def __init__(self, subsite):
        self.subsite = subsite

    # plone.app.theming >= 1.2

    @property
    def default_skin(self):
        return self.subsite.lineage_theme

    @default_skin.setter
    def default_skin(self, value):
        self.subsite.lineage_theme = value

    def getDefaultSkin(self):
        return self.default_skin

    # plone.app.theming < 1.2

    @property
    def theme(self):
        return self.subsite.lineage_theme

    @theme.setter
    def theme(self, value):
        self.subsite.lineage_theme = value

    @property
    def mark_special_links(self):
        return getattr(self.subsite, 'mark_special_links', None)

    @mark_special_links.setter
    def mark_special_links(self, value):
        self.subsite.mark_special_links = value

    @property
    def ext_links_open_new_window(self):
        return getattr(self.subsite, 'ext_links_open_new_window', None)

    @ext_links_open_new_window.setter
    def ext_links_open_new_window(self, value):
        self.subsite.ext_links_open_new_window = value

    @property
    def use_popups(self):
        return getattr(self.subsite, 'use_popups', None)

    @use_popups.setter
    def use_popups(self, value):
        self.subsite.use_popups = value

    @property
    def icon_visibility(self):
        return getattr(self.subsite, 'icon_visibility', None)

    @icon_visibility.setter
    def icon_visibility(self, value):
        self.subsite.icon_visibility = value


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

