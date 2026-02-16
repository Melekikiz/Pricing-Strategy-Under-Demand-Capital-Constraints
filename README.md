# Pricing-Strategy-Under-Demand-Capital-Constraints

**A Revenue & Risk Simulation Framework**

⚠️ This project is a simulation-based strategic pricing framework created for demonstration purposes.
It does not represent real company data.

**📌 Project Overview**

This project demonstrates how pricing decisions can be translated into a structured, risk-aware revenue strategy rather than isolated elasticity estimates.

Instead of asking:

“Can we increase prices?”

This framework asks:

Where can we increase prices safely?

What is the revenue impact under different scenarios?

How does price sensitivity translate into operational risk?

How should inventory and portfolio strategy adapt?

The project integrates elasticity modeling, scenario simulation, and operational risk mapping into a unified decision framework.

**🎯 Business Problem**

Organizations frequently increase prices to protect margins. However:

Demand may contract

Revenue may decrease

Operational risk may increase

Inventory planning may become inefficient

Promotional effectiveness may shift

This project builds a structured approach to answer:

Which regions/categories are safe for price increases?

What is the optimal balance between volume protection and margin expansion?

How should pricing strategy differ across portfolios?

**🧠 Methodology**

1️⃣ Data Preparation

Category-level demand aggregation

Regional segmentation (US, EU, APAC, TR)

Promotion-adjusted volume normalization

Revenue calculation baseline

2️⃣ Elasticity Estimation

Price elasticity of demand estimated using a log-log regression model:

%ΔQ=β×%ΔP

Where:

β = price elasticity coefficient

R² used to evaluate model explanatory strength

Elasticity classification:

|β| < 0.3 → Low sensitivity

0.3–0.7 → Moderate sensitivity

0.7 → High sensitivity

3️⃣ Scenario Simulation

Three pricing strategies were simulated:

🔴 Aggressive

High price increases

Margin expansion focus

Higher volume risk

🟡 Balanced

Moderate price increases

Revenue optimization focus

🟢 Conservative

Minimal price increases

Volume protection focus

For each scenario:

New price computed

Demand adjusted using elasticity

Revenue recalculated

Volume loss estimated

4️⃣ Revenue Engine

Revenue formula:
Revenue=Adjusted Price×Adjusted Quantity

Volume adjustment:
New Quantity=Base Quantity×(1+Elasticity×Price Change%)

This allows simulation of revenue impact before real-world execution.

5️⃣ Operational Risk Translation Layer

Elasticity scores were translated into operational implications:

Elasticity Level	Risk Implication
Low	Safe margin expansion
Moderate	Monitor closely
High	Volume protection required

This step transforms statistical output into business decision language.

6️⃣ Portfolio Resilience Mapping

Cross-analysis performed on:

Region × Category

Elasticity × Revenue share

Promotion responsiveness

This identifies:

Margin expansion zones

High-risk contraction areas

Campaign-sensitive markets

**🏗 Model Architecture**

Raw Data

   ↓
   
Elasticity Model (Log-Log Regression)

   ↓
   
Scenario Simulator (Aggressive / Balanced / Conservative)

   ↓
   
Revenue Engine

   ↓
   
Operational Risk Mapping

   ↓
   
Strategic Recommendation Layer


The framework separates statistical modeling from strategic interpretation.

**📈 Key Findings (Simulation Insights)**

APAC Electronics shows high margin expansion potential.

US Fashion is highly elastic  aggressive pricing destroys revenue.

EU region shows strong promotional multiplier effect.

Turkey requires volume-protection strategy due to sensitivity.

Revenue does not always increase with price hikes.

Balanced strategy maximizes revenue under most tested conditions.

**⚖️ Scenario Comparison Summary**
Strategy	Revenue Impact	Volume Risk	Operational Stability
Aggressive	High variance	High	Low
Balanced	Optimized	Moderate	High
Conservative	Stable	Low	Very High

Balanced strategy selected as optimal under simulation.

**📊 Strategic Insights**

Price increases must be elasticity-aware.

Regional pricing strategy should not be uniform.

Promotion-heavy regions behave differently from margin-driven markets.

Elasticity must be translated into operational planning.

Portfolio-level decisions outperform isolated category decisions.

**⚠️ Limitations**

Some categories show low R² (weak explanatory power)

Linear elasticity assumption

No cross-elasticity (substitution effects) modeled

No macroeconomic variables included

Simulation-based (not real-world implementation)

**🚀 Future Improvements**

Bayesian elasticity modeling

Cross-category substitution modeling

Dynamic pricing engine

Time-series demand modeling

Real-time BI dashboard integration

Inventory optimization integration

**🧰 Tech Stack**

Python

Pandas

NumPy

Scikit-learn

Matplotlib / Seaborn

Jupyter Notebook

SQL

**👩‍💻 Author**

Developed as a strategic pricing and revenue optimization case study.
Focused on bridging analytics and executive decision-making.

**Designed and Developed by Melek İkiz**

**Focused on Pricing Strategy, Revenue Optimization & Decision Analytics**
