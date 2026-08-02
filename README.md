# Research Paper Reading Log Template

A clean, modular LaTeX template designed for organizing academic paper summaries, literature reviews, and research logs.

Instead of dumping raw notes into a single monolithic document, this template uses a **modular chapter/topic structure** with custom LaTeX environments that eliminate boilerplate typing, automate citations, and keep your Table of Contents cleanly organized.

---

## Features

- **Zero-Boilerplate Paper Headers:** The `paperbox` environment automatically formats metadata, generates dividers, and registers paper titles directly into your Table of Contents.
- **Modular Structure:** Group papers by research theme (`topics/01_foundations/`, etc.) using `\input{}` to keep compilation fast and navigation seamless.
- **Custom Callout Boxes:** Use `\begin{insightbox}` to highlight core equations, clever algorithmic tricks, or key architecture diagrams.
- **Section Shortcuts:** Fast macros (`\loggap`, `\logmethod`, `\logresults`, `\loglimitations`, `\logtakeaways`) format consistent section headings without retyping formatting code.
- **BibTeX & Hyperref Integrated:** Alphanumeric citation labels (`[Doe26]`) with clickable colored links.

---

## Quickstart Guide

### Option 1: Use with Overleaf
1. Download this repository as a `.zip` file (or click **Use this template** to create your own repo).
2. Go to [Overleaf](https://www.overleaf.com/) and select **New Project** → **Upload Project**.
3. Upload the `.zip` file and recompile `main.tex`.

### Option 2: Use Locally (VS Code, TeXStudio, Neovim)
1. Click the green **Use this template** button at the top right of this repository to generate your own repo.
2. Clone your new repository:
   ```bash
   git clone https://github.com/BoonHow97/research-reading-log-template
   ```
3. Compile `main.tex` using `latexmk` or your preferred LaTeX build engine (ensure BibTeX/Biber is enabled).

---

## Repository Structure

```text
research-reading-log-template/
├── paperlog.sty                  # Core styling, tcolorbox setups, and shortcut macros
├── main.tex                      # Master dashboard, TOC, and \input{} calls
├── references.bib                # Master BibTeX bibliography file
├── figures/                      # Store architecture diagrams and plots here
└── topics/                       # Modular paper folders grouped by research theme
    ├── 01_foundations/
    │   └── example_paper.tex     # Example paper note
    ├── 02_primitives/
    │   └── example_paper.tex
    ├── 03_architectures/
    │   └── example_paper.tex
    └── 04_evaluation/
    │   └── example_paper.tex
```

---

## Anatomy of a Paper Note

When adding a new paper note to a topic folder, use this standard structure:

```latex
% Usage: \begin{paperbox}{Title}{Authors}{Venue & Year}{BibTeX Key}
\begin{paperbox}
  {Paper Title Goes Here}
  {Author, A., Author, B., et al.}
  {Conference / Journal 2026}
  {citationKey2026}
  Your dense, one-sentence takeaway summarizing the paper's primary contribution goes here.
\end{paperbox}

\loggap
\begin{itemize}
  \item \textbf{The Problem:} What gap or failure in prior work motivated this paper?
  \item \textbf{Why prior work fails:} Specifically why existing baselines fall short.
\end{itemize}

\logmethod
\begin{itemize}
  \item \textbf{The Clever Trick:} The core algorithmic shift, architectural change, or mathematical formulation.
\end{itemize}

\begin{insightbox}[Core Mechanism / Key Insight]
  Use this box to highlight a standout equation, loss function, or architecture diagram.
\end{insightbox}

\logresults
\begin{itemize}
  \item \textbf{Key Findings:} Standout empirical benchmarks, theoretical guarantees, or latency/accuracy improvements.
\end{itemize}

\loglimitations
\begin{itemize}
  \item \textbf{Stated limits:} Explicit limitations acknowledged by the authors.
  \item \textbf{My critique:} Unrealistic assumptions, edge cases, or computational overhead.
\end{itemize}

\logtakeaways
\begin{itemize}
  \item \textbf{Relevance:} How this connects to your current research or literature review.
  \item \textbf{Action Items:} Specific baselines to compare against or experiments to try.
\end{itemize}
```

---

## Adding a New Paper to Your Log

1. Create a new `.tex` file inside the relevant topic folder (e.g., `topics/02_primitives/smith_2026.tex`).
2. Paste the paper note structure above and fill in your notes.
3. Add the BibTeX citation to `references.bib`.
4. Open `main.tex` and include your new file under the corresponding chapter:
   ```latex
   \chapter{Core Primitives \& Protocols}
   \input{topics/02_primitives/smith_2026}
   ```
5. Recompile your document!

---

## License

This template is open-source and available under the [MIT License](LICENSE). Feel free to fork, customize, and share!