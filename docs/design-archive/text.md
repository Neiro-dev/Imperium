# Game text and naming

This section covers how Imperium's game text is written: where its wording comes from, who speaks in it and in what
tone, what each kind of text holds and leaves out, how descriptions are built, the words it keeps out, how mechanoids,
their weapons, officials, equipment and research are named, how the Chinese and English versions relate, what the
interface says and where, the sample texts, the rewrite of in-game text, and the mod's description. The names
themselves, in force and replaced, are in [terms.md](terms.md); the mechanoids are in [mechanoids.md](mechanoids.md),
the officials and promotion in [empire.md](empire.md), orders and claims in [orders.md](orders.md), techprints and the
research labels in [ruins-and-technology.md](ruins-and-technology.md), the imperial area in
[administration.md](administration.md), and Mantle, which the description does not advertise, in [mantle.md](mantle.md).

## Where the wording comes from

Game text is the text in Defs, in the Keyed files, in letters and in the interface (`.claude/rules/game-text.md` L14). Apart from protected terms it
follows the writing of the base game and the expansions, so similar text in the game's own Defs and Keyed files is
looked up first; this, and the order of terms below, is the maintainer's ruling on game content (`.claude/rules/game-text.md` L12-18).

Where the base game has a word, Imperium's labels, descriptions and interface use it, in English and in the official
Simplified Chinese as the base game uses them in the same kind of place; only Imperium's own things and its own design
ideas get new words, and this is a principle of the whole project, for the Empire, the mechanoids, city building and the
ruins alike (`Imperium-Knowledge/01_项目宪章与规范索引.md` L198, R-1104-0112a; `Imperium-Knowledge/现行/流程/设计会话工作规矩.md` L120;
`Imperium-Knowledge/现行/索引.md` L859; `Imperium-Knowledge/designs/做法史/审核与派活.md` L92). What players are to recognise rests
on the unit itself, its look, projectile, action and the effects the base game already has, and Imperium adds no hint,
marker, icon or text that the base game lacks (`Imperium-Knowledge/现行/流程/设计会话工作规矩.md` L120, R-1104-2104;
`Imperium-Knowledge/现行/索引.md` L876).

Terms are taken in this order: the English of the base game and the expansions; then names the maintainer has ruled;
then, for real-world history, the most common name in reliable English sources (`.claude/rules/game-text.md` L30-31). Any other new term is a question about
game content (`.claude/rules/game-text.md` L30-32). Game text uses the game's own terms, such as colonist, raid and caravan, and makes up no
abbreviation the game itself does not use (`.claude/rules/game-text.md` L26); so it says mechanoid, not mech (`Imperium-Knowledge/01_项目宪章与规范索引.md` L198; `Imperium-Knowledge/08_机械体设计.md` L327,
R-1104-0112).

The glossary lists the terms in force, each with its meaning, its source and, where there is one, the key that holds its
text: the decided terms, the base-game terms that the design uses or that the game-text rule names as the game's terms
to use, and the historical names the design uses (`.claude/rules/game-text.md` L36-39). A term's translation into any
language is held under the same key, in the mod's `Languages/` folder or in the base game's own translation
(`docs/glossary.md` L3-5). Decided terms, that is names the maintainer has ruled and names of Imperium's own things, are
kept word for word; when one changes, or the thing it names is withdrawn, and the name has appeared in the mod's files,
in this repository or in the old mod `Neiro-dev/RimWorld-Imperium`, the deprecated-terms data records it with its new
term, with `a new name is pending` while that is open, or with `removed` (`CONTRIBUTING.md` L103-109).
[terms.md](terms.md) gives both lists.

Imperium adjusts only the content it adds: the native Gizmos, right-click menus, Inspect panels, quest interface,
tooltips, names and logic of the base game and the expansions are its references, and it does not hide, replace or
retranslate them for a uniform style (`Imperium-Knowledge/10_文本命名与界面规范.md` L92).

## Labels

Labels are lowercase, and abbreviations and proper names keep their capitals (`.claude/rules/game-text.md` L20-21). Labels of the Def types that the game
writes as titles or in sentence case follow the game's labels of that type, letter labels start with a capital letter,
and descriptions are complete sentences (`.claude/rules/game-text.md` L20-25).

> [!NOTE]
> **Base game**: the rule takes its examples from the game's own labels: `shattered empire` and `jump pack` in
> lowercase, `EMP grenade` and `Gauranlen tree` with their capitals, the scenario `Lost Tribe` and the letter label
> `Shamblers approach`, to be checked against `Data/` (`.claude/rules/game-text.md` L20-24).

