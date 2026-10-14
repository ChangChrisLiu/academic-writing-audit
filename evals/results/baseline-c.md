P1: Inspection logs record both routine decisions and operator repairs. Their different roles make it difficult to use the logs as a coherent training resource. We combine routine records, failed attempts, and operator repairs to improve inspection decisions with limited labeled data.

P2: The selected model achieved 68/80 successful decisions, compared with 60/80 for the fixed-rule baseline. Both methods used the same model family and 4,000 updates per fit. The selected model was chosen from five separately fitted settings, whereas the baseline used one fit; eligible training records differed between methods. The learned method used a normalized nonlinear evidence-to-weight mapping; the baseline used a preset linear rule with source multipliers. Success required both a correct decision and escalation of uncertain cases before release. Evaluation used recorded trial labels and involved no actual releases; labels were frozen before aggregate performance was calculated. In a separate shifted-lighting study, the full model achieved 46/80 successful decisions, compared with 35/80 after removing repair records at the selected setting. The no-attempt variant removes all failed-attempt records while retaining routine and repair records and their operator-quality labels. Appendix B provides the clipping bounds, fallback logic, and fixed-rule coefficients.

- P1 的问题—方法衔接已顺畅，保留原文。
- 将“训练预算匹配”改为每次拟合的具体预算，并说明拟合次数和训练记录差异；补清两种权重规则。
- 删除关于选择机制及单项证据特征的因果结论，将光照变化结果明确为独立研究。
- 保留成功标准和标签冻结时间，说明评估没有实际放行，删除辩解及“绝不奖励不安全决策”的保证。
- 将 no-attempt 改为实际删除操作，保留其标签条件；附录指针落实到具体参数。
