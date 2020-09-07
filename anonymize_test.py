import anonymize
import secrets

def test_hash():
    email = secrets.token_hex(10)
    assert anonymize.verify_hash(email, anonymize.hash_email(email))
