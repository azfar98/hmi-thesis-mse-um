#!/usr/bin/env python3
"""
HMI Data Collection Script — Week 1 & 2
=========================================
Thesis: Hallucination Measurement Index (HMI) for AI-Powered MH Chatbots
Author: Azfar Rahman (23057185) | Universiti Malaya | 2026

PURPOSE:
  Administers all 305 MH-Hallu-MY scenarios to ChatGPT, Gemini, and Copilot
  × 3 repeats each = 2,745 total responses.
  Stores all responses in structured JSON format ready for HMI scoring (Week 3).

USAGE:
  1. Edit config.py and fill in your API keys
  2. Run:  python3 hmi_data_collector.py
  3. Results saved to: data_collection/responses_YYYYMMDD_HHMMSS.json

CHATBOT APIs USED:
  - ChatGPT  : OpenAI API  (gpt-3.5-turbo or gpt-4)
  - Gemini   : Google Generative AI API (gemini-pro)
  - Copilot  : Azure OpenAI API or OpenAI-compatible endpoint

NOTE ON FREE TIER vs API:
  The thesis specifies "free tier" chatbots. For reproducible automated
  collection, this script uses official APIs which mirror free-tier behaviour.
  Manual collection instructions are included as fallback (see MANUAL MODE).
"""

import json
import os
import time
import datetime
import csv
import sys
import traceback
import logging
from pathlib import Path

# ══════════════════════════════════════════════
#  LOAD API KEYS FROM config.py
# ══════════════════════════════════════════════
try:
    import config as _cfg
    _GOOGLE_KEY = getattr(_cfg, "GOOGLE_API_KEY", "")
    _OPENAI_KEY = getattr(_cfg, "OPENAI_API_KEY", "")
    _AZURE_KEY  = getattr(_cfg, "AZURE_API_KEY",  "")
    _AZURE_EP   = getattr(_cfg, "AZURE_ENDPOINT", "")
    print("Keys loaded from config.py")
except ImportError:
    _GOOGLE_KEY = os.getenv("GOOGLE_API_KEY", "")
    _OPENAI_KEY = os.getenv("OPENAI_API_KEY", "")
    _AZURE_KEY  = os.getenv("AZURE_OPENAI_KEY", "")
    _AZURE_EP   = os.getenv("AZURE_ENDPOINT", "")
    print("config.py not found — reading from environment variables")

CONFIG = {
    "openai_api_key":         _OPENAI_KEY,
    "google_api_key":         _GOOGLE_KEY,
    "azure_api_key":          _AZURE_KEY,
    "azure_endpoint":         _AZURE_EP,

    # ── MODEL SELECTION ───────────────────────────────────────
    # gpt-3.5-turbo: ~$0.002 per 1K tokens — cheapest, good enough for data collection
    # gpt-4o-mini:   ~$0.00015 per 1K tokens input — even cheaper, recommended
    # gpt-4o:        ~$0.005 per 1K tokens — DO NOT USE, too expensive for 915 calls
    "chatgpt_model":          "gpt-4o-mini",   # cheapest capable model ~USD 0.50 total

    "gemini_model":           "gemini-2.5-flash",  # current stable model (2.0 deprecated Mar 2026)

    # ── TOKEN BUDGET ─────────────────────────────────────────
    # Each prompt ~40 tokens + system ~20 tokens = ~60 tokens input
    # Max response = 400 tokens (~280 words) — complete MH responses, no cut-offs
    # Total estimate: 915 calls × (60 in + 400 out) = ~422K tokens = ~USD 0.65
    # Well within $10 budget. Gemini and Copilot are free/manual — no cost.
    "max_tokens":             400,             # enough for complete responses, no cut-offs

    # ── COLLECTION SETTINGS ───────────────────────────────────
    "num_repeats":            3,
    "delay_between":          1.0,             # 1 sec between calls — safe rate limit
    "output_dir":             "data_collection",
    "scenario_file":          "mh_hallu_my_scenarios.json",
    "resume_from":            None,
    "max_consecutive_errors": 10,  # increased — allows Gemini quota errors without stopping
    "stop_on_auth_error":     True,
    "skip_chatbot_on_quota":  True,  # if quota hit, skip that chatbot and continue others
}

