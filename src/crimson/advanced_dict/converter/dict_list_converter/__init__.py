import sys
from typing import (
    List,
    Dict,
    Any,
    TypeVar,
    Callable,
    Type,
    Set,
    get_args,
)
from collections import defaultdict


T = TypeVar("T")
K = TypeVar("K")


def get_nested_value(item: Any, key_path: str) -> Any:
    keys = key_path.split(".")
    value = item
    for key in keys:
        if isinstance(value, dict):
            value = value.get(key)
        elif hasattr(value, key):
            value = getattr(value, key)
        else:
            return None
        if value is None:
            return None
    return value


def create_type_converter(target_type: Type[K]) -> Callable[[Any], K]:
    def converter(value: Any) -> K:
        if isinstance(value, get_args(target_type)):
            return value
        raise ValueError(f"Cannot convert {value} to {target_type}")

    return converter


def group_by_key_path(
    data: List[Dict[str, Any]], key_path: str, key_type: Type[K]
) -> Dict[K, List[Dict[str, Any]]]:

    key_converter = create_type_converter(key_type)
    grouped_data: Dict[K, List[Dict[str, Any]]] = defaultdict(list)
    for item in data:
        value = get_nested_value(item, key_path)
        if value is not None:
            try:
                converted_value = key_converter(value)
                grouped_data[converted_value].append(item)
            except ValueError:
                continue  # Skip this item if conversion fails
    return dict(grouped_data)


class MultipleSingleItemError(Exception):
    """Exception raised when multiple items are found for a single key."""

    pass


def group_single_items_by_key_path(
    data: List[Dict[str, Any]], key_path: str, key_type: Type[K]
) -> Dict[K, Dict[str, Any]]:
    key_converter = create_type_converter(key_type)
    grouped_data: Dict[K, List[Dict[str, Any]]] = defaultdict(list)

    for item in data:
        value = get_nested_value(item, key_path)
        if value is not None:
            try:
                converted_value = key_converter(value)
                grouped_data[converted_value].append(item)
            except ValueError:
                continue  # Skip this item if conversion fails

    # Convert to Dict[K, Dict[str, Any]] and check for multiple items
    result: Dict[K, Dict[str, Any]] = {}
    for key, items in grouped_data.items():
        if len(items) > 1:
            raise MultipleSingleItemError(
                f"Multiple items found for key '{key}'. Use group_by_key_path function instead."
            )
        elif len(items) == 1:
            result[key] = items[0]

    return result


def analyze_path_types(data: List[Dict[str, Any]], key_path: str) -> Set[Type]:
    type_set = set()
    for item in data:
        value = get_nested_value(item, key_path)
        if value is not None:
            type_set.add(type(value))
    return type_set
