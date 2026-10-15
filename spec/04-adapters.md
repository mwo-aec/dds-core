# 04 — Adapters

version 0.1.0

The core is domain-free. An **adapter** makes it work for one domain. Each adapter lives in `adapters/<id>/` and defines:

| Part | What it defines |
|---|---|
| **Subject kinds** | The things observations and checks are about (`family`, `type`, `parameter`, `view`, `sheet` …), with how their `key` is formed |
| **Aspects** | The dotted facts read about each subject kind (`name`, `category`, `parameter.group` …), with value types |
| **Harvesters** | Deterministic tools that read artefacts into observations, registered as `TOOL-` with `phase: capture`, `readOnly: true`, `deterministic: true` |
| **Check operations** | How each check `kind` is evaluated for this domain, and any `custom` operations |
| **Generators** (optional) | Tools that produce artefacts in the Express phase, and the approval they need |
| **Resources** | The kinds of library or reference the domain needs (family libraries, parameter files, templates) |
| **Analysis hints** | Patterns worth looking for in this domain, and the questions they usually lead to |

An adapter never changes the core schemas. Domain-specific fields go in `extensions.<adapter-id>`.

## Writing a new adapter

1. List the subject kinds and how each one's `key` is built.
2. List the aspects per kind, and their value types.
3. Build or wrap a harvester that writes observations for them. Prove it is deterministic: two runs over the same material give identical observations, apart from timestamps.
4. Map check kinds to evaluations over observations.
5. Write analysis hints from what an expert in the domain looks at first.
6. Add a small example pack under `examples/`.
