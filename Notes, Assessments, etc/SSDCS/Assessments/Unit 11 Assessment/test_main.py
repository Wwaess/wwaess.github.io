from main import (
    SecureStrategy,
    InsecureStrategy,
)
import pytest

def test_brute_force_lockout():
    strategy = SecureStrategy()
    username = "test_user"
    
    # Simulate failed attempts
    for _ in range(5):
        strategy.record_failure(username)
    
    with pytest.raises(Exception):
        strategy.apply_login_rate_limit(username)
    

def test_dos_protection():
    strategy = SecureStrategy()
    username = "test_user"
    
    for _ in range(11):
        try:
            strategy.apply_request_rate_limit(username)
        except Exception:
            break
    
    with pytest.raises(Exception):
        strategy.apply_request_rate_limit(username)

def test_injection_allowed_insecure():
    strategy = InsecureStrategy()
    
    malicious = "test; DROP TABLE users; --"
    
    result = strategy.validate_input(malicious)
    
    assert result == malicious