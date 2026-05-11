# ══════════════════════════════════════════════════════════════════
# 文本取证 · Text Forensics Suite — DEMO / TEST DATA
# ══════════════════════════════════════════════════════════════════
# How to use:
#   Tab 01 (Authorship Attribution): Use AUTHOR_A_SAMPLE_* and AUTHOR_B_SAMPLE_*
#           to build profiles, then test with UNKNOWN_TEXT_*
#   Tab 02 (Same Author Detection):  Compare pairs from the SAME_AUTHOR_ section
#   Tab 03 (Tampering Detection):    Use TAMPERED_TEXT or CLEAN_TEXT
#   Tab 04 (AI Detection):           Use AI_GENERATED_* and HUMAN_WRITTEN_*
#   Tab 05 (Style Imitation):        Use any long sample as the source text
# ══════════════════════════════════════════════════════════════════


# ──────────────────────────────────────────────────────────────────
# TAB 01 & 02 — AUTHORSHIP ATTRIBUTION & SAME AUTHOR DETECTION
#
# Author A: "Alex" — academic, long sentences, formal vocabulary
# Author B: "Jordan" — casual blogger, short punchy sentences, colloquial
# Author C: "Morgan" — journalist, moderate style, factual
# ──────────────────────────────────────────────────────────────────

AUTHOR_A_SAMPLE_1 = """
The fundamental paradox of modern epistemology lies in its insistence upon the primacy
of empirical verification while simultaneously acknowledging the theoretical underpinnings
that necessarily precede any act of observation. When philosophers of science speak of
the theory-ladenness of perception, they invoke a tradition stretching from Kant through
Kuhn, one in which the naked eye is never truly naked, but always already mediated by
the conceptual apparatus the observer brings to the encounter with the world.

Consider, for instance, the celebrated case of the Müller-Lyer illusion, wherein two
line segments of identical length appear to differ owing to the orientation of arrow-like
fins appended at their termini. This perceptual phenomenon demonstrates, in microcosm,
the degree to which sensory data is actively processed and interpreted rather than
passively received. The implications for scientific methodology are profound and
far-reaching, touching as they do upon questions of measurement, instrumentation,
and the very nature of objective knowledge.

Furthermore, the proliferation of competing theoretical frameworks within any given
scientific discipline at any given historical moment suggests that the relationship
between observation and theory is irreducibly complex. Researchers trained in different
paradigms will, quite literally, see different things when confronted with the same
experimental apparatus. This is not merely a sociological observation about scientific
communities but a claim about the phenomenology of scientific experience itself.
"""

AUTHOR_A_SAMPLE_2 = """
In the long history of philosophical inquiry into the nature of consciousness, few
problems have proven as intractable as the so-called hard problem: namely, the question
of how subjective experience arises from physical processes. The explanatory gap between
neural firing patterns and the felt quality of, say, the redness of red or the painfulness
of pain has resisted all attempts at reduction, whether functionalist, eliminativist,
or otherwise.

David Chalmers, who coined the term in its current usage, distinguished sharply between
the easy problems of consciousness — those concerning the functional and behavioral
correlates of mental states — and the hard problem, which concerns phenomenal experience
as such. Even a complete functional account of how the brain processes color information,
he argued, would leave entirely untouched the question of why such processing is
accompanied by any experience at all. It is this irreducibility that marks the hard
problem as genuinely hard rather than merely difficult.

The philosophical consequences of taking this problem seriously are considerable.
If phenomenal consciousness cannot be fully captured by any physical description, however
detailed, then some form of dualism appears unavoidable, whether property dualism of the
sort Chalmers endorses or some more radical substance dualism. Alternatively, one might
embrace panpsychism — the view that experiential properties are ubiquitous in nature —
as a way of grounding phenomenal facts in the physical world without reduction.
"""

AUTHOR_B_SAMPLE_1 = """
OK so I tried making sourdough again last weekend and honestly? Total disaster. The
starter looked fine, smelled great, all bubbly and alive the way it's supposed to be.
But then I forgot to add the salt. WHO FORGETS THE SALT. Me, apparently.

The bread came out weirdly dense and kind of sweet? Like eating a very expensive
hockey puck. My roommate tried a slice and just sort of nodded politely which is
the worst possible response. Polite nodding means it's bad. If it were good she'd
have said something.

I've been at this for three months now. Three months! I've watched approximately
nine hundred YouTube videos. I have a notebook full of hydration percentages and
fold schedules. I own a Dutch oven specifically for this purpose. And yet. The bread
refuses to cooperate.

Next attempt: I'm setting a phone alarm for the salt. Multiple alarms. I'm also
going to try a lower hydration dough because maybe I've been getting too ambitious
too fast. The scoring still looks cool at least. That part I've got down. The bread
looks beautiful going into the oven. It just tastes like sadness coming out.
"""

