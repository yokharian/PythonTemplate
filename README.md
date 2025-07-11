# 🐍 Python Template
Template to quickly bootstrap Python projects.

Uses [PDM](https://pdm.fming.dev/) to manage dependencies, build distributions and publish to package repositories.


## ✨ Features
- Centralized configuration in `pyproject.toml`
- Dependency management with [PDM](https://pdm.fming.dev/)
- Testing with [unittest](https://docs.python.org/3/library/unittest.html)
- Linting with [Pylint](https://github.com/pylint-dev/pylint)
- Integration with [Visual Studio Code](https://code.visualstudio.com/)
- Building and publishing to [PyPI](https://pypi.org/project/yokharianpythontemplate/)
- Documentation hosted on [Github pages](https://yokharian.github.io/PythonTemplate/)
- CI/CD with [Github actions](https://docs.github.com/en/actions)
- Several useful implementations
	- CLI
	- Type hints
	- ~~Logging~~

For a detailed description of all features check the [documentation](https://yokharian.github.io/PythonTemplate/).

### Developers

1. If you don't have already installed [PDM]((https://pdm-project.org)) install it -> [HOW_TO_INSTALL_PDM.md](scripts/HOW_TO_INSTALL_PDM.md)
   
2. Create a virtual environment for python and install dependencies running the following command:

`You need to have a git repository initialized to avoid errors (.git folder)**`

```sh
pdm install --dev
```

## Command Line Aliases

You can use the following command line aliases to streamline your development process:

- `pdm run test_coverage`: Run test coverage analysis.
- `pdm run test`: Execute the test suite.
- `pdm run docs`: Build the documentation.