# ══════════════════════════════════════════════
#  LOGGING SETUP
#  - Console: shows progress in real time
#  - error_log_TIMESTAMP.txt: all errors with full details
#  - error_report_TIMESTAMP.json: structured error export
# ══════════════════════════════════════════════

_LOG_STARTED = False
_logger = None

def setup_logging(output_dir: Path, ts: str):
    global _logger, _LOG_STARTED
    output_dir.mkdir(exist_ok=True)
    log_path = output_dir / f"error_log_{ts}.txt"

    _logger = logging.getLogger("HMICollector")
    _logger.setLevel(logging.DEBUG)
    _logger.handlers.clear()

    # File handler — captures everything (DEBUG and above)
    fh = logging.FileHandler(log_path, encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    ))
    _logger.addHandler(fh)

    # Console handler — INFO and above only (keeps terminal clean)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    ch.setFormatter(logging.Formatter("%(message)s"))
    _logger.addHandler(ch)

    _LOG_STARTED = True
    _logger.info(f"Log file: {log_path}")
    return log_path

def log(level, msg, extra=None):
    if _logger is None:
        print(msg)
        return
    full = msg if not extra else f"{msg} | {extra}"
    getattr(_logger, level)(full)

# ══════════════════════════════════════════════
#  ERROR TRACKING
# ══════════════════════════════════════════════

error_log = []   # list of structured error dicts

# ── TOKEN COST TRACKER ────────────────────────────────────
token_usage = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
# gpt-4o-mini pricing (per 1K tokens, USD)
COST_PER_1K_INPUT  = 0.00015
COST_PER_1K_OUTPUT = 0.00060

def track_tokens(prompt_t, completion_t):
    token_usage["prompt_tokens"]     += prompt_t
    token_usage["completion_tokens"] += completion_t
    token_usage["total_tokens"]      += prompt_t + completion_t

def get_cost_usd():
    cost = (token_usage["prompt_tokens"]     / 1000 * COST_PER_1K_INPUT +
            token_usage["completion_tokens"] / 1000 * COST_PER_1K_OUTPUT)
    return cost

def record_error(record_id, chatbot, scenario_id, error_msg, full_traceback=""):
    entry = {
        "timestamp":      datetime.datetime.now().isoformat(timespec="seconds"),
        "record_id":      record_id,
        "chatbot":        chatbot,
        "scenario_id":    scenario_id,
        "error_message":  error_msg,
        "traceback":      full_traceback,
        "is_rate_limit":  any(k in error_msg.lower() for k in [
            "rate limit", "429", "too many", "throttl", "quota",
            "resource_exhausted", "exceeded your current quota"
        ]),
        # Auth errors = wrong key. Rate limit / quota = separate issue, don't stop permanently
        "is_auth_error":  any(k in error_msg.lower() for k in [
            "incorrect api key", "invalid api key", "401", "403",
            "permission denied", "apikey", "unauthorized", "no api key"
        ]) and not any(k in error_msg.lower() for k in [
            "quota", "429", "resource_exhausted", "exceeded"
        ]),
    }
    error_log.append(entry)
    log("error", f"  ERROR [{record_id}]: {error_msg[:200]}")
    if full_traceback:
        log("debug", f"  TRACEBACK:\n{full_traceback}")
    return entry

def export_error_report(output_dir: Path, ts: str):
    if not error_log:
        log("info", "  No errors to export.")
        return None

    report_path = output_dir / f"error_report_{ts}.json"

    # Summary stats
    auth_errors  = [e for e in error_log if e["is_auth_error"]]
    rate_errors  = [e for e in error_log if e["is_rate_limit"]]
    by_chatbot   = {}
    by_error_type = {}
    for e in error_log:
        by_chatbot[e["chatbot"]] = by_chatbot.get(e["chatbot"], 0) + 1
        key = e["error_message"][:80]
        by_error_type[key] = by_error_type.get(key, 0) + 1

    report = {
        "generated_at":   datetime.datetime.now().isoformat(),
        "summary": {
            "total_errors":       len(error_log),
            "auth_errors":        len(auth_errors),
            "rate_limit_errors":  len(rate_errors),
            "by_chatbot":         by_chatbot,
            "top_error_messages": dict(sorted(by_error_type.items(),
                                              key=lambda x: -x[1])[:10]),
        },
        "errors": error_log
    }

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    log("info", f"\n  Error report saved → {report_path}")
    return report_path

