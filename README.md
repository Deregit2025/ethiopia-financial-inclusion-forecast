
# Forecasting Financial Inclusion in Ethiopia

## Project Overview
This project develops a transparent, policy-oriented forecasting system to analyze and project Ethiopia’s financial inclusion trajectory using the World Bank Global Findex framework. The analysis integrates historical data, event-driven modeling, and scenario-based projections to provide actionable insights for policymakers and financial institutions.

### Core Dimensions
- **Access** — Account Ownership Rate (`ACC_OWNERSHIP`)
- **Usage** — Digital Payment Adoption Rate (`ACC_MM_ACCOUNT`, `USG_P2P_COUNT`)

### Key Highlights
- Historical trend analysis (2011–2024)  
- Scenario-based forecasts (2025–2027) under **Base**, **Optimistic**, and **Pessimistic** conditions  
- Inclusion projections vs. 60% policy target benchmark  
- Interactive dashboards for exploration and policy simulation  

---

## Business Context
Ethiopia is undergoing rapid digital financial transformation driven by:
- Expansion of mobile money platforms such as **Telebirr** and **Fayda**
- Market liberalization and emergence of new fintech entrants
- National digital infrastructure initiatives including 4G coverage expansion  

Despite progress, financial inclusion growth has slowed, making it critical to understand historical patterns, project future trends, and evaluate the effectiveness of policy interventions.

---

## Project Objectives
1. Understand and enrich Ethiopia’s financial inclusion data  
2. Analyze historical trends and structural gaps  
3. Model the impact of major events and policy interventions on financial inclusion  
4. Forecast key indicators for 2025–2027 using scenario-based methods  
5. Communicate insights via an interactive dashboard for policymakers and stakeholders  

---

## Data
### Primary Datasets
- `ethiopia_fi_unified_data.csv` — unified dataset combining observations, events, and modeled impact links
- `reference_codes.csv` — mapping of indicator and event codes to human-readable names

### Additional Resources
- `data_enrichment_log.md` — documents supplementary data sources and transformations
- Data processed to handle missing values, normalize units, and compute confidence intervals

---

## Methodology Overview
1. **Exploratory Data Analysis (EDA)**  
   - Multi-year trend analysis  
   - Event annotation and overlay on indicator trends  
   - Identification of structural gaps in access and usage metrics  

2. **Event Impact Modeling**  
   - Lagged, additive effects for major financial interventions  
   - Policy, product launches, and infrastructure developments encoded as discrete events  

3. **Forecasting & Scenario Analysis**  
   - Trend-based extrapolation for 2025–2027  
   - Scenario modeling: **Base**, **Optimistic**, **Pessimistic**  
   - Confidence intervals (upper/lower bounds) for all projections  

4. **Interactive Dashboard**  
   - Streamlit application for exploration of historical trends, forecasts, and inclusion projections  
   - Supports filtering by indicator, scenario, and year range  
   - Visual cues for 60% inclusion target benchmark  

---

## Project Structure
```

├── data/                     # Raw and processed datasets
├── notebooks/                # Task-based analysis notebooks (Task 1–5)
├── src/                      # Reusable Python modules (data processing, modeling, forecasting)
├── dashboard/                # Streamlit app
│   ├── app.py                # Main application
│   ├── plots.py              # Visualization functions
│   └── metrics.py            # KPI computation functions
├── reports/                  # Figures, charts, and summaries
├── tests/                    # Unit tests for processing, modeling, and forecasting
├── .github/
│   └── workflows/
│       └── unittests.yml     # GitHub Actions workflow
├── requirements.txt
└── README.md

````

---

## Installation & Setup

### Clone the Repository
```bash
git clone <repository_url>
cd ethiopia-financial-inclusion
````

### Create Python Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Dashboard

```bash
streamlit run dashboard/app.py
```

### Dashboard Features

1. **Overview**

   * Displays top-level KPIs: Account Ownership, Digital Payment Usage, P2P/ATM Ratio
   * Includes human-readable indicator mapping
   * Provides visual cues for trends and targets

2. **Trends Page**

   * Select one or multiple indicators (`ACC_OWNERSHIP`, `ACC_MM_ACCOUNT`, etc.)
   * Year range slider: 2011–2024
   * Event overlays show major policy/product milestones

3. **Forecasts (2025–2027)**

   * Scenario selection: Base, Optimistic, Pessimistic
   * Line charts with upper/lower confidence intervals
   * CSV download for projections

4. **Inclusion Projections**

   * Compare projected values against 60% policy target
   * Bar charts with confidence intervals
   * Indicator and scenario selection dropdowns

---

## Testing

Unit tests cover:

* Data preprocessing and cleaning
* KPI computation
* Forecast generation logic

Run all tests:

```bash
pytest tests/ --disable-warnings -v
```

### Continuous Integration

GitHub Actions workflow (`.github/workflows/unittests.yml`) executes tests on:

* Every push to main or feature branches
* Pull requests

---

## Development & Branching Workflow

* Each task is developed on a dedicated branch (`task-1` … `task-5`)
* `main` branch contains fully merged and tested code
* Commit messages reference tasks for traceability, e.g.,

  ```
  feat(task-5): add Inclusion Projections dashboard page with scenarios
  ```

---

## References

* [World Bank Global Findex](https://globalfindex.worldbank.org/)
* [Ethiopia National Bank Reports](https://www.nbe.gov.et/)
* Dashboards inspired by policy-focused visual analytics best practices



