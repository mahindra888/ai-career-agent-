# Autonomous AI Career Agent (v4.0 Community Edition) 🚀
> **100% Free & Open Source for All — Autonomous Executive Job Hunting, Multi-Platform AI Deployment (ChatGPT, Gemini, Claude, OpenAI), Cloud Workspace Provisioning, ATS Resume Tailoring & Multi-Platform Application Automation**

[License: MIT — 100% Free for Everyone](https://opensource.org/licenses/MIT)
[ChatGPT / OpenAI](https://chatgpt.com)
[Google Gemini](https://deepmind.google/technologies/gemini/)
[Anthropic Claude](https://claude.ai)

The **Autonomous AI Career Agent** is a production-ready, zero-touch career operations engine. It is **100% Free, Open-Source, and Platform-Agnostic**—built as a public community resource to help job seekers, career switchers, and engineers worldwide automate 95% of the job search process without paying for expensive tools or subscriptions.

---

## 🎁 100% Free for Everyone (Zero Paywalls / Zero Lock-in)

* **Completely Free:** No paid subscriptions, hidden fees, or premium tiers required.
* **Runs on Free AI Tiers:** Fully compatible with **ChatGPT Free**, **Google Gemini Free**, and **Anthropic Claude Free**, as well as paid/API tiers.
* **Open Source (MIT License):** You have full rights to use, fork, customize, distribute, and share this system with friends, communities, or colleagues.

---

## 🌟 Key Capabilities Across Any AI Platform

1. **Adaptive Execution Engine:**
   * **On Google Gemini:** Autonomously provisions Google Drive folders (`01` to `06`), creates tailored Google Docs, appends records to Google Sheets, and creates Gmail drafts.
   * **On ChatGPT (Free or Plus / Custom GPT):** Scans the web for verified listings, generates downloadable `.docx` Word resumes or clean ATS Markdown, and crafts ready-to-send outreach emails.
   * **On Anthropic Claude & Other LLMs:** Generates complete production-ready ATS Markdown resumes, technical mock interview guides, and 16-column tables formatted for 1-click paste into Google Sheets or Excel.
2. **Multi-Platform Job Discovery:** Scans Foundit, Indeed, LinkedIn, Naukri, and direct company career portals daily, filtering by exact experience range, tech stack, and notice period.
3. **Strict 5-Tier Link Verification:** Ranks verified application links in strict hierarchy:
   `Company ATS Portal > LinkedIn > Naukri > Foundit > Indeed`.
4. **Tailored ATS Resumes:** Formulates customized resumes matching exact job description keywords while maintaining 100% factual truth of candidate credentials.
5. **Technical Mock Interview Guides:** Formulates 8–10 company-specific technical interview questions with scenario-based architecture explanations and troubleshooting steps.
6. **Recruiter Outreach Drafts:** Prepares ready-to-send emails and portal screening answers.

---

## 📁 Repository Structure

```text
├── README.md                                          # Complete documentation & quickstart guide
├── prompts/
│   ├── AI_Career_Agent_Universal_Prompt_v4.txt       # Universal Master Prompt (100% Free Community Edition)
│   └── AI_Career_Agent_Master_Prompt_v3.txt           # Turnkey Google Workspace edition prompt
├── docs/
│   ├── Cross_Platform_Deployment_Guide.md            # Step-by-step setup on ChatGPT, Gemini, Claude, OpenAI
│   ├── AI_Career_Agent_Setup_and_Onboarding_Manual.md # User onboarding guide & 5-minute daily workflow
│   ├── Commercial_Agency_Monetization_Guide.md        # Open agency frameworks & monetization guide
│   └── The_Master_AI_Career_Agent_Complete_Product_and_Setup_Guide.docx
├── scripts/
│   └── run_ai_career_agent_openai.py                  # Standalone Python runner using OpenAI GPT-4o
├── templates/
│   ├── Google_Sheets_Tracker_Schema.csv               # 16-column application tracker CSV schema
│   └── Google_Sheets_Master_Template_Link.md          # Direct link to pre-built Google Sheet template
└── LICENSE                                            # MIT Open-Source License
```

---

## ⚡ Quickstart: Deploy for Free in 3 Minutes

### 1. Configure the Universal Prompt
Open [prompts/AI_Career_Agent_Universal_Prompt_v4.txt](prompts/AI_Career_Agent_Universal_Prompt_v4.txt) and customize your profile variables:
```yaml
Candidate Name: [Your Full Name]
Core Skillset: [e.g., Citrix CVAD, VDI, Windows Server, Azure]
Total Experience: [e.g., 3.9 Years IT / 3+ Years in Primary Tech]
Notice Period: [e.g., 15 Days or Immediate Joiner]
Preferred Locations: [e.g., Hyderabad, Bengaluru, Remote India]
Current CTC / Target CTC: [e.g., 7.0 LPA / 10.0 LPA]
```

### 2. Choose Your Platform (All Free!)

#### A. ChatGPT (OpenAI — Free or Plus)
1. Go to [ChatGPT](https://chatgpt.com).
2. Paste the prompt from `AI_Career_Agent_Universal_Prompt_v4.txt`.
3. Ask: *"Run my daily job search for [Your Role] in [Your City] matching my profile."*
4. *(Plus users can also create a dedicated Custom GPT using the instructions in docs/Cross_Platform_Deployment_Guide.md).*

#### B. Google Gemini (100% Free with Google Workspace)
1. Paste the prompt into Gemini and say: *"Schedule this to run daily at 7:45 AM local time."*
2. Gemini will autonomously manage your Google Drive, Docs, Sheets, and Gmail drafts every morning.

#### C. Anthropic Claude (Free or Pro)
1. Open [Claude](https://claude.ai).
2. Paste the prompt into your chat or Claude Project to receive complete Markdown resumes, interview guides, and tracker tables.

#### D. Standalone Python Automation (OpenAI API / Local LLMs)
```bash
pip install openai
export OPENAI_API_KEY="your-api-key"
python scripts/run_ai_career_agent_openai.py
```

---

## 🎯 Verified Multi-Platform Link Hierarchy

To prevent broken links, expired listings, and aggregator delays, the agent strictly prioritizes links in this order:

| Priority | Platform | Routing Logic |
| :---: | :--- | :--- |
| **Tier 1** | **Official Company Career Site / ATS Portal** | Direct apply link on Workday, Taleo, Greenhouse, Lever, SmartRecruiters, BrassRing. |
| **Tier 2** | **LinkedIn Jobs** | Direct job view link (`https://www.linkedin.com/jobs/view/[ID]`). |
| **Tier 3** | **Naukri.com** | Direct opening link + 1-Tap Google search forward syntax. |
| **Tier 4** | **Foundit (Monster India)** | Direct verified posting link. |
| **Tier 5** | **Indeed** | Direct verified job post link. |

---

## 🔒 Security & Account Safety Principles

Unlike brittle browser bots (Selenium/Puppeteer) that risk account suspensions:
* **Zero Credential Storage:** The agent never requests or stores login passwords, cookies, or 2FA codes.
* **1-Click Human-in-the-Loop:** The agent completes 95% of the preparation (resumes, verified links, screening answers). The candidate clicks the direct link, uploads the tailored resume, and submits in under 30 seconds.

---

## 📄 Open Source License
This project is open-sourced under the [MIT License](LICENSE) — **100% free for everyone** for personal, educational, and commercial use.