English mechanoid names are singular (`Imperium-Knowledge/designs/做法史/哨骑.md` L20, R-1103-1213c, in part replaced by
R-1105-1827a, R-1105-1827b and R-1105-1918 for the names psilos, alarius and limitaneus;
`Imperium-Knowledge/08_机械体设计.md` L181). Imperium's own buildings and items keep the rule too: the glossary writes the
imperial insignia and the imperial codicil in lowercase (`docs/glossary.md` L56-57), which settles the question the text
audit had left to the maintainer, whether such labels follow the base game's lowercase (replaces
`Imperium-Knowledge/designs/待用/文本盘点-2026-10-27.md` L569; `Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L49). The
label of a techprint is `techprint: X`, with X the label of the technology it authorizes, in Chinese `科技图纸：X`; the one
prefix lets techprints sort together and be found easily (`docs/glossary.md` L72; `.github/deprecated-terms.json`
L468-477; `Imperium-Knowledge/04_蓝图与科研授权.md` L23; `Imperium-Knowledge/10_文本命名与界面规范.md` L54) (replaces the capitalised
`Techprint: <name>` of `Imperium-Knowledge/10_文本命名与界面规范.md` L54). The colony's rank is shown as rank II and so on, in
the Chinese interface as 帝国等级 II (`docs/glossary.md` L67; `Imperium-Knowledge/10_文本命名与界面规范.md` L51;
`Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L35) (replaces the capitalised "Rank II" of
`Imperium-Knowledge/10_文本命名与界面规范.md` L51). Outpost, settlement, town, city and regional capital name a colony's rank
only in narrative text and never as a label (`docs/glossary.md` L65; `Imperium-Knowledge/03_Rank与政治权限.md` L84-92;
`Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L91).

## Who speaks, and in what tone

Imperium's narration takes from RimWorld and its expansions the attitude they take toward comparable things: who is
speaking, why the thing exists and what facts the player needs (`Imperium-Knowledge/10_文本命名与界面规范.md` L8). It keeps no ratio of base-game and imperial flavour and
puts no bureaucratic word into every sentence (`Imperium-Knowledge/10_文本命名与界面规范.md` L6-8). Content sets the tone: the Empire shows through objects,
actions, reliable settlement and the consequences of authority, not through praise; a player who ignores politics can
still play; and unknown history, hidden motives and guesses about people are not written as if known for certain
(`Imperium-Knowledge/10_文本命名与界面规范.md` L10).

Each narrating subject has its own duty and its own manner of expression (`Imperium-Knowledge/10_文本命名与界面规范.md` L12-13).
The system, the narrator and the interface (系统/旁白/UI) state what is currently known, the actions and their results,
plainly, naturally and with restraint, and does not write every prompt as an official document
(`Imperium-Knowledge/10_文本命名与界面规范.md` L14). World characters (世界人物) speak of their occupation, situation, interests and
personality; position, personality and political stance do not map one to one, and in a letter a character may have a
short personal tone that changes no result (`Imperium-Knowledge/10_文本命名与界面规范.md` L15). Formal institutions (正式机构) speak
of authority, procedure, approval and refusal, delivery and settlement: the result first, then the necessary reason and
the next step, with moderate gravity (`Imperium-Knowledge/10_文本命名与界面规范.md` L16).

The narrator of in-game text is a neutral game narrator with a plain, encyclopaedic voice, and the Empire's character
shows through facts stated plainly; quests and letters take the client as their subject, saying who it is, what it
wants, what it offers and what the player is to do, and a backstory has one or two sentences (`Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L56).

Narration addresses the player as you or your colony (你／你的殖民地), or leaves the subject out, and does not
generally use 贵殖民地; formal notices may use the colony's real name, "this settlement" (该定居点) or, where needed,
"your side" (你方) (`Imperium-Knowledge/10_文本命名与界面规范.md` L72; `Imperium-Knowledge/designs/待用/文本盘点-2026-10-27.md` L596). Archaic and pseudo-religious tones such as 朕, 尔等, 圣谕, 卑民 and 荣光
are not overused (`Imperium-Knowledge/10_文本命名与界面规范.md` L72).

Three sample lines show the tone and prove no mechanism: "The contact signal has been sent. No reply from the Empire
has been received yet."; "The application is not approved. This exceeds the current authorization."; and "This number
was struck from the register long ago... at least the register we can currently find says so." (`Imperium-Knowledge/10_文本命名与界面规范.md` L98-106).

## What each kind of text holds

Each kind of text has information it keeps and things it avoids (`Imperium-Knowledge/10_文本命名与界面规范.md` L20-31):

- Items, machines and resources: construction, use, inputs and real limits, with a short origin where it helps;
  machine descriptions follow the way the base game describes machines such as the Militor, in Imperium's own design
  language; they leave out that the Empire is the strongest, maintenance or combat abilities the thing does not have,
  and any tactics tutorial, formation advice or statement of role; the player judges the use (`Imperium-Knowledge/10_文本命名与界面规范.md` L22).
