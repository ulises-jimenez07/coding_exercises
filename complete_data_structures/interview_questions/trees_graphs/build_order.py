#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.

# Build Order

# projects a,b,c,d,e,f
# dependencies: (a,d), (f,b), (b,d), (f,a), (d,c)


def createGraph(projects, dependencies):
    projectGraph = {}
    for project in projects:
        projectGraph[project] = []
    for pairs in dependencies:
        projectGraph[pairs[0]].extend(pairs[1])
    return projectGraph


project = ["a", "b", "c", "d", "e", "f"]
dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]


def get_project_with_dependencies(projects):
    projects_dependent = set()
    for project in projects:
        projects_dependent = projects_dependent.union(set(projects[project]))
    return projects_dependent


def get_projects_without_dependencies(projects, dependant):
    projects_independent = set()
    for project in projects:
        if project not in dependant:
            projects_independent.add(project)
    return projects_independent


def findBuildOrder(projects, dependencies):
    project_graph = createGraph(projects, dependencies)

    build_order = []
    while project_graph:
        projects_dependent = get_project_with_dependencies(project_graph)
        projects_independent = get_projects_without_dependencies(project_graph, projects_dependent)
        if len(projects_independent) == 0 and project_graph:
            raise ValueError("There is a cycle in the build order")
        for independent in projects_independent:
            build_order.append(independent)
            del project_graph[independent]
    return build_order
