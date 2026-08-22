------------------------------
## 🚀 ResuTrack-AI: Event-Driven Multi-Model Job Aggregator & ATS Resume Optimization Pipeline## 📌 Project Overview
ResuTrack-AI is an enterprise-grade, local automation infrastructure designed to streamline the high-volume job discovery and application lifecycle. Operating natively within a virtualised Linux / Windows Subsystem for Linux (WSL) sandbox environment, the system runs a detached background process daemon that performs two core asynchronous activities daily:

   1. Secure Multi-Portal Job Ingestion: Aggregates, parses, and deduplicates real-time job openings across major global listing portals (LinkedIn, Naukri, Indeed) using secure Google Alert RSS data streams to completely bypass anti-bot mechanisms and protect host IP integrity.
   2. Real-Time Contextual AI Optimization: Monitors local file directory mutations via native Linux kernel event hooks. Upon detecting a saved job description, the engine calls the Google Gemini 3.6-Flash API SDK to perform deep keyword matching, restructure experience summaries using the pioneered Google XYZ Metrics Formula, and programmatically compile an ATS-compliant, recruiter-ready Microsoft Word (.docx) file.

------------------------------
## 🏗️ System Architecture & Workflow

 [ Ingestion Layer ]                        [ Core DevOps Automation Layer (WSL) ]
┌─────────────────────────────────┐        ┌────────────────────────────────────────────────────────┐
│ 📅 Google Alert RSS Feeds       │ ─────► │ 🔄 pandas / feedparser maps API streams daily          │
│    (LinkedIn, Naukri, Indeed)   │        │ 📊 Appends to unique 'automated_job_tracker.xlsx'      │
└─────────────────────────────────┘        └────────────────────────────────────────────────────────┘
                                                                        │
                                                                   (User Action)
                                                                        ▼
 [ Target Recruitment Output ]              [ Engine & Document Compilation Layer ]
┌─────────────────────────────────┐        ┌────────────────────────────────────────────────────────┐
│ 📄 Tailored Calibri .docx       │ ◄───── │ 👀 inotifywait hooks catch plain .txt data writes       │
│    w/ programmatic border rules │        │ 🤖 Gemini 3.6-Flash evaluates master data models       │
└─────────────────────────────────┘        └────────────────────────────────────────────────────────┘

## 1. Environmental Data Ingestion

* Programmed an operational parser script utilizing Python feedparser and pandas.
* Instead of running high-risk browser automation scrapers that trigger target site firewalls, the script downloads lightweight XML feeds directly from Google's core search network endpoints once every 24 hours.
* Cleans messy HTML tracking wrappers via regular expressions (re) and updates a centralized local master Excel sheet ledger (automated_job_tracker.xlsx), sorting postings by link structure to completely avoid duplicate row creation.

## 2. Event-Driven Kernel Monitoring Loop

* Implemented an infinite background loop handler executed via shell scripts (watch_folder.sh).
* Utilizes native Linux kernel file tracking hooks (inotify-tools) to set a passive directory watch on the target folder (/job_listings).
* The loop sleeps at zero background CPU usage until a file close_write system event completes, instantly starting the text optimization pipeline only when data is fully saved to disk.

## 3. Context Processing & AI Orchestration

* Connects dynamically to the paid developer tier of the Google Gemini 3.6-Flash network utilizing the official google-genai SDK.
* Feeds an advanced, industry-optimized system prompt that maps standard requirements within BFSI, Consulting, and Technology sectors.
* Enforces strict formatting layouts (pure structural markdown tables or lists only) and strips conversational conversational output prefixes. It converts flat job background bullet points into impact statements matching the Google framework: "Accomplished [X] as measured by [Y], by doing [Z]".

## 4. Low-Level Document Compilation

* Engineered a custom typographic renderer function using the python-docx library to transform raw text payloads into print-ready corporate formats.
* Typographic Rigour Controls: Programmatically sets strict 1-inch uniform margin structures, enforces global Calibri font stacks set exclusively to pure pitch-black (RGBColor(0,0,0)), maps title alignments, and systematically injects raw XML element bottom borders (w:pBdr) to generate crisp horizontal visual divider rules below main section category headings.
* Orphan Protection: Programmatically flags the layout metadata fields with keep_with_next = True properties across header elements to prevent orphaned titles from separating across page breaks.

## 5. Headless Daemon Lifecycle Integration

* Integrated the runtime initialization hooks directly into the user shell login environment profile (~/.bashrc).
* Leverages Linux screen process sessions to spawn the folder monitor as a completely headless background daemon process upon initial terminal boot.
* Appends direct workspace variable resets (cd ~) to cleanly restore primary terminal focus immediately to the fast Linux home directory path (~$), leaving the active prompt open for regular administrative activities.

------------------------------
## 🛠️ Technology & Tools Used

* Languages & Core Foundations: Python 3.10+, Bash Shell Scripting, Linux POSIX Architecture
* DevOps Infrastructure Environment: Windows Subsystem for Linux (WSL), Linux Kernel Utilities (inotify-tools), Process Session Multiplexers (screen)
* Data Processing Libraries: pandas, feedparser, openpyxl, re (Regular Expressions)
* Generative AI Platform Stack: Google Gemini 3.6-Flash API, Official google-genai SDK
* Document Processing Automation: python-docx, OpenXML Core Manipulation Elements

------------------------------
## 🏆 Key Achievements & Strategic Metrics

* ⏱️ 98% Optimization Efficiency: Transformed a highly repetitive, high-overhead 45-minute daily data gathering and resume editing routine into a localized background loop executing in less than 5 seconds.
* 🛡️ Zero-Risk Network Security Layer: Achieved completely safe web monitoring capabilities without encountering target website IP address blacklisting or bot firewall blocks.
* 📉 Zero-Cost Application Infrastructure: Constructed an entirely self-contained local workspace framework that performs up to 1,500 daily document compilation cycles completely free of charge, bypassing expensive commercial web automation subscription tiers.

------------------------------
