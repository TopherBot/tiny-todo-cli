import json
import os
from pathlib import Path
import subprocess
import sys

# Helper to invoke the CLI in a subprocess with a fresh env
def run_cli(*args, cwd=None):
    cmd = [sys.executable, "-m", "todo"] + list(args)
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return result

def test_add_and_list(tmp_path, monkeypatch):
    # Change working directory to a temp folder so we don't pollute the repo
    cwd = tmp_path
    # Add an item
    add_res = run_cli("add", "Write tests", cwd=cwd)
    assert add_res.returncode == 0
    assert "Added" in add_res.stdout
    # List items
    list_res = run_cli("list", cwd=cwd)
    assert list_res.returncode == 0
    assert "Write tests" in list_res.stdout
    # Verify JSON file content
    data_file = cwd / "todo.json"
    assert data_file.exists()
    data = json.loads(data_file.read_text())
    assert len(data) == 1
    assert data[0]["text"] == "Write tests"
    assert data[0]["done"] is False

def test_done_and_delete(tmp_path):
    cwd = tmp_path
    # Add two items
    run_cli("add", "Item 1", cwd=cwd)
    run_cli("add", "Item 2", cwd=cwd)
    # Mark first as done
    done_res = run_cli("done", "1", cwd=cwd)
    assert done_res.returncode == 0
    # Delete second
    del_res = run_cli("delete", "2", cwd=cwd)
    assert del_res.returncode == 0
    # Verify state
    data = json.loads((cwd / "todo.json").read_text())
    assert len(data) == 1
    assert data[0]["text"] == "Item 1"
    assert data[0]["done"] is True
