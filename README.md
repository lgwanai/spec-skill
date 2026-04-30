<div align="center">

# spec-skill (规范驱动开发技能)

**轻量级、强大的元提示与上下文工程系统，专为 Trae、Cursor、Cline 等 AI 编程助手打造。**

**解决"上下文腐化"问题 —— 避免大模型在填满上下文窗口后出现的质量断崖式下降。**

</div>

---

## 🌟 项目最大亮点：无缝互通的 Claude Code `gsd` 技能复刻版

本技能是知名开源项目 [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done/) (GSD) 技能的深度复刻版，并且对国内开发者更加友好。

它不仅可直接用于 **Trae、Cursor、Cline** 等主流基于 Agent 的 AI 编程环境，最强大的地方在于：**本技能生成的所有规划内容（`.planning` 目录下的各类文档）与官方 Claude Code 中的 `gsd` 技能完全互通互融！**

这意味着你可以无缝地在不同 AI 工具之间切换接力开发（例如在 Trae 中做规划，在 Cursor 中执行），而不会丢失任何核心上下文。

---

## 💡 为什么需要这个技能？

"随性编程 (Vibecoding)" 名声不佳。你描述需求，AI 生成代码，随着项目变大，你得到的往往是前后不一致、难以维护的"垃圾代码"。`spec-skill` 就是为了解决这个问题而生的。

- **拒绝企业级过家家**：没有敏捷冲刺、故事点、无休止的会议和 Jira 工作流。我们只为 Solo 开发者和小型团队提供真正有效、极简的构建系统。
- **解决上下文腐化 (Context Rot)**：将复杂的项目拆解为多个独立的、原子化的任务（Phase/Plan），每次执行时都保持清爽的上下文，确保 AI 始终保持最高水平的输出。
- **强制的 Ask-Plan-Execute (询问-计划-执行) 机制**：有效避免大语言模型在需求模糊时盲目"幻觉"输出代码，保证你想要的东西被正确地构建。

---

## 🆕 v1.1 更新

基于原版 GSD v1.37+ 的最新更新同步升级：

- **增强的 PLAN 模板**：新增 `user_setup`（外部服务配置声明）、`execution_context`（执行期上下文引用）、更结构化的 `must_haves`（含 `min_lines`、`exports`、`contains`、`via`、`pattern` 等字段），支持 TDD 计划类型和基于 Wave 的并行执行
- **扩展的配置系统**：新增 `mode`（交互/自动模式）、`granularity`（粗/标准/细粒度）、`parallelization`（并行控制）、`gates`（8 个确认检查点）、`safety`、`hooks` 等配置项
- **规范制品注册表**：`templates/README.md` 作为权威的 `.planning/` 制品索引，定义了所有规范文档及其用途
- **5 个新模板**：`VALIDATION.md`（验证架构）、`UAT.md`（用户验收测试）、`discovery.md`（阶段发现与决策）、`continue-here.md`（会话暂停/恢复）、`verification-report.md`（验证报告）
- **存量项目分析模板**：`templates/codebase/` 目录含 7 个模板（结构、架构、技术栈、约定、集成、测试、关注点），支持 brownfield 项目分析
- **工作流文档**：`workflows/` 目录含 4 个详细工作流（`execute-plan.md`、`verify-work.md`、`transition.md`、`health.md`），规范每个阶段的操作步骤

---

## 🧠 核心机制：上下文工程 (Context Engineering)

强大的 AI 必须要有正确的上下文。大多数人没有做到这一点，而 `spec-skill` 会为你自动管理。

### 核心规划文档

| 文件 | 模板 | 作用 |
|------|------|------|
| `PROJECT.md` | `templates/PROJECT.md` | 项目愿景、需求、约束、关键决策 |
| `REQUIREMENTS.md` | `templates/REQUIREMENTS.md` | 需求边界与可追溯性，明确 v1/v2/超纲 |
| `ROADMAP.md` | `templates/ROADMAP.md` | 阶段分解路线图，含成功标准和进度跟踪 |
| `STATE.md` | `templates/STATE.md` | 跨会话记忆：当前位置、决策、阻碍、性能指标 |
| `config.json` | `templates/config.json` | 工作流配置：并行化、质量门、安全设置 |

### 阶段执行文档

