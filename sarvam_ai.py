from dotenv import load_dotenv
import os

load_dotenv()

from sarvamai import SarvamAI

client = SarvamAI(
    api_subscription_key=os.getenv("sarvam_api_key")
)

response = client.text.translate(
    input="Hi, My Name is Durga Prasad, iam a Fullstack developer.",
    source_language_code="auto",
    target_language_code="gu-IN",
    speaker_gender="Male"
)

print(response)
