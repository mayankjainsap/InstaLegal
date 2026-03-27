import os
import requests
import random
import time
from datetime import datetime

# ─────────────────────────────────────────
# CONFIG (loaded more robustly)
# ─────────────────────────────────────────
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "").strip(' "')
IG_USER_ID         = os.environ.get("IG_USER_ID", "").strip(' "')
IG_ACCESS_TOKEN    = os.environ.get("IG_ACCESS_TOKEN", "").strip(' "')
APP_LINK           = "https://www.legalaiassistant.in/"

# High-quality free models from OpenRouter (2026 verified IDs)
OPENROUTER_FREE_MODELS = [
    "openai/GPT-4o-mini:free"
]

# ─────────────────────────────────────────
#  CONTENT LIBRARY — Rich & Emotional
# ─────────────────────────────────────────

LEGAL_TOPICS = [
    {
        "topic": "tenant rights when landlord illegally locks you out",
        "scenario": "Your landlord changed the locks while you were at work",
        "emotion": "shock and panic"
    },
    {
        "topic": "how police CANNOT arrest you without following proper procedure",
        "scenario": "A family member gets arrested at midnight with no reason given",
        "emotion": "fear and helplessness"
    },
    {
        "topic": "consumer rights when you receive a defective product online",
        "scenario": "You ordered a Rs.15,000 phone and received a broken one",
        "emotion": "frustration and feeling cheated"
    },
    {
        "topic": "your rights if a bank wrongly deducts money from your account",
        "scenario": "You wake up to find Rs.10,000 missing from your account",
        "emotion": "panic and confusion"
    },
    {
        "topic": "how to legally get out of a bad job offer letter",
        "scenario": "Company gave you a fake offer letter with hidden conditions",
        "emotion": "betrayal and anger"
    },
    {
        "topic": "property rights when a builder delays possession for years",
        "scenario": "You paid full amount 3 years ago but still no flat",
        "emotion": "desperation and financial stress"
    },
    {
        "topic": "how to fight a fake cheque bounce case filed against you",
        "scenario": "Someone filed a false Section 138 case to harass you",
        "emotion": "fear of jail and reputation damage"
    },
    {
        "topic": "rights of women against workplace sexual harassment under POSH Act",
        "scenario": "A woman faces harassment from her senior at office",
        "emotion": "fear of speaking up and losing job"
    },
    {
        "topic": "how to claim insurance after hospital refuses cashless treatment",
        "scenario": "Hospital emergency demands Rs.2 lakh upfront despite valid insurance",
        "emotion": "medical emergency stress"
    },
    {
        "topic": "cyber fraud — what to do in first 24 hours after online money theft",
        "scenario": "You get a fake KYC call and Rs.50,000 vanishes from your account",
        "emotion": "panic and urgency"
    },
    {
        "topic": "RTI — how any citizen can demand answers from any government office",
        "scenario": "Government office ignores your application for 6 months",
        "emotion": "powerlessness against the system"
    },
    {
        "topic": "divorce rights and what a wife is legally entitled to",
        "scenario": "Woman in unhappy marriage does not know she has financial rights",
        "emotion": "feeling trapped and uninformed"
    },
    {
        "topic": "how to legally stop loan recovery agents from harassing you",
        "scenario": "Loan agents call you 30 times a day and threaten your family",
        "emotion": "harassment and mental stress"
    },
    {
        "topic": "employee rights when company fires you without notice or reason",
        "scenario": "HR calls you on Monday morning and says today is your last day",
        "emotion": "shock and financial fear"
    },
    {
        "topic": "how to file a police complaint online without going to the station",
        "scenario": "Police station refuses to register your FIR",
        "emotion": "feeling ignored by the system"
    },
    {
        "topic": "GST overcharging — what to do when a shop charges illegal GST",
        "scenario": "Restaurant bill shows GST applied incorrectly on your order",
        "emotion": "feeling robbed in small ways every day"
    },
    {
        "topic": "domestic violence — legal steps a victim can take immediately",
        "scenario": "Woman endures abuse but does not know she can get a protection order in 24 hours",
        "emotion": "fear and trapped feeling"
    },
    {
        "topic": "social media legal rights — when someone defames you online",
        "scenario": "An ex or rival posts false damaging things about you publicly",
        "emotion": "public humiliation and reputation damage"
    },
    {
        "topic": "rights when traffic police stop you and demand a bribe",
        "scenario": "Traffic cop threatens to seize your vehicle unless you pay cash",
        "emotion": "intimidation and injustice"
    },
    {
        "topic": "legal rights of senior citizens when family abandons them",
        "scenario": "Elderly parent is thrown out of their own house by adult children",
        "emotion": "heartbreak and abandonment"
    },
]

# 6 different viral post formats
POST_FORMATS = [
    "STORY_HOOK",
    "SHOCKING_FACT",
    "MYTH_BUSTER",
    "STEP_BY_STEP",
    "RIGHTS_REMINDER",
    "WARNING_POST",
]

