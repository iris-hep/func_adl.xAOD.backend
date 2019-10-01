from setuptools import find_namespace_packages
from distutils.core import setup

xaod_template_files = []
setup(name="func_adl.xAOD.backend",
      version='1.0.0-alpha.1',
      packages=find_namespace_packages(exclude=['tests']),
      scripts=[],
      description="Functional Analysis Description Language for xAOD backends",
      long_description='Implement backend and front end analysis languages',
      author="G. Watts (IRIS-HEP)",
      author_email="gwatts@uw.edu",
      maintainer="Gordon Watts (IRIS-HEP)",
      maintainer_email="gwatts@uw.edu",
      url="http://iris-hep.org",
      download_url="http://iris-hep.org",
      license="TBD",
      test_suite="tests",
      install_requires=["requests>=2.0.0", "pandas>=0.24.0", "uproot>=3.7.0", "retry>=0.9.2", "Jinja2>=2.10"],
      setup_requires=["pytest-runner"],
      tests_require=["pytest>=3.9"],
      classifiers=[
                   # "Development Status :: 1 - Planning",
                   "Development Status :: 2 - Pre-Alpha",
                   # "Development Status :: 3 - Alpha",
                   # "Development Status :: 4 - Beta",
                   # "Development Status :: 5 - Production/Stable",
                   # "Development Status :: 6 - Mature",
                   "Intended Audience :: Developers",
                   "Intended Audience :: Information Technology",
                   "Programming Language :: Python",
                   "Programming Language :: Python  :: 3.7",
                   "Topic :: Software Development",
                   "Topic :: Data Analysis",
                   "Topic :: Utilities",
      ],
      data_files=[],
      platforms="Any",
      )