AUTHOR_B_SAMPLE_2 = """
Hot take: open plan offices are the worst invention of the past thirty years and
whoever decided that "collaboration" meant "remove all walls and force everyone to
hear each other chew" should answer for their crimes.

I've worked in three different open plan offices now. Same story every time. You
get there early hoping to beat the crowd. You put on headphones. Someone inevitably
taps you on the shoulder anyway. You take the headphones off. They just wanted to
ask if you'd seen so-and-so. You have not seen so-and-so. The headphones go back on.
This repeats six to eight times before lunch.

Studies keep coming out saying this layout tanks productivity. Nobody who actually
works in one is surprised by this. The surprise would be if somehow the noise and
constant interruption turned out to be fine.

The irony is that the actual collaboration — the important kind, the kind where you
sit down with someone and work through a real problem — doesn't happen in the open
plan. It happens in the small conference room that everyone books weeks in advance
because there are only two of them for sixty people. The open plan produces the
illusion of collaboration while making actual collaboration harder. Cool design, though.
"""

AUTHOR_C_SAMPLE_1 = """
Scientists at the University of Copenhagen announced Tuesday that they have developed
a new technique for measuring microplastic concentrations in Arctic sea ice, providing
what researchers describe as the most detailed picture yet of plastic pollution in
one of the world's most remote ecosystems.

The method, which combines infrared spectroscopy with machine learning algorithms,
can identify particles as small as 10 micrometers — roughly one-tenth the width of a
human hair. Previous techniques struggled to detect particles below 50 micrometers,
meaning a significant fraction of microplastic contamination went unmeasured.

The research team analyzed ice cores collected from twelve sites across the Arctic
during three separate expeditions between 2019 and 2022. They found microplastic
concentrations ranging from 14 to 71 particles per liter of melted ice, with higher
concentrations observed near major shipping lanes.

"What surprised us most was the variety of polymer types," said lead researcher
Dr. Emma Lindqvist. "We expected to find mostly polyethylene and polypropylene from
packaging. But we found significant quantities of nylon and polyester fibers that
appear to come from textiles — washing clothes, essentially."
"""

AUTHOR_C_SAMPLE_2 = """
The city council voted 7-2 on Monday to approve a $340 million expansion of the
downtown light rail network, extending service to three neighborhoods that have
lacked direct transit connections to the city center for decades.

Construction is expected to begin in spring next year, pending final environmental
review, and the new lines are projected to carry approximately 18,000 additional
daily riders when they open in 2027. The project will add 11.4 kilometers of track
and seven new stations.

The two dissenting votes came from council members representing districts on the
western edge of the city, who argued that the expansion prioritized density over
geographic equity. "We have neighborhoods that have been waiting twenty years for
basic bus service improvements," said council member Patricia Huang. "Before we build
a showcase project downtown, we should be asking whether the fundamentals are right."

Supporters countered that the rail expansion would reduce car traffic on several
major corridors and lower emissions by an estimated 12,000 tonnes of CO2 annually.
The project received partial federal funding through the infrastructure package
passed by Congress two years ago.
"""

# ── Unknown texts to attribute ──
UNKNOWN_TEXT_1_IS_AUTHOR_A = """
The question of whether artificial intelligence systems can be said to possess genuine
understanding — as opposed to the mere simulation of understanding — constitutes one of
the most pressing philosophical debates of the contemporary moment. John Searle's famous
Chinese Room argument, first articulated in 1980, remains the locus classicus for
skeptical positions on machine cognition. The argument, in brief, holds that syntactic
manipulation of symbols, however sophisticated, can never give rise to semantic content
of the kind we associate with genuine comprehension.

Critics of Searle's position have developed numerous responses over the intervening
decades, many of which invoke the systems reply: the claim that understanding may be
a property of the system as a whole rather than of any individual component. On this
view, the person in the Chinese Room does not understand Chinese, but the room system
does. Searle's rejoinder — that internalizing the entire system still does not produce
understanding — strikes many philosophers as question-begging, though the debate
has not been definitively resolved.

The implications for contemporary AI development are significant. If large language
models are engaging in something meaningfully analogous to understanding, then the
ethical stakes of how they are developed and deployed increase substantially.
"""

