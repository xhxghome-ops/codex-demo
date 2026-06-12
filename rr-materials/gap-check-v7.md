# Gap-Check: v7 Manuscript vs. RR1 Decision Letter

**Manuscript:** ORSC-MS-2025-20442R1 — *Turning Errors into Productivity*
**Purpose:** Map every AE/reviewer demand to what v7 currently does, and flag what still needs work before resubmission.

---

## Bottom line

v7 is a *major* overhaul that substantively answers most of the review team's concerns: the
straw-man framing is gone, the front-end is now team-sourced with a pre-entry (Wave 0) measure,
the moderator is replaced, a new validated "action error" measure is introduced, and the
moderation is now tested in a single unified growth model with end-anchored time coding. The
remaining risks fall into three tiers:

1. **Critical cleanup (do first):** the manuscript still contains intact text from the *old*
   study/version that directly contradicts the new one. A reviewer who spots this loses trust
   instantly.
2. **Theoretical gaps the AE explicitly asked for** that v7 only partially covers (work-context
   boundary conditions; error-type/cost heterogeneity; rationale for the *specific* moderator).
3. **Promised-but-not-yet-delivered empirics** (full growth-model results in appendix; the
   intercept–slope correlation the AE asked for by name).

---

## Tier 1 — Critical cleanup (leftover old-version text)

These are not judgment calls; they are contradictions that must be removed before anyone reads it.

| Where | Problem | Fix |
|---|---|---|
| Methods, sample paragraph | **An entire old-study paragraph survives**: "invited all **569** newcomers… **463**… **391**… **310**… **258 matched pairs**… **global error attribution**… annual **merit pay**… 246 entries… each leader supervising only one newcomer." This describes the OLD infrastructure-firm study and contradicts the new **294 newcomer-team / pharmaceutical** study. | Delete the entire paragraph. It is the single most damaging leftover. |
| Section heading | Theory still titled **"The Moderating Role of Newcomer Error Attribution."** Construct is now **external locus of control**. | Rename heading; sweep body for "error attribution." |
| Hypothesis 2 | Worded "Team error **prevention** culture…" while the construct is "error **aversion** culture" everywhere else (31x aversion vs 1x prevention). | Standardize on one label throughout (recommend "aversion"). |
| Methods | Literal string **"!!! INVALID CITATION !!!"** in the sample paragraph. | Fix the citation. |
| Study 1 | **N inconsistency**: Overview says "**XXX** managers"; item-generation says "**118** managers… 182 retained from **100** respondents." | Reconcile the manager N and fill XXX. |
| Study 1 | Placeholders: **"DP, 1980"** (malformed cite), **"£XX.00"** payment. | Fill in. |
| Discussion / refs | Typos: "error **ccount**", "**Scanuraa**" (Scandura), "edditing". | Proofread pass. |
| Tables / Appendix | Table notes promise results "in Online Appendix Tables **XX–XXX**." | Populate with real table numbers + content (see Tier 3). |
| Whole doc | v7 is tracked-changes; the *accepted* text reads cleanly, but old abstract/title fragments live in deletions. | Accept-all into a clean file before final proofread. |

---

## Tier 2 — Addressed well (strengths to preserve)

