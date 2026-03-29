# Hospital Supply Procurement Analysis: Uncovering Spending Patterns in Ecuadorian Public Healthcare

## Overview

This project analyzes public procurement data from an Ecuadorian hospital to understand spending patterns, supplier relationships, and cost trends. By combining web scraping, data engineering, and visualization, this analysis reveals critical insights into public healthcare purchasing behavior—demonstrating how data science can support transparency and accountability in public sector spending.

**Data Source:** Public records from the hospital website and Ecuador's Public Procurement Portal (compraspublicas.gob.ec)

---

## Research Questions

This analysis addresses three key business questions:

1. **Supplier Landscape:** What types of suppliers (individuals vs. companies) dominate hospital contracts, and how do these relationships evolve over time?

2. **Spending Trends:** How has hospital procurement spending grown annually from 2017 through mid-2020, and what patterns emerge?

3. **Seasonal & Temporal Analysis:** How does spending vary throughout the year, and what trends emerge in purchasing behavior?

---

## Procurement Processes Analyzed

- **Subasta Inversa Electrónica** (Reverse Electronic Auction): Competitive bidding process for public contracts
- **Régimen Especial** (Special Regime): Alternative procurement process for specific contract categories

Both processes are tracked through their complete lifecycle, focusing on "Adjudicado" (awarded) contracts to analyze actual spending decisions.

---

## Technical Approach

### Data Pipeline

**Data Collection:**
- Web scraping from hospital website to extract PDF metadata
- Automated scraping from compraspublicas.gob.ec to access procurement records
- Multi-source data integration (hospital records + public procurement portal)

**Data Processing:**
- PDF extraction and text parsing
- Data cleaning and standardization across multiple sources
- Time-series aggregation by year and procurement process
- Enrichment with additional context for awarded contracts

**Analysis & Visualization:**
- Temporal trend analysis (2017–2020)
- Supplier composition analysis
- Spending pattern decomposition
- Year-over-year comparisons

### Technology Stack

**Languages & Libraries:**
- Python (Pandas, Seaborn, web scraping tools)
- Jupyter Notebooks for reproducible analysis

**Data Sources:**
- Hospital website (PDFs)
- Ecuador's Public Procurement Portal (compraspublicas.gob.ec)

---

## Project Workflow

### Scripts Overview

| Script | Purpose |
|--------|---------|
| `get-urls.ipynb` | Extract URLs from hospital website for PDF files (staffing, payroll, procurement contracts) |
| `download-pdfs.ipynb` | Automate PDF downloads from extracted URLs |
| `search-processSIE.ipynb` | Extract and parse data for "Subasta Inversa Electrónica" procurement process |
| `search-processRE.ipynb` | Extract and parse data for "Régimen Especial" procurement process |
| `concat_allfiles.ipynb` | Consolidate data across multiple years into unified datasets |
| `get-alldata.ipynb` | Enrich datasets with additional details for awarded contracts ("Adjudicado" status) |
| `newgraphics.ipynb` | Generate comprehensive visualizations and trend analysis ([View Here](https://github.com/eluzuriaga83/hagp-corruption/blob/master/scripts/newgraphics.ipynb)) |

---

## Key Skills Demonstrated

**Data Engineering:**
- Web scraping and automated data collection
- Multi-source data integration
- ETL pipeline design for complex, unstructured data
- Data cleaning and validation at scale

**Data Analysis:**
- Temporal trend analysis and time-series decomposition
- Categorical analysis (supplier types, procurement processes)
- Comparative analysis across years and contract categories

**Data Visualization:**
- Clear, actionable visualizations of spending trends
- Supplier segmentation and distribution analysis
- Temporal pattern identification

**Problem Solving:**
- Working with messy, real-world public data
- Designing reproducible analysis workflows
- Translating procurement data into transparency insights

---

## Business Impact & Insights

This project demonstrates how data science supports **government transparency and public accountability**:

- Identifies spending trends that may warrant policy review
- Reveals supplier concentration and competition patterns
- Enables evidence-based procurement decision-making
- Provides public visibility into healthcare spending

---

## How to Use This Project

1. **Start with the data collection scripts** (`get-urls.ipynb` → `download-pdfs.ipynb`) to understand how data is sourced
2. **Follow the processing pipeline** (`search-processSIE.ipynb` → `concat_allfiles.ipynb`) to see data transformation steps
3. **Review the visualizations** in `newgraphics.ipynb` to understand key findings
4. **Explore the repository** for detailed annotations within each notebook

---

## Future Enhancements

- Automated monthly reporting dashboard for spending monitoring
- Supplier risk analysis and concentration metrics
- Anomaly detection for unusual procurement patterns
- Interactive visualizations for stakeholder reporting
- Integration with additional hospital systems for comparative analysis

---

## About This Project

This analysis was conducted as part of public sector transparency research, combining technical data engineering skills with a commitment to supporting government accountability. It demonstrates how open data and analytical rigor can drive insights into public spending.

---

**Repository:** [hagp-corruption](https://github.com/eluzuriaga83/hagp-corruption)
