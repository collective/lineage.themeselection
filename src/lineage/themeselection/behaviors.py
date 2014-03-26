from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import alsoProvides


class IThemeSelection(model.Schema):
    model.fieldset('settings', fields=['lineage_theme'])

    lineage_theme = schema.Choice(
        title=u'label_theme_childsite',
        description=u"Select a theme for the child site.",
        required=False,
        vocabulary='plone.app.vocabularies.Skins',
    )
alsoProvides(IThemeSelection, IFormFieldProvider)
