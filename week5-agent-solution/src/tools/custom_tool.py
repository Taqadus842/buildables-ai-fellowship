class ClauseClassifierTool:
    name = "clause_classifier"
    description = "Classifies contract clauses into categories: Payment, Termination, Liability, Confidentiality, Other."

    def _run(self, clause: str) -> str:
        clause = clause.lower()
        if "pay" in clause or "payment" in clause:
            return "Payment Clause"
        elif "terminate" in clause or "termination" in clause:
            return "Termination Clause"
        elif "liability" in clause:
            return "Liability Clause"
        elif "confidential" in clause:
            return "Confidentiality Clause"
        else:
            return "Other Clause"
