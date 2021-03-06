from setuptools import setup
import bioinfokit

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='bioinfokit',
      version=bioinfokit.__version__,

      # metadata
      author='Renesh Bedre',
      author_email='reneshbe@gmail.com',
      description='Bioinformatics data analysis and visualization',
      long_description=long_description,
      long_description_content_type="text/markdown",
      license='MIT',
      url='http://reneshbedre.github.io/',
      packages=['bioinfokit',],
      zip_safe=False,
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux, Mac",
      # "Topic :: Scientific/Engineering :: Bioinformatics",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
       ],

      install_requires=['pandas', 'numpy', 'matplotlib', 'scipy', 'scikit-learn', 'seaborn', 'matplotlib_venn',
                        'tabulate', 'termcolor', 'statsmodels', 'textwrap3', 'adjustText',],
      )