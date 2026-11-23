# 输入与数据边界

## 最小输入

接收一个JSON对象：
- `customer_id`：内部匿名键；一次仅一位客户。
- `data_origin`：`synthetic`、`approved_customer_export`。
- `as_of`：YYYY-MM-DD。
- `period`：start、end、label、complete_calendar_year。
- `scope`：本次可见资产和数据范围。
- `authorization`：purpose、customer_content_allowed；只声明当前材料既有授权，不替用户取得授权。
- `profile`：可选称呼，不存证件号、手机号或联系方式。
- `facts`：事实数组，每项有id、customer_id、kind、text、source、observed_at、confirmed、allowed_for_customer、confidence。
- `account`：可选简化人民币资产桥，见示例。省略表示未知；数值0只能表示已经核实的零。

建议facts.kind使用 `system`、`customer_confirmed` 或 `derived`。`derived`还应提供 `input_ids` 与 `formula`。不得用派生事实倒推出客户情绪或家庭角色。

## 年度与口径

以客户所在地日期确定“今年”。年度未完成或数据未对账时，用“截至……的阶段版”，禁用“全年结果已确定”。

简化资产桥为：期末 = 期初 + 流入 − 流出 + 投资损益。本例假定损益已经包含计入的费用，未另列分红、在途与转托管。本式不普遍替代真实对账；真实业务有额外项目时沿用可信源系统口径，不自行压平差异。

投资收益率只复述源系统给出的指标、算法、区间与数值。不得用(期末−期初)/期初代替有现金流账户的收益率。

四笔钱表示用途规划。基金类型、权益比例等表示资产特征。二者不可相互自动推定。没有保障数据不写“保障已足够”。

## 授权与逐客隔离

把内部语料、同事点评和客户账户分开。不将姓名与具体账户数据写入公开语料或技能源码。技能仓库仅保留公开来源的通用方法及标明虚构的样本。

批量处理中，每次模型请求只含目标客户必要资料，返回后核对customer_id与所有证据归属；跨客户、错误授权或对账冲突时隔离该任务。默认不接触真实客户数据库、不自动外发信件、不生成真实家庭画像。

提供客户纠错、删除个人叙事和不保存记忆的选择；具体保存、提醒和触达由真实产品能力承接，不能把示例按钮写成已经完成的服务。
