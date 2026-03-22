# Global Economic Health Analyzer

A data analysis project exploring **GDP growth trends** across 266 countries from **1990 to 2023**, using World Bank Open Data.

Built with Python · pandas · matplotlib · seaborn

---

## Data Source:

[World Bank Open Data](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG) — GDP growth (annual %)

Two files used:
- `API_NY.GDP.MKTP.KD.ZG` — GDP growth data for 266 countries across 60+ years
- `Metadata_Country` — Country metadata including Region and Income Group

---

##  Data Pipeline

Before any analysis, the raw data went through a full wrangling pipeline:

| Step | What happened |
|---|---|
| **Loading** | Skipped 4 metadata rows at the top of the CSV |
| **Cleaning** | Dropped unnamed ghost columns, filtered to 1990–2023 |
| **Merging** | Joined GDP data with country metadata on `Country Code` |
| **Reshaping** | Used `melt()` to transform wide format (years as columns) into tidy format (one row per country per year) |

> **NaN Strategy:** Missing GDP values were left as-is. Many countries simply don't report every year — fabricating data would compromise analytical integrity.

---

##  Key Questions Answered

### 1. Which region had the highest average GDP growth (1990–2023)?
**South Asia leads at 5.41%**, while North America trails at 1.95%.

> A high average can mask extreme volatility — context always matters.

### 2. How did the 2008 Financial Crisis affect regions?

| Region | Before Crisis | After Crisis | Difference |
|---|---|---|---|
| South Asia | 5.75% | 5.59% | -0.16% |
| Europe & Central Asia | 5.14% | 0.47% | -4.67% |
| North America | 3.16% | -0.95% | -4.11% |

- **Most resilient:** South Asia — less integrated into Western financial markets; growth driven by domestic demand, not exports
- **Hardest hit:** Europe & Central Asia — suffered both the 2008 crash and the Eurozone sovereign debt crisis (2010–2012)
- **Famous concept:** The *decoupling hypothesis* — the idea that emerging markets had become independent enough from Western economies to weather Western crises

### 3. Do high-income countries grow faster?
No — the opposite is true:

| Income Group | Avg GDP Growth |
|---|---|
| Lower middle income | 4.00% |
| Low income | 3.46% |
| Upper middle income | 3.45% |
| High income | 2.55% |

> This is the **Catch-up Effect** — poorer countries grow faster by adopting existing technology and infrastructure. Richer countries must *invent* new things to grow.

### 4. Most volatile economies
**Equatorial Guinea** tops both the highest average growth AND highest volatility lists — classic oil-dependent boom/bust cycle.

Conflict nations (Iraq, Libya, South Sudan) show extreme volatility — war destroys infrastructure, disrupts trade, and drives away investment.

### 5. COVID-19 Impact (2020)

**Worst hit:** Macao SAR, China at **-54%**
> Macao's economy is almost entirely dependent on casino tourism. Visitation dropped 99.7% in April 2020.

**Best performer:** Guyana at **+43%**
> Guyana began commercial oil extraction in late 2019. While the world collapsed, Guyana was pumping oil for the first time in its history.

---

## 📊 Visualizations

| Chart | Description |
|---|---|
| Regional Average GDP Growth | Horizontal bar chart — RdYlGn palette |
| 2008 Crisis Comparison | Grouped bar chart — Before vs After by region |
| COVID-19 Impact | Top 10 worst affected countries in 2020 |
| Country Trends | Line chart — Guyana vs Macao vs Germany (1990–2023) |

---

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/orselk98/world_bank_analyis.git
cd world_bank_analyis

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the analysis
python notebooks/analysis.py
```

---

## 📁 Project Structure

```
WORLD_BANK_ANALYSIS/
├── data/
│   ├── raw/          # Original World Bank CSV files
│   └── processed/    # Cleaned data (if exported)
├── notebooks/
│   └── analysis.py   # Main analysis script
├── output/           # Generated charts
├── requirements.txt
└── README.md
```

---

## 💡 Key Concepts Practiced

`pd.read_csv()` · `skiprows` · `melt()` · `merge()` · `groupby()` · `sort_values()` · `isin()` · `between()` · `reset_index()` · `astype()` · `seaborn` · `matplotlib`