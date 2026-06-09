import json
import networkx as nx

def export_json(G, requirements):

    output = {

        "requirements": requirements,

        "dependencies": []
    }

    for u, v, data in G.edges(data=True):

        output["dependencies"].append({

            "source": u,
            "target": v,
            "reason": data["reason"]
        })

    with open(
        "results.json",
        "w"
    ) as f:

        json.dump(
            output,
            f,
            indent=2
        )

def export_clusters(G):

    clusters = list(
        nx.weakly_connected_components(G)
    )

    for i, c in enumerate(clusters):

        print(f"\nCLUSTER {i+1}")

        for r in sorted(c):
            print(r)