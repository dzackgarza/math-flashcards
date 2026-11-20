# Contributing flashcard content

## Application contribution lessons

- **ARCH001 — Native source ownership.** Saving and studying cards use the existing
  card parser, the shared renderer, and direct Anki scheduling calls. Routing Study
  through generated packages => pass native card identities and source to these owners.
- **TEST001 — Observe the user path.** Derive acceptance tests from the specification's
  user stories and follow `test-guidelines`. Set an internal completion flag and assert
  it is set => perform the user action and assert the resulting visible or stored output.
  A transport test proves that transport; the complete Study story also needs the window.
- **TEST002 — Short feedback with retained evidence.** Keep tier 1 under five minutes,
  including setup, and retain logs and nested timing evidence with revision and input
  context. Rebuild the release after every small edit => check the affected path with
  prepared dependencies and build the release at the plan's milestones.
- **TEST003 — Select the active editing surface.** Study and the editor share card
  faces. Locate matching front text and type immediately after E => wait for
  **Return to Study** and locate the face inside the editor column before typing.
- **RESEARCH001 — Synthesize at the owner.** State findings, sources, alternatives,
  limits, and the resulting decision in the maintained document that owns the topic.
  Leave a decision in search output or chat => update the feature research, research
  register, or dependency survey before accepting work that relies on it.
- **EDIT001 — Keep input transactions writable.** Preview failures must remain visible
  without preventing the editor from publishing text changes. Throw from an image
  widget while its media map is being refreshed => render the error as a widget,
  accept the edit, and refresh the preview from the resulting source.
- **EDIT002 — Let a dialog consume its closing key.** Close a dialog on Escape and
  allow the same event to leave Study => stop propagation before closing the dialog.
  Changing the open-state flag alone can enable the underlying shortcut during
  that same event. A completed operation can leave focus on the document after
  disabling a control; use Mantine's document-level hotkey hook while the dialog
  is mounted, including input and editable targets.
- **EDIT003 — Focus the new action surface.** Open Study from a deck menu while
  leaving focus on the navigation tree => focus **Show answer** when the card
  mounts. Mantine's tree consumes Space for expansion; a visible card alone does
  not transfer keyboard control. Test the shortcut immediately after the real
  menu action, without inserting a focus click in the test.

This collection supports mathematical research. Prioritize knowledge that helps
the researcher recognize a useful result, check its hypotheses, construct an
example, compute an invariant, or carry an argument forward.

## Research context and teaching remit

Establish the research and study objectives from the current request and the
active papers, manuscripts, and research notes. Recheck those sources for each
coverage assessment; a previous assessment does not define the present scope.