- Buildings: function, real working conditions, what they operate on and necessary limits, but no dead ruin presented
  as repairable or usable at once, and no invented interaction (`Imperium-Knowledge/10_文本命名与界面规范.md` L23).
- Research and techprints: what is actually opened, and the difference between authorization, research and
  manufacture, but not that being authorized means having it built, no hidden added research and no ancient thing that
  is advanced because it is ancient (`Imperium-Knowledge/10_文本命名与界面规范.md` L24).
- An order's quote: the target, the frozen reward, the deadline and a separate acceptance state, with no risk rating,
  recommended gear, enemy strength, internal probability or hidden leaning (`Imperium-Knowledge/10_文本命名与界面规范.md` L25); the quote states the reward
  including any techprint that comes with it (`Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L68; `Imperium-Knowledge/designs/待用/文本盘点-2026-10-27.md` L57, L441; `Imperium-Knowledge/designs/RankI-设计核对-2026-10-29.md` L323).
- An accepted quest: the current physical objective, the legal actions, the deadline and the delivery conditions, with
  no repetition of the whole quote, no mechanical tutorial and no explanation of court intrigue (`Imperium-Knowledge/10_文本命名与界面规范.md` L26).
- Claims and ruins: limited records, the target as far as it is known, the real recovery and its consequences, with no
  all-knowing archaeological record and no excavation treated as a political test (`Imperium-Knowledge/10_文本命名与界面规范.md` L27).
- Events and letters: what is happening or has happened and the response it needs, announcing no arrival of people,
  payment of a reward or clearing of enemies in advance (`Imperium-Knowledge/10_文本命名与界面规范.md` L28).
- Dialogue: clear consequences of each option and differences between characters; the player does not have to read
  political hints to choose correctly (`Imperium-Knowledge/10_文本命名与界面规范.md` L29).
- Formal notices: the outcome, the necessary reason and the next step, without pointless regulation, flattery or
  deliberate contempt (`Imperium-Knowledge/10_文本命名与界面规范.md` L30).
- Edicts (敕令), great campaigns (大战役) and rebuilding (重建): rare and solemn, stating real duties and results, with
  no wording standing in for armies, logistics or engineering (`Imperium-Knowledge/10_文本命名与界面规范.md` L31).

Real dangers show through hostile entities and the events that are needed, not through revealing a quote's internal
probability; explaining the real risk of other operations does not license attaching a risk analysis to an order
(`Imperium-Knowledge/10_文本命名与界面规范.md` L39). Text tells apart technology that is mastered, material that is lost, processes that cannot be reproduced
and equipment not yet authorized, instead of calling all of it mysterious technology (`Imperium-Knowledge/10_文本命名与界面规范.md` L74).

## Descriptions

The descriptions of mechanoids, and likewise of similar items and buildings, follow the common way of all the base
game's machine descriptions (`Imperium-Knowledge/10_文本命名与界面规范.md` L33-37; `Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L58-62; `Imperium-Knowledge/designs/待用/文本盘点-2026-10-27.md` L461). The first sentence classes the thing by
weight class, kind and design intent, in the pattern of the base game's Chinese, "一种轻型……机械，设计用于……", and names
its key equipment instead of listing its functions (`Imperium-Knowledge/10_文本命名与界面规范.md` L34; `Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L59). One restrained sentence follows on a
strength and a weakness, without numbers or rules, which the stats panel gives (`Imperium-Knowledge/10_文本命名与界面规范.md` L35; `Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L60). A second
paragraph is given only to a few subjects, written as
narrative: the origin of the name, the historical situation or what people lived through, from the viewpoint of people
in the Empire's world, in a cold tone, without witty maxims or praise; utility machines usually get one or two
sentences, and the imperial flavour comes from these people and institutions, not from repeating the word "Empire" (`Imperium-Knowledge/10_文本命名与界面规范.md` L36; `Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L61).
Descriptions hold no tactics, formation advice or operating tutorial (`Imperium-Knowledge/10_文本命名与界面规范.md` L37; `Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L62).

For mechanoids the opening follows the base game's words for the same weight class: in English "A small imperial combat
mechanoid ..." and "A small imperial mechanoid designed to ...", in Chinese "一种轻型帝国作战机械族……" and "一种轻型帝国机械族，设计用于……", and
every other mention of the machine itself takes the base game's word in the same kind of sentence
(`Imperium-Knowledge/08_机械体设计.md` L327, R-1104-0112; `Imperium-Knowledge/designs/做法史/装载机.md` L32;
`Imperium-Knowledge/designs/做法史/哨骑.md` L38). A description gives no counts, conditions or mechanics, which the info card
and the ability icons show, and does not list the equipment the player can see; it says what the thing does, and conveys
its function in one oblique sentence (`Imperium-Knowledge/08_机械体设计.md` L242, R-1030-2326;
`Imperium-Knowledge/08_机械体设计.md` L278-279, R-1102-1535). Sentences that rank the mechanoids against each other were to
be deleted; the Chinese descriptions had none, so nothing was changed there
(`Imperium-Knowledge/designs/回报/Code-RankII-数值一轮.md` L20, R-1103-1604).

