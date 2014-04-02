def flatten_tree(tree):
    """Flatten a tree.
    """
    flat = []

    for node in tree:
        if len(node) == 3 and node[2]:
            flat.append(node[:2])
            flat += flatten_tree(node[2])
        else:
            flat.append(node)

    return flat
