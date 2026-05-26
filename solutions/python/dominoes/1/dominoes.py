from collections import defaultdict

def can_chain(dominoes):
    # Build graph: adjacency list and degrees
    adj = defaultdict(list)
    degrees = defaultdict(int)

    for a, b in dominoes:
        if a == b:
            degrees[a] += 2
            adj[a].append(a)  # self-loop
        else:
            degrees[a] += 1
            degrees[b] += 1
            adj[a].append(b)
            adj[b].append(a)

    # Check if all degrees are even
    for deg in degrees.values():
        if deg % 2 != 0:
            return None

    # Check connectivity
    nodes = list(degrees.keys())
    if not nodes:
        return []  # should not happen since dominoes not empty

    visited = set()
    stack = [nodes[0]]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    if len(visited) != len(nodes):
        return None

    # Find Eulerian circuit using Hierholzer's algorithm
    start = nodes[0]
    circuit = []  # will hold node sequence
    stack = [start]
    current = start

    while stack:
        if adj[current]:
            next_node = adj[current].pop()
            if current != next_node:
                # Remove current from adj[next_node]
                adj[next_node].remove(current)
            current = next_node
            stack.append(current)
        else:
            circuit.append(current)
            stack.pop()
            if stack:
                current = stack[-1]
            else:
                break

    # Now, circuit has node sequence with first and last same
    # Build chain from edges in circuit
    available_bones = dominoes.copy()
    chain = []

    for i in range(len(circuit) - 1):
        u = circuit[i]
        v = circuit[i + 1]
        found = False
        for bone in available_bones:
            a, b = bone
            if (a == u and b == v) or (a == v and b == u):
                chain.append((u, v))
                available_bones.remove(bone)
                found = True
                break
        if not found:
            return None  # should not happen

    if available_bones:
        return None

    return chain

if __name__ == '__main__':
    print(can_chain([(1, 2), (2, 3), (3, 1), (2, 4), (2, 4)]))
