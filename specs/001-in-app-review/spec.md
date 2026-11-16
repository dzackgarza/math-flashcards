# Feature Specification: In-App Review

**Feature Directory**: `specs/001-in-app-review`

**Created**: 2026-11-16

**Status**: Draft

**Input**: Review the cards with spaced repetition inside the desktop app, reusing Anki's
own scheduling code, so that studying needs no package export and no import into Anki.

## Clarifications

### Session 2026-11-16

These answers are defaults taken from repository evidence. The user has not confirmed
them. A different answer changes only the requirement named in each line.

- Q: What happens to the review history of a card that is removed from the decks? → A:
  The history is kept and the card is not offered. A card that returns with the same ID
  gets its schedule back (FR-016). Reason: deck files change under external editors, and
  a deleted history cannot be recovered.
- Q: Where does the review history live? → A: In the app's data directory for the user,
  one store for each workspace path (FR-018). Reason: this machine's convention keeps
  application data in XDG directories and out of repositories.
- Q: Is existing review history from Anki imported? → A: No. Every card starts as new
  (FR-026). Reason: no Anki profile exists at `~/.local/share/Anki2` or
  `~/.var/app/net.ankiweb.Anki`, the two locations inspected.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Review due cards in the app (Priority: P1)

The user opens the app, starts a review, and studies. The app shows the front of a card.
The user recalls the answer and reveals the back. The user grades the recall as Again,
Hard, Good, or Easy; each grade shows the interval it leads to. The app schedules the card
and shows the next one. When no card remains for today, the app says so. Every card in the
saved decks is available for review with no export, import, or other preparation by the
user.

**Why this priority**: This is the feature. Without it, study still needs a package
export and a second program.

**Independent Test**: Start the app on a workspace that was never reviewed, start a
review, grade several cards, close the app, and open it again. The graded cards keep
their schedule and the remaining cards are still offered.

**Acceptance Scenarios**:

1. **Given** a workspace with saved decks and no review history, **When** the user starts
   a review of the workspace, **Then** the app shows the front of a new card and hides its
   back.
2. **Given** a card front on screen, **When** the user reveals the answer, **Then** the
   app shows the back and four grades, each with the interval that grade produces.
3. **Given** a revealed card, **When** the user selects a grade, **Then** the app records
   the grade, schedules the card, and shows the next card.
4. **Given** a card that contains equations with the collection's macros and a TikZ-cd
   diagram, **When** the card appears in review, **Then** it renders as it does in the
   editor and in the exported package.
5. **Given** a review in progress, **When** the app closes for any reason, **Then** every
   grade already selected is kept and the next launch continues from that state.
6. **Given** no card is due and the daily limit of new cards is reached, **When** the
   user starts a review, **Then** the app states that the review for today is complete.
7. **Given** a card that the user graded Again, **When** its short relearning delay
   passes during the same session, **Then** the app offers the card again.

---

### User Story 2 - Deck changes reach review and keep history (Priority: P1)

The user keeps editing the Markdown decks. A saved change reaches review with no action by
the user. A card keeps its review history when its text changes, when it moves to another
deck, when its deck is renamed or merged, and when its position changes. A new card
appears as new.

**Why this priority**: The cards change continuously. If an edit reset or duplicated a
card's history, the schedule would be wrong after the first editing session and the
feature could not be trusted.

**Independent Test**: Grade a card until it has an interval of several days. Edit its
text, move it to another deck, and rename that deck. The card keeps its interval and due
date, shows the new text, and belongs to the renamed deck.

**Acceptance Scenarios**:

1. **Given** a card with review history, **When** the user edits its front or back and the
   deck is saved, **Then** the next review of the card shows the new text and its schedule
   and history are unchanged.
2. **Given** a card with review history, **When** the card moves to another deck, by the
   app or by an external edit of the files, **Then** it is reviewed as part of the new
   deck with its history unchanged.
3. **Given** a deck with reviewed cards, **When** the deck is renamed or merged into
   another deck, **Then** every card keeps its history.
4. **Given** a saved deck, **When** the user adds a card, **Then** the card becomes
   available as a new card without an export.
5. **Given** a card with review history, **When** the card is removed from its deck,
   **Then** the app stops offering the card and keeps its history; **When** a card with
   the same ID returns to any deck, **Then** it has its earlier schedule.
6. **Given** another program changes a deck file, **When** the app detects the change,
   **Then** review reflects the changed deck.

---

### User Story 3 - See what is due and choose what to review (Priority: P2)

The deck tree shows, for each deck and each folder, how many cards are new, in learning,
and due today. The user starts a review of one deck, one folder, or the whole workspace.

**Why this priority**: The user decides what to study from the counts. Review of the
whole workspace alone already gives value, so this follows the first two stories.

**Independent Test**: Grade cards in two decks under one folder. The counts of each deck
and of the folder change to match, and a review started on one deck offers only cards of
that deck.

**Acceptance Scenarios**:

1. **Given** a workspace with review history, **When** the deck tree appears, **Then**
   each deck and folder shows its new, learning, and due counts for today.
2. **Given** the counts on screen, **When** the user grades a card, **Then** the counts of
   its deck and of every folder above it update.
3. **Given** a deck with due cards, **When** the user starts a review from that deck,
   **Then** only cards of that deck appear.
4. **Given** a folder, **When** the user starts a review from it, **Then** cards of every
   deck below it appear.

---

### User Story 4 - Correct a grade or a card during review (Priority: P2)

The user selects the wrong grade and undoes it. The user sees an error in a card during
review, opens that card in the editor, corrects it, and returns to the review.

**Why this priority**: Wrong grades and card errors occur in every session. Without
correction the user must leave the review or accept a wrong schedule.

**Independent Test**: Grade a card, undo, and confirm that the card returns with its
earlier schedule. Open the card in the editor from the review, change its text, return,
and confirm the review shows the new text.

**Acceptance Scenarios**:

1. **Given** the user graded a card, **When** the user selects Undo, **Then** the grade is
   removed from the history and the card returns with its earlier schedule.
2. **Given** a card in review, **When** the user selects Edit, **Then** the editor opens
   that card in its deck.
3. **Given** the user edited the card from the review, **When** the user returns to the
   review, **Then** the same card appears with the corrected text.
4. **Given** a deck change reached review after the last grade, **When** the user looks
   for Undo, **Then** Undo is unavailable until the next grade, and the app shows why.

---

### User Story 5 - Control the daily load (Priority: P3)

The user sets how many new cards the app introduces each day, the maximum number of
reviews each day, and the target recall probability that the scheduler aims for.

**Why this priority**: The defaults give a usable review. The collection has several
thousand unreviewed cards, so the user needs control of the load soon after first use.

**Independent Test**: Set the new-card limit to a small number, start a review, and
confirm that the app introduces exactly that many new cards today.

**Acceptance Scenarios**:

1. **Given** a new-card limit of N, **When** the user reviews, **Then** the app introduces
   at most N new cards on that day.
2. **Given** the user raises the target recall probability, **When** cards are graded
   afterward, **Then** their intervals are shorter than under the earlier target.
3. **Given** changed settings, **When** the app restarts, **Then** the settings remain.

---

### Edge Cases

- A deck has unsaved edits when a review starts: the app saves first, as it does before
  other deck operations, then reviews the saved content.
- A deck has invalid card structure and cannot be saved: review continues with the last
  saved content, and the existing Problems list shows the deck.
- An equation in a card does not render: the review shows the same TeX error the editor
  shows.
- A card's ID changes in the source: the app treats this as the removal of one card and
  the addition of a new card.
- Two cards in different decks have the same ID: the app reports a problem that names
  both cards and does not attach either card to the other's history.
- The card on screen is removed or edited by another program during the review: the app
  shows the current state of the card, or the next card when it no longer exists.
- A second running copy of the app opens a workspace whose review history is in use: the
  second copy states that review of this workspace is in use by another window. Its
  editor keeps working, and no grade is lost or recorded twice.
- A workspace moves to a new path: the workspace at the new path starts with no history,
  and the history of the earlier path stays on disk.
- The date changes during a session: cards due on the new day become available by the
  scheduler's day boundary.
- The first use on a large workspace: the app shows progress while it prepares the cards,
  and the editor remains usable.
- The review store is damaged or missing: the app reports the error and does not create
  an empty history over an existing one.
- The app is updated while a window is open: both the earlier and the later release can
  read and write the review history, or the earlier release reports that it must restart.

## Requirements *(mandatory)*

### Functional Requirements

**Review session**

- **FR-001**: Users MUST be able to start a review of a deck, a folder, or the whole
  workspace from inside the app.
- **FR-002**: The system MUST show the front of a card with the back hidden, and reveal
  the back on the user's command.
- **FR-003**: The system MUST offer the grades Again, Hard, Good, and Easy for a revealed
  card, and MUST show for each grade the interval it produces.
- **FR-004**: The system MUST record each grade, with its time and the time the user took,
  at the moment the user selects it.
- **FR-005**: The system MUST decide card order, intervals, learning steps, daily limits,
  and the day boundary with Anki's own scheduling code. The system MUST NOT contain a
  second implementation of these rules.
- **FR-006**: The system MUST state when the review for today is complete and MUST show
  how many cards the user graded.
- **FR-007**: Users MUST be able to operate a review with the keyboard alone: reveal the
  answer and select each grade.
- **FR-008**: The system MUST show the remaining counts of new, learning, and due cards
  during a review.

**Card content**

- **FR-009**: The system MUST render a card in review through the same rendering pipeline
  as the editor and the exported package, including macros, diagrams, and images.
- **FR-010**: The system MUST make every card of every saved deck available for review
  with no export or import step.
- **FR-011**: The system MUST apply a saved change of a deck to review with no action by
  the user.
- **FR-012**: The Markdown decks MUST remain the only authored source of card content. The
  review store MUST be reproducible from the decks, except for the review history.

**Identity and history**

- **FR-013**: The system MUST identify a card in review by its card ID. Text, tags, deck,
  and position MUST NOT take part in the identity.
- **FR-014**: The system MUST keep a card's schedule and history when its text, tags,
  deck, or position changes and when its deck is renamed or merged.
- **FR-015**: The system MUST require card IDs to be unique in the workspace and MUST
  report each duplicate as a problem that names the cards.
- **FR-016**: When a card is removed from the decks, the system MUST stop offering it and
  MUST keep its schedule and history. When a card with the same ID returns, the system
  MUST restore that schedule.
- **FR-017**: The system MUST keep the review history across restarts, crashes, and
  updates of the app.
- **FR-018**: The system MUST keep the review history in the app's data directory for the
  user, with one store for each workspace path, and MUST make dated backups of it. The
  store MUST NOT be a cache: the action that rebuilds cached data MUST NOT touch it.
- **FR-019**: The system MUST NOT replace an existing review history with an empty one. A
  history that cannot be read MUST produce an error that names the file.

**Overview and control**

- **FR-020**: The system MUST show the new, learning, and due counts for each deck and
  folder, and MUST update them after each grade.
- **FR-021**: Users MUST be able to undo the last grade while that grade is the most
  recent change to the review history in the running app. When Undo is unavailable, the
  system MUST show that it is.
- **FR-022**: Users MUST be able to open the card on screen in the editor and return to
  the review.
- **FR-023**: Users MUST be able to set the daily new-card limit, the daily review limit,
  and the target recall probability. The limits apply to the workspace as a whole and to
  each deck in it. The settings MUST persist.
- **FR-024**: The system MUST NOT stop offering a card because the user failed it
  repeatedly. Only the removal of a card from the decks takes it out of review.
- **FR-027**: The interface MUST name this function **Study**. The app already uses
  **Review changes** for the comparison of a deck with its package.

**Existing behaviour**

- **FR-025**: Package export MUST keep working as it does now. Review MUST NOT depend on
  a package and MUST NOT require one to be current.
- **FR-026**: Every card MUST start as a new card. The system imports no review history
  from an Anki collection.

### Key Entities

- **Card**: One front and back pair in a deck, identified by its card ID. It has rendered
  content, tags, and one deck.
- **Deck**: One Markdown file. Its title places it in the hierarchy of folders and decks.
- **Schedule**: The review state of one card: new, learning, or in review; its due time;
  its interval; and the scheduler's memory estimate for it.
- **Review record**: One grade of one card: the time, the grade, the time the user took,
  and the schedule before and after.
- **Review session**: The sequence of cards the user grades between starting and ending a
  review of a chosen deck, folder, or workspace.
- **Scheduling settings**: The daily new-card limit, the daily review limit, and the
  target recall probability.
- **Review store**: The durable store of schedules, review records, and settings for one
  workspace.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: From a running app, the user reaches the first card of a review in at most
  two actions, with no export and no second program.
- **SC-002**: After the user selects a grade, the next card is readable within 0.5 seconds
  in 95% of cases.
- **SC-003**: After a deck is saved, its changed cards show the new content in review
  within 10 seconds, with no action by the user.
- **SC-004**: Across edits of text, moves between decks, deck renames, deck merges, and
  reorders, 100% of cards keep their due date and history.
- **SC-005**: When the app is terminated during a review, zero selected grades are lost.
- **SC-006**: On the full collection of about 3,300 cards in 68 decks, every card of
  every saved deck is available for review, and the deck tree shows counts within
  2 seconds of opening the workspace after the first preparation.
- **SC-007**: A card in review and the same card in the exported package show the same
  rendered equations and diagrams.
- **SC-008**: For 100% of grades, the interval that the app shows on the selected grade
  equals the interval that Anki's scheduler stores for the card, and Anki's own database
  check reports no problem in the review store.

## Assumptions

- One person uses the app on one desktop machine. Synchronization with AnkiWeb, review on
  a phone, shared decks, and add-ons are out of scope.
- The app is the only program that reviews these cards after this feature exists.
- Scheduling uses Anki's current algorithm, FSRS, with Anki's default parameters until
  enough history exists to fit them. Fitting the parameters to the user's history is out
  of scope for this feature.
- Each workspace has its own review history.
- The grades, their keys, and the reveal key follow Anki's conventions: Space reveals,
  and 1 to 4 select Again, Hard, Good, and Easy.
- Cards have one front and one back. Cloze deletions, typed answers, audio, and card
  templates are out of scope.
- Statistics graphs, filtered decks, custom study, burying, and manual rescheduling are
  out of scope for this feature.
- A command that permanently deletes the history of removed cards is out of scope.
- One running copy of the app studies a workspace at a time.
- The card editor, package export, Problems list, and deck organization keep their
  current behaviour.
