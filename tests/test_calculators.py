from app.calculators import calculate_subtotal

def test_calculate_subtotal_multiplies_price_by_quantity():
    # Arrange
    unit_price = 2500
    quantity = 30

    # Act
    subtotal = calculate_subtotal(unit_price, quantity)

    # Assert
    assert subtotal == 75000
    