The loader, the builder and the pollution sweeper carry the descriptions of the third version of 26 October, with the
openings above: the loader hauls bulk cargo over long distances and, lacking a ranged weapon, makes only weak melee
attacks; the builder completes construction across an area from a fixed position and can make weak blunt melee attacks
if necessary; the pollution sweeper draws pollution out of the ground and presses it into wastepacks, and lacking a
ranged weapon makes only weak melee attacks (`Imperium-Knowledge/裁定归档/2026-10.md` L292-295;
`Imperium-Knowledge/08_机械体设计.md` L327, R-1104-0112; `RimWorld-Imperium/docs/code-status.md` L19). The harvester keeps a
temporary description (`Imperium-Knowledge/08_机械体设计.md` L356, R-1104-1516;
`Imperium-Knowledge/designs/回报/Code-RankII-改名与编号.md` L10).

> [!NOTE]
> **Base game**: the pattern rests on the base game's machine descriptions: the Chinese "一种轻型机械族" and "一种轻型作战机械族",
> the English "A small mechanoid designed for hauling" and "A small combat mechanoid armed with…" of its light
> mechanoids, the Militor's description, and a second paragraph in about a quarter of them, to be checked against
> `Data/` (`Imperium-Knowledge/10_文本命名与界面规范.md` L22, L36; `Imperium-Knowledge/08_机械体设计.md` L327).

> [!NOTE]
> **Deleted**: the descriptions written for the three light combat mechanoids of rank II under the names limitanei,
> psiloi and alarius, with their openings "A light imperial (combat) mech" and "一种轻型帝国（作战）机械" and the
> limitanei's second paragraph on the old empire's frontier garrisons (`Imperium-Knowledge/08_机械体设计.md` L181-187; `Imperium-Knowledge/designs/待用/文本盘点-2026-10-27.md` L339, L508, L519). The
> line of 5 November gave those mechanoids new names and places and took the scutator off the frontier garrison
> (`Imperium-Knowledge/08_机械体设计.md` L396-402, R-1105-1827a, R-1105-1918, R-1105-1945), and the openings were changed to the base game's words
> (`Imperium-Knowledge/08_机械体设计.md` L327, R-1104-0112).

## Words kept out of player-visible text

Player-visible text holds no development words (实际, 实体, 真实, 原版, 原生, 读档, 结算, 合法 in the sense of
compliant, NoRank, Harness, Build, Plan, CBF, and internal codes such as M1, B2 and I3); no sentence that only says what
something is not; no explanation of design intent in advance; no reassuring or reminding additions such as "loaded
cargo is not affected"; no descriptions that list rules and numbers; and no pseudo-classical or honorific speech
(贵殖民地, 朕, 尔等, 圣谕, 荣光) (`Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L66-70). The word 拜占庭 (Byzantine) does not appear in it (`Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L70;
`Imperium-Knowledge/designs/待用/文本盘点-2026-10-27.md` L349).

The English and Chinese versions keep the same information, the same nature of each name and the same traits of each
character, and variables, placeholders and DefNames stay exact; renaming does not on its own change persistent
identifiers (`Imperium-Knowledge/10_文本命名与界面规范.md` L74). When a work mechanoid is renamed, its code identifiers (defName, class names, jobs, work
types, recipes) follow the new English name, and the reports and state files of the code use its Chinese formal name,
not the identifiers (`Imperium-Knowledge/08_机械体设计.md` L357, R-1104-1518; `Imperium-Knowledge/现行/机械体/通则-基线.md` L195; `Imperium-Knowledge/designs/回报/Code-RankII-改名与编号.md` L50-52).

> [!NOTE]
> **Deleted**: the line that kept the defNames when the work mechanoids were renamed (`Imperium-Knowledge/10_文本命名与界面规范.md` L59-62; `Imperium-Knowledge/08_机械体设计.md` L340,
> R-1104-0958a). It was replaced on 4 November by identifiers that follow the new English name, without old-save
> compatibility (`Imperium-Knowledge/08_机械体设计.md` L357, R-1104-1518).

## Naming mechanoids

