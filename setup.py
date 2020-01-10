from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("impl/cython_impl_function.pyx")
)