UNKNOWN_TEXT_2_IS_AUTHOR_B = """
I've been trying to get into running for literally years. Every January I download a
couch-to-5k app and every March I've quietly deleted it and moved on with my life.
This year is somehow different? Or at least different so far.

The thing that changed: I stopped trying to run in the mornings. Everyone says morning
running is the move. You feel great all day, they say. You'll have more energy, they say.
What they don't mention is that some people are not morning people and attempting vigorous
physical activity before 8am produces results that are less "energized athlete" and more
"sad zombie who has made poor choices."

Evening runs turned out to be the answer. Twenty minutes after dinner, nothing too intense.
The neighborhood is quiet, the light is good, there's a podcast playing. It's almost
enjoyable? I've done it eleven days in a row which is eleven more than my previous record.

I'm not going to say I love running now. That would be lying. But I no longer hate it
as much as I did which is a significant development.
"""

UNKNOWN_TEXT_3_IS_AUTHOR_C = """
Electric vehicle sales in Europe reached a record 2.3 million units in the first half
of the year, according to data released by the European Automobile Manufacturers
Association, representing a 24 percent increase over the same period last year.

Norway continued to lead the continent in EV adoption, with battery electric vehicles
accounting for 89 percent of all new car sales. The Netherlands, Sweden, and Denmark
also posted adoption rates above 50 percent. Germany, Europe's largest auto market,
saw EV share rise to 28 percent, up from 21 percent a year ago.

Analysts attributed the growth partly to expanded model availability across price
points and partly to government incentives in several countries. The European Union's
2035 deadline for ending sales of new combustion engine vehicles has prompted
manufacturers to accelerate electrification timelines.

Charging infrastructure has lagged vehicle growth in some markets, however. Consumer
surveys cited range anxiety and charging access as the leading barriers to adoption
among non-EV owners.
"""


# ──────────────────────────────────────────────────────────────────
# TAB 03 — TAMPERING DETECTION
# ──────────────────────────────────────────────────────────────────

CLEAN_TEXT = """
The James Webb Space Telescope has fundamentally altered our understanding of the
early universe. Launched on December 25, 2021, the observatory reached its operational
orbit around the second Lagrange point roughly six months later, after a tense
deployment sequence that engineers had long described as "thirty days of terror."

The telescope's first deep field image, released in July 2022, showed thousands of
galaxies in a patch of sky smaller than a grain of sand held at arm's length. Among
them were objects more than 13 billion years old — meaning we observe them as they
appeared less than a billion years after the Big Bang.

Since then, Webb has challenged several predictions about early galaxy formation.
Astronomers expected to find only small, irregular proto-galaxies at those distances.
Instead, the telescope has detected multiple large, well-formed galaxies that appear
to have assembled remarkably quickly after the universe began. Explaining how these
structures formed so fast has become one of the field's central open questions.

Beyond cosmology, Webb has examined the atmospheres of exoplanets in unprecedented
detail. Data from the TRAPPIST-1 system, home to seven roughly Earth-sized planets,
has shown that at least some of these worlds retain atmospheres, though the
composition and habitability remain under investigation.
"""

TAMPERED_TEXT = """
The James Webb Space Telescope has fundamentally altered our understanding of the
early universe. Launched on December 25, 2021, the observatory reached its operational
orbit around the second Lagrange point roughly six months later, after a tense
deployment sequence that engineers had long described as "thirty days of terror."

The telescope's first deep field image, released in July 2022, showed thousands of
galaxies in a patch of sky smaller than a grain of sand held at arm's length. Among
them were objects more than 13 billion years old — meaning we observe them as they
appeared less than a billion years after the Big Bang.

yo bro just buy bitcoin and stonks lmao gains only up up up to the moon 🚀🚀 get
rich fast dont listen to the haters they dont know nothing about passive income
streams and financial freedom mindset is everything grindset 24/7 hustle culture
never sleeps invest in yourself first then crypto then real estate easy money

Beyond cosmology, Webb has examined the atmospheres of exoplanets in unprecedented
detail. Data from the TRAPPIST-1 system, home to seven roughly Earth-sized planets,
has shown that at least some of these worlds retain atmospheres, though the
composition and habitability remain under investigation.
"""

ENCODING_ANOMALY_TEXT = """
This document appears normal at first glance but contains hidden anomalies.
The following sentence has zero-width characters inserted between words.
Some\u200bwords\u200bhave\u200binvisible\u200bcharacters\u200binside\u200bthem.
This can be used to watermark text or evade detection systems.
The text continues normally here and looks completely clean to the naked eye.
Another technique involves using visually similar Unicode characters.
For example, the letter \u0430 (Cyrillic a) looks identical to Latin a.
These substitutions \u0441an be used to \u0435vade keyword filters.
Forensic tools must check for such encoding-level manipulations carefully.
"""


