# 💚 Data-Driven Design Pattern

## 💛 What is it?
**Data-driven design** is a pattern where a program's behavior is controlled by **data** (tables, config, rules) instead of being hardcoded in the logic. You change what the program does by editing data, not by rewriting code.
Plain version: instead of a giant `if / elif / switch` with a branch for every case, you put the cases in a **table** and write one small piece of code that reads the table.
> Not to be confused with **data-oriented design** (see the section near the end). Same-sounding name, different goal.
## 💛 Why do we need it?
Hardcoding every case into control flow does not scale. Data-driven design buys you:
- **Add cases without touching logic.** A new case is a new row, not a new branch.
- **Less duplicated branching.** One generic engine, many data rows, instead of copy-pasted `if` blocks.
- **Non-engineers can change behavior.** Pricing rules, feature flags, and content can live in config or a spreadsheet.
- **Easier testing.** The logic has one path; you vary the data.
### 🤍 Real-world use case
A pricing service has dozens of discount rules that marketing changes weekly. Instead of shipping code every time, the rules live in a table. Marketing edits the table, the same evaluator applies them. No redeploy.
## 💛 How does it work?
You split the program into two parts:
- **The engine**: generic logic that knows how to act, but not the specifics.
- **The data**: the specifics (which cases, which values, which transitions).
The engine looks up or iterates the data and acts on it. Common shapes: dispatch tables, config-driven rules, state-transition tables, declarative validation schemas.
### 🤍 Example: dispatch table instead of a switch
Imperative, hardcoded branches:
```python
def handle(event):
    if event.type == "click":
        return on_click(event)
    elif event.type == "scroll":
        return on_scroll(event)
    elif event.type == "hover":
        return on_hover(event)
    else:
        return on_unknown(event)
```
Data-driven, the cases are a table:
```python
HANDLERS = {
    "click": on_click,
    "scroll": on_scroll,
    "hover": on_hover,
}

def handle(event):
    fn = HANDLERS.get(event.type, on_unknown)
    return fn(event)
```
Adding a new event type is now one line of data, not a new branch.
### 🤍 Example: rules as config (data, not code)
```yaml
discounts:
  - when: { plan: pro, years: 1 }
    percent: 10
  - when: { plan: pro, years: 2 }
    percent: 20
  - when: { plan: team, years: 1 }
    percent: 15
```
One evaluator reads the list and applies the first match. A new discount is a data edit that a non-engineer can make.
### 🤍 Example: a state machine as a transition table
```javascript
State     | coin      | push
--------- | --------- | ---------
locked    | unlocked  | locked
unlocked  | unlocked  | locked
```
One loop applies `(currentState, input) -> nextState` by looking it up. Adding a state or an input is a table edit, not new code.
## 💛 When it shines, when it hurts
Good fit:
- Many similar cases that share one shape.
- Cases change often, or need to change without a redeploy.
- Business users need to edit the behavior.
Bad fit (over-engineering):
- Only two or three cases. Just write the `if`. A table adds indirection for nothing.
- The "data" slowly grows conditionals, loops, and expressions until it is a second programming language you now have to maintain.
## 💛 Data-driven vs data-oriented (do not confuse)
- **Data-driven design** (this note): behavior comes from data. The goal is **flexibility**, less code churn.
- **Data-oriented design (DOD)**: organizing data in memory for CPU-cache efficiency, common in game engines and ECS. The goal is **performance**, not flexibility.
Same family of words, opposite motivations.
## 💛 Gotcha
- **Debuggability drops.** A bug in a data row is harder to trace than a bug in code, because the stack trace points at the generic engine, not the offending case. Validate your data and log which row fired.
- **Data quietly becomes code.** A simple rules table often grows into a Turing-complete DSL with its own bugs. Know when to stop and just write functions.
- **Treat the data as a source of truth.** If it lives in a DB or config file, version it and review changes like real code, because it is logic now.
- **Watch per-request cost.** A dispatch-table lookup is cheap, but evaluating a large rule set on every request can add up. Precompile or cache when it matters.
## 💛 References
- Wikipedia: Data-driven programming: https://en.wikipedia.org/wiki/Data-driven_programming
- Game Programming Patterns: Bytecode (a data-driven behavior pattern): https://gameprogrammingpatterns.com/bytecode.html
- Martin Fowler: RulesEngine: https://martinfowler.com/bliki/RulesEngine.html
