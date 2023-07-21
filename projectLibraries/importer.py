def import_all_libraries(lib: list = [], sub_lib: list = [], lib_as: list = []) -> bool:
    """
    Download and import lists of libraries and submodules. 

    Args:
        lib (list): A list of strings which are names of libraries to be downloaded and imported.
        sub_lib (list): A list of lists of strings, which are pairs of submodules to be downloaded and imported, and the library in which they are found.
        lib_as (list): A list of lists of strings, which are pairs of libraries to be downloaded and imported, and the name by which they should be imported.
    Returns: 
        bool: Always returns True
    """

    import_libraries(lib)
    import_submodules(sub_lib)
    import_libs(lib_as)

    return True

def import_libraries(lib: list = []) -> bool:
    """
    Download and import the libraries from a list.

    Arg:
        lib (list): A list of strings which are names of libraries to be downloaded and imported.

    Returns:
        bool: Always returns True
    """
    import subprocess
    import importlib

    global_vars = globals()

    for library in lib:
        try:
            imported_module = importlib.import_module(library)
            global_vars[library] = imported_module
            print(f"Successfully imported: {library}")

        except ImportError:
            print(f"Installing {library}...")

            try:
                subprocess.check_call(["pip", "install", library])
                print(f"Successfully installed: {library}")

                imported_module = importlib.import_module(library)
                global_vars[library] = imported_module
                print(f"Successfully imported: {library}")

            except (subprocess.CalledProcessError, ImportError):
                print(f"Failed to install and import: {library}")

    return True


def import_submodules(sub_lib: list = []) -> bool:
    """
    Download and import the submodules of given libraries from a list of lists.

    Arg:
        sub_lib (list): A list of lists of strings, which are pairs of submodules to be downloaded and imported, and the library in which they are found.

    Returns:
        bool: Always returns True
    """
    import subprocess
    import importlib

    global_vars = globals()

    for library, submodule in sub_lib:
        try:
            module = importlib.import_module(library)
            imported_submodule = getattr(module, submodule)
            global_vars[submodule] = imported_submodule
            print(f"Successfully imported: {library}.{submodule}")

        except (ImportError, AttributeError):

            print(f"Installing {library}...")

            try:
                subprocess.check_call(["pip", "install", library])
                print(f"Successfully installed: {library}")

                module = importlib.import_module(library)
                imported_submodule = getattr(module, submodule)
                global_vars[submodule] = imported_submodule
                print(f"Successfully imported: {library}.{submodule}")

            except (subprocess.CalledProcessError, ImportError, AttributeError):
                print(f"Failed to install and import: {library}.{submodule}")

    return True


def import_libs(lib_as: list = []) -> bool:
    """
    Download and import libraries from a list of lists under a specific name.

    Arg:
        sub_lib (list): A list of lists of strings, which are pairs of submodules to be downloaded and imported, and the library in which they are found.

    Returns:
        bool: Always returns True
    """
    import subprocess
    import importlib

    global_vars = globals()

    for library, import_name in lib_as:
        try:
            imported_module = importlib.import_module(library)
            global_vars[import_name] = imported_module
            print(f"Successfully imported: {library} as {import_name}")

        except ImportError:
            print(f"Installing {library}...")

            try:
                subprocess.check_call(["pip", "install", library])
                print(f"Successfully installed: {library}")

                imported_module = importlib.import_module(library)
                global_vars[import_name] = imported_module
                print(f"Successfully imported: {library} as {import_name}")

            except (subprocess.CalledProcessError, ImportError):
                print(f"Failed to install and import: {library} as {import_name}")

    return True
