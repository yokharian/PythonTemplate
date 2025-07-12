"""
# Content of the env object
https://mkdocs-macros-plugin.readthedocs.io/en/latest/macros/#content-of-the-env-object

Description
The env object is used for introspection, i.e. is to get information on the project or page.

Here is a list of commonly needed attributes (constants) or functions of that object:

Item	    Type	    Description
variables	attribute	The namespace that contains the variables and macros that will be available in markdown pages with {{ ... }} notation. This dictionary is initialized with the values contained in the extra section of the configuration file (and optionally, with external yaml files). This object is also accessible with the dot notation; e.g. env.variables['foo'] is equivalent to env.variables.foo.
macro       function	A decorator function that you can use to declare a Python function as a Jinja2 callable ('macro' for MkDocs).
filters     attribute	A list list of jinja2 filters (default None)
filter      function	A decorator for declaring a Python function as a jinja2 custom filter
project_dir attribute	The source directory of the MkDocs project (useful for finding or including other files)
conf        attribute	The content of the config file (mkdocs.yaml).
config      attribute	This can be a useful object; it contains the global context for MkDocs]2.
page        attribute	The information on the page being served (such as the title, etc.). For more information on its content, see MkDoc's description of the page object.
"""
import subprocess


def on_post_build(env):
    """Executed after the html pages have been produced"""
    # subprocess.run(["bash", "./download_icons.sh"], check=True)
    # subprocess.run(["bash", "./create_how_to_install_pdm.sh"], check=True)
    ...
