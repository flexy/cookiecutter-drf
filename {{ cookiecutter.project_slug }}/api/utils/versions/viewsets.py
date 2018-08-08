class VersionMixin(object):
    def _get_versioned_class(self, attribute):
        return getattr(self, attribute)[self.request.version]

    def get_filterset_class(self):
        # If filterset_classes is not set, don't do anything
        if not hasattr(self, 'filterset_classes'):
            return super().get_filterset_class()

        # Return appropriate filterset for version
        return self._get_versioned_class('filterset_classes')

    def get_serializer_class(self):
        # If serializer_classes is not set, don't do anything
        if not hasattr(self, 'serializer_classes'):
            return super().get_serializer_class()

        # Return appropriate serializer for version
        return self._get_versioned_class('serializer_classes')
