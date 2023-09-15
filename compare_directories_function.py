def compare_directories(dir1, dir2):
    """
    Compare two directories and return a list of files that are not present in both.
    """
    dir1_files = set()
    dir2_files = set()
    for root, dirs, files in os.walk(dir1):
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), dir1)
            dir1_files.add(rel_path)
    for root, dirs, files in os.walk(dir2):
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), dir2)
            dir2_files.add(rel_path)
    unique_to_dir1 = dir1_files - dir2_files
    unique_to_dir2 = dir2_files - dir1_files
    common_files = dir1_files & dir2_files
    different_files = set()
    for file in common_files:
        path1 = os.path.join(dir1, file)
        path2 = os.path.join(dir2, file)
        if os.path.isfile(path1) and os.path.isfile(path2):
            with open(path1, 'rb') as f1, open(path2, 'rb') as f2:
                if f1.read() != f2.read():
                    different_files.add(file)
    return (unique_to_dir1, unique_to_dir2, different_files)
