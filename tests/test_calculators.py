from app.calculators import (calculate_subtotal,calculate_discount,calculate_total)

import pytest


def test_calculate_subtotal_multiplies_price_by_quantity():
    # Arrange
    unit_price = 2500
    quantity = 30

    # Act
    subtotal = calculate_subtotal(unit_price, quantity)

    # Assert
    assert subtotal == 75000
    



def test_calculate_discount_returns_correct_discount():
    # Arrange
    subtotal = 120000
    discount_percentage = 15

    # Act
    discount = calculate_discount(subtotal, discount_percentage)

    # Assert
    assert discount == 18000


def test_calculate_discount_with_zero_percentage():
    # Arrange
    subtotal = 45000
    discount_percentage = 0

    # Act
    discount = calculate_discount(subtotal, discount_percentage)

    # Assert
    assert discount == 0


def test_calculate_discount_raises_error_for_negative_subtotal():
    # Arrange
    subtotal = -50000
    discount_percentage = 20

    # Act & Assert
    with pytest.raises(ValueError):
        calculate_discount(subtotal, discount_percentage)


def test_calculate_discount_raises_error_for_invalid_percentage():
    # Arrange
    subtotal = 80000
    discount_percentage = 150

    # Act & Assert
    with pytest.raises(ValueError):
        calculate_discount(subtotal, discount_percentage)


def test_calculate_total_without_discount():
    # Arrange
    unit_price = 3500
    quantity = 12

    # Act
    total = calculate_total(unit_price, quantity)

    # Assert
    assert total == 42000


def test_calculate_total_with_discount():
    # Arrange
    unit_price = 5000
    quantity = 18
    discount_percentage = 25

    # Act
    total = calculate_total(unit_price, quantity, discount_percentage)

    # Assert
    assert total == 67500


