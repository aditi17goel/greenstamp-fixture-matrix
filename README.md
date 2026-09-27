# greenstamp-fixture-matrix

Synthetic measurement fixture for greenstamp live savings runs. Contains no
production code — a tiny deterministic pytest suite (two suites, no flakes,
no network, no clock dependence) exercised by a 3×2 CI matrix
(python-version × suite).

The workflow wires the greenstamp decide/record steps exactly like
`aditi17goel/greenstamp`'s own `ci` workflow (shell-detected secret gate,
verdict-gated test steps), except the action itself is checked out from the
private `greenstamp` repo at a pinned SHA: GitHub only runs actions from the
same repository or a public one. Every greenstamp step is inert until the
`GREENSTAMP_API_URL` and `GREENSTAMP_CHECKOUT_TOKEN` secrets exist.