# ─────────────────────────────────────────
#  STEP 1 — GENERATE VIRAL CAPTION
# ─────────────────────────────────────────
def generate_caption():
    item   = random.choice(LEGAL_TOPICS)
    fmt    = random.choice(POST_FORMATS)
    day    = datetime.now().strftime("%A")
    hour   = datetime.now().hour
    timing = "morning" if hour < 12 else ("evening" if hour >= 17 else "afternoon")

    format_instructions = {
        "STORY_HOOK": f"""Open with this real-life scenario in 2 dramatic lines:
Scenario: "{item['scenario']}" — capture the feeling of {item['emotion']}.
Then write: "Here is what the law says you can do RIGHT NOW:"
Then give 5 powerful numbered action steps.""",

        "SHOCKING_FACT": f"""Open with "SHOCKING BUT TRUE:" followed by the most surprising legal fact about: {item['topic']} that most Indians do not know.
Make it feel like a revelation. Use "Did you know that legally..."
Then explain what this means for common people in 4-5 bullet points.""",

        "MYTH_BUSTER": f"""Open with "MYTH:" — state the wrong belief most Indians have about: {item['topic']}.
Then write "REALITY:" and reveal the truth clearly and powerfully.
Then give 3-4 practical tips on how to use this legal knowledge.""",

        "STEP_BY_STEP": f"""Open with an urgent question: "What would YOU do if — {item['scenario']}?"
Then write: "Here are your EXACT legal steps:"
Give 5 clear numbered steps a common person can actually follow today.""",

        "RIGHTS_REMINDER": f"""Open with: "YOUR RIGHTS — SAVE THIS POST"
List 5-6 powerful rights related to: {item['topic']} starting each with "You have the RIGHT to..."
Make each right feel empowering and surprising to the reader.""",

        "WARNING_POST": f"""Open with: "WARNING: Most Indians fall into this legal trap with {item['topic']}."
Describe the common mistake that causes {item['emotion']}.
Then give 4 clear tips to protect yourself legally.""",
    }

    prompt = f"""You are India's most viral legal rights content creator on Instagram with 2 million followers.
Your posts are known for being POWERFUL, EMOTIONAL, and highly SHAREABLE.
You write for the common Indian — not for lawyers.

TODAY'S POST FORMAT: {fmt}
LEGAL TOPIC: {item['topic']}

{format_instructions[fmt]}

RULES TO MAKE THIS POST IMPRESSIVE AND VIRAL:
1. First line MUST stop the scroll — make it shocking, emotional, or intriguing. No generic openers.
2. Use powerful emojis strategically: use emojis like these where appropriate: STOP, WARNING, CHECK MARK, LIGHTBULB, SCALES OF JUSTICE, RED CIRCLE, PIN
3. Use a blank line between every point for easy mobile reading
4. Write short punchy sentences. Maximum 12 words per sentence.
5. Use ALL CAPS for emphasis on key words only (not full sentences)
6. Naturally include this app promotion using one of these varied phrasings:
   - "Get INSTANT legal answers 24/7 at {APP_LINK}"
   - "India's FREE AI Legal Assistant is here: {APP_LINK}"
   - "Ask any legal question RIGHT NOW at {APP_LINK}"
   - "FREE legal help at your fingertips: {APP_LINK}"
7. End with a powerful call to action like: "TAG someone who NEEDS to know this" or "SAVE this — you will need it someday"
8. End with 25 relevant hashtags mixing Hindi and English:
   Always include: #legalrights #knowyourrights #indianlaw #legaladvice #kanoonkijankari #legalindia #lawfacts #rightsofindians #legaltips #indiafacts
   Plus 15 more topic-specific hashtags
9. Total length: 200 to 300 words
10. Today is {day} {timing} — make it feel current if possible

THE GOAL: Make people feel "I did NOT know this!" and immediately want to SAVE and SHARE.

Return ONLY the Instagram caption. Nothing else. No commentary."""

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com",
        "X-Title": "Legal AI Instagram Bot"
    }

    last_error = None
    for model in OPENROUTER_FREE_MODELS:
        try:
            payload = {
                "model": model,
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "You are a viral Instagram content creator specializing in Indian legal rights. "
                            "Your posts are emotional, powerful, and always go viral because they speak directly "
                            "to common people's real problems. You write in simple English with relatable Indian context. "
                            "Every post you write makes people stop scrolling, feel empowered, and share immediately."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0.92,
                "max_tokens": 1200
            }

            response = requests.post(url, json=payload, headers=headers, timeout=50)
            response.raise_for_status()
            data = response.json()
            
            # Safe extraction of content
            choices = data.get("choices", [])
            if not choices or not choices[0].get("message", {}).get("content"):
                raise ValueError("Incomplete or empty response from model.")
                
            caption = choices[0]["message"]["content"].strip()

            # Fallback: ensure app link always appears
            if APP_LINK not in caption:
                caption += f"\n\n💡 Get FREE instant legal help 24/7 → {APP_LINK}"

            print(f"✅ Caption generated | Model: {model.split('/')[-1]} | Format: {fmt} | Topic: {item['topic'][:35]}...")
            return caption, item["topic"], fmt

        except Exception as e:
            print(f"⚠️  Model {model} failed: {str(e)[:50]}... trying next.")
            last_error = e
            continue

    raise last_error if last_error else Exception("All models failed")