A mechanoid's Chinese label is in Chinese only, and its Latin name stays in the English version and in descriptions
(`Imperium-Knowledge/10_文本命名与界面规范.md` L68; `Imperium-Knowledge/08_机械体设计.md` L181). Machine names show their function, and candidate machines and facilities not yet named are
not dressed up as official translations (`Imperium-Knowledge/10_文本命名与界面规范.md` L70). Naming first looks in the base game's and the expansions'
entries, labels, descriptions and backstories, in Simplified Chinese and in English, for a ready word, and makes a new
one only where none fits (`Imperium-Knowledge/08_机械体设计.md` L410, R-1106-0736; `Imperium-Knowledge/现行/机械体/通则-基线.md` L205; `Imperium-Knowledge/现行/索引.md` L74; `Imperium-Knowledge/designs/做法史/通则-基线.md` L121).

A work mechanoid is designed in the order function, look, name: its function is chosen from the base game's work, and no
function or name is chosen for a Roman feel, which comes from its look and some of its function; a proposed name is
checked against these rules, and a rejected name is not passed off as acceptable (`Imperium-Knowledge/现行/机械体/通则-基线.md`
L191, R-1104-0958a; `Imperium-Knowledge/08_机械体设计.md` L340). The English name comes first and the Chinese follows from it
by function, as the base game's translator works (`Imperium-Knowledge/现行/机械体/通则-基线.md` L192;
`Imperium-Knowledge/08_机械体设计.md` L340). In English the name is like the base game's work machines: one word, or the
two-word kind the base game's mechanoids use, such as war urchin, lowercase, showing which job it does, using no
colonist job name (Hauler, Constructor, Grower, Cleaner) and matching nothing the base game already has
(`Imperium-Knowledge/现行/机械体/通则-基线.md` L193). In Chinese it has three characters, the name most people know from real
life, and does not repeat the base game's counterpart (`Imperium-Knowledge/现行/机械体/通则-基线.md` L194;
`Imperium-Knowledge/08_机械体设计.md` L181). Each mechanoid's formal names are in the interface and text section of its card
(`Imperium-Knowledge/现行/机械体/通则-基线.md` L195). The base game's ground pollution always says pollution, as in the pollution
pump and cleaning pollution, and tox is only for toxic gas, poisoning and toxic waste, so the pollution sweeper keeps
pollution (`Imperium-Knowledge/现行/机械体/通则-基线.md` L196; `Imperium-Knowledge/08_机械体设计.md` L340).

A combat mechanoid's English name goes by tier: at rank II, against the base game's basic tier, the basic soldier takes
the word soldier itself (stratior) and the others are named by weapon or action; at rank III, against the standard tier,
by weapon, action or a visible feature, with at most one grand name, as the base game has the cyclops; from rank IV on,
New Roman names, grander the higher the rank; and work mechanoids take a function plus a suffix (`Imperium-Knowledge/现行/机械体/通则-基线.md` L200,
R-1105-1918b). Its Chinese name is 机械 plus a modifier plus a creature or a duty character, the modifier saying
identity or duty and never a place, as the 辅 of the base game's auxiliary says a lower rank that follows the main
force; cavalry take 骑, non-humanoid mechanoids take insect-like images akin to the base game's, and work mechanoids are
"X机", as the base game's tunneler is (`Imperium-Knowledge/现行/机械体/通则-基线.md` L201, R-1105-1918b, R-1106-0659). A humanoid mechanoid is named first
in English, its Chinese is derived from the English, and other languages translate from the English; its Chinese
character is not tied to a rank, so 兵 and 卫 serve at any tier, and it names the mechanoid's character, not the weapon
it holds: the scutator is 戍卫 and not 盾卫, and the archer is 弦卫 while its English stays sagittor (`Imperium-Knowledge/现行/机械体/通则-基线.md` L202-203,
R-1106-2135b; `Imperium-Knowledge/08_机械体设计.md` L430; `Imperium-Knowledge/designs/做法史/通则-基线.md` L130). Clashes with other mods' names are not considered, since Imperium is made to the standard
of a DLC and does not make way for other mods in advance (`Imperium-Knowledge/现行/机械体/通则-基线.md` L204; `Imperium-Knowledge/08_机械体设计.md` L430). Base-game mechanoid names are
avoided only for recognisability: Imperium is the rebuilt Royalty, and names that belong to Rome in the base game's
Empire are taken back rather than avoided; no word with regional or dynastic colour is used, and the reading load on
English players is weighed (`Imperium-Knowledge/现行/机械体/通则-基线.md` L206, R-1105-1918b).

> [!NOTE]
> **Base game**: the naming rests on the base game's mechanoids: the Militor is called 机械辅兵 in Simplified Chinese
> and is not humanoid, the tunneler's Chinese takes the form "X机", and the cyclops has a grand name, to be checked
> against `Data/` (`Imperium-Knowledge/08_机械体设计.md` L401, L408).

