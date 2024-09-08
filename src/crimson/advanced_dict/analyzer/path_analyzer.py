from typing import Dict, Any, Set, List
import inspect


def get_object_attributes(obj: Any) -> Dict[str, Any]:
    """Get all non-private attributes and properties of an object."""
    attributes = {}
    for key, value in inspect.getmembers(obj):
        if not key.startswith("_") and (
            not callable(value) or isinstance(value, property)
        ):
            attributes[key] = value
    return attributes


def explore_item(
    item: Any, current_path: str, current_level: int, max_level: int, paths: Set[str]
) -> None:
    """Recursively explore an item (dict or object) and collect paths."""
    if current_level > max_level:
        return

    if isinstance(item, dict):
        items_to_explore = item.items()
    elif hasattr(item, "__dict__") or inspect.isclass(type(item)):
        items_to_explore = get_object_attributes(item).items()
    else:
        return

    for key, value in items_to_explore:
        new_path = f"{current_path}.{key}" if current_path else key
        paths.add(new_path)
        explore_item(value, new_path, current_level + 1, max_level, paths)


def find_paths_in_dict(data: Dict[str, Any], max_level: int) -> Set[str]:
    """Find all paths in a single dictionary up to a specified level."""
    paths = set()
    explore_item(data, "", 0, max_level, paths)
    return paths


def find_paths_in_dict_list(data: List[Dict[str, Any]], max_level: int) -> Set[str]:
    """Find all paths in a list of dictionaries up to a specified level."""
    all_paths = set()
    for item in data:
        all_paths.update(find_paths_in_dict(item, max_level))
    return all_paths
