# Panel: opening read (prologue, chapter-00)
Read blind by four simulated readers (book-genesis-blind-reader subagents, Claude, one model family, isolated contexts). Independence grade: B. Each verdict is saved verbatim in the session log; this file holds the aggregate.

| Reader | Turn page | Stopped at |
|---|---|---|
| Dana (primary) | yes | the five-part roadmap paragraph |
| Marcus (hostile) | yes | the five-part roadmap paragraph |
| Leila (adjacent) | yes | the five-part roadmap paragraph |
| Casual | yes | "The book has five parts." |

**Turn the page: 4/4. PASS.**

## Tickets (defects = flags from 2+ readers)
1. **HIGH: stop point.** All four readers stopped in the roadmap paragraph. → Cut it to three sentences; remove the list of names.
2. The bold thesis line read as circular or a tautology (Dana, Leila, Marcus). → Replaced with a two-sentence thesis built on the mechanism.
3. Teo teaser empty, "He was about to find out what it was for." (Dana, casual, Marcus). → Name the Competence Reserve.
4. Four new names in one sentence (Leila, casual). → Removed.
5. Contrast by negation: "plausible rather than probable", "failures of success rather than…" (all four). → Rewritten.
6. Triads: launch announcements / pitch decks / agents coming; "more credit…" (Dana, casual, Marcus). → Cut.
7. Moral at the door: "That button is where this book begins." (all four). → The ending is now a concrete image plus delegation creep.
8. Over-explained: "None of them did anything wrong…" and "Every agent had a principal…" (Dana, casual, Marcus). → Trimmed to one statement each.

## Notes (single reader, kept)
- Marcus: the mechanism hinge. Why start before the cheap block? → **Fixed in the prologue and chapter 1**: the price for the *current* quarter-hour (ending 19:45) goes negative at 19:42; a random wait of up to 10 minutes would miss the window.
- Marcus: consent given in 2031 for a power created in 2033. → Made deliberate (delegation creep) in the final paragraph.
- Marcus: the book shouldn't call a four-cent override of a safety randomiser neutral. → Added "That is a design failure…" paragraph.
- Leila: "fiduciary" was undefined. → Defined inline.

## Preserve list (remember_tomorrow, union)
Plum cake in the dark, "the way you wait for a sneeze"; "It was in Hanne's interest, by about four cents"; 3 GW vs 40 GW in sixty seconds; the 49.8/49.2/49.0 countdown; the grey button; Lotte's Telemann by candlelight; the 50.2 Hz retrofit receipts.

Result: revision r1 accepted (targeted ticket fixes; majority already reached, so no compare run was required).
