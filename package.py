name = "shotgun_python_api"

version = "3.2.0"

authors = [
    "Autodesk"
]

description = \
    """
    A Python-based API for accessing Shotgun.
    """

requires = [
    "cmake-3+",
    "pip-19+",
    "python-2.7+<3"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "shotgun_python_api-{version}".format(version=str(version))

def commands():
    env.PYTHONPATH.prepend("{root}")
