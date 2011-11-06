from zope.interface import implements
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.field import ExtensionField
from Products.Archetypes import atapi
from Products.Archetypes.utils import OrderedDict

class StringExtField(ExtensionField, atapi.StringField):
    """Selection Field for schemaextender
    """

class ThemeSelectionExtender(object):
    """Schema extender for Child Site Theme Selection.
    """

    fields = [
        StringExtField('lineage_theme',
            schemata='settings',
            mode="w",
            write_permission="Manage portal",
            required=False,
            vocabulary_factory='plone.app.vocabularies.Skins',
            widget=atapi.SelectionWidget(
                label=u"Theme for Child-Site",
                description=u"Select a theme for the child site.",
            )
        ),
    ]

    implements(IOrderableSchemaExtender)

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields

    def getOrder(self, original):
        neworder = OrderedDict()
        for schemata in original.keys():
            neworder[schemata] = original[schemata]
            if schemata == 'settings' \
               and 'lineage_theme' not in neworder['settings']:
                neworder['settings'].append('lineage_theme')
        return neworder