# ──────────────────────────────────────────────────────────────────
# TAB 04 — AI DETECTION
# ──────────────────────────────────────────────────────────────────

AI_GENERATED_TEXT = """
Artificial intelligence has fundamentally transformed the landscape of modern technology,
revolutionizing industries and reshaping the way we interact with the world around us.
In today's rapidly evolving digital era, it is crucial to understand the far-reaching
implications of these technological advancements.

Furthermore, the integration of machine learning algorithms into various sectors has
demonstrated remarkable potential for enhancing productivity and efficiency. It is worth
noting that these developments have not occurred in isolation; rather, they represent
the culmination of decades of pioneering research and innovation.

Moreover, the ethical considerations surrounding artificial intelligence are of paramount
importance. As we delve into the complexities of algorithmic decision-making, it becomes
increasingly essential to ensure that these systems operate within a robust framework of
accountability and transparency.

In conclusion, the transformative impact of artificial intelligence on society cannot be
overstated. From healthcare to finance, education to transportation, the comprehensive
integration of AI technologies is reshaping fundamental aspects of human experience.
Ultimately, navigating this technological landscape requires a nuanced understanding of
both the opportunities and the challenges that lie ahead. By fostering collaboration
between stakeholders and maintaining a commitment to ethical principles, we can unlock
the full potential of artificial intelligence while mitigating potential risks.
"""

HUMAN_WRITTEN_TEXT = """
I've been thinking about AI a lot lately, mostly because I keep using it and feeling
weird about it afterward. Like, I'll ask ChatGPT to help me draft an email and it'll
produce something perfectly competent and I'll think — okay, but now what did I
actually do today?

It's not that the output is bad. It's usually fine. It's that the process of getting
there felt hollow in a way I'm struggling to articulate. There's something that happens
when you wrestle with a sentence for twenty minutes, delete it, try again from a different
angle, and eventually land somewhere you didn't expect. The AI skips all that. Which is
the point, I guess. But "efficient" and "good" aren't always the same thing.

My friend who works in design says she's stopped using the generative image tools
because clients started treating her entire job as basically a prompt-writing exercise.
"I spent eight years learning to see," she told me. "That's not prompt engineering."

I don't think AI is going anywhere. I also don't think everyone voicing concerns
about it is a Luddite. Somewhere between "this will solve everything" and "this will
ruin everything" there's probably the actual answer, which is more boring and more
complicated and will take years to sort out.
"""

BORDERLINE_TEXT = """
Climate change presents one of the most significant challenges facing humanity today.
The scientific consensus is clear: global temperatures are rising, and human activity
is the primary driver. Rising sea levels threaten coastal communities worldwide.

Scientists have documented these changes extensively over recent decades. The data
shows accelerating ice loss in Greenland and Antarctica, more frequent extreme weather
events, and disruptions to ecosystems that took millennia to develop.

Some argue that technological solutions will emerge in time. Carbon capture, renewable
energy, and nuclear power are frequently cited possibilities. Others maintain that
systemic economic changes are also necessary, not just technological ones.

The debate continues about the most effective policy responses, but the underlying
physical reality is well established. Communities are already adapting to changes
that are locked in regardless of future emissions reductions.
"""


# ──────────────────────────────────────────────────────────────────
# TAB 05 — STYLE IMITATION SOURCE TEXTS
# ──────────────────────────────────────────────────────────────────

STYLE_SOURCE_HEMINGWAY = """
The old man fished alone in a skiff in the Gulf Stream. He had gone eighty-four days
now without taking a fish. The boy had been with him for the first forty days but
after forty days without a fish his parents had told him the old man was definitely
and finally salao, which is the worst form of unlucky, and the boy had gone at their
orders to another boat which caught three good fish the first week.

It made the boy sad to see the old man come in each day with his skiff empty. He
always went down to help him carry the coiled lines, the gaff and harpoon, and the
sail that was furled around the mast. The sail was patched with flour sacks and, furled,
it looked like the flag of permanent defeat.

The old man was thin and gaunt with deep wrinkles in the back of his neck. The brown
blotches of the benevolent skin cancer the sun brought from its reflection on the tropic
sea were on his cheeks. Everything about him was old except his eyes and they were the
same color as the sea and were cheerful and undefeated.
"""

