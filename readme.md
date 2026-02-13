# Weici-New (维克多新高中英语词汇)

[![Build Status](https://github.com/RainPPR/weici-new/actions/workflows/build.yml/badge.svg)](https://github.com/RainPPR/weici-new/actions/workflows/build.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📖 项目简介 (Introduction)

**Weici-New** 是一个专注于高中英语词汇学习的静态网页项目。它的核心目标是提供一个**极致兼容**、**零依赖**、**纯净无干扰**的电子词典体验。

本项目特别针对老旧教学设备（如运行 Windows 7 及 IE8 的计算机）进行了优化，确保在受限的硬件和网络环境下也能流畅访问。

## ✨ 主要特性 (Features)

* **🏛️ 极致兼容 (IE8+)**:
  * 严格遵循 HTML4/5 混合语法规范。
  * 使用 CSS 2.1 进行样式布局，避免 Flexbox/Grid 等现代特性。
  * 内置 `html5shiv`，确保 IE8 正确渲染语义化标签。
  * **纯静态**: 无需数据库运行时，所有内容预生成为 HTML。
* **⚡ 零依赖前端**:
  * **无 JavaScript 框架**（Vue/React/jQuery 等），无客户端脚本执行。
  * 极速加载，即便在低性能设备上也极其流畅。
* **📚 内容丰富**:
  * 完整包含音标（英/美）、词性、词频等级。
  * 提供详细的释义、例句（支持关键词高亮）、固定搭配及用法点拨。
  * **关联词跳转**: 支持同根词/派生词跳转及反向链接索引。
* **主体化**:
  * 支持自动生成索引页。
  * 支持从 SQLite 数据库批量生成。

## 🛠️ 技术架构 (Tech Stack)

* **构建环境**: [Node.js](https://nodejs.org/) (推荐 v14+)
* **数据源**: SQLite3 (`weici_ext.db`)
* **模板引擎**: [Nunjucks](https://mozilla.github.io/nunjucks/)
* **构建工具**: 原生 JS 脚本 (`build.js`) + `fs-extra`
* **HTML 压缩**: `html-minifier` (配置为 XHTML 严格模式)
* **样式**: Vanilla CSS (IE8 Compatible)

## 🚀 快速开始 (Getting Started)

### 前置要求

* 已安装 Node.js 环境。
* **注意**: 你需要自行获取 `weici_ext.db` 数据库文件。

### 安装与构建

1. 克隆仓库

   ```bash
   git clone https://github.com/RainPPR/weici-new.git
   cd weici-new
   ```

2. 获取数据文件
   将 `weici_ext.db` 放置在项目根目录下。

3. 安装依赖

   ```bash
   npm install
   ```

4. 执行构建

   ```bash
   npm run build
   ```

5. 预览：构建完成后，所有静态文件将输出到 `docs/` 目录。

   * 双击打开 `docs/index.html` 即可浏览完整词汇索引。
   * 或使用简单的 HTTP 服务器预览：`npx serve docs`。

## ⚖️ 数据来源与免责声明 (Data Source & Disclaimer)

**数据来源**: 本项目使用的核心数据库文件 `weici_ext.db` 来源于 GitHub 仓库 [1299172402/weici](https://github.com/1299172402/weici)，该仓库已于 2023年1月29日 归档 (Archived)，现为只读状态。该仓库**未包含任何开源许可证 (LICENSE)**。

**使用说明**:

* 本项目**仅作为数据的展示容器**，不对 `weici_ext.db` 中的单词数据所有权进行任何声张。
* **我不负责数据的修改、完善或校对**。本项目仅原样读取并展示数据库中的内容，不提供针对单词拼写、释义修正的数据维护服务。
* 如果您发现数据内容有误，请知悉这源于原始数据库，而非构建脚本的问题。

**关于版权**:生成的词汇内容（释义、例句等）版权归原作者（维克多英语/维词）所有。本项目仅供技术研究与个人非商业学习使用。

## 🤝 贡献指南 (Contributing)

* **纠错 (Corrections)**: 欢迎提交 Issue 或 PR 指出**代码层面**的错误（如构建脚本 Bug、样式兼容性问题）。但请注意，如前所述，我不处理单词数据的纠错。
* **功能请求 (Feature Requests)**: 由于精力有限且项目目标明确（简单、静态），我**暂不接受**新的功能性添加或复杂的架构更改请求。

---

> 🤖 **生成声明**:  
> 本 README 文件由人工智能助手 **Antigravity (Google Deepmind)** 协助生成，并经由 **RainPPR** 人工验收。  
> 生成时间: 2026-02-13