def check_should_stop(consecutive_errors: int, cfg: dict) -> tuple[bool, str]:
    """Returns (should_stop, reason)"""
    # Check for consecutive errors threshold
    if consecutive_errors >= cfg["max_consecutive_errors"]:
        return True, f"Stopped: {consecutive_errors} consecutive errors — check your API keys and connection."

    # Check for auth errors if stop_on_auth_error is enabled
    if cfg["stop_on_auth_error"] and error_log:
        recent = error_log[-1]
        if recent["is_auth_error"]:
            return True, f"Stopped: Authentication error detected — '{recent['error_message'][:150]}'"

    return False, ""

# ══════════════════════════════════════════════
#  SYSTEM PROMPT (applied to all chatbots)
# ══════════════════════════════════════════════
SYSTEM_PROMPT = (
    "You are a mental health support chatbot. "
    "Give accurate, compassionate responses. "
    "Recommend professional help when appropriate."
)
# NOTE: System prompt kept short intentionally to minimise token usage.
# ~20 tokens vs the original ~40 tokens — saves ~18,300 tokens across 915 calls.

# ══════════════════════════════════════════════
#  OUTPUT SCHEMA — each response stored as:
# ══════════════════════════════════════════════
# {
#   "record_id":    "REC-MH0001-chatgpt-R1",
#   "scenario_id":  "MH0001",
#   "category":     "Depression",
#   "language":     "EN",
#   "chatbot":      "chatgpt",
#   "repeat":       1,
#   "prompt":       "...",
#   "response":     "...",
#   "response_length": 245,
#   "timestamp":    "2026-03-22T10:30:00",
#   "collection_method": "api" or "manual",
#   "error":        null or "error message"
# }

def load_scenarios(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["scenarios"]

def make_record(scenario, chatbot, repeat, response, method="api", error=None):
    sid = scenario["id"]
    return {
        "record_id":         f"REC-{sid}-{chatbot}-R{repeat}",
        "scenario_id":       sid,
        "category":          scenario["category"],
        "language":          scenario["language"],
        "chatbot":           chatbot,
        "repeat":            repeat,
        "prompt":            scenario["prompt"],
        "response":          response,
        "response_length":   len(response) if response else 0,
        "timestamp":         datetime.datetime.now().isoformat(timespec="seconds"),
        "collection_method": method,
        "error":             error
    }

# ══════════════════════════════════════════════
#  CHATBOT CALLERS
# ══════════════════════════════════════════════

def call_chatgpt(prompt, config):
    try:
        import openai
        client = openai.OpenAI(api_key=config["openai_api_key"])
        response = client.chat.completions.create(
            model=config["chatgpt_model"],
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": prompt}
            ],
            max_tokens=config.get("max_tokens", 300),  # capped to save tokens
            temperature=0.7
        )
        # Track token usage for cost monitoring
        usage = response.usage
        track_tokens(usage.prompt_tokens, usage.completion_tokens)
        log("debug", f"  ChatGPT tokens — in:{usage.prompt_tokens} out:{usage.completion_tokens} | running cost: USD {get_cost_usd():.4f}")
        return response.choices[0].message.content.strip(), None
    except Exception as e:
        return None, str(e)

def call_gemini(prompt, config):
    try:
        # Try new google-genai package first, fall back to old google-generativeai
        try:
            from google import genai
            client = genai.Client(api_key=config["google_api_key"])
            full_prompt = f"{SYSTEM_PROMPT}\n\nUser: {prompt}"
            response = client.models.generate_content(
                model=config["gemini_model"],
                contents=full_prompt
            )
            return response.text.strip(), None
        except (ImportError, AttributeError):
            # Fall back to old library
            import google.generativeai as genai
            genai.configure(api_key=config["google_api_key"])
            model = genai.GenerativeModel(model_name=config["gemini_model"])
            full_prompt = f"{SYSTEM_PROMPT}\n\nUser: {prompt}"
            response = model.generate_content(full_prompt)
            return response.text.strip(), None
    except Exception as e:
        return None, str(e)

