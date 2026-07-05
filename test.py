from core.filter import filtering_and_tagging
from core.scorer import score_articles
from email_digest.builder import build_email_html
from email_digest.sender import send_digest_email


# 1. Input: Dummy Data (Simulating the scraper)
dummy_data = [
    {
        "title": "AI Revolution in Pakistan",
        "link": "https://example.com/1",
        "body": "The AI sector is booming. Pakistan is leading in AI adoption.",
        "source": "propakistani"
    },
    {
        "title": "New Global Smartphone Launch",
        "link": "https://example.com/2",
        "body": "A new smartphone was launched globally today.",
        "source": "techxplore"
    },
    {
        "title": "Local Weather Update",
        "link": "https://example.com/3",
        "body": "It is raining in Islamabad today, bring an umbrella.",
        "source": "propakistani"
    }
]

print("🚀 Starting Pipeline Test...")

# 2. Process Data (The Brain)
print("🧠 Filtering and Scoring articles...")
filtered_data = filtering_and_tagging(dummy_data)
scored_data = score_articles(filtered_data)

print(f"✅ Filtered down to {len(scored_data)} tech articles.")

# 3. Build the Email HTML (The Builder)
print("🎨 Building HTML email template...")
final_html = build_email_html(scored_data)

# 4. Send the Email (The Postman)
print("📨 Attempting to send Email Delivery Test...")
success = send_digest_email(final_html)

if success:
    print("🎉 Test Complete! Please check your email inbox.")
else:
    print("❌ Test Failed. Please check your terminal errors and ensure your .env file is correct.")