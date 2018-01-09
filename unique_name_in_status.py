import sublime_plugin
import os

def split_path(path):
    """Take OS into account and split string into path components"""
    path = os.path.normpath(path)
    return path.split(os.sep)

def _unique_identifier_from_lists(path, paths, identifier):
    """
    path        list of strings
    paths       list of lists of strings
    identifier  list of strings
    RETURN      identifier
    """
    if not path or not paths:
        return identifier
    identifier.append(path[-1])
    paths = [p[:-1] for p in paths if p[-1]==path[-1]]
    path = path[:-1]
    return _unique_identifier_from_lists(path, paths, identifier)

def unique_identifier(path, paths):
    """Shortest necessary list of folders identifying path uniquely
    path        str
    paths       list of strings
    RETURN      list of strings
    """
    pathlist = split_path(path)
    pathslist = [split_path(p) for p in paths if p!=path]
    unique_directories = _unique_identifier_from_lists(pathlist, pathslist, [])
    unique_directories.reverse()
    if not unique_directories:
        return []
    else:
        return unique_directories[:-1]
    return unique_directories

def _set_view_status(view):
    path = view.file_name()

    if path is not None:
        name = os.path.basename(path)
        status_name = name

        paths = [v.file_name() for v in view.window().views()]
        paths = [p for p in paths if p is not None]
        names = [os.path.basename(p) for p in paths]

        display_chain = unique_identifier(path, paths)
        if display_chain:
            directory_string = os.path.join(*display_chain)
            status_name += ' (%s)'%directory_string

        view.set_status('file_name', status_name)

    else:
        view.set_status('file_name', 'untitled')

class UniqueNameInStatus(sublime_plugin.EventListener):
    """Update view status with file_name. Name adjusts to identify view uniquely."""

    def on_activated(self, view):
        _set_view_status(view)

    def on_post_save(self, view):
        _set_view_status(view)
