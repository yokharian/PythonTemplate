## Debugging

use your favorite IDE to debug your code


Show all scripts:
``` sh
pdm run --list
```


# Unit Tests
Run tests and print coverage report with PDM script:
``` sh
pdm run test_coverage
```

Above command is equivalent to:
``` sh
python -m unittest discover --pattern '*_tests.py' --start-directory tests/ --verbose
```


## Unit Tests and Code Coverage
Run tests and print coverage report with PDM script:
``` sh
pdm run test_coverage
```

Above command is equivalent to:
``` sh
coverage run -m unittest discover --pattern '*_tests.py' --start-directory tests/ --verbose && coverage report && coverage xml
```
