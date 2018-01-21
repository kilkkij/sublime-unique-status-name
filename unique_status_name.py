import sublime_plugin
import os

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
        name = enriched_file_name(path, paths)
        view.set_status('file_name', name)
    else:
        view.set_status('file_name', 'untitled')

def valid_paths(view):
    """Return list of view paths except for Nones"""
    paths = [v.file_name() for v in view.window().views()]
    paths = [p for p in paths if p is not None]
    return paths

def enriched_file_name(file_path, other_paths):
    """Return file name that is appended with a sub-path that identifies it in case of duplicates"""
    name = os.path.basename(file_path)
    identifier_list = unique_identifier(file_path, other_paths)
    if len(identifier_list):
        subpath = os.path.join(*identifier_list)
        name += ' — %s'%subpath
    return name

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

def _unique_identifier_from_lists(path, paths, identifier):
    """Shortest necessary list of directories identifying given path uniquely.
    Arguments:
    path        [str, str, ...]
    paths       [[str, str, ...], [str, str, ...], ...]
    identifier  [str, str, ...]
    RETURN      [str, str, ...]
    """
    if not path or not paths:
        return identifier
    identifier.append(path[-1])
    if in_same_branch(path, paths):
        return identifier
    paths = [p[:-1] for p in paths if p[-1]==path[-1]]
    path = path[:-1]
    return _unique_identifier_from_lists(path, paths, identifier)

def in_same_branch(path, paths):
    """True if the given path is a sub-path of all the others
    path        list of strings
    paths       lists of strings
    """
    return all((
            len(path) < len(other_path) 
            and all(folder==other_folder for folder, other_folder in zip(path, other_path))
        ) for other_path in paths)

def split_path(path):
    """Take OS into account and split string into path components"""
    path = os.path.normpath(path)
    return path.split(os.sep)