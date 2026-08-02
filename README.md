# Research Paper Reading Log Template

A clean, modular LaTeX template designed for organizing academic paper summaries, literature reviews, and research logs.

Instead of dumping raw notes into a single monolithic document, this template uses a **modular chapter/topic structure** with custom LaTeX environments that eliminate boilerplate typing, automate citations, and keep your Table of Contents cleanly organized.

---

## ✨ Features

- **Zero-Boilerplate Paper Headers:** The `paperbox` environment automatically formats metadata, generates dividers, and registers paper titles directly into your Table of Contents.
- **Modular Structure:** Group papers by research theme (`topics/01_foundations/`, etc.) using `\input{}` to keep compilation fast and navigation seamless.
- **Custom Callout Boxes:** Use `\begin{insightbox}` to highlight core equations, clever algorithmic tricks, or key architecture diagrams.
- **Section Shortcuts:** Fast macros (`\loggap`, `\logmethod`, `\logresults`, `\loglimitations`, `\logtakeaways`) format consistent section headings without retyping formatting code.
- **BibTeX & Hyperref Integrated:** Alphanumeric citation labels (`[Doe26]`) with clickable colored links.

---

## �� Quickstart Guide

### Option 1: Use with Overleaf
1. Download this repository as a `.zip` file (or click **Use this template** to create your own repo).
2. Go to [Overleaf](https://www.overleaf.com/) and select **New Project** → **Upload Project**.
3. Upload the `.zip` file and recompile `main.tex`.

### Option 2: Use Locally (VS Code, TeXStudio, Neovim)
1. Click the green **Use this template** button at the top right of this repository to generate your own repo.
2. Clone your new repository:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git](https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git)