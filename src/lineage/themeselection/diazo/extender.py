from zope.interface import implements
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.field import ExtensionField
from Products.Archetypes import atapi
from Products.Archetypes.utils import OrderedDict

class StringExtField(ExtensionField, atapi.StringField):
    """Selection Field for schemaextender
    """

class DiazoThemeSelectionExtender(object):
    """Schema extender for Child Site Theme Selection.
    """

    fields = [
        StringExtField('lineage_diazotheme',
            schemata='settings',
            mode="w",
            write_permission="Manage portal",
            required=False,
            vocabulary_factory='lineage.themeselection.diazo.available_themes',
            widget=atapi.SelectionWidget(
                label=u"Diazo Theme for Child-Site",
                description=u"Select a Diazo based theme for the child site.",
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
               and 'lineage_diazotheme' not in neworder['settings']:
                neworder['settings'].append('lineage_diazotheme')
        return neworder
