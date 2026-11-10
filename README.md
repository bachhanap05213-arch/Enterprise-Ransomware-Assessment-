# Enterprise Ransomware Assessment

**Author:** Abhishek Ramchandra Patil  
**Topic:** Enterprise Ransomware Assessment: Drafted a corporate risk register mapped to the NIST CSF framework.

## Overview
An educational starter risk register covering common enterprise ransomware scenarios. Each entry includes affected assets, threat source, control gap, likelihood, impact, score, rating, NIST CSF 2.0 Function, treatment recommendation, owner and status.

**Important:** The sample risks and scores are illustrative, not findings from a real company. Validate them with organizational evidence before use.

## Deliverables
- `Abhishek_Ramchandra_Patil_Enterprise_Ransomware_Assessment.ipynb` — Jupyter Notebook.
- `Abhishek_Ramchandra_Patil_Enterprise_Ransomware_Assessment.py` — Python program.
- `requirements.txt` — dependencies.
- `Abhishek_Ramchandra_Patil_ProjectReport.docx` — project report.

## NIST CSF 2.0 mapping
The six Functions are Govern, Identify, Protect, Detect, Respond and Recover. This project maps each sample scenario to a primary Function at a high level; it is not a control-by-control compliance assessment.

## Scoring
Likelihood (1–5) × Impact (1–5). Illustrative bands: 1–5 Low, 6–11 Medium, 12–19 High, 20–25 Critical. Replace these with your organization's approved methodology.

## Run
Requires Python 3.9+; standard library only.
```bash
python Abhishek_Ramchandra_Patil_Enterprise_Ransomware_Assessment.py
```
The program prints the register summary and creates `ransomware_risk_register.csv`. Alternatively, open the notebook in Jupyter or Google Colab and run all cells.

## Customize
Replace example risks, scores, owners and treatments with evidence from asset inventories, interviews, architecture reviews, vulnerability information, incident history and business impact analysis. Add control evidence, residual risk, due dates and review dates as needed.

## Limitations
This project does not scan systems, validate backups, test controls, estimate actual financial loss or certify NIST CSF compliance.

## References
- NIST Cybersecurity Framework 2.0: https://www.nist.gov/cyberframework
- NIST CSF 2.0 (NIST CSWP 29): https://doi.org/10.6028/NIST.CSWP.29
- CISA StopRansomware: https://www.cisa.gov/stopransomware
