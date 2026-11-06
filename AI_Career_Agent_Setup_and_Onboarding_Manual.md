# AI Career Agent: Customer Setup & Onboarding Manual

## Welcome to Your AI Career Agent
This complete guide walks you through setting up and running your autonomous AI Career Agent.

---

## 1. Prerequisites
- A Google Account (Gmail, Google Drive, Google Sheets, Google Docs).
- Your latest Master Resume (PDF or Word format).
- Your target role parameters (Job Title, Experience, Notice Period, Target Cities).

---

## 2. Autonomous Zero-Touch Setup (New Feature!)
You no longer have to manually create folders or set up spreadsheets if you don't want to!

When you activate the **AI Career Agent Version 3.0**, the agent will autonomously check your Google Drive and provision the entire workspace automatically:
1. Creates the root folder: **`Job Application Automation`**.
2. Creates the 6 organized subfolders:
   - `01_Master_Resume` (Upload your master baseline resume here)
   - `02_Job_Descriptions` (Daily job descriptions analyzed here)
   - `03_Tailored_Resumes` (Where custom ATS resumes are placed)
   - `04_Application_Tracker` (Where the live tracker spreadsheet lives)
   - `05_Recruiter_Messages` (Where email drafts & recruiter messages live)
   - `06_Mock_Interview_Questions` (Where technical interview Q&A guides live)
3. Creates the **`Job Application Tracker`** Google Sheet with all 16 columns formatted, frozen, and ready.

*(If you already have existing folders, you can simply paste their Folder IDs into the prompt to reuse them).*

---

## 3. Configuring the Application Tracker

### Option A: Fully Automatic Provisioning (Recommended)
Simply let the AI Agent create the spreadsheet automatically inside `04_Application_Tracker` during its initial run.

### Option B: Use the Pre-Made Master Template
You can directly open and copy the master template spreadsheet:
👉 **[AI Career Agent - Master Job Application Tracker Template](https://docs.google.com/spreadsheets/d/1aNbr7vYDg4gWZbpAivsgGXi-X4DAfYk5bbu0gPfs8ic/edit)**  
*(Click **File > Make a copy** in Google Sheets to save your own copy inside your `04_Application_Tracker` folder).*

### Option C: Create It from Scratch
If you prefer creating it manually, create a Google Sheet inside `04_Application_Tracker` named `Job Application Tracker` with the following 16 column headers:
1. Date Discovered
2. Company Name
3. Job Title
4. Location / Work Mode
5. Platform Source
6. Link Priority Tier (Tier 1: Company ATS / Tier 2: LinkedIn / Tier 3: Naukri / Tier 4: Foundit / Tier 5: Indeed)
7. Verified Application Link
8. Experience Match (Yes/No)
9. Notice Period Match (15 Days / Immediate)
10. Estimated CTC / Salary
11. Tailored Resume URL (Google Doc)
12. Mock Interview Guide URL (Google Doc)
13. Application Status (Ready to Apply / Applied / Screened / Interviewing / Offer / Rejected)
14. Action Required
15. Recruiter / HR Contact
16. Next Follow-up Date

---

## 4. Activating Daily Automation
Paste the Master System Prompt into your AI Assistant interface and set an automated morning schedule (e.g., 7:45 AM daily).
Every morning, the agent will:
- Check and ensure all Google Drive folders and tracking sheets exist.
- Discover 5-10 verified job openings matching your profile.
- Provide direct application links prioritized by Company Site > LinkedIn > Naukri > Foundit > Indeed.
- Create your ATS tailored resume in Drive.
- Generate your mock interview guide.
- Prepare email drafts and update your tracker.

---

## 5. Daily Routine for Job Seekers (5-Minute Workflow)
1. **8:00 AM**: Open your Google Sheet tracker and review the day's fresh openings.
2. **8:02 AM**: Click the verified direct links (Company Site / LinkedIn / Naukri).
3. **8:04 AM**: Attach the generated tailored resume from Drive and paste the pre-written screening answers.
4. **8:05 AM**: Click Submit and mark the status as 'Applied' in your sheet.
