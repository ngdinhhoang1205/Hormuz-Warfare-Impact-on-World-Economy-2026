# The Biden-Era Economy: A Data-Driven Macroeconomic Evaluation (2021–2025)

## 📌 Project Overview
This analytics project provides a rigorous, data-driven evaluation of the US economy during President Joe Biden's administration. By cross-examining core financial and labor metrics against structural benchmarks, the dashboard contrasts empirical data with political rhetoric (specifically claims of "economic destruction") to isolate global supply chain shocks from domestic policy outcomes.

---

## 📊 Core Analytical Pillars & Data Counters

The dashboard is structured around three central macroeconomic pillars designed to test and contextualize political arguments:

### 1. Labor Market & Employment Resilience
*   **The Narrative Test:** Evaluating the claim of job stagnation and structural decline.
*   **Empirical Metrics:** 
    *   `UNRATE` (Unemployment Rate): Tracks the velocity of post-pandemic recovery, demonstrating a historic stretch of sub-4% unemployment—the longest continuous streak since the 1960s.
    *   `PAYEMS` (Total Nonfarm Payrolls): Measures absolute job creation, tracking cumulative employment expansion that eclipsed previous administration baselines.

### 2. Structural Growth & Long-Term Investment
*   **The Narrative Test:** Evaluating the claim that domestic policies caused structural economic decay.
*   **Empirical Metrics:**
    *   `GDPC1` (Real GDP): Demonstrates that the U.S. led the G7 nations in post-pandemic real economic output growth.
    *   `PRMNFILS` (Real Private Domestic Investment - Manufacturing): Highlights the structural surge in factory construction and high-tech infrastructure directly correlated with the passage of the CHIPS Act and the Inflation Reduction Act (IRA).

### 3. Deconstructing the Inflationary Shock
*   **The Narrative Test:** Attributing the 2021–2023 inflation spike exclusively to domestic fiscal policy.
*   **Empirical Metrics:**
    *   `CPIAUCSL` (Consumer Price Index - All Urban Consumers) vs. `GSCPI` (Global Supply Chain Pressure Index).
    *   **Data Correlation Logic:** By pairing consumer prices with global logistics stress, the analysis mathematically demonstrates how the inflation curve mirrors international maritime and supply chain friction (exogenous shocks) rather than purely localized policy.

---

## 🛠️ Data Infrastructure & Pipeline



Before pandemic
Last few days of 2019, people, especially Asian, were eagering preparing for their new year holiday, I heard the breaking news on my news feed about an outbreak of a strange disease in China. People suffocated and died rapidly after a few hours. Many people did not even make it to the hospital. People died at home and on the street. Videos of dead people were all over the places. That reminded me of the apocalypse movies I used to watch a lot, The walking dead, World war Z, train to busan,...I was on a coach back to my hometown on a short vacation, thinking that the road back to Saigon might be discrupted by this event, thinking that there are major changes that were going to happen and the world will never be the same for good.

