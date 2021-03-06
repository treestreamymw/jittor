error_msg = """Jittor only supports Ubuntu>=16.04 currently.
For other OS, use Jittor may be risky.
We strongly recommended docker installation:

# CPU only
>>> docker run -it --network host jittor/jittor
# CPU and CUDA
>>> docker run -it --network host jittor/jittor-cuda

Reference:
1. Windows/Mac/Linux通过Docker安装计图: https://cg.cs.tsinghua.edu.cn/jittor/tutorial/2020-5-15-00-00-docker/
"""
from warnings import warn
try:
    with open("/etc/os-release", "r", encoding='utf8') as f:
        s = f.read().splitlines()
        m = {}
        for line in s:
            a = line.split('=')
            m[a[0]] = a[1].replace("\"", "")
    assert m["NAME"] == "Ubuntu" and float(m["VERSION_ID"])>16, error_msg
except Exception as e:
    print(e)
    warn(error_msg)

import setuptools
from setuptools import setup, find_packages
import os

path = os.path.dirname(__file__)
with open(os.path.join(path, "README.md"), "r", encoding='utf8') as fh:
    long_description = fh.read()

with open(os.path.join(path, "python/jittor/__init__.py"), "r", encoding='utf8') as fh:
    for line in fh:
        if line.startswith('__version__'):
            version = line.split("'")[1]
            break
    else:
        raise RuntimeError("Unable to find version string.")

setuptools.setup(
    name='jittor',  
    version=version,
    # scripts=[],
    author="Jittor Group",
    author_email="ran.donglang@gmail.com",
    description="a Just-in-time(JIT) deep learning framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://jittor.org",
    # packages=setuptools.find_packages(),
    python_requires='>=3.7',

    packages=["jittor", "jittor.test", "jittor.models", "jittor.utils", "jittor_utils"],
    package_dir={'': os.path.join(path, 'python')},
    package_data={'': ['*', '*/*', '*/*/*','*/*/*/*','*/*/*/*/*','*/*/*/*/*/*']},
    # include_package_data=True,
    install_requires=[
        "pybind11",
        "numpy",
        "tqdm",
        "pillow",
        "astunparse",
    ],
 )

# upload to pip:
# rm -rf dist && python3.7 ./setup.py sdist && python3.7 -m twine upload dist/*
