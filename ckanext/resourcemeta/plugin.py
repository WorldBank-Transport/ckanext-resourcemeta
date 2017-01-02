import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class ResourcemetaPlugin(plugins.SingletonPlugin,
                         toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IDatasetForm)

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'resourcemeta')

    def _modify_package_schema(self, schema):
        schema['resources'].update({
            'release_date': [
                toolkit.get_validator('ignore_missing'),
                toolkit.get_converter('convert_to_extras')
            ]
        })
        schema['resources'].update({
            'geographical_coverage': [
                toolkit.get_validator('ignore_missing'),
                toolkit.get_converter('convert_to_extras')
            ]
        })
        schema['resources'].update({
            'exceptions': [
                toolkit.get_validator('ignore_missing'),
                toolkit.get_converter('convert_to_extras')
            ]
        })
        schema['resources'].update({
            'formulas': [
                tk.get_validator('ignore_missing'),
                tk.get_converter('convert_to_extras')
            ]
        })
        schema['resources'].update({
            'definitions': [
                tk.get_validator('ignore_missing'),
                tk.get_converter('convert_to_extras')
            ]
        })
        schema['resources'].update({
            'units_used': [
                tk.get_validator('ignore_missing'),
                tk.get_converter('convert_to_extras')
            ]
        })
        schema['resources'].update({
            'unique_identifier_field': [
                tk.get_validator('ignore_missing'),
                tk.get_converter('convert_to_extras')
            ]
        })
        schema['resources'].update({
            'coordinate_reference_system': [
                tk.get_validator('ignore_missing'),
                tk.get_converter('convert_to_extras')
            ]
        })
        return schema

    def create_package_schema(self):
        schema = super(ResourcemetaPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(ResourcemetaPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(ResourcemetaPlugin, self).show_package_schema()
        schema['resources'].update({
            'release_date': [
                toolkit.get_validator('ignore_missing'),
                toolkit.get_converter('convert_from_extras')
            ]
        })
        schema['resources'].update({
            'geographical_coverage': [
                toolkit.get_validator('ignore_missing'),
                toolkit.get_converter('convert_from_extras')
            ]
        })
        schema['resources'].update({
            'exceptions': [
                toolkit.get_validator('ignore_missing'),
                toolkit.get_converter('convert_from_extras')
            ]
        })
        schema['resources'].update({
            'formulas': [
                tk.get_validator('ignore_missing'),
                tk.get_converter('convert_from_extras')
            ]
        })
        schema['resources'].update({
            'definitions': [
                tk.get_validator('ignore_missing'),
                tk.get_converter('convert_from_extras')
            ]
        })
        schema['resources'].update({
            'units_used': [
                tk.get_validator('ignore_missing'),
                tk.get_converter('convert_from_extras')
            ]
        })
        schema['resources'].update({
            'unique_identifier_field': [
                tk.get_validator('ignore_missing'),
                tk.get_converter('convert_from_extras')
            ]
        })
        schema['resources'].update({
            'coordinate_reference_system': [
                tk.get_validator('ignore_missing'),
                tk.get_converter('convert_from_extras')
            ]
        })
        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return False

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []
