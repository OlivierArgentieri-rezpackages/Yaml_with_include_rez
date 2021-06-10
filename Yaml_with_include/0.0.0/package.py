name = "yaml_with_include"
version = "0.0.0"
build_command = False
timestamp=0

requires = [
    "PyYAML"
]


tests = {
    "unit": {
        "command": "python -m pytest {root}/yaml_with_include",
        "requires": ["pytest"],
        "run_on": ["default", "pre_release"]
    },
    "lint": {
        "command":
        "pylint --rcfile={root}/.pylintrc --fail-under=8 {root}/yaml_with_include",
        "requires": ["pylint", "pytest"],
        "run_on": ["default", "pre_release"]
    }
}

tools = ["run_test.sh"]

def commands():
    env.PYTHONPATH.append("{root}/yaml_with_include")
    env.PATH.append("{root}/yaml_with_include")
    env.PATH.append("{root}/tools")

