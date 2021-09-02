from setuptools import setup

setup(
    name='SE-Homework-2b',
    version=open('VERSION', 'r').read().strip(),
    author='rdeodha',
    author_email='rdeodha@ncsu.edu',
    license='MIT',
    url='https://github.com/SN-18/SE-Homework-2b',

    install_requires=open('requirements.txt').readlines(),

    description='Homework-2b Repo',
    long_description="""\
        This repo is being used as a
        example repo for Homework-2b.
      """,
    keywords=['python', 'homework-2b'],
    classifiers=[
          'License :: OSI Approved :: MIT License',
          "Programming Language :: Python",
          "Development Status :: 1 - Planning",
          "Intended Audience :: Developers",
          "Topic :: Software Development",
    ],

    packages=["code"],
)
