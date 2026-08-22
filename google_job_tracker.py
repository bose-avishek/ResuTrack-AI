import os
import re
import feedparser
import pandas as pd
from datetime import datetime

# ==========================================
# ⚙️ CUSTOM CONFIGURATION SECTION
# ==========================================
# Paste your actual copied Google Alert RSS URL links inside this list below:
ALERT_FEEDS = [
     "https://www.google.co.in/alerts/feeds/02717465477893071212/17678123056156896503", # Alert 1 Link
     "https://www.google.co.in/alerts/feeds/02717465477893071212/14109638409449922261", # Alert 2 Link
     "https://www.google.co.in/alerts/feeds/02717465477893071212/14109638409449919493"  # Alert 3 Link
]

EXCEL_FILE = "automated_job_tracker.xlsx"
# ==========================================

def clean_html_tags(raw_html):
    """Removes messy Google bold formatting tags from the title text."""
    clean_text = re.sub(r'<[^>]*>', '', raw_html)
    # Fix common html space codes
    clean_text = clean_text.replace('&nbsp;', ' ').replace('&amp;', '&')
    return clean_text.strip()

def extract_jobs_from_feeds():
    print(f"🔄 Scanning Google Alert feeds at {datetime.now().strftime('%H:%M:%S')}...")
    
    new_jobs_list = []
    
    for feed_url in ALERT_FEEDS:
        # Securely download the data stream directly from Google's servers
        parsed_feed = feedparser.parse(feed_url)
        
        for entry in parsed_feed.entries:
            # Clean out structural text items
            job_title = clean_html_tags(entry.title)
            raw_link = entry.link
            
            # Clean up Google's redirect tracking wrappers to get the true application URL link
            clean_link = raw_link
            if "url=" in raw_link:
                match = re.search(r'url=([^&]*)', raw_link)
                if match:
                    clean_link = match.group(1)
            
            # Record structural row details
            new_jobs_list.append({
                "Date Found": datetime.now().strftime("%Y-%m-%d"),
                "Job Listing Alert Title": job_title,
                "Application URL Link": clean_link,
                "Status": "Unapplied"
            })
            
    if not new_jobs_list:
        print("Done. No new alert entries found right now.")
        return

    # Check for an existing tracker file to prevent overwriting past data rows
    if os.path.exists(EXCEL_FILE):
        existing_df = pd.read_excel(EXCEL_FILE)
        new_df = pd.DataFrame(new_jobs_list)
        
        # Deduplicate using the Application Link so you never track the same job twice
        combined_df = pd.concat([existing_df, new_df]).drop_duplicates(subset=["Application URL Link"], keep="first")
    else:
        combined_df = pd.DataFrame(new_jobs_list)

    # Save to your local Excel sheet layout configuration
    combined_df.to_excel(EXCEL_FILE, index=False)
    print(f"📊 Excel sheet updated successfully! Total unique jobs saved: {len(combined_df)}")

if __name__ == "__main__":
    extract_jobs_from_feeds()