#!/usr/bin/env python
import setuptools


def get_version(filename):
    with open(filename) as in_fh:
        for line in in_fh:
            if line.startswith('__version__'):
                return line.split('=')[1].strip()[1:-1]
    raise ValueError("Cannot extract version from %s" % filename)


setuptools.setup(
    name="{{ cookiecutter.project_name }}",
    version=get_version("{{ cookiecutter.module_name }}.py"),
    url="{{ cookiecutter.url }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    description="{{ cookiecutter.description }}",
    install_requires=[
        'Click',
    ],
    extras_require={'dev': ['pytest',]},
    py_modules=['{{ cookiecutter.module_name }}'],
    entry_points='''
        [console_scripts]
        {{ cookiecutter.script_name }}={{ cookiecutter.module_name }}:main
    ''',
    classifiers=[
        'Environment :: Console',
        'Natural Language :: English',
        {%if cookiecutter.license == "GPL"%}'License :: OSI Approved :: GNU General Public License v2 (GPLv2),'{%elif cookiecutter.license == "Public Domain"%}'License :: Public Domain',{%else%}'License :: OSI Approved :: MIT License',{%endif%}
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
