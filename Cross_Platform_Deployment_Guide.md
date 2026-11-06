# AI Career Agent: Cross-Platform Deployment Guide (ChatGPT, Gemini, Claude, OpenAI)

The **AI Career Agent (Version 4.0)** is engineered to operate seamlessly across any major AI platform. This guide provides step-by-step instructions for deploying and running your career agent on **ChatGPT (OpenAI)**, **Google Gemini**, **Anthropic Claude**, and **OpenAI API / Python**.

---

## 1. Deploying on ChatGPT (OpenAI)

### Option A: Build a Custom GPT (Best for ChatGPT Plus / Team / Enterprise)
Creating a dedicated Custom GPT gives you a persistent, 1-click career copilot that remembers your profile and generates downloadable resumes.

1. **Open ChatGPT**: Go to [chatgpt.com](https://chatgpt.com) and click on **Explore GPTs > Create** (or navigate to GPT Builder).
2. **Configure Tab**:
   * **Name:** `AI Career Agent`
   * **Description:** `Autonomous Executive Job Hunting, ATS Resume Tailoring & Multi-Platform Application Automation.`
   * **Instructions:** Paste the entire contents of `prompts/AI_Career_Agent_Universal_Prompt_v4.txt` into the Instructions box. Fill in your name, experience, target locations, and contact details.
3. **Capabilities:**
   * ✅ **Web Browsing:** Enable (Required for scanning live job postings on Foundit, Indeed, LinkedIn, Naukri).
   * ✅ **Code Interpreter / Data Analysis:** Enable (Allows ChatGPT to generate downloadable `.docx` Word resumes and `.csv` trackers).
   * ⬜ DALL-E Image Generation: Optional / Not required.
4. **Knowledge Files:**
   * Upload `templates/Google_Sheets_Tracker_Schema.csv`.
   * Upload your baseline master resume (PDF or Word format).
5. **Conversation Starters:**
   * `"Search today's fresh Citrix Administrator openings in Hyderabad / Remote."`
   * `"Generate my daily Citrix Job Application Report."`
   * `"Create a tailored ATS resume and mock interview guide for [Company Name]."`
   * `"Update my application tracker table with new roles."`
6. **Save & Publish:** Click **Create > Only Me** (or share with your team).

### Option B: Running in Standard ChatGPT Chat
If you don't use Custom GPTs, simply:
1. Open a new chat in **ChatGPT (GPT-4o)** with Web Search enabled.
2. Paste the `AI_Career_Agent_Universal_Prompt_v4.txt` prompt.
3. Ask: *"Run my daily job search for Citrix Administrator and Support Engineer roles in Hyderabad / Remote India matching my profile."*
4. ChatGPT will browse the web, select top roles, format tailored ATS resumes, generate interview guides, and provide copy-paste rows for your tracker.

---

## 2. Deploying on Google Gemini

### Option A: Scheduled Action / Autonomous Agent Mode
Gemini has native Google Workspace integrations (Google Drive, Docs, Sheets, Gmail).
1. Paste `AI_Career_Agent_Universal_Prompt_v4.txt` into Gemini.
2. Instruct Gemini: *"Schedule this to run daily at 7:45 AM local time."*
3. Gemini will autonomously search the web every morning, create Google Docs directly in your Google Drive folders (`03_Tailored_Resumes`, `06_Mock_Interview_Questions`), append rows to your Google Sheet tracker, and output the report in chat.

### Option B: Gemini Gems (Gemini Advanced)
1. Open Gemini and click **Gem Manager > New Gem**.
2. Name it **`AI Career Agent`**.
3. Paste the Universal Master Prompt into the instructions.
4. Save and launch your Gem anytime to trigger instant daily job hunting.

---

## 3. Deploying on Anthropic Claude

1. **Claude Projects (Claude Pro / Team)**:
   * Go to [claude.ai](https://claude.ai) and open **Projects > Create Project**.
   * Name: `AI Career Agent`.
   * Add Instructions: Paste `AI_Career_Agent_Universal_Prompt_v4.txt`.
   * Add Project Knowledge: Upload your baseline master resume and `Google_Sheets_Tracker_Schema.csv`.
2. **Execution**:
   * Claude will use Artifacts to generate clean Markdown resumes, technical interview guides, and formatted tables ready to paste into Google Sheets in one click.

---

## 4. Running via Python & OpenAI API (CLI / Automated Cron)

For developers and technical users who want a headless, automated script running on a server or laptop:

1. Clone or download the repository files.
2. Install dependencies:
   ```bash
   pip install openai python-dotenv
   ```
3. Set your OpenAI API Key:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```
4. Run the automated script:
   ```bash
   python scripts/run_ai_career_agent_openai.py
   ```
5. The script automatically executes the prompt via `gpt-4o`, saves tailored resumes and mock interview docs locally into `./output/`, and prints your daily job report.

---

## 5. Feature Comparison Across Platforms

| Feature | ChatGPT (Custom GPT) | Gemini (Workspace) | Claude (Projects) | OpenAI API (Python) |
| :--- | :---: | :---: | :---: | :---: |
| **Web Search & Discovery** | ✅ Native Browsing | ✅ Native Search | ✅ Web Search / User Input | ✅ Serper / Tavily / Web |
| **Tailored Resumes** | ✅ `.docx` / Markdown | ✅ Google Docs | ✅ Markdown / Artifacts | ✅ Local `.docx` / `.md` |
| **Mock Interview Guides** | ✅ `.docx` / Markdown | ✅ Google Docs | ✅ Markdown / Artifacts | ✅ Local `.docx` / `.md` |
| **Tracker Updates** | ✅ `.csv` & Copy Rows | ✅ Google Sheets API | ✅ Copy-ready Table | ✅ Local CSV / GSheets API |
| **Recruiter Outreach** | ✅ Copy & Mailto | ✅ Gmail Drafts | ✅ Copy & Mailto | ✅ Text / SMTP send |
| **Automation Cadence** | On-demand / Custom GPT | Native Scheduled Action | On-demand | Linux Cron / Celery |