| 文件 | 模板 | 作用 |
|------|------|------|
| `PLAN.md` | `templates/PLAN.md` | 可执行的原子任务计划，XML 结构，含 must_haves 和目标逆向验证 |
| `SUMMARY.md` | `templates/SUMMARY.md` | 阶段完成后总结，含依赖图和上下文组装元数据 |
| `CONTEXT.md` | `templates/discovery.md` | 阶段讨论中捕获的设计决策、用户偏好和假设 |
| `VALIDATION.md` | `templates/VALIDATION.md` | 验证架构，含 Given/When/Then 测试场景 |
| `UAT.md` | `templates/UAT.md` | 用户验收测试结果与问题跟踪 |
| `VERIFICATION.md` | `templates/verification-report.md` | 执行后验证报告，对照 must_haves 逐项检查 |

### 会话连续性

| 文件 | 作用 |
|------|------|
| `.continue-here.md` | 会话暂停时的交接文件，记录当前位置和待办事项 |
| `.planning/todos/` | 跨会话捕获的想法和待办任务 |

---

## 🎯 使用场景

- **从零启动复杂项目**：将模糊的初始想法转化为结构清晰、分步骤可执行的开发计划，确保项目地基稳固。
- **大型需求迭代与重构**：在现有项目中添加复杂功能时，通过多轮讨论澄清边界，确保前后逻辑一致且不破坏现有架构。
- **控制 AI "幻觉" 与代码发散**：通过强制的"用户确认"机制（Ask-Wait-Ask），防止 AI 偏离开发目标。
- **规范化团队 AI 开发流**：统一 AI 辅助开发的过程产出，方便团队其他成员或未来的 AI Agent 接手。
- **存量项目分析**：通过 `templates/codebase/` 模板系统分析现有代码库的架构、技术栈、约定和技术债务。
- **跨会话协作**：通过 `continue-here.md` 和 `STATE.md` 实现会话暂停和恢复，支持多人接力开发。
- **外部服务集成**：通过 PLAN 模板的 `user_setup` 字段声明需要人工配置的外部服务（API 密钥、数据库、第三方服务）。

---

## 🚀 核心工作流 (How It Works)

在对话框中唤醒并使用该技能（例如发送："@spec-skill 帮我开发一个基于 React 的待办事项工具"）。工作流将严格遵循以下步骤：

1. **项目初始化**：AI 会帮你梳理并创建项目的基础上下文文件（`.planning/PROJECT.md`、`config.json` 等）。
2. **需求讨论（阻塞阶段）**：AI 会围绕需求进行多轮提问，直到彻底理清功能边界和技术栈约束。参考 `references/questioning.md`。
3. **路线图规划**：AI 会将需求拆解为多个开发阶段（Phase），并生成 `.planning/ROADMAP.md`。
4. **阶段计划与评审（阻塞阶段）**：在进入每一个 Phase 之前，AI 会进行调研并生成详细的原子化任务计划 `PLAN.md`。**此时 AI 会停止操作并等待你的确认**。
5. **代码执行**：你确认后，AI 按照 `workflows/execute-plan.md` 执行：逐任务实现→逐任务验证→逐任务原子提交。
6. **验证与总结**：每阶段完成后，AI 按照 `workflows/verify-work.md` 对照 must_haves 进行目标逆向验证，失败则生成修复计划，成功则按照 `workflows/transition.md` 更新项目状态并准备下一阶段。
7. **健康检查**：随时可通过 `workflows/health.md` 检查 `.planning/` 目录完整性，支持自动修复。

---

## 📂 项目结构

