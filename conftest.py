import pytest

def pytest_collect_file(parent, path):
    if path.ext == '.ipynb' and path.basename.startswith('example'):
        return pytest.Module.from_parent(parent, fspath=path)