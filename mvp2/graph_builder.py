import networkx as nx

def build_graph(requirements):

    G = nx.DiGraph()

    for req in requirements:

        G.add_node(req["id"])

    for src in requirements:

        src_outputs = set(
            src["facts"]["outputs"]
        )

        for dst in requirements:

            if src["id"] == dst["id"]:
                continue

            dst_inputs = set(
                dst["facts"]["inputs"]
            )

            common = src_outputs & dst_inputs

            if common:

                G.add_edge(
                    src["id"],
                    dst["id"],
                    reason=list(common)
                )

    return G