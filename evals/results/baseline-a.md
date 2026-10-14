**P1**

Inspection logs record both routine decisions and operator repairs. Using the logs as a coherent training resource requires accounting for their different roles. We combine routine records, failed attempts, and operator repairs to improve inspection decisions with limited labeled data.

**P2**

Success required both a correct decision and escalation of uncertain cases before release. No real release occurred during evaluation, and evaluation labels were frozen before aggregate performance was calculated. The selected model achieved 68/80 successful decisions, compared with 60/80 for the fixed-rule baseline. The methods shared the model family and a nominal budget of 4,000 updates per fit, but selection used five separately fitted settings, compared with one baseline fit, and eligible training records differed. The fixed-rule baseline used a preset linear rule with source multipliers, while the learned family used a normalized nonlinear evidence-to-weight mapping. In an independent shifted-lighting study, the full model achieved 46/80 successful decisions, compared with 35/80 after removing repair records at the selected setting. The no-attempt variant removes all failed-attempt records while retaining routine and repair records and the operator-quality labels on those remaining records. Appendix B provides the clipping bounds, fallback logic, and fixed-rule coefficients.

修改理由：

1. P1 保留首尾两句，仅把中间句改为直接承接“不同记录的作用”。
2. 将“训练预算匹配”改为每次拟合预算相同，交代五次与一次拟合及训练记录差异；删除未被隔离实验支持的选择、特征和鲁棒性因果结论。
3. 保留成功标准与标签冻结事实，删去辩解及绝对安全保证，并明确评估中没有实际放行。
4. 将光照变化结果标为独立研究；明确 no-attempt 删除的是失败记录，剩余记录仍有操作员质量标签。
5. 正文简述两种权重规则的区别，附录指向具体实现参数。
