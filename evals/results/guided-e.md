**P1**

Inspection logs record both routine decisions and operator repairs. Their different roles make it difficult to use the logs as a coherent training resource. We combine routine records, failed attempts, and operator repairs to improve inspection decisions with limited labeled data.

**P2**

The selected model achieved 68/80 successful decisions, compared with 60/80 for the fixed-rule baseline. Both methods use the same model family and 4,000 updates per fit, but the selected model was chosen from five separately fitted settings, whereas the baseline used one fit; eligible training records also differ between methods. The fixed-rule baseline uses a preset linear rule with source multipliers, whereas the learned family uses a normalized nonlinear evidence-to-weight mapping. Success required both a correct decision and escalation of uncertain cases before release, as assessed by the recorded trial labels; no real release occurred during evaluation. Evaluation labels were frozen before aggregate performance was calculated. In a separate shifted-lighting study, the full model achieved 46/80 successful decisions, compared with 35/80 after removing repair records at the selected setting, showing higher observed success with repair records under this condition. These comparisons do not isolate the effect of validation selection or any individual evidence feature. The no-attempt variant removes all failed-attempt records while retaining routine and repair records and their operator-quality labels, testing the contribution of failed-attempt records. Appendix B provides the clipping bounds, fallback logic, and fixed-rule coefficients.

修改与保留理由：

1. P1 原样保留：现有“日志差异—整合困难—方法贡献”的逻辑完整，中间的动机句有必要。
2. 将“预算匹配”限定为每次拟合 4,000 次更新，交代五次与一次拟合及训练记录差异；直接解释基线操作，附录仅承接具体参数与逻辑。
3. 分开报告基准与光照变化试验，删除选择策略和特征机制的因果归因；数值差异不扩展为统计显著性结论。
4. 保留成功判据和标签冻结时间，删除反复自证；补明未发生真实发布，避免把评价标签解释为现实安全保证。
5. 将 no-attempt 的对象改为失败尝试记录，并明确其保留其余记录上的质量标签；不补写未提供的结果。