> [!NOTE]
> **Deleted**: the naming line of 26 October, by which mechanoids took Latin or Greek proper names with historical
> grounds and Chinese labels said only their function, with work machines keeping short proper names (`Imperium-Knowledge/08_机械体设计.md` L68-80;
> `Imperium-Knowledge/10_文本命名与界面规范.md` L68-70), and its steps of 5 and 6 November, by which humanoids of rank II took 兵 and of rank III 卫, and the
> two languages each kept their own rhythm without translating each other (`Imperium-Knowledge/08_机械体设计.md` L401, R-1105-1918b; `Imperium-Knowledge/08_机械体设计.md` L408,
> R-1106-0659; `Imperium-Knowledge/designs/做法史/通则-基线.md` L13). The humanoid naming of 6 November replaced them (`Imperium-Knowledge/08_机械体设计.md` L430, R-1106-2135b), and the work
> mechanoids were renamed on 4 November (`Imperium-Knowledge/08_机械体设计.md` L340, R-1104-0958a).

## Naming weapons

A mechanoid's weapon first takes a provisional name, and its formal name comes from the unit's look, as the base game's
mechanoid weapons do; no name holds the working fluid, none clashes with a weapon for people, and a weapon grown on the
body, with no weapon item, is called by that body part (`Imperium-Knowledge/08_机械体设计.md` L299, R-1103-1213g;
`Imperium-Knowledge/designs/做法史/哨骑.md` L19). Weapon names drawn from the working fluid all read like manuals
(`Imperium-Knowledge/designs/研究/主轴对比-工质与自动机传统-2026-11-03.md` L18). In battle a mechanoid's melee attacks are named by
the part they strike with, as the base game does, such as 矛尖 for the spear point, 盾 for the shield and 头 for the head
(`Imperium-Knowledge/08_机械体设计.md` L278, R-1031-0216). The spear the scutator throws is the same as the spear in its hand
and takes no name of its own (`Imperium-Knowledge/08_机械体设计.md` L446, R-1110-0208b).

> [!NOTE]
> **Base game**: the base game's mechanoid weapons take their names from the unit, such as the needle gun of the 机械蝎蝽
> and the scythe blade of the 飞螳, to be checked against `Data/` (`Imperium-Knowledge/08_机械体设计.md` L299).

> [!NOTE]
> **Unverified**: the stratior's weapon has only the provisional name stratior long rifle (列兵长枪); its formal name,
> and the descriptions of the stratior and its weapon, which are temporary text, wait for the maintainer under item 58
> of the to-decide list (`Imperium-Knowledge/designs/回报/Code-RankII-列兵替换.md` L8; `Imperium-Knowledge/designs/做法史/列兵.md` L31, R-1111-0646).

## Naming officials, equipment and research

Imperial officials take function names in Chinese and plain names in English, and their Greek originals appear only in
descriptions (`Imperium-Knowledge/06_行政设施与地区活动.md` L172); [terms.md](terms.md) lists them. The main line of the Empire's technology has only an
internal name, for now 自动机传统 (automaton tradition), which players do not see; the research names players see
follow the base game's structure, with no word of their own for the line (`Imperium-Knowledge/designs/研究/主轴对比-工质与自动机传统-2026-11-03.md` L110).

## Chinese and English

The English name is fixed first and the Chinese is translated from it (`Imperium-Knowledge/designs/回报/调研-开发流程全套.md` L75, R-1104-0958a; `Imperium-Knowledge/designs/回报/调研-流程-游戏设计与制作.md` L106).
Proper names and their localisation are kept in a table of names in Chinese and English with notes (`Imperium-Knowledge/10_文本命名与界面规范.md` L45-66;
`Imperium-Knowledge/designs/回报/调研-流程-游戏设计与制作.md` L227-228). The Chinese interface leaves no English: as the base game's official Chinese translates every
system name of Royalty, Imperium's system names are all Chinese, 委托 for orders, 请求 for requests, 发掘 for claims and
等级 for rank, while the documents keep the English names as terms (`Imperium-Knowledge/10_文本命名与界面规范.md` L43; `Imperium-Knowledge/designs/RankI-设计核对-2026-10-29.md` L319; `Imperium-Knowledge/designs/待用/文本盘点-2026-10-27.md` L6).

> [!NOTE]
> **Base game**: the official Chinese translation of the base game renders all of Royalty's system names in Chinese, and
> the base game already speaks of a "trade request", to be checked against `Data/` (`Imperium-Knowledge/10_文本命名与界面规范.md` L43, L49).

> [!NOTE]
> **Deleted**: the line of 26 October that kept orders, claims, duties and rank in English in the Chinese text as well
> (`Imperium-Knowledge/10_文本命名与界面规范.md` L43; `Imperium-Knowledge/designs/待用/文本盘点-2026-10-27.md` L254, L581, L616). The ruling of 27 October that the Chinese interface leaves no English voided
> it (`Imperium-Knowledge/10_文本命名与界面规范.md` L43; `Imperium-Knowledge/designs/待用/文本盘点-2026-10-27.md` L6).

