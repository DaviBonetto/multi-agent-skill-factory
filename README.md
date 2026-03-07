<div align="center">

# 🤖 Multi-Agent Skill Factory

<a href="https://github.com/DaviBonetto/multi-agent-skill-factory/actions"><img alt="Build Status" src="https://img.shields.io/github/actions/workflow/status/DaviBonetto/multi-agent-skill-factory/daily_forge.yml?branch=main&style=for-the-badge"></a>
<a href="https://github.com/DaviBonetto/multi-agent-skill-factory/blob/main/LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge"></a>
<a href="https://groq.com"><img alt="Powered by Groq" src="https://img.shields.io/badge/Powered%20by-Groq-f55a3c.svg?style=for-the-badge"></a>
<a href="https://python.org"><img alt="Python 3.11+" src="https://img.shields.io/badge/python-3.11+-blue.svg?style=for-the-badge"></a>

**An autonomous, multi-agent CI/CD pipeline that orchestrates, generates, and validates highly technical AI skills daily.**

[Key Features](#-key-features) • [Architecture](#%EF%B8%8F-multi-agent-architecture) • [Getting Started](#-getting-started) • [Workflow Guidelines](#%EF%B8%8F-workflow-guidelines) • [License](#-license)

</div>

<br/>

## 🌟 Key Features

The **Multi-Agent Skill Factory** operates on a zero-intervention CI/CD schedule. It leverages state-of-the-art LLMs (like LLaMA 3.3 70B via Groq) to independently research, draft, refine, review, and commit production-ready technical skills (`.md` guides) to your system.

- **Sequential Worker with Token Bucket**: Custom built rate limiter mathematically tuned to respect tight 30 RPM limits, sidestepping `HTTP 429` completely. 🚦
- **6-Agent Orchestration**: Specialized roles—Planner, Builder, Refiner, Validator, Integrator, and Auditor—operating recursively to ensure maximum code output quality. 👥
- **In-Memory Anti-Duplication Pipeline**: Pre-processes existing repositories of skills using TF-IDF logic (Scikit-Learn) to prevent generating duplicate knowledge context. 🧠
- **State Manager Backups**: Saves intermittent checkpoints locally in `/tmp` to gracefully handle API crashes across generation loops without data loss. 💾
- **100% CI/CD Driven**: Relies purely on GitHub actions to wake up, fetch keys via Secrets, run the Python matrix, and publish commits via PAT impersonation. 🚀

## 🏗️ Multi-Agent Architecture

The factory's intelligence is divided into specialized agents working in cascading **Waves**, modeled around Big Tech Software Engineering roles.

### 🌊 Wave 1: Planning

- **A1: The Planner (Orchestrator)**: Scans the existing corpus of files and brainstorms novel, senior-level skill concepts, outputting them in strict JSON.

### 🌊 Wave 2: The Factory (The Loop)

- **A2: The Builder (Creator)**: Drafts the raw Markdown of the SKILL.md.
- **A3: The Refiner (Security/Reliability)**: Injects edge cases, exception handling, and bulletproofs the technical implementation.
- **A4: The Validator (QA/Reviewer)**: Acts as a strict gatekeeper. If the logic is hallucinated or dangerous, it blocks the skill and forces a rewrite (`PASS/FAIL`).

### 🌊 Wave 3: Integration

- **A5: The Integrator (Release Manager)**: Writes conventional-commit histories based on the successfully assembled batch.
- **A6: The Auditor (Global QA)**: Assesses the entire `/tmp/` batch to verify 20 complete files are prepared. Acts as the `go/no-go` decision for the CI pipeline.

## 🚀 Getting Started

To run this factory in your own environments, you will need a Groq API Key and a Fine-Grained GitHub PAT.

### Local Initialization

```bash
# Clone the factory
$ git clone https://github.com/DaviBonetto/multi-agent-skill-factory.git
$ cd multi-agent-skill-factory

# Install Dependencies
$ pip install -r requirements.txt

# Set your Groq API key in an .env file
$ echo "GROQ_API_KEY=gsk_your_key_here" > .env

# Run the single loop manually
$ python main.py
```

### GitHub Actions (Cloud Automation)

1. Navigate to **Settings > Secrets and variables > Actions**.
2. Add `GROQ_API_KEY`: Your Groq API key.
3. Add `BOT_GITHUB_TOKEN`: A Personal Access Token (PAT) with `contents: write` permissions.
4. The `.github/workflows/daily_forge.yml` is scheduled to run daily at 02:00 AM UTC.

## ⚙️ CI/CD Reliability

The framework employs a "Graceful Degradation" strategy. If the Validator agent (A4) rejects a skill beyond maximum retry attempts, that single thread is dropped while the rest of the batch continues. As long as **at least 1 skill** survives the Gauntlet, the Integrator (A5) will gracefully package a semantic commit for the successful survivors.

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

<div align="center">
  <sub>Built with ❤️ by Davi Bonetto. Powered by OSS LLMs.</sub>
</div>
