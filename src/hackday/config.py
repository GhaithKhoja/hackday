"""hackday development configuration."""
import pathlib
# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'
# Secret key for encrypting cookies
SECRET_KEY = b"\xa1\xe4\x83\x95\xb4\xf1\x8d\x14\xaa\x89\xc5\x02\x66\xca\xb7\x12\x39\xf4\x88\x67"
SESSION_COOKIE_NAME = 'login'
# File Upload to var/uploads/
hackday_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = hackday_ROOT / 'var' / 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
