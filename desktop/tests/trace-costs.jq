# Sum the time of each kind of Playwright action in a trace (jq --slurp).
# A kind is the method and its selector with quoted text replaced by "…".
# Trace format: "before" and "after" events joined by callId
# (https://github.com/microsoft/playwright/blob/main/packages/trace/src/trace.ts).
(map(select(.type == "before"))
  | map({key: .callId, value: {
      kind: (.class + "." + .method + " "
        + (.params.selector // "" | tostring | gsub("\"[^\"]*\""; "\"…\""))),
      start: .startTime}})
  | from_entries) as $started
| map(select(.type == "after" and $started[.callId] != null))
| map($started[.callId] + {ms: (.endTime - $started[.callId].start)})
| group_by(.kind)
| map({kind: .[0].kind, calls: length, seconds: (map(.ms) | add / 1000)})
| sort_by(-.seconds)
| .[]
| "\(.seconds * 10 | round / 10) s\t× \(.calls)\t\(.kind)"
