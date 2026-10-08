Handling: Unclassified — public

# Contribution Scope

This project maps **who supplies what, how dependent a supply chain is, and
where the chokepoints are**. It does not document how components are designed,
built, or perform. This policy sits alongside HANDLING.md and
DATA-CONTRIBUTIONS.md, and applies to every contribution, including those from
domain experts in propulsion, avionics, materials, and other hardware fields.

## In scope

- Schemas, validators, tooling, visualization, and documentation.
- Supply-chain mapping information drawn from public sources: suppliers and
  their public product categories, materials and process categories,
  public capacity indicators, workforce and training programmes, and
  dependency relationships between them.
- Use-case modules built on the above (for example, a turbo-pump supply chain
  map expressed as categories and relationships).
- Synthetic datasets, evaluation tasks, and benchmark harness code.

## Out of scope — do not submit

Technical data about how a component or system is designed, made, tested, or
performs, including drawings and CAD, dimensions and tolerances, process
parameters, simulation inputs or outputs, test results, and performance curves.

This applies **even if you believe the information is publicly available**.
Public availability does not settle whether information is controlled, and the
project does not need it. If in doubt, leave it out and ask a maintainer.

Also out of scope: anything marked above "Unclassified — public", non-public
third-party contract text or figures, personal information, and credentials
(see HANDLING.md).

## How domain experts contribute

Domain experts add the most value by reviewing the **taxonomy and
relationships**, not specifications. Examples:

- checking that part, material, and process categories match how the industry
  describes them;
- identifying single-source or low-redundancy categories by name;
- reviewing schema fidelity and gaps in a use-case module;
- reviewing a methodology note for analytical errors.

## Data

Data contributions follow DATA-CONTRIBUTIONS.md. Until a revised rule is
published there, only synthetic data, or public data licensed for redistribution
and model training, is accepted.

## Clearance before contributing

Before contributing, confirm that your employer, university or research
institution, and any funder of your work permits it. The CLA and CCLA ask you to
represent this.

## Handling a mistake

If you submit out-of-scope material by accident, do not open a public issue
describing it. Contact the maintainers listed in MAINTAINERS.md. Maintainers
may reject a contribution, and where necessary remove content from repository
history. Maintainers may also decline or limit participation where required by
law.