STYLE_SOURCE_AUSTEN = """
It is a truth universally acknowledged, that a single man in possession of a good
fortune, must be in want of a wife. However little known the feelings or views of such
a man may be on his first entering a neighbourhood, this truth is so well fixed in the
minds of the surrounding families, that he is considered as the rightful property of
some one or other of their daughters.

"My dear Mr. Bennet," said his lady to him one day, "have you heard that Netherfield
Park is let at last?" Mr. Bennet replied that he had not. "But it is," returned she;
"for Mrs. Long has just been here, and she told me all about it." Mr. Bennet made no
answer. "Do you not want to know who has taken it?" cried his wife impatiently.
"You want to tell me, and I have no objection to hearing it."

This was invitation enough. "Why, my dear, you must know, Mrs. Long says that
Netherfield is taken by a young man of large fortune from the north of England. That
he came down on Monday in a chaise and four to see the place, and was so much delighted
with it, that he agreed with Mr. Morris immediately; that he is to take possession before
Michaelmas, and some of his servants are to be in the house by the end of next week."
"""

STYLE_SOURCE_TECHNICAL = """
The system architecture consists of three primary layers: the data ingestion layer,
the processing layer, and the presentation layer. Each layer is independently scalable
and communicates via a well-defined API contract, ensuring loose coupling between
components.

The data ingestion layer handles incoming event streams from multiple source systems.
Messages are normalized into a canonical schema and placed onto a Kafka topic for
downstream consumption. The layer implements exactly-once delivery semantics using
idempotency keys, which prevents duplicate records from propagating into the system.

The processing layer consumes from Kafka and applies a series of stateless
transformations defined as pure functions. Results are materialized into a PostgreSQL
database with appropriate indexing to support the query patterns required by the
presentation layer. Connection pooling is handled by PgBouncer, which sits between
the application servers and the database.

The presentation layer exposes a REST API backed by a read replica of the PostgreSQL
cluster. Response caching is handled at the CDN level for high-traffic endpoints,
with a TTL of 60 seconds for most resources. Authentication uses JWT tokens with
RSA-256 signing, validated on every request at the API gateway before traffic reaches
application servers.
"""


# ──────────────────────────────────────────────────────────────────
# QUICK REFERENCE — copy-paste guide
# ──────────────────────────────────────────────────────────────────
USAGE_GUIDE = """
QUICK COPY-PASTE GUIDE
======================

TAB 01 — Authorship Attribution
  Step 1: Add author name "Alex"   → paste AUTHOR_A_SAMPLE_1 → Build Profile
          Add author name "Alex"   → paste AUTHOR_A_SAMPLE_2 → Build Profile  (same author, appends)
          Add author name "Jordan" → paste AUTHOR_B_SAMPLE_1 → Build Profile
          Add author name "Jordan" → paste AUTHOR_B_SAMPLE_2 → Build Profile
          Add author name "Morgan" → paste AUTHOR_C_SAMPLE_1 → Build Profile
  Step 2: Paste UNKNOWN_TEXT_1_IS_AUTHOR_A → Analyze Authorship  (expect: Alex)
          Paste UNKNOWN_TEXT_2_IS_AUTHOR_B → Analyze Authorship  (expect: Jordan)
          Paste UNKNOWN_TEXT_3_IS_AUTHOR_C → Analyze Authorship  (expect: Morgan)

TAB 02 — Same Author Detection
  SAME author test:   Text A = AUTHOR_A_SAMPLE_1,  Text B = AUTHOR_A_SAMPLE_2  → expect high similarity
  DIFF author test:   Text A = AUTHOR_A_SAMPLE_1,  Text B = AUTHOR_B_SAMPLE_1  → expect low similarity

TAB 03 — Tampering Detection
  Clean text:    paste CLEAN_TEXT       → low risk score, no anomalies
  Tampered text: paste TAMPERED_TEXT    → high risk, style break detected in middle paragraph
  Encoding:      paste ENCODING_ANOMALY_TEXT → zero-width & Cyrillic substitution flags

TAB 04 — AI Detection
  Likely AI:     paste AI_GENERATED_TEXT   → high AI score (many signals)
  Likely human:  paste HUMAN_WRITTEN_TEXT  → low AI score
  Borderline:    paste BORDERLINE_TEXT     → medium/uncertain score

TAB 05 — Style Imitation
  Hemingway style:  paste STYLE_SOURCE_HEMINGWAY  → short declarative sentences
  Austen style:     paste STYLE_SOURCE_AUSTEN     → longer, nested, ironic
  Technical style:  paste STYLE_SOURCE_TECHNICAL  → dense, precise, formal
"""
