## Installation

<a href="https://repology.org/project/pdm/versions">
    <img src="https://repology.org/badge/vertical-allrepos/pdm.svg" alt="Packaging status" align="right">
</a>

PDM requires python version 3.9 or higher. Alternatively, you can download the standalone binary file from the [release assets](https://github.com/pdm-project/pdm/releases).

### Via Install Script

Like Pip, PDM provides an installation script that will install PDM into an isolated environment.

**For Linux/Mac**

```bash
curl -sSL https://pdm-project.org/install-pdm.py | python3 -
```

**For Windows**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://pdm-project.org/install-pdm.py | py -"
```

For security reasons, you should verify the checksum of `install-pdm.py`.
It can be downloaded from [install-pdm.py.sha256](https://pdm-project.org/install-pdm.py.sha256).

The installer will install PDM into the user site and the location depends on the system:

- `$HOME/.local/bin` for Linux
- `$HOME/Library/Python/<version>/bin` for MacOS
- `%APPDATA%\Python\Scripts` on Windows

You can pass additional options to the script to control how PDM is installed:

```
usage: install-pdm.py [-h] [-v VERSION] [--prerelease] [--remove] [-p PATH] [-d DEP]

optional arguments:
  -h, --help            show this help message and exit
  -v VERSION, --version VERSION | envvar: PDM_VERSION
                        Specify the version to be installed, or HEAD to install from the main branch
  --prerelease | envvar: PDM_PRERELEASE    Allow prereleases to be installed
  --remove | envvar: PDM_REMOVE            Remove the PDM installation
  -p PATH, --path PATH | envvar: PDM_HOME  Specify the location to install PDM
  -d DEP, --dep DEP | envvar: PDM_DEPS     Specify additional dependencies, can be given multiple times
```

You can either pass the options after the script or set the env var value.

### Alternative Installation Methods

If you are on macOS and using `homebrew`, install it by:

```bash
brew install pdm
```

If you are on Windows and using [Scoop](https://scoop.sh/), install it by:

```
scoop bucket add frostming https://github.com/frostming/scoop-frostming.git
scoop install pdm
```

Otherwise, it is recommended to install `pdm` in an isolated environment with `pipx`:

```bash
pipx install pdm
```

Or you can install it under a user site:

```bash
pip install --user pdm
```

With [asdf-vm](https://asdf-vm.com/)

```bash
asdf plugin add pdm
asdf install pdm latest
```

## Quickstart

**Create a new PDM project**

```bash
pdm new my-project
```

Answer the questions following the guide, and a PDM project with a `pyproject.toml` file will be ready to use.

**Install dependencies**

```bash
pdm add requests flask
```

You can add multiple dependencies in the same command. After a while, check the `pdm.lock` file to see what is locked for each package.

## Badges

Tell people you are using PDM in your project by including the markdown code in README.md:

```markdown
[![pdm-managed](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fpdm-project%2F.github%2Fbadge.json)](https://pdm-project.org)
```

[![pdm-managed](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fpdm-project%2F.github%2Fbadge.json)](https://pdm-project.org)

## PDM Eco-system

[Awesome PDM](https://github.com/pdm-project/awesome-pdm) is a curated list of awesome PDM plugins and resources.

## Sponsors

<p align="center">
    <a href="https://cdn.jsdelivr.net/gh/pdm-project/sponsors/sponsors.svg">
        <img src="https://cdn.jsdelivr.net/gh/pdm-project/sponsors/sponsors.svg"/>
    </a>
</p>

## Credits

This project is strongly inspired by [pyflow] and [poetry].

[pyflow]: https://github.com/David-OConnor/pyflow
[poetry]: https://github.com/python-poetry/poetry

## License

This project is open sourced under MIT license, see the [LICENSE](LICENSE) file for more details.
