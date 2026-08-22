#!/bin/bash

# Force strict absolute directory mapping paths
BASE_DIR="/mnt/c/Users/bosea/Downloads/Resume_Optimizer"
WATCH_DIR="$BASE_DIR/job_listings"
SCRIPT_NAME="$BASE_DIR/free_gemini_resume_optimizer.py"
TRACKER_SCRIPT="$BASE_DIR/google_job_tracker.py"

cd "$BASE_DIR" || exit

echo "👀 Folder watcher active! Tracking Google Alerts once daily and monitoring folder drops..."

INTERVAL=86400
LAST_RUN=0

while true; do
    CURRENT_TIME=$(date +%s)
    
    # 1. Trigger the Google Alert tracker ONLY if 24 hours have passed since the last run
    if (( CURRENT_TIME - LAST_RUN >= INTERVAL )); then
        echo "📅 [Daily-Loop] Running your 24-hour Google Alert job tracking scan..."
        python3 "$TRACKER_SCRIPT"
        LAST_RUN=$CURRENT_TIME
    fi

    # 2. Monitor your resume folder explicitly using absolute path structures
    # It waits up to 30 seconds for a text write event to finish saving completely
    inotifywait -t 30 -e close_write "$WATCH_DIR" 2>/dev/null
    
    # If a new resume text file write event was registered during those 30 seconds:
    if [ $? -eq 0 ]; then
        echo "⚡ [Resume-Trigger] New job description detected! Running Gemini writer..."
        python3 "$SCRIPT_NAME"
    fi
done