# ─────────────────────────────────────────
#  STEP 2 — GENERATE STUNNING IMAGE
# ─────────────────────────────────────────
def generate_image_url(topic, fmt):
    # Premium cinematic visual style matched to post format
    style_map = {
        "STORY_HOOK":     "cinematic dramatic courtroom scene India, powerful emotional lighting, photorealistic, 8k ultra detailed",
        "SHOCKING_FACT":  "bold premium editorial design, deep navy blue background, gold scales of justice, glowing typography, award winning",
        "MYTH_BUSTER":    "split composition design, bold red versus green, modern professional infographic, vibrant high contrast",
        "STEP_BY_STEP":   "clean modern minimal design, numbered layout, Indian legal symbols, white and midnight blue, premium quality",
        "RIGHTS_REMINDER":"powerful constitutional poster, Constitution of India, bold impactful typography, tricolor gold accents, dramatic",
        "WARNING_POST":   "urgent alert design, deep red and black, bold warning symbols, serious dramatic tone, high contrast editorial",
    }

    style    = style_map.get(fmt, "premium legal illustration, striking visual, professional design, India, ultra detailed")
    keywords = topic.replace(" ", "+").replace(",", "").replace("'", "").replace(".", "")[:55]
    seed     = random.randint(10000, 99999)

    image_prompt = (
        f"Indian+legal+rights+{keywords}+"
        f"{style.replace(' ', '+').replace(',', '+')}"
    )
    image_url = (
        f"https://image.pollinations.ai/prompt/{image_prompt}"
        f"?width=1080&height=1080&nologo=true&enhance=true&seed={seed}"
    )

    print(f"✅ Image crafted | Style: {fmt}")
    return image_url


# ─────────────────────────────────────────
#  STEP 3 — POST TO INSTAGRAM GRAPH API
# ─────────────────────────────────────────
def post_to_instagram(image_url, caption):
    base_url = f"https://graph.facebook.com/v19.0/{IG_USER_ID}"
    headers = {"Authorization": f"Bearer {IG_ACCESS_TOKEN}"}

    # Safe debug info
    print(f"📡 API Version: v19.0 | Target ID: {IG_USER_ID[:4]}***{IG_USER_ID[-4:] if len(IG_USER_ID) > 4 else ''}")
    print(f"🔑 Token check: length={len(IG_ACCESS_TOKEN)}, prefix={IG_ACCESS_TOKEN[:7]}...")

    print("📤 Creating media container...")
    container_resp = requests.post(
        f"{base_url}/media",
        data={
            "image_url":    image_url,
            "caption":      caption,
        },
        headers=headers,
        timeout=30
    )
    container_resp.raise_for_status()
    container_id = container_resp.json().get("id")
    print(f"✅ Container created: {container_id}")

    print("⏳ Waiting for media to process...")
    time.sleep(12)

    for attempt in range(6):
        status_resp = requests.get(
            f"https://graph.facebook.com/v19.0/{container_id}",
            params={"fields": "status_code"},
            headers=headers,
            timeout=15
        )
        status = status_resp.json().get("status_code", "")
        if status == "FINISHED":
            print("✅ Media ready!")
            break
        print(f"  Status: {status} — retrying ({attempt+1}/6)...")
        time.sleep(8)

    print("🚀 Publishing to Instagram...")
    publish_resp = requests.post(
        f"{base_url}/media_publish",
        data={
            "creation_id":  container_id,
        },
        headers=headers,
        timeout=30
    )
    publish_resp.raise_for_status()
    post_id = publish_resp.json().get("id")
    print(f"✅ Posted! Post ID: {post_id}")
    return post_id


# ─────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────
def main():
    print("=" * 55)
    print(f"⚖️  Legal AI Instagram Bot — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 55)

    if not all([OPENROUTER_API_KEY, IG_USER_ID, IG_ACCESS_TOKEN]):
        raise ValueError(
            "Missing secrets! Check: OPENROUTER_API_KEY, IG_USER_ID, IG_ACCESS_TOKEN"
        )

    try:
        caption, topic, fmt = generate_caption()
        print(f"\n📝 Caption Preview:\n{caption[:200]}...\n")

        image_url = generate_image_url(topic, fmt)
        post_id   = post_to_instagram(image_url, caption)

        print("\n🎉 LIVE on Instagram! legalaiassistant.in is growing! 🚀")
        print(f"📊 Post ID: {post_id}")

    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e.response.status_code} — {e.response.text}")
        raise
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        raise


if __name__ == "__main__":
    main()
