
import os

def minimal_identifying_path(path, paths):
    """Shortest necessary list of folders identifying path uniquely
    path        str
    paths       list of strings
    RETURN      list of strings
    """
    pathlist = split_path(path)
    pathslist = [split_path(p) for p in paths if p!=path]
    return minimal_identifying_path_from_lists(pathlist, pathslist)

def split_path(path):
    """Return a list of strings defining a path, using OS delimiter"""
    path = os.path.normpath(path)
    return path.split(os.sep)

def minimal_identifying_path_from_lists(path, paths):

	# Compare only to namesakes
	path, paths = paths_ending_in_same_name(path, paths)

	# There are no namesakes
	if not paths:
		return []

	# Find the lowest-tier folder necessary to define unique path
	for i, folder in enumerate(path):
		for other_path in paths:
			# Other path ends here
			if len(other_path) <= i:
				return path[i-1:]
			# Other path branches here
			elif folder != other_path[i]:
				return path[i:]
	# Current file is "highest"
	return path[-1:]

def paths_ending_in_same_name(path, paths):
	return path[:-1], [p[:-1] for p in paths if len(p) and p[-1]==path[-1]]
