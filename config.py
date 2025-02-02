import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_ID = os.getenv("API_ID", "27805819")
API_HASH = os.getenv("API_HASH", "7372a27cd4dc20b792bb117b038db7ef")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7481943486:AAEWhDdfqQEE9SA3vBQb4MZ_MsM8p3hgSVc")
SESSION = os.getenv("SESSION", "BQGoSHsAt-kneFsPDgFBXUjxim7d8PT6nMfQZUATeOuSXRwwL1o43z63EytXmVINC_xnEIcMP1wz8G5PNQvJQGl8iSj8UC9KRrTnNaQyD7fb7G381ft3_2hBVAgioO4l8ollcltDtCJRFBsFhUN5dOPwfVA8WNCQ2OooVZPa9n_segouxGxLB7p51PdwQ0ewu94P2COz0OZQ5Ieu3bev0nKQ9iPuAxjaO4ryTTYkVmJQF4tgSJ3amoVY9ad3ldteq1tAUgdK5HJqVhDO8xX7ngxEHhjjVKgDIrQyt8LuX4hKaCve2izbIsid2pcuMePPpeB92wHte2ZzTzv1yeiH_AwX_7G-bQAAAAG9QfXgAA")

# Ensure all required variables are set
required_vars = ["API_ID", "API_HASH", "BOT_TOKEN", "SESSION"]
missing_vars = [var for var in required_vars if not globals()[var]]

if missing_vars:
    raise RuntimeError(f"Missing required environment variables: {', '.join(missing_vars)}")