# Contract: a laid-out city

R2's generation writes one file per city it lays out, and the check reads it (spec FR-008; research R-7). The game does
not load it and the mod does not ship it. Until R2, the files are written by hand for the tests (spec, Assumptions).
Field rules are in [../data-model.md](../data-model.md).

```xml
<?xml version="1.0" encoding="utf-8"?>
<LaidOutCity>
  <template>ExampleRiverTown</template>
  <kit>Empire</kit>
  <size>(350,350)</size>
  <terrain>
    <Soil><rects><li>(0,0,349,349)</li></rects></Soil>
    <WaterMovingChestDeep><rects><li>(180,0,189,349)</li></rects></WaterMovingChestDeep>
  </terrain>
  <roofs />
  <things>
    <Wall><position>(40,0,40)</position><rotation>North</rotation><stuff>BlocksGranite</stuff></Wall>
    <Door><position>(40,0,60)</position><rotation>East</rotation><stuff>WoodLog</stuff></Door>
  </things>
  <parts>
    <li><name>westBank</name><rects><li>(20,20,170,330)</li></rects></li>
    <li><name>bridge</name><rects><li>(170,150,199,154)</li></rects></li>
  </parts>
  <features>
    <li><name>river</name><rects><li>(180,0,189,349)</li></rects><flowsFrom>North</flowsFrom></li>
  </features>
</LaidOutCity>
```

- Positions, rects, `flowsFrom` and part places are those of the city as laid out, after generation picked, mirrored,
  turned and stretched its template.
- A thing larger than one cell holds `rect`, the cells it covers as the game gives them.
- The form follows the template and kit forms: a field added there for generation is added here when the check needs
  it.

## A reading

A reading is a reference city drawn on the game's cells in the same form, set beside its reference pictures until it
matches them; the culture's template and kit are taken from it (spec FR-036; research R-7). It holds `reference`, the
name the template's `reference` gives the city, in place of `template` and `kit`, and the parts and features it reads:

```xml
<LaidOutCity>
  <reference>ExampleHillfort</reference>
  <size>(350,350)</size>
  ...
</LaidOutCity>
```

It is kept in `readings/` of the repository of the mod that holds the template, as the template's source, and is not
in the mod's released files; its reference pictures are kept outside the repository (FR-028).
