from typing import TypedDict, List


class AstNodeMock(TypedDict):
    lineno: 5


class Position(TypedDict):
    lineno: int
    end_lineno: int
    col_offset: int
    end_col_offset: int


class NodeWithInfo(TypedDict):
    node: AstNodeMock
    position: Position


ast_node_with_position: List[NodeWithInfo] = [
    {
        "node": {"lineno": 5},
        "position": {
            "lineno": 5,
            "end_lineno": 6,
            "col_offset": 0,
            "end_col_offset": 15,
        },
    },
    {
        "node": {"lineno": "9"},
        "position": {
            "lineno": 9,
            "end_lineno": 10,
            "col_offset": 0,
            "end_col_offset": 41,
        },
    },
    {
        "node": {"lineno": 25},
        "position": {
            "lineno": 25,
            "end_lineno": 26,
            "col_offset": 4,
            "end_col_offset": 12,
        },
    },
]


class Custom:
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return f"Custom({self.value})"


complex_data = [
    {
        "id": 1,
        "node": {"name": "function1", "value": 10, "type": "regular"},
        "metadata": Custom("meta1"),
    },
    {
        "id": 2,
        "node": {"name": "function2", "value": "20", "type": Custom("special")},
        "metadata": "some meta data",
    },
    {
        "id": 3,
        "node": {"name": [1, 2, 3], "value": 30.5, "type": True},
        "metadata": [1, 2, 3],
    },
    {
        "id": "4",
        "node": {
            "name": Custom("custom_function"),
            "value": Custom("custom_value"),
            "type": None,
        },
        "metadata": {"key": "value"},
    },
    {
        "id": 5,
        "node": {
            "name": "function2",
            "value": [1, "2", 3.0],
            "type": ("tuple", "type"),
        },
        "metadata": 42,
    },
]
