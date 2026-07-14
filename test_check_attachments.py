from check_attachments import check_attachments

def test_flags_pass_with_no_attachments():
    test_cases = [
        {"id": "TC001", "status": "Pass", "attachments": 0}
    ]
    result = check_attachments(test_cases)
    assert result["summary"]["total_flagged"] == 1

def test_does_not_flag_fail_with_no_attachments():
    test_cases = [
        {"id": "TC002", "status": "Fail", "attachments": 0}
    ]
    result = check_attachments(test_cases)
    assert result["summary"]["total_flagged"] == 0

def test_does_not_flag_pass_with_attachments():
    test_cases = [
        {"id": "TC003", "status": "Pass", "attachments": 2}
    ]
    result = check_attachments(test_cases)
    assert result["summary"]["total_flagged"] == 0

def test_total_checked_is_correct():
    test_cases = [
        {"id": "TC001", "status": "Pass", "attachments": 2},
        {"id": "TC002", "status": "Pass", "attachments": 0},
        {"id": "TC003", "status": "Fail", "attachments": 0}
    ]
    result = check_attachments(test_cases)
    assert result["summary"]["total_checked"] == 3