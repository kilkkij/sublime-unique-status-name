
import os

def file_identifier(file_path, other_paths):
    """Return file name that is appended with a sub-path that identifies it in case of duplicates"""
    name = os.path.basename(file_path)
    identifier_list = directory_identifier(file_path, other_paths)
    if len(identifier_list):
        subpath = os.path.join(*identifier_list)
        name += ' — %s'%subpath
    return name

def directory_identifier(path, paths):
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
    """Return a list of strings defining a path, using OS delimiter"""
    path = os.path.normpath(path)
    return path.split(os.sep)