```
spec-skill/
├── SKILL.md                  # 技能定义与核心工作流
├── README.md                 # 本文件
├── templates/                # 文档模板（20 个文件）
│   ├── README.md             # 规范制品注册表（权威索引）
│   ├── PROJECT.md            # 项目愿景模板
│   ├── ROADMAP.md            # 路线图模板
│   ├── STATE.md              # 状态记忆模板
│   ├── REQUIREMENTS.md       # 需求模板
│   ├── PLAN.md               # 阶段计划模板 ★ v1.1 增强
│   ├── SUMMARY.md            # 总结模板
│   ├── config.json           # 配置模板 ★ v1.1 扩展
│   ├── discovery.md          # 阶段发现模板 ★ 新增
│   ├── VALIDATION.md         # 验证架构模板 ★ 新增
│   ├── UAT.md                # 用户验收模板 ★ 新增
│   ├── continue-here.md      # 会话交接模板 ★ 新增
│   ├── verification-report.md # 验证报告模板 ★ 新增
│   └── codebase/             # 存量项目分析模板 ★ 新增
│       ├── structure.md      # 目录结构与模块
│       ├── architecture.md   # 架构模式与组件关系
│       ├── stack.md          # 技术栈与版本
│       ├── conventions.md    # 编码约定与命名规范
│       ├── integrations.md   # 外部服务与依赖
│       ├── testing.md        # 测试方法与覆盖率
│       └── concerns.md       # 已知问题与技术债务
├── workflows/                # 工作流文档 ★ 新增
│   ├── execute-plan.md       # 计划执行（含原子提交、错误恢复）
│   ├── verify-work.md        # 阶段验证（含 must_haves 检查、UAT）
│   ├── transition.md         # 阶段转换（含上下文更新、下一阶段准备）
│   └── health.md             # 健康检查（含完整性验证、自动修复）
├── references/               # 参考文档
│   ├── questioning.md        # 提问策略与心理模型
│   └── verification-patterns.md # 验证模式与工作流
└── scripts/                  # 自动化脚本
    ├── init_project.py       # 项目初始化
    ├── validate_project.py   # 项目校验
    └── package_skill.py      # 技能打包分发
```

---

## 📦 安装方式

要将本技能安装并导入到你的 AI Agent 或 IDE（如 Trae, Cursor, Cline）中，请按照以下步骤操作：

1. **克隆仓库**：
   ```bash
   git clone git@github.com:lgwanai/spec-skill.git
   cd spec-skill
   ```

2. **打包技能**：
   运行项目内置的打包脚本，将技能文件打包为可分发的 `.zip` 压缩包：
   ```bash
   python scripts/package_skill.py
   ```
   *打包完成后，你会在项目根目录的 `dist/` 文件夹下看到生成的 `spec-skill_*.zip` 文件。*

3. **导入到 IDE/Agent**：
   - 打开 Trae IDE 或兼容的 Agent 平台的"技能（Skills）"管理面板。
   - 选择"导入技能"，并上传刚才生成的 `.zip` 包。
   - 导入成功后，技能名称将显示为 `spec-skill`。

---

## ❓ 常见问题 (FAQ)

**Q1: 为什么 AI 一直在问我问题，而不是直接给我写代码？**
**A1:** 这是本技能的核心机制。为了保证开发质量，`spec-skill` 强制在编写代码前必须理清所有模糊的需求细节。如果你只需要一段简单的代码片段，建议直接向基础 AI 助手提问，无需调用本技能。可通过 `config.json` 中的 `gates` 配置调整确认检查点的严格程度。

**Q2: 每次生成 Plan 之后 AI 就停下来了，这是 Bug 吗？**
**A2:** 不是 Bug。在生成阶段计划（PLAN）后，系统被强制设定为"等待用户确认"。你必须显式地告诉 AI "计划没问题，请继续"或者"修改一下第三步"，它才会进行实质性的代码编写和文件修改。如果希望减少确认步骤，可将 `config.json` 中的 `mode` 设为 `"yolo"`（不推荐）。

**Q3: 项目中的 `scripts`、`templates`、`workflows` 目录分别有什么用？**
**A3:**
- `scripts/` — 可执行的自动化工具：项目初始化、结构校验、技能打包。
- `templates/` — 所有规范文档的模板文件，含 `codebase/` 子目录用于存量项目分析。参见 `templates/README.md` 获取完整制品索引。
- `workflows/` — 各阶段的操作步骤文档（执行计划、验证工作、阶段转换、健康检查），AI 在执行对应阶段时会加载这些文档。
- `references/` — 参考文档，用于指导 AI 的提问策略和验证方法。

**Q4: 如何暂停工作并在之后恢复？**
**A4:** 告诉 AI "暂停工作"，它会自动创建 `.continue-here.md` 文件，记录当前的阶段、计划、任务位置。下次恢复时，AI 会读取该文件并从中断处继续。

**Q5: 如何在现有项目中使用 spec-skill？**
**A5:** 使用 `templates/codebase/` 下的模板，让 AI 先分析你的代码库（结构、架构、技术栈、约定），然后将分析结果作为项目上下文载入，再开始规划新的开发工作。
