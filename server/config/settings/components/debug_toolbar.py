def custom_show_toolbar(request):
    from debug_toolbar.middleware import show_toolbar

    return show_toolbar(request) and not request.path.startswith("/wg-admin")


DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": custom_show_toolbar}
