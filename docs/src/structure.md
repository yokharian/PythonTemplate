---
icon: material/file-document
---
# Project Structure

/// html | pre
	markdown: block
:vscode-icons-opened-folder-python: **ROOT**
├─ :vscode-icons-folder-default: .github         GitHub configuration and workflows
├─ :vscode-icons-folder-default: .staging        Build artifacts and other ignored files
├─ :vscode-icons-folder-vscode: .vscode         VS Code configuration
├─ :vscode-icons-markdown: README.md       Project readme
├─ :vscode-icons-folder-docs: **docs**            **Online Documentation**
│   ├─ :vscode-icons-folder-default: include
│   ├─ :vscode-icons-folder-default: overrides
│   ├─ :vscode-icons-folder-default: src
│   ├─ :vscode-icons-yaml: mkdocs.yaml
│   ├─ :vscode-icons-markdown: pypi.md
│   └─ :vscode-icons-markdown: specs.md
├─ :vscode-icons-default: pdm.lock        Dependency lock file
├─ :vscode-icons-toml: pyproject.toml  Python project configuration
├─ :vscode-icons-folder-default: scripts         Build scripts and PDM plugins
├─ :vscode-icons-default: setup.py        Setup script for installation
├─ :vscode-icons-folder-default: **src**             Main package **source code**
│  ├─ :vscode-icons-python: __init__.py             Package initialization
│  ├─ :vscode-icons-python: __main__.py             Entry point
│  ├─ :vscode-icons-python: cli.py              Command-line interface
│  ├─ :vscode-icons-python: core.py             Core functionality
│  └─ :vscode-icons-default: py.typed            Type checking marker
└─ :vscode-icons-folder-test: **tests**            **Tests** for the main package
   ├─ :vscode-icons-python: __init__.py             Package initialization
   └─ :vscode-icons-python: core_tests.py       Tests
///

