# Comprehensive Guide to MkDocs-Material for New Developers

## Introduction

Welcome to our documentation system! This guide will help you understand how to use MkDocs with the Material theme to modify, debug, and extend our project's online documentation. By the end of this guide, you'll be able to confidently make changes to the documentation and understand the structure of the `docs` folder.

## What is MkDocs and Material for MkDocs?

[MkDocs](https://www.mkdocs.org/) is a fast, simple, and static site generator that's designed to build project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file.

[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) is a theme for MkDocs that offers a modern, responsive, and customizable design for your documentation. It provides many features out of the box, such as:

- Responsive design that works on all devices
- Multiple color schemes (light/dark mode)
- Search functionality
- Code highlighting
- Navigation and table of contents
- And much more!

## Project Documentation Structure

Our documentation is organized in the `docs` directory with the following structure:


/// html | pre
	markdown: block
:vscode-icons-folder-default: docs/ # ROOT
├── :vscode-icons-folder-default: .cache/          Cache directory for MkDocs
├── :vscode-icons-folder-default: include/         Reusable content snippets
├── :vscode-icons-folder-default: overrides/       **Theme assets & customizations**
│   ├── :vscode-icons-folder-default: .icons/         Custom icons
│   ├── :vscode-icons-folder-default: fonts/          Custom fonts
│   └── :vscode-icons-folder-default: partials/       Custom HTML templates
├── :vscode-icons-folder-default: src/             **Documentation source files**
│   ├── :vscode-icons-folder-default: features/        Feature documentation
│   ├── index.md            Home page (symlinked to README.md)
│   ├── structure.md        Project structure documentation
│   └── ...                 Other documentation files
├── mkdocs.yaml         MkDocs configuration
├── custom_hooks.py     Custom Python hooks for MkDocs
└── **(various scripts...)**     Helper scripts for documentation
    _can be executed with python or bash_

///


### Key Components

1. **src/**: Contains all the Markdown files that make up the documentation content.
2. **mkdocs.yaml**: The configuration file for MkDocs.
3. **overrides/**: Contains customizations to the Material theme.
4. **custom_hooks.py**: Contains Python functions that are executed during the build process.

## Setting Up Your Environment

### Prerequisites

- Python 3.12 or higher
- PDM (Python Dependency Manager)

### Installation

1. Install PDM by following the instructions in `how_to_install_pdm.md`.
2. Install the project dependencies:

```bash
pdm install --dev
```

This will install MkDocs, Material for MkDocs, and other required packages.

## Understanding the Configuration (mkdocs.yaml)

The `mkdocs.yaml` file is the heart of your MkDocs configuration. It defines:

- Basic project information (name, description, etc.)
- Repository information
- Navigation structure
- Theme configuration
- Extensions and plugins
- Build settings

Here's a breakdown of the key sections:

### Project Information

```yaml
site_name: Python Project Template
site_description: Template to quickly bootstrap Python projects.
site_author: Sofia Escobedo
site_url: https://yokharian.github.io/PythonTemplate/
```

### Repository Configuration

```yaml
repo_name: python-project-template
repo_url: https://github.com/yokharian/PythonTemplate
edit_uri: !ENV [ editUri, -/edit/main/docs/src/ ]
```

### Navigation Structure

The `nav` section defines the structure of your documentation's navigation menu:

```yaml
nav:
  - Home: index.md
  - Features:
      - features/index.md
      - features/dependencies.md
      - features/development.md
      - features/debugging.md
      - features/documentation.md
      - features/release.md
  - structure.md
  - how_to_install_pdm.md
  - examples.md
  - contributing.md
```

### Theme Configuration

```yaml
theme:
    name: material
    features:
      - content.action.view
      - content.code.annotate
      - content.code.copy
      - content.tabs.link
      - navigation.footer
      - navigation.indexes
      - navigation.top
      - toc.follow
    icon:
        logo: simple/python
        repo: simple/gitlab
    custom_dir: overrides
    palette:
      - scheme: default
        media: '(prefers-color-scheme: light)'
        toggle:
            name: Switch to dark mode
            icon: material/weather-night
      - scheme: slate
        media: '(prefers-color-scheme: dark)'
        toggle:
            name: Switch to light mode
            icon: material/weather-sunny
```

## Creating and Organizing Content

### File Structure

All documentation content is stored in the `docs/src/` directory. The structure of this directory should mirror the navigation structure defined in `mkdocs.yaml`.

### Creating New Pages

1. Create a new Markdown file in the appropriate directory under `docs/src/`.
2. Add the page to the navigation in `mkdocs.yaml`.

### Page Metadata

You can add metadata to your Markdown files using YAML front matter:

```markdown
---
icon: material/file-document
title: Custom Title
description: Page description
---

# Page Content
```

### Linking Between Pages

You can link to other pages in your documentation using relative paths:

```markdown
[Link to another page](../path/to/page.md)
```

## Customizing the Theme

### Custom Directory Structure

The `overrides/` directory contains customizations to the Material theme:

- `overrides/.icons/`: Custom icons
- `overrides/fonts/`: Custom fonts
- `overrides/partials/`: Custom HTML templates

### Custom Icons

We use VS Code icons for our documentation. These are downloaded automatically by the `download_icons.sh` script.

### Custom HTML Templates

You can override any part of the Material theme by creating a file with the same path in the `overrides/` directory. For example, `overrides/partials/actions.html` overrides the actions buttons in the documentation.

## Using Custom Hooks

The `custom_hooks.py` file contains Python functions that are executed during the build process:

```python
def define_env(env):
    """Main function"""

def on_pre_page_macros(env):
    """Executed just before the Jinja2 directives (markdown page) have been rendered"""
    subprocess.run(["bash", "./download_icons.sh"], check=True)
    subprocess.run(["bash", "./create_how_to_install_pdm_instructions.sh"], check=True)

def on_post_build(env):
    print('post')
```

These hooks allow you to:
- Run scripts before or after the build process
- Define custom variables and functions for use in your Markdown files
- Modify the build process in various ways

## Building and Previewing Documentation

### Local Development Server

To preview your documentation locally:

```bash
pdm run serve_docs
```

This will start a local development server at http://127.0.0.1:8000/ that automatically reloads when you make changes to your documentation.

### Building Documentation

To build the documentation:

```bash
pdm run docs
```

This will generate the static site in the `.staging/pages/` directory.

## Debugging Common Issues

### Missing Dependencies

If you encounter errors related to missing dependencies, make sure you've installed all the required packages:

```bash
pdm install --dev
```

### Navigation Issues

If pages are not appearing in the navigation, check:
1. The file exists in the correct location
2. The file is correctly referenced in the `nav` section of `mkdocs.yaml`
3. The file has valid Markdown syntax

### Custom Theme Issues

If your theme customizations are not working:
1. Check that the files are in the correct location in the `overrides/` directory
2. Verify that the `custom_dir` option is set correctly in `mkdocs.yaml`
3. Clear the `.cache/` directory and rebuild

### Extension Issues

If Markdown extensions are not working:
1. Verify that the extension is correctly configured in `mkdocs.yaml`
2. Check the extension documentation for correct usage

## Advanced Features

### Custom Scripts

Our documentation system uses several custom scripts:

- `download_icons.sh`: Downloads VS Code icons for use in the documentation.
- `create_how_to_install_pdm_instructions.sh`: Generates the PDM installation instructions.

### Integration with CI/CD

The documentation is built and deployed automatically when changes are pushed to the main branch. This is configured in the CI/CD pipeline.

## Additional Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs Documentation](https://squidfunk.github.io/mkdocs-material/)
- [Markdown Guide](https://www.markdownguide.org/)
- [PyMdown Extensions Documentation](https://facelessuser.github.io/pymdown-extensions/)
