# ⚖️ Instagram Legal Bot — Free Auto-Poster

Automatically posts legal tips to Instagram **twice a day** using:
- 🤖 **Gemini AI** (free) — writes captions
- 🎨 **Pollinations.ai** (free) — generates images
- 📸 **Instagram Graph API** (free) — posts content
- ⚙️ **GitHub Actions** (free) — runs automatically

---

## 📁 File Structure

```
your-repo/
│
├── instagram_bot.py          ← Main bot script
├── requirements.txt          ← Python dependencies
├── .github/
│   └── workflows/
│       └── post.yml          ← Auto-run schedule
└── README.md
```

---

## 🚀 Setup Guide (One Time Only)

### Step 1 — Get Free Gemini API Key
1. Go to → https://aistudio.google.com/app/apikey
2. Click **"Create API Key"**
3. Copy the key — you'll need it in Step 4

---

### Step 2 — Setup Instagram for API Access
1. Convert your Instagram to a **Creator or Business account**
   - Go to Settings → Account → Switch to Professional Account
2. Go to → https://developers.facebook.com
3. Click **"My Apps"** → **"Create App"**
4. Choose **"Business"** type
5. Add the **"Instagram Graph API"** product
6. Link your **Facebook Page** to your Instagram account
7. Go to **Graph API Explorer** → generate a **User Access Token**
   - Select permissions: `instagram_basic`, `instagram_content_publish`
8. Get your **Instagram User ID**:
   ```
   GET https://graph.facebook.com/v19.0/me/accounts?access_token=YOUR_TOKEN
   ```
   Then:
   ```
   GET https://graph.facebook.com/v19.0/{page_id}?fields=instagram_business_account&access_token=YOUR_TOKEN
   ```

> ⚠️ **Note**: The default token expires in 60 days.
> To get a long-lived token (60 days), use:
> ```
> GET https://graph.facebook.com/v19.0/oauth/access_token
>   ?grant_type=fb_exchange_token
>   &client_id={app_id}
>   &client_secret={app_secret}
>   &fb_exchange_token={short_lived_token}
> ```

---

### Step 3 — Create GitHub Repository
1. Go to → https://github.com/new
2. Create a **new private repository** (e.g. `legal-insta-bot`)
3. Upload all files:
   - `instagram_bot.py`
   - `requirements.txt`
   - `.github/workflows/post.yml`

---

### Step 4 — Add Secrets to GitHub
1. In your repo → **Settings** → **Secrets and variables** → **Actions**
2. Click **"New repository secret"** and add these 3 secrets:

| Secret Name | Value |
|---|---|
| `GEMINI_API_KEY` | Your Gemini API key from Step 1 |
| `IG_USER_ID` | Your Instagram Business User ID |
| `IG_ACCESS_TOKEN` | Your Instagram Access Token |

---

### Step 5 — Test It Manually
1. Go to your repo → **Actions** tab
2. Click **"Instagram Legal Bot"**
3. Click **"Run workflow"** → **"Run workflow"**
4. Watch the logs — you should see ✅ at each step
5. Check your Instagram — post should appear! 🎉

---

## ⏰ Posting Schedule

| Time (IST) | UTC Cron |
|---|---|
| 9:00 AM | `30 3 * * *` |
| 7:00 PM | `30 13 * * *` |

To change timing, edit `.github/workflows/post.yml` and update the cron values.
Use → https://crontab.guru to calculate UTC time from IST.

---

## 📝 Customizing Content

In `instagram_bot.py`, you can edit:

- **`LEGAL_TOPICS`** list → add/remove topics you want to post about
- **`POST_STYLES`** list → change the style of posts
- The **Gemini prompt** → adjust tone, length, language (e.g. add Hindi)

---

## 💡 Tips for Growth

- ✅ Post consistently (the bot handles this!)
- ✅ Reply to comments manually — Instagram rewards engagement
- ✅ Use Instagram Stories (manual) to complement bot posts
- ✅ Add location tags manually when possible
- ❌ Don't use any other bots for likes/follows — risk of ban

---

## 🔧 Troubleshooting

| Error | Fix |
|---|---|
| `Missing environment variables` | Check GitHub Secrets are named exactly right |
| `400 Bad Request` from Instagram | Access token expired — regenerate it |
| `Image not processed` | Pollinations.ai was slow — retry manually |
| Bot not running on schedule | GitHub Actions may delay by up to 15 min |

---

## 🆓 Total Cost: ₹0

Everything used is on a free tier. No credit card needed.
