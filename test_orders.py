def test_sample_order_id(sample_order):
    assert sample_order["order_id"] > 0

def test_sample_status_str(sample_order):
    assert isinstance(sample_order["status"], str)

def test_sample_total_num(sample_order):
    assert sample_order["total"] > 0

def test_sample_items_empty(sample_order):
    assert len(sample_order["items"]) > 0
