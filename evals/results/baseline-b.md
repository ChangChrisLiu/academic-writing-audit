P1: Inspection logs record both routine decisions and operator repairs. Their different roles make it difficult to use the logs as a coherent training resource. We combine routine records, failed attempts, and operator repairs to improve inspection decisions with limited labeled data.

P2: The selected model achieved 68/80 successful decisions, compared with 60/80 for the fixed-rule baseline. The baseline uses a preset linear rule with source multipliers, whereas the learned family uses a normalized nonlinear evidence-to-weight mapping. Both methods share the model family and a nominal budget of 4,000 updates per fit; the selected model was chosen from five separately fitted settings, whereas the baseline used one fit. Eligible training records differed between methods. Labels were frozen before aggregate performance was calculated. Success required both a correct decision and escalation of uncertain cases before release; no real release occurred during evaluation. In a separate shifted-lighting study, the full model achieved 46/80, compared with 35/80 when repair records were removed at the selected setting. The no-attempt variant removes all failed-attempt records while retaining routine and repair records and their operator-quality labels. Appendix B provides clipping bounds, fallback logic, and fixed-rule coefficients.

- P1 的“记录角色不同—整合用于训练”逻辑已顺，保留原文。
- 补明两种权重规则，并将 Appendix B 指向具体实现参数。
- 将“匹配训练预算”改为每次拟合预算一致，说明五次与一次拟合及训练记录差异。
- 分开报告两组试验，删除选择和特征有效性的因果断言；纠正 no-attempt 消融对象为失败记录，而非质量标签。
- 保留标签冻结及成功标准，删除自辩和安全保证，并注明评估未发生真实放行。
