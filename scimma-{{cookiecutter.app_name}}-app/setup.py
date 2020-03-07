import os
from setuptools import setup

# read in README
this_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_dir, 'README.md'), 'rb') as f:
    long_description = f.read().decode().strip()

# requirements
install_requires = [
    "scimma-client >= 0.0.4",
]
extras_require = {
    'dev': ['pytest', 'pytest-console-scripts', 'pytest-cov', 'flake8', 'flake8-black'],
    'docs': ['sphinx', 'sphinx_rtd_theme', 'sphinxcontrib-programoutput'],
}

setup(
    name = 'scimma-{{ cookiecutter.app_name }}-app',
    description = '{{ cookiecutter.app_description }}',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = '{{ cookiecutter.git_url }}',
    author = '{{ cookiecutter.author_name }}',
    author_email = '{{ cookiecutter.author_email }}',
    license = 'BSD 3-Clause',

    packages = ['scimma.apps.{{ cookiecutter.app_name }}'],

    entry_points = {
        'console_scripts': [
            'scimma-{{ cookiecutter.app_name }} = scimma.apps.{{ cookiecutter.app_name }}.__main__:main',
        ],
    },

    python_requires = '>=3.6.*',
    install_requires = install_requires,
    extras_require = extras_require,
    setup_requires = ['setuptools_scm'],
    use_scm_version = {
        'write_to': 'scimma/apps/{{ cookiecutter.app_name }}/_version.py'
    },

    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'License :: OSI Approved :: BSD License',
    ],

)
