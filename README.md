# ci-dedupe-fixture-matrix

Synthetic measurement fixture for cidedupe live savings runs. Contains no
production code — a tiny deterministic pytest suite (two suites, no flakes,
no network, no clock dependence) exercised by a 3×2 CI matrix
(python-version × suite).

The workflow wires the cidedupe decide/record steps exactly like
`aditi17goel/ci-dedupe`'s own `ci` workflow (shell-detected secret gate,
verdict-gated test steps), except the action itself is checked out from the
private `ci-dedupe` repo at a pinned SHA: GitHub only runs actions from the
same repository or a public one. Every cidedupe step is inert until the
`CIDEDUPE_API_URL` and `CIDEDUPE_CHECKOUT_TOKEN` secrets exist.
