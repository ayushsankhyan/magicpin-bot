# Magicpin AI Challenge - Build Log

## Project Goal

Build an intelligent merchant assistant similar to Vera that can:

* Understand merchant context
* Understand customer context
* Understand trigger context
* Generate personalized WhatsApp messages
* Handle multi-turn conversations
* Detect auto-replies
* Detect merchant intent
* Produce highly specific, context-aware responses

Target: Maximize score across:

1. Specificity
2. Category Fit
3. Merchant Fit
4. Trigger Relevance
5. Engagement Compulsion

---

# Phase 1 - Dataset Setup

## Objective

Understand and load the challenge dataset.

### Actions

* Extracted challenge ZIP
* Identified dataset generator
* Generated synthetic dataset

Generated:

* 50 merchants
* 200 customers
* 100 triggers
* 5 categories

### Why

The challenge revolves around structured context. Before any AI logic can be built, all context sources must be accessible programmatically.

---

# Phase 2 - Project Architecture

## Folder Structure

magicpin-bot/

core/
conversation/
prompts/
tests/
data/
expanded/

### Why

Separation of concerns:

core/

* business logic

conversation/

* conversational intelligence

prompts/

* LLM instructions

tests/

* validation and debugging

expanded/

* generated challenge dataset

---

# Phase 3 - Data Loader

## Files

core/loader.py

### Functionality

Loads:

* categories
* merchants
* customers
* triggers

### Why

Provides a single access layer for all challenge entities.

Benefits:

* reusable
* testable
* easy debugging

---

# Phase 4 - Trigger Routing

## Files

core/router.py

### Functionality

Maps trigger types to conversation strategies.

Example:

research_digest → research

perf_dip → performance

festival_upcoming → festival

review_theme_emerged → review

### Why

Different triggers require different communication styles.

A research update should create curiosity.

A performance dip should create urgency.

A review issue should create awareness.

Without routing, all messages become generic.

---

# Phase 5 - Fact Extraction Engine

## Files

core/planner.py

### Functionality

Transforms raw merchant JSON into structured facts.

Example:

Merchant JSON
↓
Facts

* Merchant Name
* CTR
* Views
* Calls
* Active Offers
* Signals
* Review Themes
* Conversation History

### Why

LLMs perform better when given concise facts rather than huge JSON objects.

Benefits:

* lower token usage
* better consistency
* easier debugging
* improved personalization

---

# Phase 6 - Strategy Layer

## Files

core/planner.py

Method:

create_strategy()

### Functionality

Converts trigger type into communication strategy.

Examples:

research_digest
→ curiosity

perf_dip
→ loss aversion

review_theme_emerged
→ social proof

### Why

The challenge explicitly rewards engagement.

Compulsion mechanisms improve merchant response rates.

---

# Phase 7 - Message Composer V1

## Files

core/composer.py

### Functionality

Generates first version of merchant messages.

Inputs:

* facts
* strategy

Outputs:

* personalized message

### Why

Provides deterministic message generation before introducing LLM rewriting.

Benefits:

* predictable behavior
* easier testing
* clear evaluation baseline

---

# Current Status

Completed:

✓ Dataset generation

✓ Loader

✓ Trigger Router

✓ Fact Extraction

✓ Strategy Layer

✓ Composer V1

In Progress:

□ Intent Detection

□ Auto Reply Detection

□ Dynamic Trigger Handling

□ GPT Rewrite Layer

□ Conversation Memory

□ Submission Generator

□ Evaluation Harness

---

# Lessons Learned

1. Structured reasoning outperforms prompt-only approaches.

2. Merchant history is a valuable personalization signal.

3. Review themes provide high-engagement opportunities.

4. Trigger-specific strategies are essential for scoring well.

5. The challenge rewards product thinking more than machine learning.

# Phase 8 - Auto Reply Detection

File:
conversation/auto_reply.py

Purpose:
Detect merchant WhatsApp business auto responses.

