
import sublime_plugin
import os
from .unique_file_identifier import file_identifier

class UniqueNameInStatus(sublime_plugin.EventListener):
    """Update view status with file_name. Name adjusts to identify view uniquely."""

    def on_activated(self, view):
        set_view_status(view)

    def on_post_save(self, view):
        set_view_status(view)

def set_view_status(view):
    """
    view        sublime_plugin view
    """
    path = view.file_name()
    if path is not None:
        paths = valid_paths(view)
        enriched_name = file_identifier(path, paths)
        view.set_status('file_name', enriched_name)
    else:
        view.set_status('file_name', 'untitled')

def valid_paths(view):
    """Return list of view paths except for Nones"""
    paths = [v.file_name() for v in view.window().views()]
    paths = [p for p in paths if p is not None]
    return paths
