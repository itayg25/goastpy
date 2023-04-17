import os
import sys
import ctypes
import subprocess
from ctypes import c_char_p
from threading import Lock, Thread

GO_LIBRARY = f"goastparser.so"


class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        # Now, imagine that the program has just been launched. Since there's no
        # Singleton instance yet, multiple threads can simultaneously pass the
        # previous conditional and reach this point almost at the same time. The
        # first of them will acquire lock and will proceed further, while the
        # rest will wait here.
        with cls._lock:
            # The first thread to acquire the lock, reaches this conditional,
            # goes inside and creates the Singleton instance. Once it leaves the
            # lock block, a thread that might have been waiting for the lock
            # release may then enter this section. But since the Singleton field
            # is already initialized, the thread won't create a new object.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class GoAstLib(metaclass=SingletonMeta):

    @staticmethod
    def __find_go_executable():
        go_executable = "go" + (".exe" if sys.platform == "win32" else "")
        for path in os.environ["PATH"].split(os.pathsep):
            executable_path = os.path.join(path.strip('"'), go_executable)
            if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
                return executable_path
        raise FileNotFoundError("Go executable not found in the system's PATH")

    @staticmethod
    def __build_go_library_if_not_exists():
        if not os.path.exists(GO_LIBRARY):
            print("Building Go shared library...")
            try:
                go_executable = GoAstLib.__find_go_executable()
            except FileNotFoundError as e:
                print(f"Error finding Go in path: {e}, trying to use default homebrew path")
                go_executable = '/opt/homebrew/bin/go'
            try:
                subprocess.check_call([go_executable, "build", "-o", GO_LIBRARY, "-buildmode=c-shared", "main.go",
                                       "goastparser_export.go"])
            except subprocess.CalledProcessError as e:
                print(f"Error building Go shared library: {e}")
                raise

    @staticmethod
    def __configure_go_function(go_lib):
        go_lib.ParseSourceCode.restype = c_char_p
        go_lib.ParseSourceCode.argtypes = [c_char_p]

    @staticmethod
    def __load_go_library():
        return ctypes.CDLL(os.path.join(os.path.dirname(__file__), GO_LIBRARY))

    def __init__(self):
        self.lib = self.__load_go_library()
        self.__configure_go_function(self.lib)

    @staticmethod
    def lib():
        return GoAstLib().lib
