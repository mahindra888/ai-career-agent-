#!/usr/bin/env python3
"""
AI Career Agent - OpenAI API Automated Runner (v4.0 Universal Edition)
Runs the AI Career Agent autonomously using OpenAI's GPT-4o model.
"""

import os
import sys
from datetime import datetime
from pathlib import Path

try:
    from openai import OpenAI
except ImportError:
    print("Error: The 'openai' package is required. Install it using: pip install openai")
    sys.exit(1)

def load_system_prompt():
    prompt_path = Path(__file__).parent.parent / "prompts" / "AI_Career_Agent_Universal_Prompt_v4.txt"
    if not prompt_path.exists():
        # Fallback to current directory or v3
        prompt_path = Path(__file__).parent.parent / "prompts" / "AI_Career_Agent_Master_Prompt_v3.txt"
    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable is not set.")
        print("Please set it with: export OPENAI_API_KEY='your-key-here'")
        sys.exit(1)

    client = OpenAI(api_key=api_key)
    system_prompt = load_system_prompt()

    user_query = f"""
Execute my daily career search for today ({datetime.now().strftime('%B %d, %Y')}).
Target Roles: Citrix Administrator, Citrix Support Engineer, VDI Operations.
Location: Hyderabad / Remote India.
Experience: 3.9 Years IT / 3+ Years Citrix CVAD.
Notice Period: 15 Days.

Tasks:
1. Search and select 3 high-match active openings from top boards.
2. For each role, provide full tailored ATS resume content.
3. For each role, formulate a dedicated technical mock interview preparation guide with in-depth answers.
4. Prepare recruiter outreach emails and standard screening answers.
5. Provide multi-platform verified direct links (Tier 1 to Tier 5).
6. Output 16-column table rows formatted for instant copy-paste into Google Sheets.
7. Deliver the full CITRIX JOB APPLICATION REPORT.
"""

    print(f"[*] Starting AI Career Agent Run via OpenAI GPT-4o [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]...")
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ],
            temperature=0.3
        )
        
        report_content = response.choices[0].message.content
        output_dir = Path(__file__).parent.parent / "output"
        output_dir.mkdir(parents=True, exist_ok=True)
        
        report_file = output_dir / f"Citrix_Job_Application_Report_{datetime.now().strftime('%Y%m%d')}.md"
        with open(report_file, "w", encoding="utf-8") as f:
            f.write(report_content)
            
        print(f"[+] Application report generated successfully: {report_file}")
        print("\n" + "="*80 + "\n")
        print(report_content)
        print("\n" + "="*80 + "\n")
        
    except Exception as e:
        print(f"[-] Execution error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
