# TradingBot Project Blueprint

## Purpose

TradingBot is a long-term project designed to teach software engineering, quantitative finance, machine learning, and AI through the process of building a complete trading platform.

The objective is not to create a profitable trading system immediately.

The objective is to learn how to design, build, test, maintain, and improve complex software systems using professional development practices.

---

# Project Philosophy

Build first.

Learn through implementation.

Improve through iteration.

Every feature should teach a new technical skill while contributing to the final platform.

---

# Core Principles

1. Keep the project structure stable.
2. One feature should have one clear purpose.
3. Documentation is part of development.
4. Working software is more important than perfect software.
5. Refactor only when necessary.
6. Learn what is needed for the current milestone.
7. Build incrementally.
8. Commit frequently.
9. Never commit broken code.
10. Keep the repository clean and organized.

---

# Technology Stack

## Development

* Python
* Git
* GitHub
* Visual Studio Code

## Data

* pandas
* numpy

## Visualization

* matplotlib

## Dashboard

* Streamlit

## Machine Learning

* scikit-learn

## Deep Learning

* PyTorch

## AI

* Ollama

## API

* FastAPI

## Deployment (Future)

* Docker

---

# Project Structure

TradingBot/

├── README.md
├── ROADMAP.md
├── CHANGELOG.md
├── requirements.txt
├── main.py
│
├── data/
├── docs/
├── notebooks/
├── tests/
│
└── src/
├── api/
├── backtesting/
├── dashboard/
├── data/
├── indicators/
├── models/
├── strategies/
├── utils/
└── config/

---

# Folder Responsibilities

## src/data

Data collection.

Data cleaning.

Data loading.

---

## src/indicators

Technical indicators.

Examples:

* SMA
* EMA
* RSI
* MACD

---

## src/strategies

Trading strategies.

Examples:

* Moving Average Crossover
* RSI Strategy
* Breakout Strategy

---

## src/models

Machine learning models.

Examples:

* Random Forest
* XGBoost
* LSTM

---

## src/backtesting

Strategy evaluation.

Performance metrics.

Portfolio simulation.

---

## src/dashboard

User interface.

Charts.

Analytics.

---

## src/api

External interfaces.

REST endpoints.

---

## src/utils

Reusable helper functions.

---

## src/config

Configuration files.

Constants.

Settings.

---

# Development Workflow

Every feature follows the same process.

## Step 1

Read ROADMAP.md.

Choose one task.

---

## Step 2

Plan the implementation.

Keep the scope small.

---

## Step 3

Write code.

Place files in the correct folders.

---

## Step 4

Test the feature.

Confirm it works.

---

## Step 5

Update documentation.

Update CHANGELOG.md if work is completed.

Update README.md if user-facing functionality changes.

---

## Step 6

Commit changes.

---

## Step 7

Push changes to GitHub.

---

# Git Workflow

Check repository status:

git status

Stage all files:

git add .

Commit changes:

git commit -m "Meaningful commit message"

Push changes:

git push

View commit history:

git log --oneline

---

# Commit Message Rules

Good examples:

Add stock downloader

Implement RSI indicator

Create dashboard layout

Add LSTM training pipeline

Fix moving average calculation

Refactor data loader

Avoid messages such as:

update

fix

test

final

final_v2

asdf

---

# Naming Conventions

## Python Files

snake_case.py

Examples:

stock_downloader.py

moving_average.py

---

## Functions

snake_case()

Examples:

load_data()

calculate_rsi()

run_backtest()

---

## Classes

PascalCase

Examples:

StockDownloader

BacktestEngine

TradingStrategy

---

## Constants

UPPER_CASE

Examples:

DEFAULT_LOOKBACK

MAX_POSITION_SIZE

---

# Useful Commands

## Open Project

code .

---

## Open Specific File

code README.md

---

## Create Virtual Environment

python -m venv .venv

---

## Activate Virtual Environment (Windows CMD)

.venv\Scripts\activate

---

## Install Dependencies

pip install -r requirements.txt

---

## Save Dependencies

pip freeze > requirements.txt

---

## Run Application

python main.py

---

# Daily Workflow

1. Open terminal

2. Navigate to project

cd %USERPROFILE%\Dev\02_Projects\TradingBot

3. Open VS Code

code .

4. Read ROADMAP.md

5. Build one feature

6. Test

7. Update documentation

8. Commit

9. Push

---

# Session Checklist

Before ending a session:

* Code runs successfully.
* Documentation is updated.
* Git status is clean.
* Changes are committed.
* Changes are pushed to GitHub.

---

# References

Project planning:
ROADMAP.md

Project history:
CHANGELOG.md

Project overview:
README.md