"The 17th case, which has received significant public attention in recent days, is N.H.N (female, 26 years old), temporarily residing on Truc Bach Street, Ba Dinh District, Hanoi.
According to the Hanoi Department of Health, on February 15th, the patient departed from Noi Bai Airport to visit relatives in London (England), arriving in London on February 16th. On February 18th, the patient traveled from London to Milan, Lombardy province (Italy) for tourism (at this time, Lombardy province had not yet recorded a Covid-19 outbreak).
On February 20th, the patient returned to London. On February 25th, the patient traveled from London to Paris (France) for a one-day trip, where she met her sister (currently, the patient's sister has been reported to be infected with Covid-19). On February 26th, the patient returned to London.
On February 29th, the patient experienced coughing but did not seek medical attention. On March 1st, the patient experienced additional body aches and fatigue, but it is unclear whether they had a fever. On the same day, the patient boarded Vietnam Airlines flight VN 0054 to return to Vietnam.
The plane landed at Noi Bai Airport at 4:30 AM on March 2nd (at this time the patient did not have a fever). After completing immigration procedures, the patient was driven home in a private family car to Truc Bach Street. That day, the patient had a slight fever.
On March 5th, the patient developed a fever (38°C), a persistent cough with phlegm, fatigue, and sought medical attention at Hong Ngoc Hospital, 55 Yen Ninh Street, Ba Dinh District. The patient was diagnosed with pneumonia (X-ray showed a cloudy area at the base of the right lung). The patient was then transferred to the National Hospital for Tropical Diseases, Kim Chung Branch (Dong Anh District) for monitoring and treatment. There, N.H.N. was confirmed positive for SARS-CoV-2.
On the evening of March 6th, Hanoi decided to lock down Truc Bach Street, where patient number 17 had been residing since returning to Hanoi. 176 residents in this neighborhood were also quarantined." According to thanhnien.vn. That was the story of one the most boycotted person in Vietnam during the Pandemic for being careless in such a sensitive time. Not even Donald Trump, the president of US, took it seriously when it comes to Covid-19, thinking that it was similar to any other kind of seasonal flu.

Trump's administrastion response to the crisis and consequences
The federal response to the initial outbreak of COVID-19 under the Trump administration is frequently analyzed in public policy literature as a profound failure of warning-response integration, resulting in severe human and institutional consequences. Despite decades of specialized pandemic preparedness planning and explicit intelligence briefings detailing the impending threat in early 2020, the administration’s reaction was largely characterized by political friction, systemic delays, and highly centralized narrative management. Rather than executing a whole-of-government containment strategy, top leadership frequently minimized the virus's severity to protect economic metrics, clashed with career scientists, and relied on partial, top-down measures like travel restrictions while structural preparation lagged.

This response pattern triggered critical breakdowns across the machinery of government. Long-standing structural frictions between agencies like the Department of Health and Human Services (HHS), the CDC, and the White House slowed the upward flow of actionable intelligence. Consequently, during the vital initial window of the outbreak, the United States missed opportunities to implement robust mass testing, contact tracing, and medical supply chain coordination. The administration's public messaging frequently directly contradicted the consensus of its own public health officials, creating a fragmented information landscape that eroded public trust and left states to compete aggressively against one another for scarce personal protective equipment (PPE) and ventilators.

The consequences of these systemic vulnerabilities were severe and enduring. Public health assessments, including reports published in The Lancet, estimated that a substantial portion of early American COVID-19 fatalities could have been averted with a more proactive, cohesive federal strategy. Beyond the immediate toll of human life, the crisis deeply politicized foundational public health institutions, straining the relationship between federal oversight and state-level execution. Ultimately, the administration's early crisis management illustrated how political polarization and centralized executive skepticism can transform a heavily forecasted, well-simulated biological threat into an acute strategic surprise.

The impacts of Trump's administration on the economy during and after covid 19
1. The Immediate Crisis Shock and Emergency Relief (2020)
When the pandemic struck in early 2020, the U.S. economy faced its worst contraction since the Great Depression, with unemployment spiking to an unprecedented 14.7% in April 2020.

In response, the administration pivoted toward massive, bipartisan fiscal intervention. Working with Congress, President Trump signed two monumental stimulus bills into law in 2020—the CARES Act ($2.2 trillion) in March and a follow-up consolidated relief package ($900 billion) in December.

Household Income Cushioning: The administration deployed direct Economic Impact Payments ($1,200 per qualified adult in the first wave) and expanded unemployment insurance by $600 per week. Data from the Council of Economic Advisers later showed these measures successfully prevented millions of families from falling into poverty, temporarily raising disposable income despite massive job losses.

Corporate and Small Business Stabilizing: The Paycheck Protection Program (PPP) provided forgivable loans to small and medium-sized businesses to incentivize keeping workers on payroll. Concurrently, the administration supported the Federal Reserve's massive expansion of liquidity, backing corporate credit and halting a projected wave of small business bankruptcies.

2. Supply Chains and Market Friction
While fiscal relief kept consumer demand afloat, the administration’s broader operational handling of the pandemic created unique market frictions.

Fragmented Procurement: As noted in public administration literature, the administration's initial failure to establish centralized medical supply chains forced individual states and private healthcare networks to compete against one another. This fragmentation drove up procurement costs for personal protective equipment (PPE) and ventilators, introducing localized economic inefficiencies.

Trade Policy Adjustments: Existing tariff wars (particularly with China) and localized travel bans disrupted global manufacturing pipelines. While aimed at long-term isolation of foreign threats, these friction points complicated the raw material imports needed by domestic manufacturers during the height of the shutdown.

3. Post-Crisis Economic Consequences (2021 and Beyond)
The decisions made during 2020 set the stage for the macroeconomic landscape that followed the administration's tenure.

The Inflation Runway: The massive infusion of direct cash payments and aggressive monetary easing successfully jump-started consumer demand. However, because consumer demand roared back much faster than frozen global supply chains could recover, this combination laid the groundwork for the severe inflation wave that hit the U.S. economy starting in 2021.

Exploding National Debt: The emergency stimulus packages, combined with reduced tax revenues from the 2017 corporate tax cuts and the 2020 economic freeze, added roughly $7.8 trillion to the gross national debt during Trump's single term. This drastic fiscal expansion significantly reduced the federal government's long-term budget flexibility.

Labor Market Shift: Programs like the PPP successfully made an estimated 80% of corporate layoffs temporary rather than permanent. While this allowed for a rapid initial "V-shaped" hiring recovery in late 2020, it also accelerated broader, permanent structural shifts toward remote work and logistics-heavy industries.

<p align="center">
  <img src="images\Screenshot 2026-07-19 152346.png" alt="Power BI Economic Dashboard" width="800px">
</p>