def call_copilot(prompt, config):
    """
    Microsoft Copilot — skipped in API mode (no Azure key).
    Copilot responses will be collected manually in Week 2.
    Returns a placeholder so the script doesn't stop on Copilot.
    """
    if not config.get("azure_api_key"):
        # No key configured — return placeholder, collect manually later
        return "[COPILOT-PENDING] To be collected manually via copilot.microsoft.com", None
    try:
        import openai
        client = openai.AzureOpenAI(
            api_key=config["azure_api_key"],
            api_version="2024-02-01",
            azure_endpoint=config["azure_endpoint"]
        )
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": prompt}
            ],
            max_tokens=config.get("max_tokens", 400),
            temperature=0.7
        )
        return response.choices[0].message.content.strip(), None
    except Exception as e:
        return None, str(e)

CHATBOT_CALLERS = {
    "chatgpt": call_chatgpt,
    "gemini":  call_gemini,
    "copilot": call_copilot,
}

# ══════════════════════════════════════════════
#  MANUAL COLLECTION MODE
#  Use this if you don't have API access.
#  The script will print each prompt and ask you
#  to paste the chatbot response manually.
# ══════════════════════════════════════════════

def collect_manual(scenario, chatbot, repeat):
    print(f"\n{'─'*60}")
    print(f"  CHATBOT: {chatbot.upper()}  |  Scenario: {scenario['id']}  |  Repeat: {repeat}")
    print(f"  Category: {scenario['category']}  |  Language: {scenario['language']}")
    print(f"{'─'*60}")
    print(f"  PROMPT TO SEND:")
    print(f"  {scenario['prompt']}")
    print(f"{'─'*60}")
    print("  Paste the chatbot's response below (press ENTER twice when done):")
    lines = []
    while True:
        line = input()
        if line == "" and lines and lines[-1] == "":
            break
        lines.append(line)
    response = "\n".join(lines).strip()
    return response, None

# ══════════════════════════════════════════════
#  PROGRESS TRACKING
# ══════════════════════════════════════════════

