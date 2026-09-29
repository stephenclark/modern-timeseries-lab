# Chapter 00: Engineering a Reproducible Forecasting Project

Before fitting a forecasting model, this chapter establishes the engineering
rules used throughout the portfolio.

The goal is not infrastructure for infrastructure's sake. Time-series analysis
is particularly vulnerable to subtle errors such as temporal leakage, revised
historical observations, non-reproducible notebooks, and inconsistent
train/test boundaries.

Engineering discipline is therefore part of the statistical method.

## Learning objectives

By the end of this chapter you should be able to:

- reproduce the Python environment from `uv.lock`;
- explain what belongs in Git and what should stay outside it;
- run identical quality checks locally and in CI;
- capture enough environment information to reproduce an experiment;
- distinguish raw, interim and modelling-ready data;
- explain several common forms of time-series leakage;
- use branches and pull requests as part of an analytical workflow.

## 1. Reproduce the environment

The project uses `uv`.

From a clean checkout:

```bash
uv sync --locked
```

Run commands inside the managed environment:

```bash
uv run python
uv run pytest
uv run ruff check .
```

The lock file is committed because dependency versions are part of the
research record.

## 2. Git stores instructions, not warehouses

Commit:

- source code;
- notebooks that are useful analytical artefacts;
- small test datasets;
- configuration;
- documentation;
- data provenance;
- compact tables and selected figures where appropriate.

Do not commit:

- large raw datasets that can be recreated;
- model caches;
- checkpoints;
- `.venv`;
- working DuckDB databases;
- credentials;
- large generated output directories.

A good repository should make it possible for another analyst to recreate the
analysis without requiring Git to contain every byte used during development.

## 3. Raw data is immutable

Files in:

```text
data/raw/
```

represent source evidence.

Transformations create new products in:

```text
data/interim/
data/processed/
```

rather than silently modifying source files.

This becomes particularly important with official statistics because historical
values can be revised after publication.

## 4. Notebooks explain; packages implement

Jupyter notebooks are encouraged in this portfolio because exploration,
visualisation and narrative are important parts of the learning process.

Reusable logic belongs in:

```text
src/tsportfolio/
```

A useful rule:

> If the same function is needed by a second notebook, it probably belongs in
> `src/`.

## 5. Every forecast has an information boundary

Before training a model, explicitly identify:

- forecast origin;
- forecast horizon;
- target observations available at the origin;
- historical-only covariates;
- genuinely known-future covariates;
- publication delays;
- revised data.

These distinctions become formal modelling contracts later in the course.

## 6. Local quality gate

Before committing:

```bash
make check
```

or equivalently:

```bash
uv run ruff check .
uv run pytest
```

## 7. Continuous integration

GitHub Actions runs the same checks for pushes and pull requests.

The CI workflow deliberately stays small.

It does not download large foundation models or execute GPU training jobs.
Later chapters will test forecasting interfaces using tiny fixtures and leave
expensive experiments as explicit research runs.

## 8. Inspect the environment

Run:

```bash
make environment
```

This reports:

- Python version;
- operating system;
- architecture;
- Git branch;
- commit;
- working-tree state;
- key package versions.

Later we will extend this into experiment metadata including model version,
dataset version, forecast horizon, context length, covariates, random seed,
runtime and hardware.

## Exercise 00.1: rebuild the laboratory

Delete the local environment:

```bash
rm -rf .venv
```

Then recreate it:

```bash
uv sync --locked
make check
```

The project should recover without manually reinstalling packages.

## Exercise 00.2: identify leakage

Write down three examples of information leakage in an economic forecasting
problem.

For each example explain:

1. what information leaked;
2. why it would not have been available at the historical forecast origin;
3. why the resulting validation score would be misleading.

Consider:

- subsequently revised official statistics;
- centred rolling-window features;
- explanatory variables published after the target month;
- accidentally fitting scalers against the entire dataset.

## Exercise 00.3: inspect Git history

Run:

```bash
git status
git branch
git log --oneline --decorate --graph --all
```

Identify:

- the current branch;
- its upstream remote;
- where it diverged from `main`;
- which project files are intentionally ignored.

## Definition of done

Chapter 00 is complete when:

- `uv sync --locked` succeeds;
- `uv run ruff check .` succeeds;
- `uv run pytest` succeeds;
- `make environment` succeeds;
- GitHub Actions passes;
- the pull request is reviewed and merged into `main`.

Once that is true, the forecasting work can begin on a reproducible foundation.