> [!NOTE]
> **Unverified**: the first release's languages and who gives the final review of the Chinese. A research report reads
> the English-first ruling as a first release in English and Chinese and recommends English and Simplified Chinese at
> the beta, with the maintainer reviewing the Chinese, which is a recommendation, not a ruling (`Imperium-Knowledge/designs/回报/调研-流程-游戏设计与制作.md` L207, L343).

## The interface

Each new system has one entry in the base game's learning helper (学习助手): orders, requests, claims, the imperial
area, the shuttle pad, the promotion application and the deployable mechanoids; the entry says only how to operate the
system and does not explain the mechanism behind it, and the campaign's entry appears at the first campaign
(`Imperium-Knowledge/10_文本命名与界面规范.md` L78).

Each fact is stated once, in the place that suits it best: the Gizmo or the right-click command gives the action, the
tooltip gives a condition or consequence that is not obvious, a disabled reason states what is really missing, the
Inspect panel shows the state that is useful now, and the quest shows physical progress; a sentence that only repeats
what a button means, and whose removal loses no information needed to operate, is removed (`Imperium-Knowledge/10_文本命名与界面规范.md` L80).

> [!NOTE]
> **Base game**: the learning helper is the base game's, to be checked against `Data/` (`Imperium-Knowledge/10_文本命名与界面规范.md` L78).

> [!WARNING]
> **Conflict**: the Chinese form of the rank requirement. The same name table, of one date, has the interface write
> 帝国等级 II, and its sample writes the requirement as 帝国等级 I.
> - The requirement reads "需要帝国等级 I。／需要帝国等级 {0}（当前 {1}）。", and the interface writes the rank as
>   帝国等级 II (`Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L35, L89).
> - 帝国等级 I is among the names the table replaces, with 政治等级, Rank1, NoRank and Political Rank (`Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L35).

## Sample texts

The text rewrite sets these samples as its standard (`Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L72-90; `Imperium-Knowledge/11_开发进度与未决事项.md` L43):

- Imperial recognition: an imperial representative brings an agreement; if the colony accepts, its settlement is
  registered as an outpost of the Empire, which starts to send transport ships and officials, and the colony receives
  them and helps keep order in the area; it may refuse, or decide again before the representative leaves; once it is
  recognized, the settlement is registered as an outpost, and the Empire's transport ships, patrols and officials pass
  by from time to time (`Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L76-77).
- The imperial insignia is the Empire's local administrative mark: imperial staff do business only in a settlement that
  has one, and only inside the imperial area the player marks out, and its pattern changes with the settlement's
  standing (`Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L78; `docs/glossary.md` L55).
- A ruined terminal is old, its casing rusted, and it seems to have a little power left, which makes it flicker and
  crackle now and then (`Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L80).
- A techprint is a technical drawing of imperial standard equipment; once it is registered, the colony is permitted to
  make that equipment (`Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L81; `docs/glossary.md` L92).
- The sentry ballista is a foldable automatic ballista whose hydraulic arm cannot be controlled directly and which
  shoots only the nearest enemy; its bolts are refilled with steel, and folded it can be carried elsewhere and set up
  again (`Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L82).
- A claim over a contested ruin: an imperial officer tells the colony privately of an old imperial depot that two armed
  groups are fighting over; he wants a core from deep inside it; if the colony brings it back within 30 days it keeps
  everything else it finds; the depot's security system may still be running
  (`Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L83).
- A mining order: the ore mined is split as agreed between the colony's share and the firm's, automatically as it is
  loaded onto the return shuttle; on an order without support the Empire supplies only transport, and the people and the
  force are the colony's own (`Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L85-86).
- After an order ends, the Empire replies that the record of its fulfilment has been received and is being handled by
  routine procedure, with notice to follow once the formalities are complete
  (`Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L87).
- A backstory: the judicial investigator is an imperial official who traces forged official papers and people who use
  the Empire's name, work that has taught the character to trust no one
  (`Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L88).

> [!NOTE]
> **Deleted**: the sample for the Tabularium (档案署) as the terminal for dealing with the Empire, where contact,
> orders, the registration of techprints and the imperial records were handled (`Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L79), and the Tabularium as the
> place a techprint is registered (`Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L81). The deprecated-terms data removes the Tabularium; its functions are in
> the interface that the button at the bottom of the screen opens (`.github/deprecated-terms.json` L362-381).

