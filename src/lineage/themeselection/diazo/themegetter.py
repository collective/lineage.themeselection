from zope.component import adapter
from zope.component import queryUtility
from zope.interface import implementer
from plone.app.theming.interfaces import IThemeSettings
from plone.app.theming.interfaces import IThemeSettingsGetter
from plone.app.theming.utils import getAvailableThemes
from plone.registry.interfaces import IRegistry
from collective.lineage.interfaces import IChildSite
from zope.interface import directlyProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary

@adapter(IChildSite)
@implementer(IThemeSettingsGetter)
def get_theme_settings(context):

    themes = available_themes()

    registry = queryUtility(IRegistry)
    if registry is None:
        return None

    try:
        settings = registry.forInterface(IThemeSettings, False)
    except KeyError:
        return None

    return settings

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
    theme_items = map(lambda x:(x.title, x.name), themes)
    return SimpleVocabulary.fromItems(theme_items)
directlyProvides(available_themes_vocab, IVocabularyFactory)
