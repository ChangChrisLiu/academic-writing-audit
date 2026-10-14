**P1**

Inspection logs record routine decisions, failed attempts, and operator repairs. We combine these records to improve inspection decisions with limited labeled data.

**P2**

On the benchmark, the selected model achieved 68/80 successful decisions, compared with 60/80 for the fixed-rule baseline. The methods share a model family and a nominal budget of 4,000 updates per fit, but the selected model was chosen from five separately fitted settings, whereas the baseline used one fit; eligible training records also differed. The fixed-rule baseline uses a preset linear rule with source multipliers, while the learned family uses a normalized nonlinear evidence-to-weight mapping. Success required both a correct decision and escalation of uncertain cases before release. Labels were frozen before aggregate performance was calculated; these labels describe the evaluation endpoint, and no real release occurred during evaluation. In a separate shifted-lighting study, the full model achieved 46/80 successful decisions, compared with 35/80 after removing repair records at the selected setting. The no-attempt variant removes all failed-attempt records while retaining routine and repair records and their operator-quality labels. Appendix B provides clipping bounds, fallback logic, and fixed-rule coefficients.

- P1 保留研究目的，合并重复列举，删去笼统的困难表述。
- 将“训练预算匹配”改为具体的单次预算、拟合次数与记录差异，并明确两种权重规则。
- 删除无法支持的选择机制、特征重要性和鲁棒性因果结论；将光照偏移结果作为独立研究报告。
- 保留标签冻结与成功判据，删去辩解和安全保证；明确评估中没有真实放行。
- 将 no-attempt 描述为移除失败记录，避免误称为质量标签消融；附录指向具体参数与逻辑。
