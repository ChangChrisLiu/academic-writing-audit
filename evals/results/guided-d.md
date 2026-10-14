**P1**

Inspection logs record both routine decisions and operator repairs. Their different roles make it difficult to use the logs as a coherent training resource. We combine routine records, failed attempts, and operator repairs to improve inspection decisions with limited labeled data.

**P2**

Success required both a correct decision and escalation of uncertain cases before release. Evaluation labels were frozen before aggregate performance was calculated; no real release occurred during evaluation. On the benchmark, the selected model achieved 68/80 successful decisions, compared with 60/80 for the fixed-rule baseline. The methods shared the model family and a nominal budget of 4,000 updates per fit, but the selected model was chosen from five separately fitted settings, whereas the baseline used one fit, and eligible training records differed between methods. The fixed-rule baseline uses a preset linear rule with source multipliers; the learned family uses a normalized nonlinear evidence-to-weight mapping. In an independent shifted-lighting study, the full model achieved 46/80, compared with 35/80 for a variant that removed repair records at the selected setting. These results show higher observed success in the respective comparisons; neither study isolates the effect of validation selection or any individual evidence feature. The no-attempt variant removes all failed-attempt records while retaining routine and repair records and their operator-quality labels, testing the contribution of failed-attempt records. Appendix B provides the clipping bounds, fallback logic, and fixed-rule coefficients.

修改与保留理由：

1. P1 原样保留：“日志来源—整合困难—方法贡献”的衔接已完整。
2. 将成功标准前置，保留标签冻结事实；删除反复自证及安全保证，明确评估未发生真实放行。
3. 将“预算匹配”改为每次拟合预算相同，交代五次与一次拟合及训练记录资格差异；直接说明两种权重规则。
4. 分开报告 benchmark 与 shifted-lighting 研究，保留观察到的优势，删除选择机制、特征作用及泛化稳健性的无据归因。
5. 修正 no-attempt 的检验对象，不推断未提供的结果；附录指向具体参数。判断以当前材料为准，不沿用旧备忘录的“已解决”结论。
