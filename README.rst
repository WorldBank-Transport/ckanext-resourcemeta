
====================
ckanext-resourcemeta
====================

CKAN extension adding metadata fields to resources.

----------------------------------
Included Resource Metadata fields
----------------------------------

- ``release_date``
- ``geographical_coverage``
- ``exceptions``
- ``formulas``
- ``definitions``
- ``units_used``
- ``unique_identifier_field``
- ``coordinate_reference_system``

------------
Requirements
------------

CKAN_


------------
Installation
------------

To install ckanext-resourcemeta:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-resourcemeta Python package into your virtual environment::

     pip install git+https://github.com/WorldBank-Transport/ckanext-resourcemeta.git

3. Add ``resourcemeta`` to the ``ckan.plugins`` setting in your CKAN
   config file, for example in your ``/etc/ckan/default/production.ini``
   or in your ``development.ini`` file

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload

~~~~
NOTE
~~~~
If you have multiple plugins overriding resource templates you may need to add ``resourcemeta``
before those plugins in your ``ckan.plugins`` setting, for example ::

    ckan.plugins = ... resourcemeta other_resource_template_plugin


------------------------
Development Installation
------------------------

To install ckanext-resourcemeta for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/WorldBank-Transport/ckanext-resourcemeta.git
    cd ckanext-resourcemeta
    python setup.py develop

Then add ``resourcemeta`` to the ``ckan.plugins`` setting in your CKAN.


If you would like to contribute source code to this plugin feel free to fork the github repository
https://github.com/WorldBank-Transport/ckanext-resourcemeta and set it as an ``upstream`` remote. For more information about forking a github repostiry check https://help.github.com/articles/fork-a-repo/ or search for additional online resources.


.. _CKAN: http://ckan.org
