from zope.component import adapter
from zope.component import queryUtility
from zope.interface import implementer
from plone.app.theming.interfaces import IThemeSettings
from plone.app.theming.interfaces import IThemeSettingsLookup
from plone.app.theming.utils import getAvailableThemes
from plone.registry.interfaces import IRegistry
from collective.lineage.interfaces import IChildSite
from zope.interface import directlyProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary

@adapter(IChildSite)
@implementer(IThemeSettingsLookup)
def get_theme_settings(context):

    themes = available_themes()
    field = context.Schema().get('lineage_diazotheme', None)
    if field is None:
        return
    theme_name = field.get(context)
    if not theme_name:
        return
    theme = themes[theme_name]

    registry = queryUtility(IRegistry)
    if registry is None:
        return None

    try:
        settings = registry.forInterface(IThemeSettings, False)
    except KeyError:
        return None

    settings = ThemeSettingsProxy(settings, theme)
    return settings


class ThemeSettingsProxy(object):
    """ Proxy object, which passes the original object through except for some
    attributes.
    """

    def __init__(self, settings, theme):
        self.settings = settings
        self.theme = theme

    def __getattr__(self, name):
        """ Return attributes from theme, if available. Otherwise the proxied
        object.
        """
        theme = object.__getattribute__(self, 'theme')
        if name == 'currentTheme':
            return theme.__name__
        if name == 'enabled':
            # No need to have a Diazo theme enabled in main site
            return True

        # Prefer ITheme instead of IThemeSettings??
        value = getattr(theme, name, None)
        if value:
            print "%s %s" % (name, theme.__name__)
            return value

        settings = object.__getattribute__(self, 'settings')
        return getattr(settings, name)


def available_themes():
    themes = getAvailableThemes()
    theme_dict = dict()
    for theme in themes:
        theme_dict[theme.__name__] = theme
    return theme_dict

def available_themes_vocab(context):
    """ Vocabulary for Available Diazo Themes.
    """
    themes = available_themes()
    theme_items = map(lambda x:(x.title, x.__name__), themes.values())
    return SimpleVocabulary.fromItems(theme_items)
directlyProvides(available_themes_vocab, IVocabularyFactory)
