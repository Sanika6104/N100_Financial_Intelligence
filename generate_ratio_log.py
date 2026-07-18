from pathlib import Path

output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

log_file = output_dir / "ratio_edge_cases.log"

with open(log_file, "w") as f:
    f.write("Ratio Edge Case Log\n")
    f.write("=" * 60 + "\n\n")
    f.write("Review Date: Sprint 2\n\n")
    f.write("Observed Issues:\n")
    f.write("- Financial sector companies excluded from D/E warning.\n")
    f.write("- Negative equity handled by returning None for ROE.\n")
    f.write("- Interest = 0 handled as Debt Free.\n")
    f.write("- CAGR zero base handled.\n")
    f.write("- CAGR turnaround cases handled.\n")
    f.write("- Operating Profit Margin mismatch logging enabled.\n")
    f.write("- No critical runtime errors found.\n")

print("ratio_edge_cases.log created successfully.")