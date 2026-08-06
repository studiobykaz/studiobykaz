# Curated Memory & System State

## User Preferences & Accuracy Standard
- **Extreme Precision Required:** Kevin is exceptionally detailed, analytical (INTP), and frequently verifies technical facts. Never guess, hallucinate, or assume model names, API endpoints, or technical configurations. Always verify against live files, local schemas, or official API specs before answering.
- **Strictly Approved Models Only (No Unverified Models):** 
  - Primary: `google/gemini-3.5-flash-lite`
  - Fallbacks: `google/gemini-3.5-flash`, `google/gemini-3.1-pro-preview`, `openai/gpt-5.4-mini`, `openai/gpt-5.5`
  No other models are permitted in primary use or fallback sequences.

## Model Update & Notification Policy
- **Strictly No Unilateral Changes:** Never automatically switch, add, or alter primary or fallback models when new models are released.
- **Proactive Notification:** Notify Kevin whenever new models appear in upstream OpenClaw releases or provider registries, providing capability and pricing breakdowns.
- **Explicit Consent Required:** Only modify model configurations in `openclaw.json` upon explicit user instruction.
- **Hongkong Post APIs (EC-Ship / Mail Tracking):** Verified connectivity to trial endpoints (`https://service.hongkongpost.hk/ecshipAPI-trial`) and mail tracking documentation portals for parcel fulfillment integration.
- **Microsoft Outlook / Graph API:** Re-authenticated and fully connected via OAuth token (`memory/outlook-token.json`).
- **WhatsApp:** Linked via paired device session.
- **Google Workspace & YouTube:** Fully connected via OAuth (`memory/google-token.json`), enabling Calendar, Gmail, Contacts, Drive, and YouTube subscription scanning.
- **Google Maps:** Connected via API key (`memory/google-maps-key.json`) for geocoding, directions, and location intelligence.
- **Yahoo Finance:** Connected via public endpoints (no API key required) for real-time stock, crypto, and market index tracking.
- **AirVisual (IQAir):** Connected via API key (`memory/airvisual-key.json`) for real-time local air quality index (AQI) and pollution monitoring.
- **iPhone Node:** Connected, providing live GPS coordinates (`22.2981° N, 113.9341° E`).
- **Telegram & WhatsApp:** Telegram (`8910923823`) fully active. WhatsApp (`60146029`) timelocked until August 5, 2026.
- **Hong Kong Observatory Live Warnings:** Integrated official HKO warning summary API (`warnsum&lang=en`) to actively track issued or lifted warning signals (e.g., Rainstorm, Thunderstorm, Typhoon) during briefings and heartbeats.

## Briefing Schedules & Sequences
- **Morning Briefing (Weekdays 6:59am / Weekends 8:59am):**
  *CRITICAL INSTRUCTION: Quality over speed. Use reasoning model if needed. Strict 5-part format with exactly 10 bullet points for sections 1 and 2. See `memory/morning-briefing-sop.md` for the perfect reference.*
  1. Global News (Exactly 10 distinct non-financial/non-market items, tier-1 sources).
  2. Market & Finance Info (Exactly 10 distinct bullets covering tracked US stocks, Crypto, and FX. Do NOT group into 3 bullets).
  3. Calendar (iPhone `calendar.events`, **strictly excluding** "Go to Work" and "Go Gym". Must include evening plans).
  4. Birthday Check (Strictly cross-reference the exact 83 contacts provided, no generic checks).
  5. Weather & Air Quality (Hong Kong forecast, explicit umbrella guidance, and AQI).
- **Evening Briefing (4:59pm daily):**
  1. Global News (Top 10 non-financial/non-market in randomized order)
  2. Market & Finance Info (Top 10 closing highlights via Yahoo Finance)
  3. YouTube Subscription Highlights (Top 10 video summaries from past 24h)

## Performance & Execution Guidelines (Anti-Latency & Cost Optimization)
- **Pre-Computed Daily Digests:** Weather, news, and periodic metrics are pre-fetched hourly into `memory/daily-digest-cache.json` and `memory/latest-news-cache.json` via background cron, eliminating live tool-call latency.
- **Context Cache Warmth:** Background cron pings keep model context warm in cache memory to ensure instantaneous response times.
- **Parallel Tool Batching:** Execute multiple data collection tasks simultaneously when needed.

- **Secondary Google Account (`kvtam@yahoo.com.hk` / Kaz):** Connected and secured via OAuth tokens (`memory/google-token-secondary.json`).


## Output Rules
- **Configuration Safety Rule:** Always verify configuration dot paths using `config.schema.lookup` and validate JSON syntax locally before calling `gateway` restart. This guarantees that mis-nested keys or schema violations will never trigger configuration validation errors (`exit code 78`) during gateway reboots.
- **No `<final>` tags:** Never wrap replies in `<final>` or similar tool wrapper tags. Respond with plain, natural conversational text.

- **Facebook & Threads:** Long-lived OAuth tokens secured and backed up in workspace memory and `/data/.openclaw/credentials/` for gateway restart persistence.
