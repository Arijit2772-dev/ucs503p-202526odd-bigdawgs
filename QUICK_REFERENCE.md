# ⚡ Quick Reference Card

**One-page cheat sheet for LapPrice Pro**

---

## 🚀 Start the App

```bash
# Navigate to folder
cd /Users/arijitsingh/Documents/lpp

# Run app
streamlit run app_new.py

# Opens automatically at:
# http://localhost:8501
```

---

## 📁 Important Files

| File | Purpose | Size |
|------|---------|------|
| `app_new.py` | ⭐ Main app (run this!) | 58 KB |
| `models/pipe.pkl` | 🧠 ML model | 19 MB |
| `models/df.pkl` | 📊 Sample data | 125 KB |
| `requirements.txt` | 📦 Dependencies list | 82 B |

---

## 🎯 What Each File Does (One-Liner)

```
app_new.py          → The entire app (UI + logic)
requirements.txt    → List of tools needed
models/pipe.pkl     → Trained prediction brain
models/df.pkl       → Sample laptop data
.streamlit/config   → Color theme, settings
data/lookups/       → Pre-computed prices
scripts/            → Utility tools (run once)
docs/               → Documentation
```

---

## 🔧 Common Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app_new.py

# Stop app
Ctrl + C (in terminal)

# Check Python version
python --version

# Check if Streamlit installed
streamlit --version
```

---

## 🎨 Key Features

```
1. Quick Presets    → Student/Gamer/Professional/Designer
2. Price Prediction → ML-powered accurate pricing
3. Config Score     → Rates your laptop (0-100)
4. AI Insights      → Smart suggestions
5. Market Analysis  → Where it stands in market
6. Recommendations  → Similar laptop suggestions
7. Value Analysis   → Is it worth the money?
8. TCO Calculator   → 5-year cost projection
```

---

## 💡 How It Works (5 Steps)

```
1. You enter specs    → Brand, RAM, CPU, etc.
2. App creates hash   → Unique ID: "abc123"
3. Looks up in DB     → O(1) instant search
4. Calculates extras  → Scores, insights, tips
5. Shows results      → Beautiful UI with cards
```

---

## 🎯 Code Structure (Simplified)

```python
# app_new.py structure:

# Part 1: IMPORTS (Lines 1-11)
import streamlit as st
import numpy as np
import pandas as pd

# Part 2: FUNCTIONS (Lines 24-297)
def create_laptop_hash(...)      # Creates unique ID
def calculate_config_score(...)  # Rates laptop
def generate_ai_insights(...)    # Smart tips
# ... 20+ more functions

# Part 3: UI SETUP (Lines 298-311)
st.set_page_config(...)           # Window settings

# Part 4: STYLING (Lines 312-688)
st.markdown("""<style>...</style>""")  # Pretty colors

# Part 5: DATA LOADING (Lines 689-753)
@st.cache_data
def load_data_from_github_pages():
    # Downloads 399K predictions

# Part 6: UI COMPONENTS (Lines 754-1608)
# Header, sidebar, tabs, buttons, results
```

---

## 🔍 Key Concepts

### Hash Function
```
Input:  Dell + 8GB + i5 + Intel HD
↓
Output: "abc123def456"

Purpose: Unique ID for O(1) lookup
```

### O(1) Lookup
```
Slow: Loop through 399K items  → 2 seconds ❌
Fast: Direct dictionary access → 0.001 seconds ✅

predictions["abc123"] = 45000  ← Instant!
```

### Caching
```
First run:  Downloads data → 3 seconds
Next runs:  Uses saved copy → Instant ✅

@st.cache_data ← Magic decorator
```

---

## 📊 Prediction Flow

```
┌─────────────────┐
│  User Input     │
│  Dell, 8GB, i5  │
└────────┬────────┘
         │
    ┌────▼─────┐
    │   Hash   │
    │  "abc123"│
    └────┬─────┘
         │
    ┌────▼─────┐
    │  Lookup  │  predictions["abc123"]
    │  45000   │
    └────┬─────┘
         │
    ┌────▼─────┐
    │ Calculate│  Scores, insights
    │  Extras  │
    └────┬─────┘
         │
    ┌────▼─────┐
    │  Display │  Beautiful UI
    │  Results │
    └──────────┘
```

---

## 🎨 UI Sections

```
┌──────────────────────────────────┐
│  Header         Logo + Title     │
├──────────────────────────────────┤
│  Sidebar        Configuration    │
│  ├─ Presets     Quick configs    │
│  ├─ Profile     User type        │
│  ├─ Specs       Form inputs      │
│  └─ Advanced    More options     │
├──────────────────────────────────┤
│  Main Content   Results area     │
│  ├─ Tab 1       Price            │
│  ├─ Tab 2       Market           │
│  ├─ Tab 3       Insights         │
│  ├─ Tab 4       Recommendations  │
│  └─ Tab 5       Value Analysis   │
├──────────────────────────────────┤
│  Footer         Credits          │
└──────────────────────────────────┘
```

---

## 🔢 Important Numbers

```
399,237    → Total pre-computed predictions
58 MB      → JSON lookup file size
19 MB      → ML model size
95%        → Prediction accuracy
0.2s       → Average prediction time
~1s        → App load time (after cache)
8501       → Default Streamlit port
```

---

## 🆘 Troubleshooting

### App won't start
```bash
# Check Python installed
python --version

# Install requirements
pip install -r requirements.txt

# Try running again
streamlit run app_new.py
```

### Port already in use
```bash
# Kill existing Streamlit
pkill -f streamlit

# Or use different port
streamlit run app_new.py --server.port 8502
```

### Prediction takes long
```
First prediction: ~3 seconds (loading data)
Next predictions: ~0.2 seconds (cached)

This is normal! ✅
```

### Can't see results
```
1. Check if you clicked "Get AI Prediction"
2. Scroll down to see results
3. Try switching tabs
```

---

## 📚 Learn More

```
BEGINNER_GUIDE.md   → Detailed explanation (everything!)
VISUAL_GUIDE.md     → Diagrams and pictures
README.md           → Project overview
```

---

## 🎓 Key Takeaways

1. **`app_new.py`** = The entire app
2. **Streamlit** = UI framework (makes it pretty)
3. **O(1) lookup** = Speed secret (pre-computed)
4. **GitHub Pages** = Free data storage
5. **Machine Learning** = The prediction brain

---

## 🎯 Common Tasks

### Add new laptop data
```bash
cd scripts
python generate_large_dataset.py
```

### Update predictions
```bash
cd scripts
python precompute_predictions.py
```

### Change theme colors
```
Edit: .streamlit/config.toml
Change: primaryColor, backgroundColor
```

### Change port
```bash
streamlit run app_new.py --server.port 8502
```

---

## 💬 Still Confused?

Read the full guides:
- 📖 **BEGINNER_GUIDE.md** - Everything explained
- 🎨 **VISUAL_GUIDE.md** - Pictures and diagrams
- 📋 **README.md** - Project overview

Or ask specific questions! 🙋‍♂️

---

**Made by Team Big_dawgs** 🚀