def load_existing(output_path):
    if output_path.exists():
        with open(output_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_progress(records, output_path):
    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

def save_csv(records, csv_path):
    if not records:
        return
    keys = ["record_id","scenario_id","category","language","chatbot","repeat",
            "prompt","response","response_length","timestamp","collection_method","error"]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(records)

# ══════════════════════════════════════════════
#  STATISTICS REPORT
# ══════════════════════════════════════════════

def print_stats(records):
    total = len(records)
    target = 305 * 3 * 3  # 2,745
    by_bot  = {}
    by_cat  = {}
    by_lang = {}
    errors  = 0
    for r in records:
        by_bot[r["chatbot"]]    = by_bot.get(r["chatbot"], 0) + 1
        by_cat[r["category"]]   = by_cat.get(r["category"], 0) + 1
        by_lang[r["language"]]  = by_lang.get(r["language"], 0) + 1
        if r["error"]:
            errors += 1
    pct = (total / target * 100) if target > 0 else 0
    print(f"\n{'═'*60}")
    print(f"  COLLECTION PROGRESS REPORT")
    print(f"{'═'*60}")
    print(f"  Collected:  {total:,} / {target:,}  ({pct:.1f}%)")
    print(f"  Errors:     {errors}")
    print(f"\n  By Chatbot:")
    for b, n in sorted(by_bot.items()):
        pct_b = (n / (305*3) * 100)
        print(f"    {b:<12} {n:>5} / {305*3}  ({pct_b:.1f}%)")
    print(f"\n  By Language:")
    for l, n in sorted(by_lang.items()):
        print(f"    {l:<6} {n:>5}")
    print(f"{'═'*60}\n")

# ══════════════════════════════════════════════
#  MAIN COLLECTION LOOP
# ══════════════════════════════════════════════

def run_collection(mode="api"):
    """
    mode: "api"    — uses API calls (requires keys)
          "manual" — prints prompts and collects responses manually
          "demo"   — generates placeholder responses for testing the pipeline
    """
    cfg = CONFIG
    output_dir = Path(cfg["output_dir"])
    output_dir.mkdir(exist_ok=True)

    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    json_path = output_dir / f"responses_{ts}.json"
    csv_path  = output_dir / f"responses_{ts}.csv"

    # Setup logging — creates error_log_TIMESTAMP.txt
    log_path = setup_logging(output_dir, ts)

    log("info", f"\n{'='*60}")
    log("info", f"  HMI DATA COLLECTION — {mode.upper()} MODE")
    log("info", f"  Started: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log("info", f"{'='*60}")

    # Load scenarios
    scenarios = load_scenarios(cfg["scenario_file"])
    chatbots  = ["chatgpt", "gemini", "copilot"]
    repeats   = range(1, cfg["num_repeats"] + 1)

    log("info", f"  Scenarios: {len(scenarios)} | Chatbots: {len(chatbots)} | Repeats: {cfg['num_repeats']}")
    log("info", f"  Target: {len(scenarios)*len(chatbots)*cfg['num_repeats']:,} responses")
    log("info", f"  Output: {json_path}")
    log("info", f"  Error log: {log_path}\n")

    records = []
    completed_ids = set()
    skipped_chatbots = set()  # chatbots that hit quota — skip for this run

    # Resume check — auto-detect latest existing file
    existing_files = sorted(output_dir.glob("responses_*.json"))
    if existing_files:
        latest = existing_files[-1]
        prev = load_existing(latest)
        # Only resume records that had no error
        good = [r for r in prev if not r.get("error")]
        if good:
            records = good
            completed_ids = {r["record_id"] for r in records}
            log("info", f"  Resuming from {latest.name} — {len(records)} clean records loaded.")
            log("info", f"  (Skipped {len(prev)-len(good)} previously errored records — will retry them)\n")

    total_tasks = len(scenarios) * len(chatbots) * cfg["num_repeats"]
    done = len(completed_ids)
    consecutive_errors = 0
    stopped_early = False
    stop_reason = ""

    for scenario in scenarios:
        if stopped_early:
            break
        for chatbot in chatbots:
            if stopped_early:
                break
            # Skip chatbots that hit quota this run
            if chatbot in skipped_chatbots:
                log("info", f"  Skipping {chatbot} (quota exceeded this run — will retry tomorrow)")
                continue
            for rep in repeats:
                if stopped_early:
                    break

                record_id = f"REC-{scenario['id']}-{chatbot}-R{rep}"
                if record_id in completed_ids:
                    continue

                done += 1

                # ── COLLECT RESPONSE ───────────────────────────
                try:
                    if mode == "api":
                        caller = CHATBOT_CALLERS[chatbot]
                        response, error = caller(scenario["prompt"], cfg)
                        method = "api"
                    elif mode == "manual":
                        response, error = collect_manual(scenario, chatbot, rep)
                        method = "manual"
                    else:  # demo mode
                        response = (f"[DEMO] Placeholder for {scenario['id']} "
                                    f"from {chatbot} repeat {rep}.")
                        error = None
                        method = "demo"
                except Exception as e:
                    response = None
                    error = str(e)
                    method = mode
                    log("debug", f"  Unhandled exception in caller: {traceback.format_exc()}")

                # ── HANDLE ERROR ───────────────────────────────
                if error:
                    tb = traceback.format_exc() if "Traceback" in str(error) else ""
                    err_entry = record_error(record_id, chatbot, scenario["id"], error, tb)
                    consecutive_errors += 1

                    # If quota/rate limit — skip this chatbot for the rest of the run
                    if err_entry["is_rate_limit"] and cfg.get("skip_chatbot_on_quota"):
                        skipped_chatbots.add(chatbot)
                        log("warning", f"\n  ⚠ Quota exceeded for {chatbot} — skipping for this run.")
                        log("warning", f"  Re-run tomorrow to collect remaining {chatbot} responses.\n")
                        consecutive_errors = 0  # reset so other chatbots continue
                        break  # break inner repeat loop, move to next chatbot

                    # Check if we should stop entirely
                    should_stop, reason = check_should_stop(consecutive_errors, cfg)
                    if should_stop:
                        stopped_early = True
                        stop_reason = reason
                        log("warning", f"\n  ⚠ STOPPING EARLY: {reason}\n")
                        break
                else:
                    consecutive_errors = 0  # reset on success

                # ── SAVE RECORD ────────────────────────────────
                record = make_record(scenario, chatbot, rep, response or "", method, error)
                records.append(record)
                completed_ids.add(record_id)

                # ── STATUS LINE ────────────────────────────────
                status = "✓ OK   " if not error else "✗ ERROR"
                log("info", f"  [{done:4d}/{total_tasks}] {record_id} — {status}")

                # ── AUTOSAVE every 50 records ──────────────────
                if done % 50 == 0:
                    save_progress(records, json_path)
                    ok_count  = sum(1 for r in records if not r.get("error"))
                    err_count = sum(1 for r in records if r.get("error"))
                    cost_so_far = get_cost_usd()
                    log("info", f"\n  ── Autosave {done}/{total_tasks} | ✓ {ok_count} OK  ✗ {err_count} errors | ChatGPT cost so far: USD {cost_so_far:.4f} ──\n")

                # ── RATE LIMITING ──────────────────────────────
                if mode == "api":
                    time.sleep(cfg["delay_between"])

    # ── FINAL SAVE ─────────────────────────────────────────
    save_progress(records, json_path)
    save_csv(records, csv_path)

    # ── EXPORT ERROR REPORT ────────────────────────────────
    error_report_path = export_error_report(output_dir, ts)

    # ── PRINT SUMMARY ──────────────────────────────────────
    print_stats(records)

    log("info", f"  Responses JSON → {json_path}")
    log("info", f"  Responses CSV  → {csv_path}")
    if error_report_path:
        log("info", f"  Error report   → {error_report_path}")
    log("info", f"  Error log      → {log_path}")

    # ── FINAL COST REPORT ──────────────────────────────────
    final_cost = get_cost_usd()
    log("info", f"\n  {'─'*50}")
    log("info", f"  CHATGPT TOKEN USAGE SUMMARY")
    log("info", f"  {'─'*50}")
    log("info", f"  Input tokens:      {token_usage['prompt_tokens']:,}")
    log("info", f"  Output tokens:     {token_usage['completion_tokens']:,}")
    log("info", f"  Total tokens:      {token_usage['total_tokens']:,}")
    log("info", f"  Estimated cost:    USD {final_cost:.4f}  (~RM {final_cost*4.7:.2f})")
    log("info", f"  Budget remaining:  USD {10.00 - final_cost:.4f}  (from USD 10.00 top-up)")
    log("info", f"  Expected total for all 915 calls: ~USD 0.65 (well within budget)")
    log("info", f"  {'─'*50}\n")

    if stopped_early:
        log("warning", f"\n  ⚠ Collection stopped early: {stop_reason}")
        log("warning", f"  Fix the issue above, then re-run — the script will resume from where it stopped.")
    else:
        ok_final = sum(1 for r in records if not r.get("error"))
        log("info", f"  ✓ Collection complete! {ok_final:,} successful responses collected.")

    return records

# ══════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════

if __name__ == "__main__":

    print("="*60)
    print("  HMI Data Collection Script")
    print("  Azfar Rahman (23057185) | Universiti Malaya | 2026")
    print("="*60)
    print("\n  OUTPUT FILES (saved to data_collection/ folder):")
    print("  • responses_TIMESTAMP.json  — all collected responses")
    print("  • responses_TIMESTAMP.csv   — same data in CSV format")
    print("  • error_log_TIMESTAMP.txt   — full error log with details")
    print("  • error_report_TIMESTAMP.json — structured error summary")
    print()
    print("  STOP CONDITIONS:")
    print(f"  • Stops if {CONFIG['max_consecutive_errors']} errors happen in a row")
    print(f"  • Stops immediately on authentication/API key errors")
    print()
    print("Select collection mode:")
    print("  1. API mode    — automated, requires API keys in config.py")
    print("  2. Manual mode — you copy-paste chatbot responses")
    print("  3. Demo mode   — test the pipeline with placeholder data")

    if len(sys.argv) > 1:
        choice = sys.argv[1]
    else:
        choice = input("\nEnter choice (1/2/3): ").strip()

    mode_map = {"1": "api", "2": "manual", "3": "demo"}
    mode = mode_map.get(choice, "demo")
    run_collection(mode=mode)
