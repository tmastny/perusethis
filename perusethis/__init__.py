import os
from os.path import join

def create_package(path):


    assert os.path.isdir(path)

    name = os.path.basename(path)

    use_directory(name)

    with open(join(name, "__init__.py"), "w") as f:
        f.write("def hello(): print('hello world'")


    use_manifest()


def use_directory(name):
    os.mkdir(name)


def use_manifest():
    # make manifest
    pass


def use_setup(name):
    # create readme and manifest
    dir = os.path.dirname(os.path.abspath(__file__))
    setup_template = open(join(dir, "setup.txt"), "r").read()


    with open("setup.py", "w") as f:
      f.write(setup_template.format(name=name))



def use_readme(type="md"):
    # create file
    # add to manifest
    pass

def use_test(name):
    # check if tests are created
    # create https://python-packaging.readthedocs.io/en/latest/testing.html
    if not os.path.isdir("tests"):
        os.mkdir("tests")

    with open(join("tests", "test_" + name + ".py"), "w") as f:
        f.write("def test_func(): assert 1 == 2")

    # create file


# Tetsting
#   pytest has structures for temp directories:
#   https://docs.pytest.org/en/latest/getting-started.html#request-a-unique-temporary-directory-for-functional-tests


