name = 'infi.clickhouse_orm'
namespace_packages = ['infi']
install_requires = [
    'iso8601 >= 0.1.12',
    'pytz',
    'requests',
    'setuptools',
    'six'
    ]
console_scripts = []
gui_scripts = []
package_data = []
homepage = 'https://github.com/Infinidat/infi.clickhouse_orm'


SETUP_INFO = dict(
    name = name,
    version = 'asd',
    author = 'Dmitry',
    author_email = 'a71d97l747@gmail.com',

    url = homepage,
    license = 'BSD',
    description = "asd",

    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers = [
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Database"
    ],

    install_requires = install_requires,
    namespace_packages = namespace_packages,

    package_dir = {'': 'src'},
    package_data = {'': package_data},
    include_package_data = True,
    zip_safe = False,

    entry_points = dict(
        console_scripts = console_scripts,
        gui_scripts = gui_scripts,
        ),
)

if SETUP_INFO['url'] is None:
    _ = SETUP_INFO.pop('url')


def setup():
    from setuptools import setup as _setup
    from setuptools import find_packages
    SETUP_INFO['packages'] = find_packages('src')
    _setup(**SETUP_INFO)


if __name__ == '__main__':
    setup()

