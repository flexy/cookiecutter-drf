class VersionMixin(object):
    def _get_versioned_class(self, attribute):
        attribute = getattr(self, attribute)
        version = self.request.version

        # Return default if version is not specified
        if not version:
            return attribute['default']

        try:
            # Return version
            return attribute[version]
        except KeyError:
            # Return default if version not found
            return attribute['default']

    def get_filterset_class(self):
        try:
            # Return appropriate filterset for version
            return self._get_versioned_class('filterset_classes')
        except AttributeError:
            # If filterset_classes is not set, don't do anything
            return super().get_filterset_class()

    def get_serializer_class(self):
        try:
            # Return appropriate serializer for version
            return self._get_versioned_class('serializer_classes')
        except AttributeError:
            # If serializer_classes is not set, don't do anything
            return super().get_serializer_class()
