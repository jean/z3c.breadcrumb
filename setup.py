#!python
from setuptools import setup, find_packages

setup(name='z3c.breadcrumb',
      version='0.1.0',
      author = "Zope Community",
      author_email = "zope3-dev@zope.org",
      license = "ZPL 2.1",
      keywords = "breadcrumb zope zope3",
      url='http://svn.zope.org/z3c.breadcrumb',

      zip_safe=False,
      packages=find_packages('src'),
      include_package_data=True,
      package_dir = {'':'src'},
      namespace_packages=['z3c',],
      install_requires=[
          'setuptools',
          ],
     )

