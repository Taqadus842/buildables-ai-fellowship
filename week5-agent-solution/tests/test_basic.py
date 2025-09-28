import os
from src.tools.custom_tool import ClauseClassifierTool

def test_classifier():
    tool = ClauseClassifierTool()
    assert tool._run("Payment must be made in 30 days") == "Payment Clause"
    assert tool._run("Either party may terminate") == "Termination Clause"
    assert tool._run("Vendor not liable for damages") == "Liability Clause"
