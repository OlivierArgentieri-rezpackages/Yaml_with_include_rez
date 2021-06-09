name = "yaml_include"
version = "0.0.0"
build_command = False


requires = [
    "PyYAML"
]

def commands():
    env.PYTHONPATH.append("{root}/src")
    env.PATH.append("{root}/src")