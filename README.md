# Digital Epidemiology of Cannabis-Opioid Impairment in U.S. Fatal Crashes (2018–2023)

> A longitudinal, multi-dimensional surveillance framework analyzing the impact of cannabis-polysubstance co-use on motor vehicle fatalities across the United States.

Live surveillance: https://aidea1.github.io/US-Cannabis-Polysubstance-Fatalities/
---

## 📋 Table of Contents

- [Research Overview](#research-overview)
- [Methodology](#methodology-digital-epidemiology--surveillance)
- [Digital Surveillance Map](#the-digital-surveillance-map-variable-descriptions)
- [Data](#data)

---

## Research Overview

This study provides a longitudinal, multi-dimensional analysis of the impact of cannabis-polysubstance co-use on motor vehicle fatalities. Set against the backdrop of the fentanyl-driven overdose epidemic, the research pioneers a **digital epidemiology framework** to analyze whether cannabis legalization acts as a *substitute* or a *complement* to opioid impairment in high-kinetic traffic environments.

---

## Methodology: Digital Epidemiology & Surveillance

The core of this research utilizes **Digital Epidemiology** to track the "outbreak" patterns of substance-involved fatalities. Using a dataset of **44,655 fatal involvements**, we apply spatiotemporal mapping to observe the interaction between three epidemiological components:

| Component | Description |
|-----------|-------------|
| **Toxicological Agent** | Substances involved |
| **Host** | The driver |
| **Environment** | Roadway and policy context |

---

## The Digital Surveillance Map: Variable Descriptions

The geospatial component of this study serves as a **dynamic surveillance instrument**, integrating seven layers of epidemiological data into an interactive interface.

### A. Spatiotemporal Localization
Utilizing coordinate-based geolocation, every fatal crash is mapped onto a high-resolution roadmap. This enables identification of **Toxicological Hotspots** and transit corridors where the synergistic risks of cannabis and opioids are physically concentrated.

### B. Chronological Distribution (Date & Time)
Every incident is stamped with a precise `DATETIME` value, enabling analysis of:
- Diurnal oscillations
- Seasonal trends
- Policy-response shifts across the 2018–2023 study window

### C. Kinetic Energy Monitoring (Speed Recorded)
Recorded **velocity (MPH)** is integrated as a proxy for kinetic energy potential. Speed at each crash site is mapped to analyze the *severity gradient* — determining how specific substance combinations interact with high-speed environments to influence fatality rates.

### D. Toxicological Taxonomy (Drug Combinations)

A unified color-coding system identifies the impairment profile of each case. This is the primary layer for monitoring **Synergistic Risks**:

| Color | Combination | Notes |
|-------|-------------|-------|
| 🟣 Purple | Opioid + Cannabis | Primary focus of the Fentanyl Surge analysis |
| 🔴 Red | Alcohol + Cannabis | |
| 🟠 Orange | Stimulant + Cannabis | |
| 🟢 Green | Cannabis Only | Baseline for policy assessment |
| 🔵 Blue | Polysubstance 3+ | Extreme toxicological complexity |

### E. Ecological Context (Rural-Urban Status)
Each incident is categorized by its `RUR_URB` status, representing the **Environment** in the epidemiological triad. This determines whether the opioid-cannabis surge is primarily an urban phenomenon or has reached rural high-speed corridors.

### F. Behavioral Cycles (Weekend Status)
The surveillance tool distinguishes between **Weekday** and **Weekend** involvements, where Weekend is defined as:
```
Friday 18:00 → Monday 06:00
```

This identifies how recreational behavioral cycles post-legalization influence the overall fatality burden.

### G. Risk Stratification (Holiday Risk / HRT)
**Holiday Risk (High-Risk Temporal)** is defined as high-volatility windows encompassing:
- Federal holidays
- 72–96 hour travel buffers

The map visualizes these windows to observe how mass transit and celebratory behaviors amplify the lethal synergy of cannabis and opioids.


## Data
- **Total Fatal Involvements:** 44,655
- **Study Period:** 2018–2023
- **Source:** [FARS — Fatality Analysis Reporting System](https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars)

---

## 📬 Contact & Connect

**Akshaya Bhagavathula**
North Dakota State University

🔗 [Faculty Profile](https://www.ndsu.edu/people/akshaya-bhagavathula)


- **Total Fatal Involvements:** 44,655
- **Study Period:** 2018–2023
- **Source:** [FARS — Fatality Analysis Reporting System](https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars)
