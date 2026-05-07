---
name: dupont-analysis
display_name: DuPont Analysis
class: lens
underlying_class: native
domain: finance
source: DuPont de Nemours and Company, 1920s; formalized by F. Donaldson Brown
best_for:
  - Isolating drivers of return on equity
  - Diagnosing profitability vs. efficiency vs. leverage issues
  - Comparing peer companies on individual performance levers
one_liner: "Decompose ROE into asset efficiency, profitability, and financial leverage to find the real performance drivers."
---

# DuPont Analysis

## Overview
DuPont Analysis decomposes Return on Equity (ROE) into three measurable components: Net Profit Margin (profitability), Asset Turnover (efficiency), and Equity Multiplier (leverage). Instead of viewing ROE as a single opaque metric, the framework reveals which operational or financial lever drives performance — or explains deterioration. Practitioners use it to identify whether a company's ROE strength comes from pricing power, asset management, or financial structure, and to spot hidden vulnerabilities (e.g., high ROE from unsustainable leverage masking poor profitability).

## Analytical Procedure

### Phase 1 — Gather Financial Data

1. **Collect the company's latest audited financials.** You need:
   - Net Income (bottom line of income statement)
   - Total Revenue (top line)
   - Total Assets (balance sheet)
   - Total Shareholders' Equity (balance sheet)
   - Compare period should match (quarterly, annual, or trailing twelve months)

2. **If comparing peers, collect the same four line items for each peer.** Ensure all use the same accounting standard (GAAP, IFRS) and measure period.

3. **Flag any one-time items in net income.** Restate net income to exclude extraordinary gains/losses (asset sales, litigation settlements, restructuring charges) so the decomposition reflects ongoing operations, not noise.

### Phase 2 — Calculate the Three Components

4. **Calculate Net Profit Margin:**
   - Formula: Net Income ÷ Revenue
   - What it shows: How much profit is generated per dollar of sales
   - Interpretation: Compressed margins signal pricing pressure, rising COGS, or operating expense bloat

5. **Calculate Asset Turnover:**
   - Formula: Revenue ÷ Total Assets
   - What it shows: How much revenue is generated per dollar of assets deployed
   - Interpretation: Low turnover signals either underutilized assets or capital-intensive business; high turnover suggests efficient asset use (but verify it's not from asset sales)

6. **Calculate Equity Multiplier:**
   - Formula: Total Assets ÷ Shareholders' Equity
   - What it shows: How many dollars of assets are financed per dollar of equity (i.e., the leverage ratio)
   - Interpretation: Higher multiplier = more debt relative to equity; low multiplier = conservative capital structure

7. **Calculate ROE (verification):**
   - Formula: Net Profit Margin × Asset Turnover × Equity Multiplier
   - Confirm this equals Net Income ÷ Shareholders' Equity
   - If it doesn't, recheck calculations

### Phase 3 — Trend and Compare

8. **Plot each component as a time series for the company.** Use at least three years of data. Look for:
   - Margin expanding or compressing?
   - Asset turnover improving or degrading?
   - Leverage increasing or deleveraging?

9. **Benchmark each component against peer medians.** Create a side-by-side table:
   - Does the company's margin exceed peers? By how much?
   - Does its asset turnover exceed peers?
   - Does it use more or less leverage than peers?

10. **Identify which components drive the ROE gap.** If the company's ROE exceeds peers, which of the three components explains it? If it lags, which component is the bottleneck?

### Phase 4 — Diagnosis and Stress

11. **For the lagging component (if any), drill into sub-drivers:**
   - If margin is low: Compare COGS as % of revenue, operating expenses as % of revenue, and tax rate to peers. Which sub-item is the problem?
   - If asset turnover is low: Calculate turnover for key asset categories (receivables, inventory, fixed assets). Which asset class is underutilized?
   - If leverage is low: Note debt-to-equity ratio and cost of debt. Is the company under-leveraged relative to its risk profile?

12. **Test sensitivity.** For the company's current components, calculate what ROE would be if one component matched the peer median while others stayed the same. Example: "If our margin matched the peer median, ROE would rise from 12% to 15%."

## Evaluation Criteria

| Check | Pass |
|---|---|
| All four financial line items (NI, Revenue, Assets, Equity) are from the same period | Y/N |
| One-time items have been identified and excluded from net income | Y/N |
| All three components are calculated and verified to produce the reported ROE | Y/N |
| At least three years of trend data are plotted | Y/N |
| Peer comparison includes at least two direct competitors | Y/N |
| Sub-drivers of the lagging component (if any) have been identified | Y/N |
| Sensitivity analysis shows the impact of closing one component gap | Y/N |

## Red Flags

- Equity Multiplier is extremely high (>5x) but ROE is not exceptionally high. The company is taking on leverage without commensurate returns — this is hidden risk.
- Net Profit Margin is negative or near zero, but high Asset Turnover and Equity Multiplier produce a positive ROE. This masks a structurally unprofitable business; the numbers are an artifact of capital velocity, not sustainable earnings.
- Asset Turnover is unusually high compared to historical trend, but asset base has shrunk dramatically. The company may have sold core assets; this is a one-time effect, not an operational improvement.
- All three components improved year-over-year, but ROE is flat. Recheck for changes in accounting policies, currency effects, or non-controlling interests that offset the operational gains.
- Peer comparison uses companies in different industries or with different business models. Retail and capital equipment manufacturing have fundamentally different asset turnover expectations; the comparison is invalid.
- Net income has been restated to exclude losses, but the original reported figure includes them. The analysis is now disconnected from what investors actually saw.

## Output Format

```
## DuPont Analysis Report

**Company:** <name>
**Period:** <quarter/year>
**Reference date(s):** <start and end of period>

### Financial Inputs
| Item | Value | Notes |
|---|---|---|
| Net Income | $<> | (one-time items excluded) |
| Revenue | $<> | |
| Total Assets | $<> | |
| Shareholders' Equity | $<> | |

### Component Calculations
| Component | Formula | Value | Interpretation |
|---|---|---|---|
| Net Profit Margin | NI / Revenue | ___% | <one sentence on profitability) |
| Asset Turnover | Revenue / Assets | <_._>x | <one sentence on efficiency> |
| Equity Multiplier | Assets / Equity | <_._>x | <one sentence on leverage> |
| **ROE (product)** | **Margin × Turnover × Multiplier** | **___%** | **Verification against reported** |

### Trend (3-Year)
| Year | Margin | Turnover | Multiplier | ROE |
|---|---|---|---|---|
| <YYYY> | ___% | <_>x | <_>x | ___% |

### Peer Comparison
| Metric | Company | Peer Median | Peer Range | Position |
|---|---|---|---|---|
| Margin | ___% | ___% | ___–___% | Above / At / Below |
| Turnover | <_>x | <_>x | <_>–<_>x | Above / At / Below |
| Multiplier | <_>x | <_>x | <_>–<_>x | Above / At / Below |
| ROE | ___% | ___% | ___–___% | Above / At / Below |

### Component Diagnosis
**Most impactful driver of ROE:** <Margin / Turnover / Leverage>

**Lagging component (if any):** <which one; why>

**Sub-driver breakdown (if needed):**
| Sub-item | Company | Peer Median | Gap |
|---|---|---|---|

### Sensitivity Analysis
*If [lagging component] matched peer median, ROE would change from __% to __%, a gain of __%.*

### Key Findings
1. <Finding 1>
2. <Finding 2>
3. <Finding 3>

### Confidence
<high | medium | low> — <Justification based on data quality, peer comparability, and trend stability>
```
