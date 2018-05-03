from django.contrib.auth.hashers import PBKDF2PasswordHasher

class APPENCRYPEPASS(PBKDF2PasswordHasher):
    """
    Alternate PBKDF2 hasher which uses SHA1, the default PRF
    recommended by PKCS #5. This is compatible with other
    implementations of PBKDF2, such as openssl's
    PKCS5_PBKDF2_HMAC_SHA1().
    """
    algorithm = "pbkdf2_sha1_cas"
    iterations = 10
   