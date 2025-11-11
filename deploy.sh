#!/bin/bash

# 🚀 LapPrice Pro - Quick Deployment Script
# This script prepares your project for fast deployment

echo "======================================================================"
echo "  🚀 LAPPRICE PRO - DEPLOYMENT SETUP"
echo "======================================================================"
echo ""

# Check if Git LFS is installed
echo "📦 Step 1: Checking Git LFS..."
if command -v git-lfs &> /dev/null; then
    echo "   ✅ Git LFS is installed"
else
    echo "   ⚠️  Git LFS not found. Installing..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install git-lfs
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt-get install git-lfs
    fi
    git lfs install
    echo "   ✅ Git LFS installed successfully"
fi

# Initialize Git LFS
echo ""
echo "🔧 Step 2: Initializing Git LFS..."
git lfs install
echo "   ✅ Git LFS initialized"

# Track large files with Git LFS
echo ""
echo "📂 Step 3: Tracking large files..."
git lfs track "*.pkl"
git lfs track "*.csv"
git lfs track "*.h5"
git lfs track "*.model"
echo "   ✅ Large files configured for Git LFS"

# Add all files
echo ""
echo "➕ Step 4: Adding files to git..."
git add .gitattributes
git add requirements.txt
git add railway.json
git add render.yaml
git add .streamlit/config.toml
git add laptop_data_400k.csv
git add generate_large_dataset.py
git add app.py
git add DEPLOYMENT_GUIDE.md
echo "   ✅ Files staged for commit"

# Show status
echo ""
echo "📊 Step 5: Current git status:"
git status

# Commit
echo ""
echo "💾 Step 6: Committing changes..."
git commit -m "feat: Add 400k dataset and deployment configuration

- Generated synthetic dataset with 400,000 realistic laptop entries
- Added deployment configs for Streamlit Cloud, Railway, and Render
- Configured Git LFS for large files
- Updated color system for better accessibility
- Ready for fast deployment"

echo "   ✅ Changes committed"

# Push
echo ""
echo "🚀 Step 7: Pushing to GitHub..."
echo "   Note: First push might take a while due to large files..."
git push origin main

echo ""
echo "======================================================================"
echo "  ✅ DEPLOYMENT READY!"
echo "======================================================================"
echo ""
echo "Your project is now ready for deployment. Choose one:"
echo ""
echo "1️⃣  STREAMLIT CLOUD (Recommended - Fastest)"
echo "   → Go to: https://streamlit.io/cloud"
echo "   → Click 'New app'"
echo "   → Select your repo and app.py"
echo "   → Deploy! (takes 2-3 minutes)"
echo ""
echo "2️⃣  RAILWAY"
echo "   → Go to: https://railway.app"
echo "   → New Project → Deploy from GitHub"
echo "   → Select your repo"
echo "   → Deploy! (takes 3-5 minutes)"
echo ""
echo "3️⃣  RENDER"
echo "   → Go to: https://render.com"
echo "   → New + → Web Service"
echo "   → Connect GitHub repo"
echo "   → Deploy! (takes 5-7 minutes)"
echo ""
echo "📖 Full deployment guide: DEPLOYMENT_GUIDE.md"
echo "======================================================================"
