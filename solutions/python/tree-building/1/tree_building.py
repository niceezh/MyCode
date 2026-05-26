class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    if not records:
        return None
    records.sort(key=lambda record: record.record_id)
    if [record.record_id for record in records] != [i for i in range(len(records))]:
        raise ValueError('Record id is invalid or out of order.')
    nodes = []
    for record in records:
        if record.record_id < record.parent_id:
            raise ValueError('Node parent_id should be smaller than its record_id.')
        if record.record_id == record.parent_id and record.record_id != 0:
            raise ValueError('Only root should have equal record and parent id.')
        nodes.append(Node(record.record_id))
    for record in records:
        if record.record_id == 0:
            continue
        nodes[record.parent_id].children.append(nodes[record.record_id])
    return nodes[0]
