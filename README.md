# Beauty Trends SQL
SQL analysis of influencer vs. traditional vs. prestige beauty brand performance using Sephora product and review data.

## Overview
With the rise of celebrity and creator-founded beauty brands, I wanted to know: do influencer brands actually perform better, or is it just hype? I pulled a Sephora product and review dataset (~8,500 products, 1M+ reviews) from Kaggle, loaded it into SQLite, and wrote a series of SQL queries to find out.

## Dataset
- **Source**: [Sephora Products and Skincare Reviews](https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews) via Kaggle
- **Size**: 8,494 products, 1,094,411 reviews
- **Brand classification**: Brands manually classified into three tiers — influencer/creator (Fenty, Rare Beauty, Summer Fridays, etc.), prestige (La Mer, Tatcha, Charlotte Tilbury, etc.), and traditional (everything else)

## Key Findings

### 1. Influencer brands rate lowest overall
| Brand Type | Avg Rating | Recommend Rate |
|------------|------------|----------------|
| Prestige | 4.31 | 85% |
| Traditional | 4.30 | 84% |
| Influencer | 4.24 | 82% |

Despite the cultural dominance of influencer brands, they consistently underperform prestige and traditional brands on both rating and recommendation rate.

### 2. Prestige is the worst value for money
| Brand Type | Avg Price | Price Per Rating Point |
|------------|-----------|----------------------|
| Prestige | $87.20 | $20.25 |
| Traditional | $43.05 | $10.01 |
| Influencer | $41.07 | $9.69 |

Influencer brands are actually the best value dollar-for-dollar — they're priced similarly to traditional brands but the gap in quality is small. Prestige is by far the worst value at over $20 per rating point.

### 3. Hype decay is real — but not universal
Tracking ratings year-over-year reveals a clear pattern for most influencer brands: ratings spike at launch and decline as novelty fades.

- **LAWLESS**: 4.69 (2020) → 3.00 (2023) — steepest decay in the dataset
- **JLo Beauty**: 4.10 (2021) → 3.70 (2023) — most expensive influencer brand at $57.65 avg, worst performer
- **CAY SKIN**: 4.34 (2022) → 3.76 (2023) — sharp drop after launch year

Exceptions exist though — **Summer Fridays** recovered from a rough 2020 (3.62) and is now trending up at 4.51 in 2023. **KORA Organics** has maintained relevance since 2017 with relatively stable ratings, suggesting Miranda Kerr's brand has real staying power.

### 4. Smaller influencer brands outperform celebrity megabrands
| Brand | Reviews | Avg Rating |
|-------|---------|------------|
| Gisou | 81 | 4.90 |
| Danessa Myricks Beauty | 67 | 4.63 |
| LAWLESS | 251 | 4.60 |
| KORA Organics | 7,307 | 4.36 |
| Summer Fridays | 15,004 | 4.15 |
| JLo Beauty | 3,004 | 4.11 |

The smaller creator brands (Gisou, Danessa Myricks) consistently outperform the mega-celebrity brands (JLo, Fenty Skin). Niche expertise beats name recognition.

### 5. Influencer brands are concentrated in Makeup, absent in Fragrance
Influencer brands have 15 brands and 424 products in Makeup — nearly matching prestige despite having fewer total brands. In Fragrance, only 2 influencer brands exist with 24 products. Fragrance remains a category dominated by heritage and prestige houses.

## Tech Stack
- **Python** — data ingestion and analysis (pandas, SQLAlchemy)
- **SQLite** — local database
- **SQL** — aggregations, window functions, CTEs, LEFT JOINs, date functions

## How to Run
1. Clone the repo
2. Download the dataset from Kaggle and place CSVs in `/data`
3. Create a virtual environment and run `pip install pandas sqlalchemy`
4. Run `python ingest.py` to build the database
5. Modify `queries.sql` and run `python analyze.py` to explore
```

---