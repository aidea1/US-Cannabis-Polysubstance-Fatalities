## 🗺️ Surveillance Map — Code Walkthrough

> **⚠️ Educational Reference Only**
> This code is shared strictly for transparency and methodological reproducibility. The underlying dataset (`FARS_ENRICHED_TEMPORAL_2026.csv`) is not publicly available. You cannot run this script without institutional access to the enriched FARS dataset.

---

### Dependencies
```
pandas
folium
folium[plugins]
```

---

### Step 1 — Load & Clean the Dataset
```python
import pandas as pd
import folium
from folium.plugins import FastMarkerCluster

# Load the enriched FARS dataset (not publicly distributed)
# Expected columns: LATITUDE, LONGITUD, DATETIME, RUR_URB,
#                   DRUG_COMBINATION_TYPE, ESTIMATED_SPEED_LIMIT,
#                   HIGH_RISK_TEMPORAL, IS_WEEKEND_WINDOW
df = pd.read_csv("FARS_ENRICHED_TEMPORAL_2026.csv", encoding='latin1')

# Drop records missing geolocation — required for mapping
df_clean = df.dropna(subset=['LATITUDE', 'LONGITUD']).copy()

# Cast DATETIME to string for tooltip rendering
df_clean['DATETIME_STR'] = df_clean['DATETIME'].astype(str)

# Decode the RUR_URB numeric code into a human-readable label
# FARS codes: 1=Rural, 2=Urban, 6=Other, 9=Unknown
rural_urban_map = {1: "Rural", 2: "Urban", 6: "Other", 9: "Unknown"}
df_clean['RUR_URB_LABEL'] = df_clean['RUR_URB'].map(rural_urban_map).fillna("Unknown")
```

---

### Step 2 — Toxicological Color Scheme
```python
# Each drug combination type is assigned a distinct hex color.
# This palette is the primary visual layer of the surveillance map.
color_map = {
    'Cannabis Only':                  '#27AE60',  # Green   — baseline reference group
    'Cannabis + Stimulant':           '#E67E22',  # Orange  — stimulant co-use
    'Cannabis + Alcohol':             '#C0392B',  # Red     — alcohol co-use
    'Cannabis + Opioid':              '#8E44AD',  # Purple  — primary focus (fentanyl surge)
    'Cannabis Polysubstance (3+)':    '#0F4AEA',  # Blue    — extreme toxicological complexity
    'Stimulant Only':                 '#2980B9',  # Steel   — non-cannabis stimulant cases
    'Other Polysubstance (No Cannabis)': '#7F8C8D' # Grey  — non-cannabis polysubstance
}
```

---

### Step 3 — Initialize the Base Map
```python
# Centered on the geographic centroid of the contiguous United States
# OpenStreetMap is used as the tile layer for open reproducibility
m = folium.Map(
    location=[37.0902, -95.7129],
    zoom_start=4,
    tiles='OpenStreetMap'
)
```

---

### Step 4 — Interactive Marker Rendering (JavaScript Callback)
```python
# FastMarkerCluster uses a JavaScript callback to render each crash
# as a styled CircleMarker with an epidemiological tooltip.
#
# Row index reference:
#   row[0] = LATITUDE
#   row[1] = LONGITUDE
#   row[2] = Hex color (drug combination)
#   row[3] = HIGH_RISK_TEMPORAL flag  (1 = Holiday Risk Window)
#   row[4] = DRUG_COMBINATION_TYPE    (string label)
#   row[5] = ESTIMATED_SPEED_LIMIT    (MPH)
#   row[6] = DATETIME_STR             (crash timestamp)
#   row[7] = RUR_URB_LABEL            (Rural / Urban / Other)
#   row[8] = IS_WEEKEND_WINDOW flag   (1 = Fri 18:00 – Mon 06:00)

callback = """
function (row) {
    var marker = L.circleMarker([row[0], row[1]], {
        radius:      6,
        fillColor:   row[2],
        color:       'white',
        weight:      1,
        fillOpacity: 0.8
    });

    marker.bindTooltip(
        "<div style='font-family: Arial; font-size: 13px; line-height: 1.5;'>" +
        "<b style='font-size: 13px; color: #2C3E50;'>" + row[6] + "</b><br>" +
        "<hr style='margin: 4px 0; border: 0; border-top: 1px solid #EEE;'>" +
        "<b>DRUG:</b> "         + row[4] + "<br>" +
        "<b>SPEED:</b> "        + row[5] + " MPH<br>" +
        "<b>GEO:</b> "          + row[7] + "<br>" +
        "<b>TIMING:</b> "       + (row[8] == 1 ? "Weekend Window" : "Weekday") + "<br>" +
        "<b>HOLIDAY RISK:</b> " + (row[3] == 1 ? "YES" : "No") +
        "</div>",
        {sticky: true}
    );
    return marker;
}
"""
```

---

### Step 5 — Build the Data Payload & Render Clusters
```python
# Construct the row array fed into each marker's callback.
# Order must exactly match the row index reference above.
map_data = []
for idx, row in df_clean.iterrows():
    color = color_map.get(row['DRUG_COMBINATION_TYPE'], '#BDC3C7')  # default: light grey
    map_data.append([
        row['LATITUDE'],
        row['LONGITUD'],
        color,
        int(row['HIGH_RISK_TEMPORAL']),
        str(row['DRUG_COMBINATION_TYPE']),
        str(row['ESTIMATED_SPEED_LIMIT']),
        str(row['DATETIME_STR']),
        str(row['RUR_URB_LABEL']),
        int(row['IS_WEEKEND_WINDOW'])
    ])

FastMarkerCluster(data=map_data, callback=callback).add_to(m)
```

---

### Step 6 — Watermark & Export
```python
# A non-interactive watermark is injected into the HTML output
# to assert authorship and enforce the educational-use designation.
watermark_html = """
<div style="
    position: fixed;
    bottom: 10px;
    right: 10px;
    z-index: 10000;
    font-size: 20px;
    color: rgba(150, 150, 150, 0.5);
    font-weight: bold;
    font-family: Arial, sans-serif;
    pointer-events: none;
    user-select: none;">
    © 2026 Akshaya Bhagavathula — Marijuana Fatalities Study — Educational Purpose Use Only
</div>
"""
m.get_root().html.add_child(folium.Element(watermark_html))

# Export the final interactive HTML map
m.save("CHRONO_FARS_AUDITOR_2026.html")
print("Surveillance map generated successfully.")
```

---

> 📌 **Note:** File paths have been removed. The dataset `FARS_ENRICHED_TEMPORAL_2026.csv` is a derived, institution-specific enrichment of the [NHTSA FARS database](https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars) and is **not available for public download**.