Starting points include the
[research statement](../../research/writing/research-statement/ResearchStatement.md),
the [Coble manuscript](../../research/writing/coble/surfaces-and-moduli/surface-types.md),
and the user's coauthored paper, Alexeev–Engel–Garza–Schaffler,
[*Compact moduli of Enriques surfaces of degree 2*](https://doi.org/10.1017/nmj.2025.10).
Follow the work relevant to the current task from these sources, including newer
work and changed objectives. Use drafts to establish intent; verify mathematical
claims against their sources. Keep established results, draft claims, and proposed
extensions distinct.

The cards supply working knowledge for this research, not a substitute for
doing it. They do not aim to reproduce entire papers, establish new comparison
theorems, solve open classification problems, retain every computed orbit or
boundary table, or teach every research program pursued by a cited author.
The papers and research notes own those arguments and results. Cards may retain
a construction, theorem, compact table, or derivation from them when it is a
repeatedly needed tool or an authored way to recover that tool.

The audience is a graduate-level mathematical researcher. Explanations need
not start from elementary mathematics, but basic definitions and calculations
remain legitimate recall targets. A topic appearing in the user's own work
does not establish mastery of every prerequisite; absence from the decks does
not establish ignorance. No personal mastery profile is supplied by this remit.

The collection also has independent algebra, analysis, topology, geometry,
number theory, and other study subjects described in
[the subject guide](docs/deck-subjects.md). Their existing authored material is
not disposable because it falls outside the current research task. Conversely, a
tool's usefulness in an unrelated subject does not make it a missing
prerequisite for that task.

## Understand the research before evaluating coverage

Before classifying topics, reconstruct the mathematics of the work being
evaluated. Read the relevant constructions and arguments, not just abstracts,
definition lists, or search matches.

1. Establish the objective and the objects involved. Identify what the work
   constructs, computes, classifies, or proves, and why the current study task
   needs it. Distinguish the user's research from background literature and
   independent study.
2. Follow the argument from inputs to output. For each substantive step, recover
   the objects, maps, operations, hypotheses, and conclusion. Work through the
   equations and diagrams enough to explain why the step is valid. Follow cited
   results when their role or hypotheses are unclear.
3. Recover implicit dependencies from those operations. Translate local notation
   and unnamed constructions into their standard mathematical forms. Ask what
   knowledge lets a reader perform the step even if the paper never names that
   knowledge. Check definitions, hypotheses, local models, and calculations;
   keyword absence is not evidence that a tool is unused.
4. Check the reconstruction mathematically. Explain how successive steps fit
   together, what supplies each required hypothesis, and what changes when a
   relevant hypothesis fails. Use a simple instance or local calculation where
   it tests understanding. If a step cannot be explained, investigate it before
   judging its prerequisites.
5. Only then compare those dependencies with the cards. Search equivalent
   terminology and inspect full answers and examples. Separate reusable inputs
   from results produced by the paper, and determine what the learner needs to
   recognize, reconstruct, or apply again.

For example, a diagram with commuting involutions calls for identifying the
group they generate, the intermediate quotients, and the invariant algebras.
That analysis reveals the covering theory in use even without the phrase
“abelian cover.” Check the actual base and maps before applying a smooth or flat
cover formula. This illustrates how to infer a dependency; it is not a topic
list for future research.

The evidence for a coverage judgment is an explained mathematical use at a
source location. A list of terms or citations does not establish understanding.
Record that evidence in the requested assessment or change rationale. Keep
paper-specific dependency inventories out of these instructions; derive them
from the current sources when needed.

## Evaluate usefulness through a mathematical task

For each proposed coverage finding, connect the candidate to an operation the
learner needs to perform. State that operation concretely: construct a double
cover from branch data, compute a discrepancy, identify a cusp from an isotropic
sublattice, recover a boundary component from a diagram, or check the hypotheses
of a comparison theorem. "Relevant to moduli" does not identify an operation.

Then distinguish the candidate's role and the recall target:

- **Background assumed by the argument:** recall the usable definition,
  theorem, calculation, or example, including hypotheses.
- **A construction used in the research:** recall its inputs, operations,
  output, and a recoverable example, including specialized constructions.
- **A result or classification produced by the research:** decide which part
  must be available for another argument. A construction rule or useful compact
  classification can deserve a card; copying the entire output is not automatic.
- **Incidental machinery or a separate research topic:** identify a task in the
  research or an independent study subject before claiming a coverage gap.

A construction card should make the operation recoverable; memorizing an
unexplained paper-local symbol does not achieve the same purpose. A textbook
application establishes a use somewhere in mathematics. Trace its dependency
on the current research or study objective before claiming a coverage gap.

Evaluate relevance, existing coverage, and personal familiarity separately.
Check current fronts and backs, equivalent terminology, and authored examples
before declaring a gap. Authorship of a paper is evidence of research relevance,
not a measurement of recall. Neither a missing card nor an unfamiliar-looking
term proves what the user does or does not know. Use explicit learning goals or
actual review evidence for claims about personal knowledge.

Keep the supporting task and source location with the editorial judgment in
the requested answer or change rationale. Do not create a separate coverage
ledger. If the dependency or teaching purpose remains unresolved after checking
the available sources, report that precise uncertainty and preserve existing
material; do not convert it into a removal decision. These checks must also be
applied to an audit's proposed replacements before remediation starts.

## Select knowledge within that remit

Select material before deciding how to present it as cards. Give priority to
the working knowledge needed for the research and study subjects above: definitions,
constructions, theorem statements, formulas, examples, and techniques that a
researcher needs to read papers and carry out arguments. Foundational material
qualifies even when papers routinely assume it without citation. Include the
prerequisites and practical calculations needed to use that knowledge.

Specialized material belongs when its use serves the current research or study
objective. Its origin in a particular paper does not make it peripheral.
Establish its role through the argument that uses it.

Use in another paper or textbook can establish that a tool is reusable, but
does not by itself establish a reason to teach it here. Shared vocabulary
does not establish a mathematical dependency. Apply the same relevance test
to familiar and unfamiliar terminology.

A paper's newly defined object is not automatically a prerequisite for reading
that paper. Determine whether it is the object being investigated, a tool
needed in the user's work, or incidental machinery. A construction can become
working knowledge through its use in the current research even if it is
rare elsewhere. A definition introduced to state one paper's particular result
can remain in reading notes. Age, popularity, a citation, and the existence of
a precise definition do not decide between these cases.

Assess a proposed addition by what the learner will need to recognize,
reconstruct, or apply again. Do not turn a paper's sequence of definitions into
a deck by default, or treat every concept absent from the collection as a gap.
These selection criteria apply to concepts and results as well as examples.

Before calling existing material out of scope, check its role in the research
sources above, the independent subject scope, and its authored context. Failure
to find a use is an unresolved relevance question, not evidence for removal.
An audit must distinguish that uncertainty from a supported exclusion. A request
to remediate an audit does not supply missing evidence for its judgments.

## Choose prompts by research use

Assess coverage by the research tasks the cards prepare the learner to perform.
For a theorem, prioritize recognizing when it applies, recalling the precise
hypotheses and conclusion, and applying it in different settings. For a
construction, prioritize the input data, the construction itself, conditions
that make it valid, and properties of the resulting object. Include examples
and counterexamples that help choose a method or detect an invalid application.

Proof study is long-tail coverage. Add proof questions when a proof technique
has a concrete research use, such as adapting a result to new hypotheses or
reusing a construction from its proof. Routine applications take priority over
reconstructing standard proofs. A missing proof card alone does not establish
a coverage gap.

## Build and reuse a simple example repertoire

Develop a small stock of familiar mathematical objects that can serve many
purposes. When choosing an example, search that stock first. Prefer a case
whose construction, relevant properties, and calculations the researcher can
recover from familiar ideas. Repeated use should deepen intuition and connect
topics while reducing the amount of separate material to remember.

Choose the least complicated example that exhibits the intended phenomenon.
Apply this priority equally to examples of definitions, counterexamples, and
failures caused by removing a theorem's hypothesis. A collection of elementary
cases can be more useful than a single elaborate construction. Judge simplicity
by the knowledge and reasoning needed to reconstruct the example, not merely
by the length of its equation or description.

Small variations of familiar objects belong to this repertoire too. Try changing
a coefficient or invariant, specializing a parameter, taking a product, or
performing a familiar operation such as a blowup. State what changes, what
persists, and which feature explains the result. For a failed hypothesis,
isolate its role while retaining the other hypotheses whenever possible.
Use a more involved construction when the simpler repertoire cannot capture
the required phenomenon. Extend that repertoire through these connections.

This priority guides additions and example selection. Apply the editorial
rules below when improving an existing authored example or derivation.

## Prioritize compact representations of relationships

Give high priority to composite cards that organize a connected body of
knowledge in one place. Use implication chains, diagrams, tables, and concise
annotations to make the structure visible. For an implication hierarchy,
combine the full chain with a short list of examples showing where the
converses fail. Reuse the familiar example repertoire to explain those
boundaries. A card can test several facts when their relationships form the
idea being learned; one fact per card is not a default requirement.

For initial learning, establish this connected representation before expanding
it into separate prompts for each implication, converse, example, or
rearrangement. Prefer a compact representation that helps the researcher
reconstruct the whole pattern. Compression should expose relationships and
retain the hypotheses needed to interpret them, rather than merely abbreviate
the text or collect unrelated facts.

Focused cards serve a complementary, later purpose. Use them to test individual
parts of the composite, distinguish apparent familiarity from understanding,
and locate gaps through spaced-repetition results. Those results can guide
targeted practice of weak links. Treat this diagnostic coverage as long-tail
work after the composite card, not as a replacement for it. A review grade on
the composite alone does not identify which part needs attention.

## Write for recall and rapid checking

Most cards should present compact mathematical structure. The learner should
be able to compare an attempted answer with the back directly, without first
extracting the answer from an expository paragraph.

- Put the requested definition, formula, conclusion, or construction first.
- Use equations and implication chains for relationships, tables for parallel
  comparisons, lists for conditions and examples, and aligned steps for calculations.
- Keep hypotheses and quantifiers next to the statements they govern. Give
  shared assumptions once when they apply to an entire table or chain.
- Use short prose where it explains a mechanism, distinguishes cases, or supplies
  a mnemonic cue. Place explanations beside the facts they explain.
- Omit article-style introductions, historical framing, rhetorical transitions,
  repeated summaries, and commentary announcing the importance of the material.
- Keep references secondary to the answer. Source discussion belongs on a card
  only when identifying or comparing sources is itself the retrieval task.
- Record a card's sources in the `cite` attribute of its front div, in Pandoc
  citation syntax with Zotero's Better BibTeX citation keys:
  `::: {.front card-id="…" cite="[@AEGS25, §3.7; @Nik80, Prop. 1.4.1]"}`.
  Write no `Reference:` paragraph or prose citation in a card face. Add a
  missing work to Zotero first; `just check-citations` checks every key
  against the running Zotero library. A remark that a paragraph attaches to a
  citation is mathematics: keep it in the answer.

Compact presentation is compatible with substantial composite cards. Organize
their connected content so the structure and the points of comparison are visible;
do not split it into isolated prompts merely to shorten each card. Do not achieve
brevity by dropping hypotheses, examples, intermediate reasoning, or authored
memory aids. Preserve useful derivations and the author's voice under the
editorial rules below. Longer prose is appropriate when the explanation itself
is what the card asks the learner to reconstruct.

### Compress sentence structure, preserve mathematical content

Use the shortest readily understood form that retains the requested knowledge.
Sentence fragments, labels, and mathematical notation are normal flashcard
forms. Complete literary sentences are optional. Do not replace clear prose
with an artificial voice, invented abbreviations, or a string of disconnected
keywords.

Prefer standard mathematical notation to prose that merely spells out a
symbolic condition or relation. For example, write “where $a,b>0$” rather than
“where the two parameters are positive,” and $x\in U\cap V$ rather than
“$x$ belongs to each of the two sets.” Apply this to hypotheses, quantifiers,
membership, inequalities, maps, and relations. Name the objects explicitly;
do not make the reader recover them from phrases such as “each entry.” Use
prose for interpretation, reasoning, and memory cues that notation alone does
not convey. Keep notation standard and readable, with all necessary
conventions and quantifier scope explicit.

The minimum answer retains the object, assumptions, property or operation,
quantifiers, and conclusion. An example also needs the feature that establishes
its role. A calculation or explanation needs the steps requested by the prompt
and the connections needed to recover them. Reuse context established on the
front or in shared assumptions; do not repeat it in every row.

Prefer these transformations when their stated context applies:

| Verbose structure | Compact form |
| --- | --- |
| Metadiscourse: “It is important to observe that…”; “We now recall that…” | Delete the introduction; state the fact. |
| Repeated question: “The definition of a … is the following…” | Give the definition directly. |
| Definition wrapper: “We say that $X$ is $P$ if and only if…” | “$X$ is $P$ iff …”, or “$P\iff\cdots$” under a clear label. |
| Predicate padding: “$X$ has the property that it is normal” | “$X$ normal.” |
| Cleft sentence: “It is the exceptional divisor $E$ that has discrepancy $-1$” | “$a(E)=-1$.” Retain any intended exclusivity explicitly. |
| Existential scaffolding: “There exists an integer $m>0$ such that $mD$ is Cartier” | “$\exists m\in\mathbb Z_{>0}: mD$ Cartier.” Preserve existence. |
| Nominalization: “Perform a computation of the intersection number” | “Compute $D\cdot C$.” |
| Weak verb plus noun: “Make a choice of a point $p\in X$” | “Choose $p\in X$.” |
| Passive construction: “The blowup of $X$ at $p$ is taken” | “Blow up $p\in X$.” |
| Relative-clause packaging: “Let $X$ be a variety which is smooth and projective over $\mathbb C$” | “$X/\mathbb C$ smooth projective.” |
| Conditional packaging: “Under the assumption that $P$ holds, we can conclude that $Q$ holds” | “$P\Rightarrow Q$.” |
| Causal packaging: “The reason that $Q$ holds is that $P$ holds” | “$Q$, since $P$”, or “$P\Rightarrow Q$” when this is the full reasoning. |
| Possibility padding: “We can use adjunction in order to compute…” | “By adjunction: [formula].” Include its hypotheses where needed. |
| Contrastive packaging: “However, it is not necessarily the case that the converse holds” | “Converse fails: [counterexample].” |
| Example announcement: “An example illustrating this phenomenon is given by…” | “Example: [object; decisive property].” |
| Repeated subjects: “$X$ is normal. $X$ is Cohen–Macaulay. $X$ is not smooth.” | “$X$: normal, CM, singular.” Use CM only when established vocabulary. |
| Nested case prose: “In the first case …, whereas in the second case …” | A case split or table with explicit conditions and outcomes. |
| Fact followed by paraphrase: formula, then “In other words…” restating it | Keep one representation unless the second supplies a useful interpretation or memory cue. |
| Evaluation and emphasis: “This is a very useful and important consequence” | Delete; or name the concrete application when that is part of the task. |

Articles and copulas can disappear in labels and lists: “Exceptional curve:
$E\cong\mathbb P^1$, $E^2=-2$.” Remove them only when the referent and relation
remain clear. Passive voice is not intrinsically wrong; “$E$ is contracted”
may be the shortest precise description when the morphism is already fixed.
Do not force every sentence into the same template.

Preserve the logic during every transformation:

- Keep $\forall$, $\exists$, uniqueness, quantifier order, and dependence of
  choices. $\forall x\,\exists y$ and $\exists y\,\forall x$ differ.
- Keep negation, exceptions, restrictions, and inequality endpoints. “Not all”
  is different from “none”; $>0$ is different from $\ge0$.
- Preserve the direction and strength of a relation: implication, equivalence,
  equality, isomorphism, and equality up to a choice are distinct.
- Keep mathematical modifiers such as “normal,” “proper,” “relative,” and
  “geometrically.” A relative clause may carry a hypothesis; compress its
  grammar, not its restriction.
- Keep causal and conditional connections explicit. “$P$. $Q$.” does not
  express “$P\Rightarrow Q$.” Use arrows, “if,” “since,” or an aligned derivation
  when they carry meaning.
- Name an object again when a pronoun would have multiple possible referents.
- Preserve authored derivations and mnemonic routes. Compress surrounding
  prose without removing the steps that make the result recoverable.

Do not impose a word cap or a token-reduction target. Judge a revision by whether
the same mathematical answer is easier to retrieve and check. A dense composite
card can retain many related facts. Splitting it into isolated fragments is not
a substitute for exposing their structure.

These rules adapt the removal of linguistic overhead in
[Caveman Compression](https://github.com/wilpel/caveman-compression/blob/main/SPEC.md)
and the preservation of technical content in
[caveman](https://github.com/JuliusBrussee/caveman/blob/main/skills/caveman/SKILL.md).
The projects concern LLM communication; their token-saving claims do not
establish effects on human recall. In particular, do not adopt blanket deletion
of logical connectives. The use of direct verbs and removal of empty phrases
also follows the
[Microsoft concise-writing guidance](https://learn.microsoft.com/en-us/style-guide/word-choice/use-simple-words-concise-sentences).

### Remove language that obscures the retrieval task

The learner should retrieve mathematics and check the answer without first
decoding the author's phrasing. Reject wording that hides the objects,
operations, relationships, or decisive distinctions, even when it is short.

| Pattern | Flashcard failure | Required form |
| --- | --- | --- |
| Hidden objects and operations | “The recovery of the sequence is achieved through dualization” buries the operation in abstract nouns. | “Dualize: [sequence]”, retaining the intermediate steps that explain how to obtain it. |
| Abstract noun piles | “Boundary coefficient admissibility controls singularity classification” leaves the actual test unstated. | Under the stated pair hypotheses: “SNC boundary: klt iff all $b_i<1$; lc iff all $b_i\le1$.” |
| Ambiguous references | “This preserves the relevant property” requires guessing both the operation and the property. | Name what acts, on which object, and what it preserves. |
| Empty significance claims | “An important bridge between the theories” supplies no retrievable relationship. | State the implication, correspondence, formula, or concrete use. |
| Buried distinctions | Expository setup delays the quantifier, inequality, or exception that distinguishes the concepts. | Put the distinguishing condition first, with its assumptions; place supporting explanation beside it. |
| Invented metaphors and terminology | “The boundary is the gatekeeper of admissibility” adds a translation task and competes with established terminology. | State the boundary condition in standard mathematical language. |
| Repeated paraphrases | Reading a formula aloud in prose adds another pass through the same content. | Retain the formula and any explanation that adds interpretation, reasoning, or a useful memory cue. |

These patterns cause specific problems for review:

- An unclear retrieval target leaves the learner unsure what to produce.
- An answer without explicit criteria cannot reliably identify a missing
  hypothesis, wrong quantifier, or incorrect conclusion.
- Familiarity with polished wording can conceal inability to reconstruct the
  mathematical relationship. Ask for the relationship and make it checkable.
- Invented terminology competes with standard vocabulary and existing authored
  memory cues.
- Buried content imposes the same decoding work on every repetition.

Before accepting a card, check that the learner can immediately identify the
objects, conditions, operation or relationship, and conclusion relevant to its
prompt, then compare an attempted answer against them. A short sentence can
fail this check; a substantial derivation or comparison table can pass it.
Repair the wording while preserving mathematical content and useful authored
explanations. Do not infer poor quality from a stylistic marker alone.

This applies the clarity taxonomy in
[Zonder Labs, Why is AI Slop so Frustrating to Read?](https://zonderlabs.com/slop):
hidden actors and actions, vague wording, and empty statements or misplaced
emphasis. The consequences for flashcard review above are editorial reasoning
for this collection; the article does not establish learning outcomes.

### Make technical sentences interpretable

The article's annotated Triton/CUDA example also shows failures that shortening
alone cannot fix: unnamed comparison quantities, unexplained technical terms,
hidden actions, and conclusions delayed behind implementation details. Apply
the following rules to mathematical cards.

| Failure | Required repair |
| --- | --- |
| A comparison omits what is compared | Name the invariant or relation and both objects. Replace “same numbers” with the actual equality, such as $h^i(X,\mathcal O_X)=h^i(Y,\mathcal O_Y)$ with its range of $i$. Equal dimensions do not mean that the cohomology groups have been canonically identified. |
| A number has no stated meaning | Attach its quantity, normalization, reference value, or domain. “Degree $2$” must identify the map, divisor, or extension whose degree is meant. Numerical precision cannot supply a missing referent. |
| A technical label hides the condition or mechanism | Replace unexplained compound labels with the condition itself. Use established technical terms, but define unfamiliar terms needed to understand the answer. An acronym or specialized noun does not explain its own role. |
| The same object acquires several names | Keep notation and terminology stable. Introduce aliases explicitly; do not alternate between a construction, method, model, and strategy when it is unclear whether they denote the same object. |
| A status description hides a mathematical operation | Replace “the sequence is now in dual form” with the functor applied and the resulting sequence. State the exactness conditions and any resulting Ext terms. |
| A verb lacks its required objects or relation | “The change can be attributed” leaves the attribution unspecified. Name the operation and its effect: for a blowup of a smooth surface at a point, $K_{\widetilde X}=\pi^*K_X+E$ and $K_{\widetilde X}^2=K_X^2-1$. |
| A metaphor assigns an action to the wrong subject | Replace claims that a parameter “fixes” or “unlocks” a result with the actual dependence: which choice satisfies which condition, and why. Keep a useful authored mnemonic beside the precise relation. |
| Detail interrupts the main assertion | Complete the claim before adding examples, qualifications, or calculations. Keep hypotheses attached to the claim; move supporting detail into a following line, table, or aligned calculation. |
| A decisive conclusion appears as an afterthought | State the conclusion in the answer's main position. If an example disproves an implication, name that implication and show the satisfied hypothesis and failed conclusion. |
| Several claims are compressed into a sentence with unclear connections | Separate the clauses and label their logical roles: assumption, operation, result, reason, or counterexample. Preserve the relationships in the composite card. |

Read the resulting sentence for meaning, not just grammatical correctness.
Can the reader identify what changes, what is compared, what the verb asserts,
and which condition supports the conclusion? If an omitted fact cannot be
recovered from the card's stated context, verify and supply it. Do not guess a
missing quantity, baseline, hypothesis, or causal explanation merely to produce
a fluent rewrite.

### Organize the whole card around the knowledge being recalled

Identify the answer's main point before shortening its sentences. Give the
requested knowledge the main position; keep supporting material subordinate
and visibly connected to it. Repair misplaced emphasis first. Further deletion
is optional when it would remove useful explanation or an authored memory cue.

Match the organization to the retrieval task:

| Task | Visible organization |
| --- | --- |
| Definition | Object and ambient assumptions; defining conditions and quantifiers |
| Theorem | Hypotheses attached to the conclusion; exceptions and scope beside the claims they qualify |
| Construction | Input; operation; output and its required properties |
| Comparison | Shared assumptions; parallel criteria; examples separating the classes |
| Implication or failed converse | Precise relation; example satisfying the premise and failing the proposed conclusion |
| Calculation or derivation | Starting data; connected steps; result, with each justification beside its step |

These are organizational guides, not mandatory templates. Preserve an authored
route that already makes the mathematics recoverable. Composite cards can
combine these forms while keeping their relationships visible.

Align sentence structure with mathematical structure. Prefer “$f$ contracts
$E$” to “The exceptional contraction behavior is realized through $f$.”
If the question concerns $E$, “$E$ is contracted by $f$” may place the emphasis
better. Abstract objects and passive constructions are legitimate mathematical
language; reject them when they hide the relevant object or operation, not
merely because they are abstract or passive.

Use natural combinations of established mathematical words. Defining an invented
phrase does not justify retaining it. “Coefficient admissibility behavior”
adds a translation step where explicit coefficient inequalities would answer
the question. For each sentence, identify the proposition or explanatory
connection it contributes. Familiar words and grammatical correctness do not
rescue a sentence with no discernible point.

Keep the status of claims explicit. Distinguish a proved result from a heuristic,
conjecture, computed example, or prediction. State what a calculation establishes
and which general conclusion still needs an argument. A transition such as
“therefore” must not silently promote an observation or proposed explanation
into a theorem.

Exclude argumentative framing that answers no part of the prompt. Do not invent
a dispute, defense, or dramatic reversal before giving the mathematics. A real
misconception or false converse belongs when the card asks the learner to
distinguish it; state the disputed claim and the decisive evidence directly.

Control dependencies between clauses. Introduce notation before using it, keep
names stable, and put each qualification beside its target. Break up chains of
pronouns, parentheses, comparisons, and renamed objects when the reader must
backtrack to determine which assertion belongs to which object. Use separate
lines or a table while retaining the logical connections.

After local wording edits, review the front and back as a whole. Check that:

- the answer's organization matches the question;
- shared assumptions have clear scope and individual qualifications remain attached;
- examples support the definition or distinction without interrupting it;
- each conclusion remains connected to its justification;
- the learner can compare a recalled answer with the card without reorganizing it.

These rules extend the cited Zonder analysis to mathematical recall. Its
emphasis on sentence subjects, actions, natural wording, and main points
supports the clarity rules. The distinctions between theorem, heuristic, and
prediction, and the whole-card checks, are editorial applications to this
collection.

### Worked replacements for whole-card clarity

These examples demonstrate the preceding rules. “Before” text is deliberately
defective; “after” text supplies the answer to the stated prompt. Preserve the
mathematical information and useful reasoning when making comparable edits.

**Match the organization to the prompt.**

Front: “Define a $\mathbb Q$-Cartier divisor. How does this differ from
$\mathbb Q$-factoriality of a variety?”

Before:

> A smooth variety is locally factorial. Multiples of divisors are relevant
> here. For a normal variety, one considers whether every Weil divisor has a
> positive multiple that is Cartier. An individual Weil divisor is called
> $\mathbb Q$-Cartier when it has such a multiple.

After:

> $X$ normal; $D$ a Weil divisor.
>
> | Notion | Condition |
> | --- | --- |
> | $D$ $\mathbb Q$-Cartier | $\exists m\in\mathbb Z_{>0}:mD$ Cartier |
> | $X$ $\mathbb Q$-factorial | $\forall D,\ \exists m_D\in\mathbb Z_{>0}:m_DD$ Cartier |
>
> Smooth $X$: locally factorial, hence $\mathbb Q$-factorial.

The comparison now displays the change of quantifier. The supporting smooth
example follows it.

**Move the requested conclusion ahead of supporting detail.**

Front: “For the blowup $\pi:\widetilde S\to S$ of a smooth projective complex
surface at a point, how does $K^2$ change?”

Before:

> The exceptional curve $E$ has square $-1$. Also $\pi^*K_S\cdot E=0$ and
> $K_{\widetilde S}=\pi^*K_S+E$. Expanding this square shows that the canonical
> self-intersection decreases by one.

After:

> $K_{\widetilde S}^2=K_S^2-1$.
>
> Calculation:
> $$K_{\widetilde S}=\pi^*K_S+E,\qquad
> (\pi^*K_S)\cdot E=0,\qquad E^2=-1,$$
> hence
> $$K_{\widetilde S}^2=(\pi^*K_S+E)^2=K_S^2-1.$$

The calculation survives; its conclusion is immediately available for checking.

**Choose the subject according to the question.**

Shared setup: $\pi:\operatorname{Bl}_pS\to S$, with exceptional curve $E$.

Before, for either prompt:

> The occurrence of contraction of the exceptional locus is effected by the
> blowdown morphism.

After:

| Front | Back |
| --- | --- |
| “What does $\pi$ contract?” | “$\pi$ contracts $E$ to $p$.” |
| “What happens to $E$ under $\pi$?” | “$E$ is contracted to $p$ by $\pi$.” |

Both voices are clear. Each sentence begins with the object the prompt asks about.

**Separate calculations from universal claims.**

Front: “Does checking $n=0,1$ establish that $n^2+n+41$ is prime for every
integer $n\ge0$?”

Before:

> The values are $41$ and $43$, both prime, so the expression always produces
> primes.

After:

> No.
>
> - Checked cases: $f(0)=41$, $f(1)=43$.
> - Universal claim: $\forall n\ge0,\ f(n)$ prime.
> - Counterexample: $f(41)=41^2+41+41=41\cdot43$.

The computed cases remain true; they do not establish the universal claim.
When a conjecture remains unresolved, label it as a conjecture instead of
inventing either a proof or a counterexample.

**Remove invented disputes; retain the actual contrast.**

Front: “Does normality imply smoothness for a complex variety?”

Before:

> Normality is not the villain here. The real story is that smoothness asks
> for something stronger, and the quadratic cone illustrates that distinction.

After:

> No. $X=V(xy-z^2)\subset\mathbb A^3_{\mathbb C}$ is normal but singular.
>
> - Hypersurface $\Rightarrow$ Cohen–Macaulay $\Rightarrow S_2$.
> - Singular locus: $\{0\}$, of codimension $2$ $\Rightarrow R_1$.
> - $R_1+S_2\Rightarrow$ normal; the vertex is singular.

The replacement answers the actual implication question and checks both
properties of the counterexample.

**Untangle references and attach each qualification to its object.**

Front: “For coordinate axes $D_1,D_2\subset\mathbb A^2_{\mathbb C}$, compare
$(\mathbb A^2,D_1)$ and $(\mathbb A^2,D_1+D_2)$ as plt and dlt pairs.”

Before:

> With the second added it is still dlt, although this is no longer plt since
> blowing it up gives discrepancy $-1$, unlike the first, where it is $0$.

After:

> Let $E$ be the exceptional divisor of the blowup of the origin.
>
> | Boundary $\Delta$ | $a(E,\mathbb A^2,\Delta)$ | Classification |
> | --- | --- | --- |
> | $D_1$ | $0$ | plt, hence dlt |
> | $D_1+D_2$ | $-1$ | dlt, not plt |
>
> Both boundaries are SNC. The identity is a log resolution with no exceptional
> divisors, so both pairs are dlt. The smooth coefficient-one component gives
> a plt pair; with both components present, $E$ violates the plt inequality.

The blowup center, pair, divisor, and discrepancy are explicit. The table
compares the examples; the explanation distinguishes witnessing dlt from
disproving plt.

**Repair a disorganized answer whose sentences are individually clear.**

Front: “Dualize a short exact sequence of vector bundles
$0\to\mathcal A\to\mathcal B\to\mathcal C\to0$. Why is the dual sequence exact?”

Before:

> $\mathcal C$ is locally free. The dual sequence ends in $\mathcal A^\vee$.
> The sheaf $\mathcal Ext^1(\mathcal C,\mathcal O_X)$ vanishes.
> Apply $\mathcal Hom(-,\mathcal O_X)$. This functor is left exact.
> The dual sequence begins with $\mathcal C^\vee\to\mathcal B^\vee$.

After:

> Apply $\mathcal Hom(-,\mathcal O_X)$:
> $$0\to\mathcal C^\vee\to\mathcal B^\vee\to\mathcal A^\vee
> \to\mathcal Ext^1(\mathcal C,\mathcal O_X).$$
> $\mathcal C$ locally free $\Rightarrow
> \mathcal Ext^1(\mathcal C,\mathcal O_X)=0$. Therefore
> $$0\to\mathcal C^\vee\to\mathcal B^\vee\to\mathcal A^\vee\to0.$$

The replacement preserves how to obtain the sequence. It orders the operation,
the resulting exact sequence, the vanishing reason, and the conclusion.
The Ext here is the sheaf Ext; global Ext need not vanish.

## Ban mathematical hand-waving

A card must give enough information to reconstruct the requested statement,
check an example, and judge an attempted answer. Hand-waving that conceals
this information is prohibited. Compression must preserve the mathematical
content needed for the task. Apply this rule to definitions, theorem statements,
examples, calculations, and explanations alike.

| Prohibited omission | Required replacement |
| --- | --- |
| Hidden predicates: “a suitable resolution,” “appropriate conditions,” “a nice space” | State the conditions that make the object or choice qualify. |
| Missing hypotheses: “vanishing applies,” “the usual assumptions” | State the relevant hypotheses, including the field, characteristic, regularity, properness, positivity, and Cartier conditions when needed. In an application, identify why they hold. |
| Ambiguous quantifiers: “on a resolution,” “for large multiples” | Distinguish existence from universality and one chosen model from all models. Specify thresholds, divisibility, and parameter dependence as required by the statement. |
| Unexplained genericity or size: “general position,” “sufficiently positive” | Give the incidence exclusions, parameter-space condition, or positivity requirement being used. Do not make the learner guess what the qualifier excludes. |
| Undefined conventions or objects | Identify the ambient objects, notation, sign and indexing conventions, and the domain and codomain of maps when these affect the answer. |
| Unspecified constructions: “resolve,” “perturb,” “take a quotient” | Specify the input, operation, and required output: for example, the blowup center, permitted perturbation, or group and action. |
| Circular definitions: “the good singularities,” “the resolution that works” | Give an independent criterion that decides membership in the class. |
| Labels standing in for examples: “a standard counterexample” | Identify the object and the properties that establish the claimed distinction. A separating example must satisfy one condition and fail the other. |
| Missing decisive calculations: “one checks,” “clearly,” “by a standard computation” | Supply the equality, inequality, invariant, or short argument that settles the question when that step is part of the requested task. |
| Unexplained relationships: “these are related,” “essentially equivalent” | State the implication, equivalence, isomorphism, or correspondence, its hypotheses, and any choices on which it depends. |
| References replacing answers: “see the theorem,” “as above” | Give the requested mathematical content on the card. References support the answer; they do not supply a missing definition or conclusion. |
| Unspecified remainder: “and so on,” “etc.” in a classification or recipe | State the full requested list or a precise rule that determines its remaining entries. |

These are semantic requirements, not a banned-word search. Terms such as
“general,” “canonical,” and “sufficiently large” have precise mathematical
uses. State their meaning and quantifiers when they carry the content being
tested. An existence theorem need not provide an effective numerical bound:
state the existence and dependencies of the bound instead of inventing one.

Use established terminology as vocabulary, but expand it when its definition
or its distinction from a neighboring notion is the task. For example, a dlt
definition must specify the resolution conditions and which exceptional
divisors satisfy the discrepancy inequality. Naming a resolution alone does
not supply those conditions.

This does not require adding a proof to every statement. Supply the information
needed for the question asked, retain useful authored derivations, and keep
composite cards compact through formulas, tables, and explicit examples.

## Edit existing cards by synthesis

Existing cards contain authored choices about how to recall and use mathematics.
Preserve their voice, question, notation, examples, mnemonic cues, and route
through an argument. A derivation may be the means of remembering a formula.
The priority assigned to new proof cards does not authorize removing an
existing derivation.

Integrate corrections and additions into that structure. Repair a false step,
supply a missing hypothesis, or extend an answer while keeping the useful
reasoning around it. Before accepting a rewrite, compare it with the original:
account for each removed explanation, intermediate equality, example, and
retrieval cue. Mathematical equivalence of the final answer is insufficient
if the edit loses the author's way of reaching it. Put a distinct new task in
a separate card instead of replacing an existing question with that task.
Ask before changing a sound authored approach merely to prefer another one.

Preserve useful additions as well as the original material. When an edit needs
repair, work from its current state and retain valid corrections, hypotheses,
examples, and explanations. Add the missing reasoning beside those improvements;
compare against both the original card and the expanded version.

## Require retrieval before revealing the answer

Put the question on the front and the answer on the back. Ask the learner to
produce the intended knowledge: state a definition, explain a connection, or
solve a problem. Keep the information being tested out of the prompt so answering
requires retrieval [1, 2].

Test mathematical content, not a source's theorem, proposition, or definition
number. Use the mathematical object, hypotheses, conclusion sought, or standard
name to identify the task. Source numbers may appear only as locators in the
card's `cite` attribute, separate from the answer. Remove bare source numbers;
moving an unexplained number from the front into the answer does not fix the card.
For example, replace “Thm 4.3.1 (fundamental)” with “How does the lattice
exponential $e_L(ax)$ depend on $e_L(x)$ and $a^{-1}L/L$?” Preserve the formula
and its derivation on the back. A source locator is not a mathematical recall cue.

## Practise the intended use of the knowledge

Match the question to the research task being practised. Ask for a theorem's
statement when its precise form must be available from memory. Present a
problem and ask the learner to choose and justify a method when the goal is
recognizing which result to use [3, 5].

Include application questions with different examples or assumptions. These
should require using the concept in the given case [3].

## Include conceptual retrieval where understanding is the goal

When understanding a relationship is the goal, ask the learner to explain it.
Suitable prompts include “Why is this hypothesis needed?” and “How do these
concepts differ?” Keep that relationship in the question when dividing material
into cards. Use factual questions for facts that need to be recalled [3, 5, 6].

## Provide corrective feedback

Supply the correct answer on the back so the learner can check and correct the
attempted response [1, 4]. Match it to the task: give the requested definition,
explanation, proof, or solution. For a multiple-choice question, identify the
correct alternative [4].

## Include questions that distinguish related concepts

For concepts or methods that learners must distinguish, contribute cases that
ask which applies and why. Include cases requiring different choices, so mixed
review exercises the distinction [7].

## Research references

1. Dunlosky et al. (2013). [Improving Students' Learning With Effective Learning
   Techniques](https://pubmed.ncbi.nlm.nih.gov/26173288/).
2. Agarwal, Nunes, and Blunt (2021). [Retrieval Practice Consistently Benefits
   Student Learning](https://eric.ed.gov/?id=EJ1319572).
3. Pan and Rickard (2018). [Transfer of Test-Enhanced Learning: Meta-Analytic
   Review and Synthesis](https://doi.org/10.1037/bul0000151).
4. Butler and Roediger (2008). [Feedback Enhances the Positive Effects and
   Reduces the Negative Effects of Multiple-Choice
   Testing](https://doi.org/10.3758/MC.36.3.604).
5. Agarwal (2019). [Retrieval Practice & Bloom's Taxonomy: Do Students Need Fact
   Knowledge Before Higher Order Learning?](https://eric.ed.gov/?id=EJ1205208).
6. Lin, McDaniel, and Miyatsu (2018). [Effects of Flashcards on Learning Authentic
   Materials](https://doi.org/10.1016/j.jarmac.2018.05.003).
7. Brunmair and Richter (2019). [Similarity Matters: A Meta-Analysis of Interleaved
   Learning and Its Moderators](https://pubmed.ncbi.nlm.nih.gov/31556629/).
