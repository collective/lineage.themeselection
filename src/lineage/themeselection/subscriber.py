def switch_skin(obj, event):
    """Switch to the skin selected for the child site.
    """
    field = obj.Schema().get('lineage_theme', None)
    if field is None:
        return
    theme = field.get(obj)
    if not theme:
        return 
    obj.changeSkin(theme, event.request)