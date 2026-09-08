# Data

Shared data lives here so each agent does not create its own duplicate folder.

**The industry and the final dataset have not been chosen yet.** Anything in this
directory today is synthetic development data — final dataset TBD.

## Folders

| Folder | Contents |
| --- | --- |
| `raw/` | Reserved for the final source / reference data once the domain is selected. Currently empty. |
| `test_cases/` | Synthetic RFQs, development cases, and later evaluation cases. |

`processed/` does not exist yet. Add it (and it is already gitignored) once
something actually generates derived data.

## Three stages

**Stage 1 — graph smoke test (where we are now).**
No real dataset needed. `test_cases/sample_rfq.json` is one deliberately
domain-neutral RFQ, just enough to prove that
`START -> intake -> pricing -> quotation -> END` runs and that state flows
correctly. Run it with `python -m pricing_agent`.

**Stage 2 — tiny synthetic development data (once the domain is chosen).**
Enough for each agent owner to develop against before the real dataset exists.
Deliberately *not* written yet: concrete customers, products, or pricing rules
cannot be invented without implicitly choosing the industry, and whatever we
invent now would anchor that decision and then be thrown away.

What we *can* agree on now is the list of **cases** we want, because these
describe branch and failure modes rather than any particular industry. Fill
these in once the domain lands:

- [ ] complete, normal request
- [ ] missing quantity
- [ ] unknown customer
- [ ] unknown product / service
- [ ] rush request
- [ ] large quantity / discount threshold

Six to ten cases is plenty. The point is that a human can read every case and
understand it at a glance.

**Stage 3 — final shared dataset.**
Chosen by the team, used for integration and evaluation.

## Conventions

- **One JSON file per test case**, not a single big array file. Three people
  appending to one array conflict on every pull request; separate files never do.
- Keep files small and human-readable. If a case needs explaining, add a comment
  field inside it.
- Reference data files (customers, products, pricing rules) can be added here
  when the owning agent actually needs them.
