import os
from setuptools import setup

# read in README
this_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_dir, 'README.md'), 'rb') as f:
    long_description = f.read().decode().strip()

# requirements
install_requires = [
    "hop-client >= 0.2",
]
extras_require = {
    'dev': [
        'autopep8',
        'flake8',
        'pytest >= 5.0, < 5.4',
        'pytest-console-scripts',
        'pytest-cov',
    ],
    'docs': [
        'sphinx',
        'sphinx_rtd_theme',
        'sphinxcontrib-programoutput',
    ],
}

setup(
    name = 'hop-plugin-{{ cookiecutter.plugin_name }}',
    description = '{{ cookiecutter.plugin_description }}',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = '{{ cookiecutter.git_url }}',
    author = '{{ cookiecutter.author_name }}',
    author_email = '{{ cookiecutter.author_email }}',
    license = 'BSD 3-Clause',

    packages = ['hop.plugins'],

    entry_points = {'hop_plugin': ["{{ cookiecutter.plugin_name }}-plugin = hop.plugins.{{ cookiecutter.plugin_name }}"]},
    version = '0.0.1',

    python_requires = '>=3.6.*',
    install_requires = install_requires,
    extras_require = extras_require,
    zip_safe = False,

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