| AE / Reviewer point | What v7 does |
|---|---|
| **Straw-man framing** (AE-1; R2-T1; R3-1) | Reframed: "entry is a learning process"; positions contribution as *what happens after* an error (diagnosis→regulation), building on—not overturning—the literature. New title. **Strong.** |
| **Self-report front-end / reverse causality** (AE-2; R1-1a,4a; R2-E1,E2) | Error culture now **coworker-rated at Wave 0 (pre-entry)**; action errors **mentor-rated**; performance **leader-rated** → 4-source separation. Centralized hiring gives genuine temporal precedence. **Strong design answer.** |
| **Level of analysis** (R1-1a) | Culture moved to **team level** with aggregation stats reported (rwg=.955, ICC1=.483, ICC2=.813). |
| **LGO/PGO confound** (AE-1; R1-1b) | Controls for **learning & performance goal orientation, proactivity, psychological safety**; shows culture predicts curvature net of these. **Strong.** |
| **Moderator replacement** (AE-3; R1-2; R3-2) | "Global error attribution" → **external locus of control** (Rotter tradition), framed via sensemaking. |
| **Single-model moderation test** (AE-4.3) | Now one **unified latent growth model** (intercept/linear/quadratic regressed on culture × LOC). **Directly answers the AE.** |
| **Intercept = end of onboarding** (AE-4.4) | Time coded **−3,−2,−1,0**; intercept = final-wave error level. **Directly answers the AE.** |
| **Non-linear trajectory** (R2-T4) | Curvature is now the *centerpiece* (accelerating decline; quadratic significant, cubic n.s.). **Strong.** |
| **Error construct conflation** (AE-5; R3-3.1; R2-5 tautology) | New **action-error** construct + Study 1 scale development; content-validated as distinct from performance/mastery/proficiency (csv). **Strong.** |
| **High alphas / weak CFA** (R3-3.2) | New measure; CFA now CFI=.953, RMSEA=.018. |
| **Moderated-mediation detail** (R3-3.3) | Bias-corrected bootstrap (20,000), conditional indirect effects, index of moderated mediation reported. |
| **Two-cultures interaction** (R1-1c) | Tested; n.s.; reported as additive in supplementary. |
| **Actor vs. observer mechanism** (R1-3) | NOW theorized (legibility/observer route as a *consequence* of the capacity account). NB your notes said "not sure what reviewer means" — it IS addressed in text; the **response memo must say so**. |

---

## Tier 3 — Gaps still needing real work

1. **Work-context boundary conditions (AE-5, first half; R2-T2; R3-4.4).**
   The AE explicitly asked: *in what contexts is trial-and-error advisable vs. not?* (the surgeon /
   high-reliability example). v7's only boundary condition is an **individual** moderator (LOC).
   The **contextual** boundary lives only in Limitations/Future Directions.
   → Recommend a short **scope-conditions** passage in theory: tie the standardized R&D/production
   sample to *where* the accelerating-spiral logic should hold, and name contexts where error
   prevention dominates. This is a named AE demand, not optional.

2. **Error-type / cost heterogeneity (R2-T3; R3-3.1).**
   Action error is treated as unidimensional/gestalt. R2 stressed costly vs. trivial errors; R3
   stressed that some "errors" are socialization/sensemaking, not competence failures.
   → The new action-error definition narrows this usefully, but **acknowledge cost heterogeneity**
   explicitly and state it as a scope condition.

3. **Why *this* moderator, over self-efficacy / risk aversion (R3-2).**
   v7 now *controls* for self-efficacy and risk propensity (good — shows incremental validity),
   and frames LOC via sensemaking. But the theory section should state **why LOC is theoretically
   primary**, not merely another trait. Also: H5 (aversion × LOC) is **n.s.**, explained only
   *post hoc*. R3 will probe this — strengthen the a priori rationale or soften H5.

4. **Full growth-model results the AE demanded by name (AE-4.1, 4.2).**
   AE asked for fixed effects, random effects, the **full variance–covariance matrix**, and
   specifically **the intercept–slope correlation**. Table notes *promise* these in
   "Appendix Tables XX–XXX" but the appendix is a placeholder.
   → Actually populate; surface the intercept–slope correlation where a reader will find it.

5. **Revisit the "prevention isn't harmful" point (R2-T1 tail; R2-Other-2).**
   In the OLD data, prevention had no effect; in the NEW data, **aversion culture significantly
   dampens acceleration**. That's a cleaner story — but the Discussion/Practical Implications
   should explicitly reconcile this with R2's earlier observation and update the managerial advice.

6. **Chinese single-firm context (R3-4.4).**
   Acknowledged in Limitations, but R3 wanted a sentence on how national/organizational culture
   could shape interpretation of error climates. Cheap to add; closes the loop.

---

## Suggested sequencing

1. Tier 1 cleanup (half a day; mechanical but mandatory).
2. Tier 3 #1 and #3 (the two named theoretical asks) — highest leverage for round 2.
3. Tier 3 #4 (populate appendix tables).
4. Then draft the point-by-point response memo, citing page numbers into the cleaned manuscript.
