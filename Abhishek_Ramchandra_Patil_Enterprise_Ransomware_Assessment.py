"""Enterprise Ransomware Assessment — Abhishek Ramchandra Patil.
Illustrative risk register mapped to NIST CSF 2.0. Customize using organizational evidence."""
import csv
from dataclasses import dataclass, asdict

@dataclass
class Risk:
    risk_id: str
    scenario: str
    affected_assets: str
    threat_source: str
    control_gap: str
    likelihood: int
    impact: int
    nist_csf_function: str
    recommended_treatment: str
    owner: str
    status: str = "Open"
    @property
    def score(self): return self.likelihood * self.impact
    @property
    def rating(self):
        return "Critical" if self.score >= 20 else "High" if self.score >= 12 else "Medium" if self.score >= 6 else "Low"

def sample_risks():
    return [
      Risk("R-01","Phishing causes credential theft and ransomware entry","Email, identity, endpoints","Phishing group","Weak phishing resistance or reporting","4","5","Protect","Deploy phishing-resistant MFA, email filtering, awareness and reporting","Identity Lead"),
      Risk("R-02","Compromised privileged account enables broad encryption","Directory, cloud identity, servers","Credential thief","Excessive privilege or weak admin controls",3,5,"Protect","Use PAM, least privilege, separate admin accounts and MFA","IT Operations Lead"),
      Risk("R-03","Unpatched internet-facing system is exploited","VPN, gateways, public apps","External attacker","Delayed patching or incomplete asset inventory",4,4,"Identify","Inventory assets and prioritize exposed critical patches","Infrastructure Lead"),
      Risk("R-04","Backups are encrypted, deleted or unavailable","Backup platform and repositories","Ransomware operator","Online backups or untested restores",3,5,"Recover","Maintain offline/immutable backups and test restoration","Continuity Lead"),
      Risk("R-05","Lateral movement spreads ransomware","Endpoints, file servers, network","Ransomware operator","Flat network or limited EDR coverage",3,5,"Detect","Segment critical systems and monitor endpoints and lateral movement","SOC Manager"),
      Risk("R-06","Sensitive data is exfiltrated before encryption","File shares, databases, customer records","Ransomware operator","Weak data access governance or egress monitoring",3,5,"Protect","Classify data, restrict access and monitor unusual transfers","Data Protection Lead"),
      Risk("R-07","Incident response is delayed or inconsistent","Enterprise services","Readiness gap","Untested playbook or unclear authority",3,4,"Respond","Approve and exercise ransomware response playbook","Incident Response Lead"),
      Risk("R-08","Supplier compromise introduces ransomware","Supplier access, managed services","Compromised supplier","Limited supplier assurance and access monitoring",3,4,"Govern","Assess suppliers, constrain remote access and require incident notice","Third-Party Risk Lead")
    ]

def export_csv(risks, path="ransomware_risk_register.csv"):
    fields=list(asdict(risks[0]).keys())+["score","rating"]
    with open(path,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
        for r in risks:
            row=asdict(r); row.update(score=r.score,rating=r.rating); w.writerow(row)

if __name__=="__main__":
    risks=sample_risks()
    for r in risks: print(r.risk_id, r.score, r.rating, r.nist_csf_function, r.scenario)
    export_csv(risks)
    print("Created ransomware_risk_register.csv")
