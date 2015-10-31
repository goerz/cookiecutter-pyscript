# {{ cookiecutter.project_name }} #

{{ cookiecutter.description }}

Author: {{ cookiecutter.author_name }} <<{{ cookiecutter.author_email }}>>

Website: [Github][]

[Github]: {{ cookiecutter.url }}#{{ cookiecutter.project_name }}


## Installation ##

It is strongly recommended that you use [virtualenv][]/[pipsi][]/[conda env][].
Activate your environment, and then run

    pip install {{ cookiecutter.project_name }}

This will install `{{ cookiecutter.script_name }}` in the environment's `bin` folder.

[virtualenv]: http://docs.python-guide.org/en/latest/dev/virtualenvs/
[pipsi]: https://github.com/mitsuhiko/pipsi#pipsi
[conda env]: http://conda.pydata.org/docs/using/envs.html


## Usage ##

See `{{ cookiecutter.script_name }} -h`


## License ##
{% if cookiecutter.license == 'GPL'%}
This software is available under the terms of the GPLv2. See [LICENSE][] for
details.
{% elif cookiecutter.license == "Public Domain" %}
This software is in the public domain. See [LICENSE][] for details.
{% else %}
This software is available under the terms of the MIT license. See [LICENSE][]
for details.
{% endif %}
[LICENSE]: LICENSE
