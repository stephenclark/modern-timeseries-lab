# Data

Large datasets are deliberately excluded from Git.

The repository should contain the instructions and metadata required to obtain
and reproduce data, rather than becoming a warehouse for source files.

## Directory convention

### `raw/`

Immutable data exactly as obtained from the source.

Do not manually edit files in this directory.

### `interim/`

Intermediate transformations that are useful during processing but are not
yet modelling-ready.

### `processed/`

Clean, validated datasets suitable for analysis or modelling.

### `sample/`

Small datasets and fixtures that are safe to commit to Git and useful for
examples and automated tests.

## Provenance requirements

Each external dataset should document, where applicable:

- dataset name;
- publisher;
- source URL or API endpoint;
- retrieval date;
- licence or reuse conditions;
- geographic coverage;
- temporal coverage;
- frequency;
- units;
- source-series identifiers;
- transformations applied;
- whether historical observations may be revised;
- checksum for downloaded source files where useful.

A suggested metadata record is:

```yaml
dataset: abs_labour_force
publisher: Australian Bureau of Statistics
source_url: null
retrieved_at: null
licence: null

coverage:
  geography: Australia
  start: null
  end: null
  frequency: monthly

provenance:
  source_file: null
  sha256: null
  revision_sensitive: true

transformations: []
Time-series warning

For forecasting, current historical data is not always equivalent to the data
available at a historical forecast date.

Economic and labour-market statistics may be revised after publication.

Later chapters will distinguish:

latest-vintage historical data;
real-time/vintage data;
historical covariates;
genuinely known-future covariates.

This distinction is essential for avoiding hindsight leakage.
