def determine_build_order(projects, dependencies):
    dependency_tree = {p: set() for p in projects}
    build_order=[]
    unbuilt_projects= set(projects)

    for dependency, project in dependencies:
        dependency_tree[project].add(dependency)
    print(dependency_tree)
    while unbuilt_projects:
        something_built=False
        print(unbuilt_projects)
        for project in list(unbuilt_projects):
            dependencies=dependency_tree[project]
            if not unbuilt_projects.intersection(dependencies):
                build_order.append(project)
                unbuilt_projects.remove(project)
                something_built=True
        if not something_built:
            raise Exception("No valid build order exists")
        
    return build_order


projects = ["a", "b", "c", "d", "e", "f", "g"]
dependencies = [
    ("d", "g"),
    ("a", "e"),
    ("b", "e"),
    ("c", "a"),
    ("f", "a"),
    ("b", "a"),
    ("f", "c"),
    ("f", "b"),
]
determine_build_order(projects, dependencies)

projects = ["a", "b"]
dependencies = [("a", "b"), ("b", "a")]
determine_build_order(projects, dependencies)
