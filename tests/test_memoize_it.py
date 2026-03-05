"""Tests for memoize-it."""

import pytest
from memoize_it import it


class TestIt:
    """Test suite for it."""

    def test_basic(self):
        """Test basic usage."""
        result = it("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            it("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = it(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
