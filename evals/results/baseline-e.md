**P1**

Inspection logs record both routine decisions and operator repairs. We combine routine records, failed attempts, and operator repairs to improve inspection decisions with limited labeled data.

**P2**

The selected model achieved 68/80 successful decisions, compared with 60/80 for the fixed-rule baseline. The methods shared a model family and a budget of 4,000 updates per fit. Model selection used five separately fitted settings, whereas the baseline used one fit; eligible training records also differed between methods. The fixed-rule baseline used a preset linear rule with source multipliers, whereas the learned family used a normalized nonlinear evidence-to-weight mapping. Success required both a correct decision and escalation of uncertain cases before release. These criteria were assessed using trial labels frozen before aggregate performance was calculated; no real release occurred during evaluation. In an independent shifted-lighting study, the full model achieved 46/80 successful decisions, compared with 35/80 for a variant that removed repair records at the selected setting. The no-attempt variant removes all failed-attempt records while retaining routine and repair records and their operator-quality labels. Clipping bounds, fallback logic, and fixed-rule coefficients are provided in Appendix B.

修改理由：

1. 保留 P1 已顺畅的日志介绍与研究目标，删除笼统的困难陈述，使两句直接衔接。
2. 将“matched training budgets”改为准确的每次拟合预算，交代五次与一次拟合、训练记录差异，并明确两种权重规则。
3. 删除选择机制、单个证据特征及鲁棒性的因果断言；独立呈现光照变化实验，仅报告所给结果。
4. 保留成功判据与标签冻结事实，删去自证清白和绝对安全保证，并说明评价中没有实际放行。
5. 将 no-attempt 的描述改为实际删除和保留的内容，不推断未提供的结果；附录指针落实到具体参数与逻辑。
