import pytest

import sys

from typing import List, Dict, Type, Union

# Add example_tools path

import dict_list

from dict_list import (
    AstNodeMock,
    NodeWithInfo,
    Position,
    Custom,
)


from crimson.advanced_dict.converter.dict_list_converter import (
    group_by_key_path,
    group_single_items_by_key_path,
    analyze_path_types,
)


def test_init():

    ast_node_dict_list: List[NodeWithInfo] = dict_list.ast_node_with_position
    new_data: Dict[int, NodeWithInfo] = group_single_items_by_key_path(
        ast_node_dict_list, "node.lineno", key_type=Type[int]
    )

    new_data
    maybe_empty_data: Dict[int, NodeWithInfo] = group_single_items_by_key_path(
        ast_node_dict_list, "node.lineno", key_type=Type[str]
    )

    maybe_empty_data
    analyze_path_types(
        data=ast_node_dict_list, key_path="node.lineno"
    )

    new_data = group_single_items_by_key_path(
        data=ast_node_dict_list, key_path="node.lineno", key_type=Type[Union[int, str]]
    )

    new_data
    improperly_highlighted = group_single_items_by_key_path(
        data=ast_node_dict_list, key_path="node.lineno", key_type=Union[int, str]
    )

    improperly_highlighted
    complex_data = dict_list.complex_data

    try:

        group_single_items_by_key_path(
            data=complex_data, key_path="node.name", key_type=Type[str]
        )

    except Exception as e:

        print("Error: ", e)
    new_data = group_by_key_path(
        data=complex_data, key_path="node.name", key_type=Type[Union[Custom, str]]
    )

    hash_solved = {}

    for key, item in new_data.items():

        hash_solved[str(key)] = item

    hash_solved
    paths = analyze_path_types(complex_data, "node.name")

    paths
    try:

        group_by_key_path(
            data=complex_data,
            key_path="node.name",
            key_type=Type[Union[Custom, List, str]],
        )

    except Exception as e:

        print("Error: ", e)
    from crimson.advanced_dict.converter.dict_list_converter import (
        get_nested_value,
        create_type_converter,
    )
