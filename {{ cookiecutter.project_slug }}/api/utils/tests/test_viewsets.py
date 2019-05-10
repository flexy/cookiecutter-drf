import pytest

from ..versions.viewsets import VersionMixin


class TestVersionMixin:
    def _setup(self, mocker):
        # Setup class instance
        instance = VersionMixin()

        # Setup attributes
        instance.filterset_classes = {}
        instance.serializer_classes = {}
        instance.request = mocker.Mock()

        return instance

    def test_get_versioned_class(self, mocker):
        instance = self._setup(mocker)

        # Save values for later
        filterset_1 = "FilterSet1"
        filterset_default = "FilterSetDefault"

        # Check cases
        # No default, version not specified
        instance.request.version = None

        with pytest.raises(KeyError):
            instance._get_versioned_class("filterset_classes")

        # No default, version not found
        instance.request.version = "100.0"

        with pytest.raises(KeyError):
            instance._get_versioned_class("filterset_classes")

        # No default, version specified
        instance.request.version = "1.0"
        instance.filterset_classes["1.0"] = filterset_1

        result = instance._get_versioned_class("filterset_classes")
        assert result == filterset_1

        # Default, version not specified
        instance.request.version = None
        instance.filterset_classes["default"] = filterset_default

        result = instance._get_versioned_class("filterset_classes")
        assert result == filterset_default

        # Default, version not found
        instance.request.version = "100.0"

        result = instance._get_versioned_class("filterset_classes")
        assert result == filterset_default

        # Default, version specified
        instance.request.version = "1.0"

        result = instance._get_versioned_class("filterset_classes")
        assert result == filterset_1

    def test_get_filterset_class(self, mocker):
        instance = self._setup(mocker)

        # Patch methods
        versioned_class = mocker.Mock()
        instance._get_versioned_class = versioned_class

        # Check cases
        # Runs without error
        instance.get_filterset_class()

        versioned_class.assert_called_with("filterset_classes")

        # filterset_classes not found
        versioned_class.side_effect = AttributeError

        with pytest.raises(AttributeError) as error_info:
            instance.get_filterset_class()

        assert (
            error_info.value.args[0]
            == "'super' object has no attribute 'get_filterset_class'"
        )

    def test_get_serializer_class(self, mocker):
        instance = self._setup(mocker)

        # Patch methods
        versioned_class = mocker.Mock()
        instance._get_versioned_class = versioned_class

        # Check cases
        # Runs without error
        instance.get_serializer_class()

        versioned_class.assert_called_with("serializer_classes")

        # serializer_classes not found
        versioned_class.side_effect = AttributeError

        with pytest.raises(AttributeError) as error_info:
            instance.get_serializer_class()

        assert (
            error_info.value.args[0]
            == "'super' object has no attribute 'get_serializer_class'"
        )
