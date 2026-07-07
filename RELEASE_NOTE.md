# Release Notes

## v1.1.0 (Sync from get-shit-done v1.37+)

**日期**: 2026-07-07

### 🔄 get-shit-done 内容同步

本版本从源项目 `get-shit-done` 的 skill 子目录迁移真实的内容改进，分 6 个阶段完成同步，全部内容已去 GSD 化，保持 spec-skill 自包含与 `/spec-` 命令体系。

**去耦原则**：所有迁移内容统一执行 `/gsd-`→`/spec-`、移除子代理引用、移除外部路径（`@~/.claude/get-shit-done`）、移除 gsd-sdk / state-lock / surface / worktree 等机制依赖，使 spec-skill 完全自包含。

#### 阶段 1：引用修复
- 修复 4 处残留的 `/gsd:` 命令引用与 `@~/.claude/get-shit-done` 外部路径引用（涉及 `STATE.md`、`PROJECT.md`、`references/verification-patterns.md`）。

#### 阶段 2：references 引入（8 个新增）
- `checkpoints.md`（精简重写版，解外部引用）
- `common-bug-patterns.md`
- `debugger-philosophy.md`
- `thinking-models-debug.md`
- `domain-probes.md`
- `ai-evals.md`
- `tdd.md`
- `user-story-template.md`

以上文件均已去 GSD 化。

#### 阶段 3：templates 更新
- **修改 4 个**：
  - `verification-report.md`：三态验证 + Anti-Patterns Found
  - `UAT.md`：五态模型 + 严重度推断
  - `STATE.md`：Deferred Items
  - `config.json`：新增 `ship` / `git.create_tag`
- **新增 6 个**：`SECURITY.md`、`DEBUG.md`、`retrospective.md`、`user-profile.md`、`user-setup.md`、`research.md`

#### 阶段 4：workflows 去耦合并（4 个）
- `execute-plan.md`：`atomic_close_out_invariant` 等 10 项改进
- `health.md`：`error_codes` 表 + W009 / W019
- `transition.md`：verification debt + `partial_completion` + `cleanup_handoff`
- `verify-work.md`：UAT philosophy + 严重度推断 + cold-start smoke test 第 7 步大幅增强

#### 阶段 5：commands 同步（4 个）
- `quick.md`：`--discuss` / `--full` / `--validate` / `--research` + `list` / `status` / `resume` 子命令 + slug 卫生化
- `execute.md`：`--wave` / `--gaps-only` / `--interactive` + flag handling rule
- `health.md`：`--context`
- `plan.md`：`--prd` / `--mvp` / `--gaps`

#### 阶段 6：SKILL.md 更新
- 补充 `TRIGGER when:` 行
- 更新命令表 flags
- 资源清单登记新增 6 模板 + 8 references

#### 源项目状态说明
源项目 `get-shit-done` 已被标记弃用（compromised，引导到 fork）。本次仅迁移其 skill 子目录中真实的内容改进，未采纳其弃用元数据。

---

## v1.0.0 (Initial Release)

**日期**: 2026-03-29

### 🎉 新特性 (Features)
- **核心工作流同步**: 与知名开源项目 `gsd-build/get-shit-done` 的最新改进保持同步，包含最新的模板设计、`must_haves` 验证机制和优化的 Ask-Plan-Execute 工作流 (`5c6da10`)。
- **无缝互通**: 生成的规划内容（`.planning` 目录下的各类文档）与官方 Claude Code 中的 `gsd` 技能完全互通互融。
- **上下文工程**: 提供结构化的 `PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md`, `STATE.md`, `PLAN.md` 和 `SUMMARY.md` 模板，解决大模型长上下文腐化问题。

### 📖 文档 (Documentation)
- **README 优化**: 引入原 `gsd` 项目的核心特性介绍，详细阐述了“上下文工程”机制、使用场景和核心工作流 (`653a5ab`)。
- **配置与指引更新**: 更新了项目的仓库地址为 `spec-skill` (`2d85620`)。

### 🛠 优化与重构 (Chores & Refactoring)
- **目录结构扁平化**: 优化了项目目录结构，将其扁平化到项目根目录，更便于管理和打包发布 (`687c3c2`)。
- **构建配置清理**: 将 `dist` 目录移出版本控制，并更新 `.gitignore` 保持代码仓库整洁 (`451c705`)。