> [!NOTE]
> **Deleted**: the fifth version of the rewriting sample, whose machine lines used old names and looks, with its drafts
> for the low-shield drop pack, the forward smoke generator, the performance commendation, trade with the transport
> officer, help with judicial arrests and the rental of machines (`Imperium-Knowledge/designs/整理/整理记录-2026-11-02.md` L149). The samples above replaced it
> (`Imperium-Knowledge/designs/整理/整理记录-2026-11-02.md` L149, R-1104-0958a).

## The Empire's identity text in the old mod

The old mod RimWorld-Imperium shows the Empire faction as Empire (帝国), its leader title and the stellarch's label as
Exarch (总督), the label of the bestower as Imperial Envoy (帝国使节), the throne room's role as Audience Hall with the native
Chinese, and four backstory titles as Noble House Cook (名门私厨), Noble Bastard (名门私生子), Provincial Noble Scion
(地方名门子弟) and Noble Scion (名门子弟); the faction description is the base game's in English and Imperium's own in
Chinese, and one church backstory keeps its native English with imperial church text in Chinese (`RimWorld-Imperium/docs/royalty-text-display-mapping.md` L5-17).
Imperium keeps no text for Royalty's titles, honor, permits, bestowal and tribute, since those routes are retired, and
recognition works by interacting with a thing (`RimWorld-Imperium/docs/royalty-text-display-mapping.md` L25). The dialogue of recognition offers Join (加入), Decline
(拒绝) and Defer (保留意见) (`RimWorld-Imperium/docs/imperial-contact-v0.md` L65).

## The rewrite of in-game text

Text is reviewed in this order: find the base game's text in a comparable context, fix the narrator, check the real
mechanism and the variables, keep the information needed to operate, check the boundary of what is unknown, remove
honorifics and filler, check the Chinese and English display, truncation and placeholders, and check variants and
consistency with saves (`Imperium-Knowledge/10_文本命名与界面规范.md` L108). Only text that is really redundant or wrong is changed, and a text task does not restructure
gameplay (`Imperium-Knowledge/10_文本命名与界面规范.md` L108).

In-game text is rewritten once, system by system, with the implementation of rank II: first the text of retired content
is deleted, then names are changed, the Chinese system names included, and then the tone is unified, to the standard
and samples above, to the mechanoid descriptions and to each mechanoid card's section on interface and text
(`Imperium-Knowledge/11_开发进度与未决事项.md` L43). The rewrite changes only player-visible text and text that removed content leaves invalid, and puts the
finished descriptions into the mechanoids' text (`Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L4, L50).

## The mod's description

The mod's description, in About.xml and on the Workshop page, is written by the maintainer and edited by Claude
(`Imperium-Knowledge/11_开发进度与未决事项.md` L43). Faction and terrain generation are not advertised in the description, the update notes or in-game text;
players find them on expeditions (`Imperium-Knowledge/09_地图生成与CBF技术.md` L445, R-1028-0159).

> [!NOTE]
> **Unverified**: the Workshop page and the About description. The page's positioning waits until the city is in the
> game, and only an initial judgment is kept on record: the page says first that Imperium is not a title mod, not a
> large content pack and not a historical reconstruction, keeping it apart from VFE-Empire; its first image is a
> top-down view of a Roman city; it does not mention the generation, so that players find it themselves; and
> prerequisites and compatibility follow the charter (`Imperium-Knowledge/11_开发进度与未决事项.md` L61, R-1029-2100). The About description is written by the
> maintainer later, and the rewrite leaves a placeholder (`Imperium-Knowledge/designs/待用/文本重写指令-随RankII批次.md` L10).

> [!NOTE]
> **Deleted**: the initial judgment's one-sentence pitch of a Roman-style empire run on water power, its three things of
> the Empire, hydraulics and expedition destinations, and the waterline in its first image rest on the hydraulics the
> maintainer deleted (`Imperium-Knowledge/11_开发进度与未决事项.md` L61).

## Writing about the design

The design's own text keeps a sentence style: it does not discuss walls as symmetric, asymmetric or polygonal, does not
personify the Empire, writes no sentence that explains what something is not but states it positively, explains no
design intent in advance and ends no sentence with a reminder or reassurance (`Imperium-Knowledge/现行/流程/设计会话工作规矩.md`
L116, R-1029-2026; `Imperium-Knowledge/designs/tools/审查清单-条文.md` L62-65;
`Imperium-Knowledge/designs/tools/prompts/通用.md` L13). Numbers in the clauses written for Code are written as concrete
sizes, quantities and positions only where the figure is itself a design decision; otherwise the purpose and a sample
are written, and no impression words (`Imperium-Knowledge/designs/tools/审查清单-条文.md` L66). A sentence about Roman history
that asserts with words such as 本就, 本来就, 向来, 历来 or 自古 names its source (`Imperium-Knowledge/designs/tools/目录配置.md`
L180-181, R-1111-2218; `Imperium-Knowledge/designs/tools/红线表.md` L31).