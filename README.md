# NHL End-to-End Data Analytics Project

An end-to-end analytics pipeline built on public NHL data: automated ingestion, SQL modeling, Power BI dashboards, and machine learning to predict game outcomes.

> **Status:**  In progress!!!

## The questions this project answers

- What actually drives winning in the NHL?
- How much does home ice advantage matter?
- Which team statistics are the best predictors of a win?
- Which teams are most likely to win next, and how might the season play out?

*(Refine these as the analysis develops.)*

*Please note: This project explores not only what drives winning in the NHL, but also how team dynamics, player performance, and contextual factors interact to shape outcomes across seasons.*

## Initial Architecture

<img width="1284" height="593" alt="image" src="https://github.com/user-attachments/assets/575edc4d-e278-44ab-809a-c72712d17fdb" />


## Tech stack

- **Python:** extraction, cleaning, EDA, machine learning (pandas, scikit-learn, seaborn)
- **SQL / PostgreSQL:** transformation, modeling, analytical queries
- **AWS:** Lambda and S3 for automated ingestion
- **GitHub Actions:** version control, automation, documentation
- **Power BI:** interactive dashboards
- **Snowflake:** planned final phase, migrating the warehouse layer

## Machine learning plan

- **Target:** game win probability
- **Baseline:** logistic regression, compared against a "home team always wins" benchmark
- **Next:** gradient boosting if it improves performance
- **Validation:** time-based train/test split, using only information available before each game
- **Secondary output:** season simulations based on predicted probabilities

## Roadmap

- [ ] Phase 1: Ingest NHL data (teams, games, standings, team and skater stats)
- [ ] Phase 2: Exploratory Data Analysis (EDA)
- [ ] Phase 3: Clean and model the data in PostgreSQL
- [ ] Phase 4: Team Performance dashboard
- [ ] Phase 5: ML model and Predictions dashboard
- [ ] Phase 6: Automate with Lambda and GitHub Actions
- [ ] Phase 7: Player Performance and General NHL dashboards
- [ ] Phase 8: Migrate warehouse layer to Snowflake

## Initial Repository structure

```
nhl-analytics/
├── data/            # local sample data (not committed in full)
├── ingestion/       # Python scripts and Lambda code
├── sql/             # staging and analytics SQL scripts
├── notebooks/       # EDA and ML notebooks
├── dashboards/      # Power BI files and screenshots
├── docs/            # project documentation
└── README.md
```


## Key findings

*To be added once the analysis is complete.*

## Dashboards

*Screenshots and published link to be added.*

## How to run

*Setup and run instructions to be added as the pipeline is built.*

## Data source

Public NHL API. All data belongs to the NHL; this project is for educational and portfolio purposes.

## Author

**José Osorio** · Data Analyst
[LinkedIn](https://www.linkedin.com/in/jose-miguel-osorio-davila-67b126348/)
