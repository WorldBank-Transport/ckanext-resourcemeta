from datetime import datetime
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

try:
    from ckan.lib.plugins import DefaultTranslation
except ImportError:
    class DefaultTranslation():
        pass


class ResourcemetaPlugin(plugins.SingletonPlugin,
                         toolkit.DefaultDatasetForm,
                         DefaultTranslation):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IDatasetForm)
    plugins.implements(plugins.IResourceController)

    try:
        plugins.implements(plugins.ITranslation)
    except AttributeError:
        pass

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
            'aggregation_level': [
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
            'aggregation_level': [
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
        return schema

    def before_create(self, context, resource):
        pass

    def after_create(self, context, resource):
        pass

    def before_update(self, context, current, resource):
        resource['last_modified'] = datetime.utcnow()

    def after_update(self, context, resource):
        pass

    def before_delete(self, context, resource, resources):
        pass

    def after_delete(self, context, resources):
        pass

    def before_show(self, resource):
        pass

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return False

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []
