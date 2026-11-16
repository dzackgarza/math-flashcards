# Feature Specification: In-App Review

**Feature Directory**: `specs/001-in-app-review`

**Created**: 2026-11-16

**Status**: Draft

**Input**: Review the cards with spaced repetition inside the desktop app, reusing Anki's
own scheduling code, so that studying needs no package export and no import into Anki.
The app adapts and reuses Anki as the base of a personal mathematics learning system for
one person over a career. It records as much as it can observe about that person's
learning, keeps the record permanently, and makes it available for statistical analysis.

## Purpose

This feature is the first part of a learning system for one person, not a general
flashcard program. Four aims decide its requirements:

1. **Durable knowledge.** The person wants to recall this material for a whole career.
   The time scale is decades, not the weeks before an examination.
2. **A lifelong repository.** The decks are where the person puts everything they want to
   remember for life. The system must stay usable as the collection and its history grow
   for decades.
3. **A complete record.** The system collects and keeps as much data about the person's
   performance as it can observe. Data that is not recorded at the moment of a review
   cannot be recovered later.
4. **Analysis of that record.** The person organizes their own learning from the data,
   with statistical methods and with results from learning research. The record must show
   which subjects are weak, so that the person studies them further or looks for books
   and papers on them, and which are fluent, so that they get little review and little
   emphasis.

Anki supplies the scheduler and its data model. Where Anki's behaviour serves a general
audience against these aims (a cap on recorded answer time, a review log with no card
content or subject, removal of an undone grade), the app adds what the aims need and
does not copy the limit.

## Clarifications

### Session 2026-11-16, requirement stated by the user

- The purpose above is a stated requirement, not a default. It adds User Stories 6 and 7,
  FR-028 to FR-046, and SC-009 to SC-014, and it changes FR-018, FR-021, and the handling
  of a workspace that moves to a new path.

### Session 2026-11-16, defaults

These answers are defaults taken from repository evidence. The user has not confirmed
them. A different answer changes only the requirement named in each line.

- Q: What happens to the review history of a card that is removed from the decks? → A:
  The history is kept and the card is not offered. A card that returns with the same ID
  gets its schedule back (FR-016). Reason: deck files change under external editors, and
  a deleted history cannot be recovered.
- Q: Where does the review history live? → A: In the app's data directory for the user,
  one store for each workspace (FR-018). Reason: this machine's convention keeps
  application data in XDG directories and out of repositories. A store belongs to a
  workspace, not to a path: when the path changes, the user attaches the store to the new
  path (FR-041).
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

### User Story 6 - Keep a complete record of my learning for analysis (Priority: P1)

Every time the app shows a card, it records what happened: when, which card, what content
the card had at that moment, its deck and tags, how long the user took to reveal the
answer and how long to grade, the grade, and the scheduler's estimate of the user's
memory before and after. The app also records what changes around the reviews: sessions,
undone grades, cards added, edited, moved, removed, and restored, and each change of a
scheduling setting. Nothing in this record is deleted or overwritten. The user opens the
record with their own data tools and analyses it by subject, by time, and by card.

**Why this priority**: A review that is not recorded in full is lost for every later
analysis. The record must be complete from the first grade, so it is part of the first
usable version, with User Stories 1 and 2.

**Independent Test**: Study several cards, undo one grade, edit one card, and move one
card. Open the record with a standard database tool while the app runs. Each event is
present with its fields, the undone grade is present and marked, and the record gives the
text of each card as the user saw it.

**Acceptance Scenarios**:

1. **Given** a card on screen, **When** the user reveals and grades it, **Then** the
   record has one entry with the time, the card ID, the deck and tags at that moment, the
   content shown, the time to reveal, the time to grade, the grade, the interval each
   grade offered, and the memory estimate before and after.
2. **Given** the user took longer than Anki's limit for recorded answer time, **When** the
   grade is recorded, **Then** the record has the full time.
3. **Given** the user undoes a grade, **When** the record is read, **Then** the grade is
   still present, with the time of the undo.
4. **Given** a card was reviewed, then edited, then reviewed again, **When** the record is
   read, **Then** each review gives the content the user saw at that review.
5. **Given** a card is shown and the user leaves the session without a grade, **When** the
   record is read, **Then** that presentation is present, with no grade.
6. **Given** the app is running, **When** the user opens the record with a standard
   database tool, **Then** the tool reads every entry, and the app keeps working.
7. **Given** a record that an earlier release wrote, **When** a later release opens it,
   **Then** every earlier entry is readable and unchanged.
8. **Given** a workspace folder that moved to a new path, **When** the user opens it,
   **Then** the app offers the existing record for that folder and does not start an
   empty one without the user's choice.

---

### User Story 7 - Fit the scheduler to my own history (Priority: P3)

The user asks the app to fit the scheduler's memory model to their own review history.
The app uses Anki's own fitting and evaluation code, shows how well the fitted model
predicts the history, and applies the fitted parameters when the user accepts them. The
record keeps each set of parameters and the time it applied from.

**Why this priority**: Anki's default parameters give a usable schedule, and a fit needs
history that only exists after months of use. The fit is the first use of the record to
organize the user's learning.

**Independent Test**: With a prepared history of sufficient size, run the fit, accept it,
and confirm that the intervals offered for a card change and that the record holds the
earlier and the later parameters with their times.

**Acceptance Scenarios**:

1. **Given** enough review history, **When** the user runs the fit, **Then** the app shows
   the fitted parameters and Anki's measures of their accuracy against the history.
2. **Given** a fit on screen, **When** the user accepts it, **Then** later intervals use
   the fitted parameters, and the record holds the earlier and later parameter sets.
3. **Given** too little history for Anki's fitting code, **When** the user runs the fit,
   **Then** the app states that and changes nothing.

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
- A workspace moves to a new path, or the data moves to a new machine: the app finds no
  store for the path, lists the stores that exist, and asks the user to attach one or to
  start a new one. It never starts an empty history without that choice when a store
  exists.
- A grade is recorded by the scheduler and the app stops before it writes its own entry:
  at the next start the app writes the missing entry from the scheduler's log and marks
  the fields it could not observe.
- The user's attention leaves the app while a card is on screen: the record gives the
  time the window was not in focus, apart from the total time.
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
  user, with one store for each workspace, and MUST make dated backups of it. The
  store MUST NOT be a cache: the action that rebuilds cached data MUST NOT touch it.
- **FR-019**: The system MUST NOT replace an existing review history with an empty one. A
  history that cannot be read MUST produce an error that names the file.

**Overview and control**

- **FR-020**: The system MUST show the new, learning, and due counts for each deck and
  folder, and MUST update them after each grade.
- **FR-021**: Users MUST be able to undo the last grade while that grade is the most
  recent change to the review history in the running app. When Undo is unavailable, the
  system MUST show that it is. Undo restores the schedule; the learning record keeps the
  undone grade (FR-031).
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

**Learning record**

- **FR-028**: For each presentation of a card, the system MUST record: the time, with the
  local time zone offset; the card ID; the deck, folder, deck title, and tags of the card
  at that moment; an identifier of the content shown; the session and the position in
  it; the kind of presentation (new, learning, review, relearning); the time from showing
  the front to the reveal; the time from the reveal to the grade; the time the window was
  not in focus; the grade, or the fact that the user left without one; the interval each
  of the four grades offered; the scheduler's state and memory estimate for the card
  before and after; and the scheduling settings and parameter set in effect.
- **FR-029**: The system MUST record times as measured. A limit that the scheduler applies
  to its own recorded answer time MUST NOT limit the learning record.
- **FR-030**: The system MUST keep the content of each card as the user saw it at each
  presentation, so that an analysis can read what was shown after the card is edited or
  removed.
- **FR-031**: The system MUST NOT delete or overwrite an entry of the learning record. An
  undo, a correction, and a removal are new entries that refer to earlier ones.
- **FR-032**: The system MUST record each session with its start, its end, and its scope.
- **FR-033**: The system MUST record each change to a card that the review store applies:
  added, content changed, tags changed, moved, removed, restored, with its time.
- **FR-034**: The system MUST record each change of a scheduling setting and each change
  of the scheduler's parameters, with the earlier value, the later value, and the time.
- **FR-035**: The system MUST record, with each entry, the release of the app and the
  version of the scheduler that wrote it.
- **FR-036**: The learning record MUST be complete without the scheduler's own database:
  every grade that the scheduler holds is also in the learning record, with the
  scheduler's values for it.
- **FR-037**: The learning record MUST be readable with standard data tools, without this
  app and without Anki, while the app runs and when it does not.
- **FR-038**: The project MUST document every field of the learning record: its meaning,
  its unit, and when it is empty.
- **FR-039**: The format of the learning record MUST only grow. Every entry written by an
  earlier release MUST stay readable and unchanged under every later release.
- **FR-040**: The dated backups (FR-018) MUST include the learning record.
- **FR-041**: A store MUST belong to a workspace and not to its path. When the system
  finds no store for the path of a workspace and at least one store exists, it MUST ask
  the user to attach an existing store or to start a new one.
- **FR-042**: Users MUST be able to find the location of the learning record from inside
  the app.
- **FR-043**: The learning record MUST stay on the user's machine. The system MUST NOT
  send any part of it elsewhere.

**Scheduling for long-term retention**

- **FR-044**: When the reviews due exceed what the user studies in a day, the system MUST
  offer first the cards that the scheduler estimates the user is most likely to have
  forgotten, so that cards the user knows best wait longest.
- **FR-045**: Scheduler tags that mark a card as repeatedly failed MUST survive every
  deck change, so that the record and the review store both show which cards are weak.
- **FR-046**: Users MUST be able to fit the scheduler's parameters to their own review
  history with Anki's own fitting code, see Anki's measures of the fit, and accept or
  reject it.

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
- **Learning record**: The permanent, append-only record of everything the app observes
  about the user's learning in one workspace. It is part of the review store and is
  readable without the app and without Anki.
- **Presentation**: One showing of one card to the user, with its times, its grade or
  the absence of one, the content shown, the card's subject at that moment, and the
  scheduler's state before and after.
- **Content version**: The front and back of a card as shown at a presentation.
- **Card change**: One change that the review store applied to a card: added, content
  changed, tags changed, moved, removed, or restored.
- **Settings change**: One change of a scheduling setting or of the scheduler's
  parameters, with the earlier and later values.

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
- **SC-009**: 100% of presentations, graded or not, are in the learning record with every
  field of FR-028. Every grade in the scheduler's log has its entry in the learning
  record.
- **SC-010**: Across undo, card edits, moves, removals, deck reorganization, app updates,
  **Rebuild cached data**, and a change of the workspace path, zero entries of the
  learning record are lost or changed.
- **SC-011**: With a standard database tool and the field documentation alone, the user
  computes, for any folder, deck, or tag and any period: the number of presentations, the
  share graded Again, and the mean time to reveal. No access to the app or to Anki's
  database is needed.
- **SC-012**: For any past presentation, the record gives the exact front and back that
  the user saw.
- **SC-013**: A record written by the first release of this feature is readable, with
  every entry unchanged, by each later release.
- **SC-014**: A recorded time above Anki's limit for answer time equals the measured
  time within 0.1 seconds.

## Assumptions

- One person uses the app on one desktop machine. Synchronization with AnkiWeb, review on
  a phone, shared decks, and add-ons are out of scope.
- The app is the only program that reviews these cards after this feature exists.
- Scheduling uses Anki's current algorithm, FSRS, with Anki's default parameters until
  the user accepts a fit to their own history (User Story 7).
- Each workspace has its own review history.
- The subject of a card, for analysis, is its folder, its deck, and its tags. The system
  adds no separate subject classification.
- Views inside the app that analyse the learning record, and recommendations of study
  material from it, are later features. This feature produces the record they need and
  makes it readable with external tools.
- The app has no command that deletes any part of the learning record.
- The grades, their keys, and the reveal key follow Anki's conventions: Space reveals,
  and 1 to 4 select Again, Hard, Good, and Easy.
- Cards have one front and one back. Cloze deletions, typed answers, audio, and card
  templates are out of scope.
- Filtered decks, custom study, burying, and manual rescheduling are out of scope for
  this feature.
- One running copy of the app studies a workspace at a time.
- The card editor, package export, Problems list, and deck organization keep their
  current behaviour.
