#!/bin/bash

echo "🔄 Activating Recursive Intelligence Environment..."

# Step 1: Activate virtual environment
if [ -d "$HOME/aimee_env" ]; then
    source "$HOME/aimee_env/bin/activate"
else
    echo "⚠️ Virtual environment not found. Creating one..."
    python3 -m venv "$HOME/aimee_env"
    source "$HOME/aimee_env/bin/activate"
    pip install --upgrade pip
    pip install -r requirements.txt
fi

# Step 2: Navigate to framework directory
cd "$(dirname "$0")"

# Step 3: Launch orchestrator
echo "🧠 Launching Aimee Recursive Echo Verse..."
python3 Recursive\ Intelligence\ Orchestrator.py
