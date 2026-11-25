# #28: the certification run holds eight runners instead of sixteen

`results/certify-workflow-bounded-runners.patch`, clean under `git apply --check` against main.

The change is one strategy key:

    strategy:
      fail-fast: false
      max-parallel: 8
      matrix: ${{ fromJSON(needs.plan.outputs.matrix) }}

- **Bounded runners.** At most eight of the run's jobs exist at once, so half the account's runners stay
  free for the other repositories' CI while certification runs — which is the issue's acceptance.
- **The same shards, budgets and work.** The plan job still produces sixteen shards of 16, each with
  `timeout-minutes: 350` and `certify --minutes 330 --shard i/16 --phase fields`. Nothing about which
  cards a shard certifies, or how long a shard may compute, changes; the second eight start as the
  first eight finish.
- **The cost is wall time, and it stays inside a day.** The last full run (42844490886's sibling
  certification run) took about 5 h 45 min with all sixteen in parallel; two waves of the same shard
  budget is about 11 h 30 min, so a run dispatched at 03:17 still ends before the next day's cron. With
  `max-parallel: 4` it would not: four waves are about 23 h, which collides with the next scheduled run
  and the `certify` concurrency group. Eight is the largest bound that keeps a run inside a day and the
  smallest that halves the runners.

Not checked here: a hosted runner. The evidence is the next scheduled run's job list — eight `certify`
jobs in progress at a time, and the other repositories' runs starting while it holds them.
