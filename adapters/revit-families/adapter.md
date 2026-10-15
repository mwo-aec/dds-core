# Adapter: revit-families

version 0.1.0 · reference implementation: RaD add-in (Digital Reframe)

For the job **"Create a Revit family to our standards"**: capturing how an owner builds families, distilling their standards, and generating new families against them.

## Subject kinds

| Kind | Key | Notes |
|---|---|---|
| `family` | file name, e.g. `Door-Single-Flush.rfa` | or `<project>/<family name>` when harvested from a loaded project |
| `type` | `<family>/type/<type name>` | |
| `parameter` | `<family>/param/<parameter name>` | |
| `formula` | `<family>/param/<name>/formula` | when a parameter carries one |
| `reference-plane` | `<family>/refplane/<name or element id>` | |
| `nested-family` | `<host family>/nested/<nested family name>` | |
| `material` | `<family>/material/<name>` | |
| `subcategory` | `<family>/subcategory/<name>` | object styles |
| `type-catalogue` | `<family>.txt` | |

## Aspects

| Subject | Aspects (value type) |
|---|---|
| family | `name` (string), `category` (string), `template` (string), `hostVersion` (string), `isHosted` (bool), `hostType` (string), `typeCount` (int), `fileBytes` (int), `workPlaneBased` (bool), `alwaysVertical` (bool), `sharedFlag` (bool, when nested elsewhere) |
| type | `name` (string) |
| parameter | `name`, `kind` (`family`/`shared`/`builtin`), `isInstance` (bool), `dataType` (string), `group` (string), `hasFormula` (bool), `formula` (string), `valueByType` (object), `sharedGuid` (string), `isReporting` (bool), `isLocked` (bool) |
| reference-plane | `name`, `isReference` (string: strong/weak/not a reference …), `isDefinesOrigin` (bool) |
| nested-family | `name`, `category`, `isShared` (bool), `count` (int), `associatedParameters` (array), `driverParameter` (string, family-type selector), `sourcePath` (string, when known) |
| material | `name`, `class` (string), `isParameterDriven` (bool) |
| subcategory | `name`, `lineWeight` (int), `colour` (string) |

## Harvester

| Tool | RaD equivalent | Notes |
|---|---|---|
| `TOOL-RVT-FAM-HARVEST` | `harvest_families` | read-only; opens each `.rfa` in the background and closes without saving |
| `TOOL-RVT-FAM-SUMMARY` | `get_harvest_summary` | an analysis aid; its output is a summary, not observations |
| `TOOL-RVT-FAM-CONFORM` | `check_harvest_conformance` | runs checks over a capture: the Distil test |

**To align RaD:** have `harvest_families` write `captures/<run>/capture.json` and `observations.jsonl` per the core schemas, alongside its own fingerprints.

## Generators (Express)

`create_family`, `build_family_from_shape`, `add_family_parameter`, `add_family_type`, `add_reference_plane`, `add_dimension`, `lock_faces_to_planes`, `flex_family`, `save_family`, `load_family_into_project`. Generated families go to a scratch folder first; loading into a live project is a step with `finalYes: true`.

## Resources this domain needs

- `library`: approved families to nest (profiles, hardware, generic components), by category. **Needed for nested and shared families**: a generator pulls nested components from here rather than building them each time.
- `parameter-file`: shared parameter file(s).
- `template`: family templates (`.rft`) by category.
- `catalogue`: type catalogues.

## Analysis hints

Look for, and report with counts:
- naming styles and prefixes for families, types, parameters, reference planes, materials, subcategories;
- parameter type codes (`TXT_`, `URL_`, `FAM_` …) and their consistency with `dataType`;
- shared vs family parameters, and shared GUID conflicts (same name, different GUID);
- parameters every family carries (identity candidates);
- grouping (`group`) habits;
- nesting: shared vs non-shared, association to host parameters, family-type selectors;
- reference plane naming and strength;
- near-duplicate families or types (a question: duplicate or variant?);
- outliers in file size, type count.

**Questions this domain usually needs a person for:** why a family is nested shared; which of two naming styles is current; whether a library location is authoritative; when a family-type selector is preferred over separate families; what an empty parameter is for.