Why:
Challenge explicitly identifies auto-reply pollution as a major weakness.

Benefits:

- fewer wasted turns
- better replay performance
- improved merchant experience

---

# Phase 9 - Intent Detection

File:
conversation/intent.py

Purpose:
Detect explicit merchant actions.

Examples:

- I want to join
- Go ahead
- Proceed

Why:
Challenge explicitly states Vera often fails intent handoff.

Benefits:

- immediate onboarding flow
- better conversion
- better replay scores
# Phase 11 - Conversation Intelligence

Files:

* conversation/state.py
* conversation/topic_extractor.py

Purpose:

Convert conversation history into reusable merchant memory.

Features:

* Topic tracking
* Repetition avoidance
* Interest detection
* Conversation continuity

Example:

Merchant:
"Focus on whitening and aligners"

Stored Memory:

["whitening", "aligners"]

Future Benefit:

Messages can reference previous interests instead of repeating generic recommendations.

Why:

Replay tests reward continuity and punish repetitive interactions.

Expected Impact:

* Higher engagement
* Better personalization
* Improved replay performance

Dataset
│
├── Categories
├── Merchants
├── Customers
└── Triggers
        │
        ▼
Loader
        │
        ▼
Planner
        │
        ├── Fact Extraction
        └── Strategy Generation
        │
        ▼
Conversation Layer
        │
        ├── Intent Detection
        ├── Auto Reply Detection
        ├── Topic Extraction
        └── Conversation Memory
        │
        ▼
Composer
        │
        ▼
Final Message
# Phase 12 - Context-Aware Message Planning

Files:

* core/planner.py
* core/composer.py

Purpose:

Generate messages using structured merchant intelligence rather than raw JSON.

Process:

Merchant Data
↓
Fact Extraction
↓
Strategy Selection
↓
Message Composition

Extracted Signals:

* CTR
* Views
* Calls
* Leads
* Active Offers
* Review Themes
* Merchant Signals
* Conversation History

Examples:

Signal:

stale_posts:22d

Action:

Suggest fresh content creation.

Signal:

ctr_below_peer_median

Action:

Suggest profile optimization.

Signal:

high_risk_adult_cohort

Action:

Suggest recall or preventive care campaigns.

Why:

Raw JSON contains too much noise.

By extracting only meaningful facts, the system becomes:

* More explainable
* Easier to debug
* More consistent
* More personalized

Expected Impact:

* Higher specificity
* Better merchant fit
* Better trigger relevance
# Phase 13 - Merchant Health Scoring

Files:

* core/health_score.py

Purpose:

Convert multiple merchant signals into a single interpretable business health metric.

Inputs:

* CTR signals
* Engagement signals
* Review sentiment
* Content freshness

Outputs:

Health Score (0–100)

Example:

100
↓
-15 CTR below peer median
-10 stale posts
+5 recent engagement
+3 positive reviews
-3 negative reviews

Final Score:
80

Why:

Individual signals are difficult to prioritize.

A unified score helps:

* prioritize recommendations
* simplify communication
* increase message specificity

Expected Impact:

* Better merchant personalization
* Stronger performance recommendations
* Higher specificity scores

# Phase 14 - Trigger Intelligence Layer

Files:

* core/handlers/performance.py
* core/handlers/research.py
* core/handlers/review.py

Purpose:

Convert trigger events into actionable business recommendations.

Approach:

Trigger
↓
Handler
↓
Business Insight
↓
Recommendation
↓
Message

Examples:

Performance Trigger:

Signal:
ctr_below_peer_median

Recommendation:
Improve profile conversion.

Research Trigger:

Signal:
new industry finding

Recommendation:
Provide concise research summary.

Review Trigger:

Signal:
negative review trend

Recommendation:
Address recurring customer concern.

Why:

Triggers alone are not useful.

Merchants need actionable recommendations.

Expected Impact:

* Better trigger relevance
* Higher engagement
* Stronger merchant fit
