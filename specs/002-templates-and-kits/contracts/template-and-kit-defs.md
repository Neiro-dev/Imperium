# Contract: template and kit definitions

Other authors add a culture by writing these two kinds of definition and nothing else (spec FR-033, FR-034). The
game loads them from `Defs/`, Mantle's generation reads them (R2), and the check reads them outside the game. Field
rules are in [../data-model.md](../data-model.md); sources in [../research.md](../research.md) R-1, R-3 to R-5 and
R-8. The examples are shapes, not content.

## A kit

```xml
<?xml version="1.0" encoding="utf-8"?>
<Defs>
  <Mantle.KitDef>
    <defName>Empire</defName>
    <label>Empire</label>
    <nameMaker>ExampleNamer</nameMaker>
    <skeleton>
      <parts>
        <li><name>core</name><kind>Core</kind></li>
        <li><name>firstSquare</name><kind>Plaza</kind></li>
        <li><name>mainStreet</name><kind>MainStreet</kind></li>
        <li><name>mainGate</name><kind>Gate</kind></li>
        <li><name>palaceQuarter</name><kind>PalaceQuarter</kind></li>
        <li><name>walls</name><kind>WallLine</kind><optional>true</optional></li>
      </parts>
      <relations>
        <li><relation>Inside</relation><a>firstSquare</a><b>core</b></li>
        <li><relation>Adjoins</relation><a>mainStreet</a><b>mainGate</b></li>
        <li><relation>Farther</relation><a>palaceQuarter</a><b>mainGate</b><than>core</than></li>
      </relations>
    </skeleton>
    <wallSettings>
      <wallDef>Wall</wallDef>
    </wallSettings>
    <groups />
    <fill />
  </Mantle.KitDef>
</Defs>
```

## A template

```xml
<?xml version="1.0" encoding="utf-8"?>
<Defs>
  <Mantle.TemplateDef>
    <defName>ExampleRiverTown</defName>
    <label>example river town</label>
    <kit>Empire</kit>
    <reference>
      <name>ExampleRiverTown</name>
      <pictures>
        <li>screenshot</li>
      </pictures>
    </reference>
    <allowedRivers>
      <li>River</li>
    </allowedRivers>
    <minMapSize>(350, 1, 350)</minMapSize>
    <terrainShape>
      <terrain>
        <Soil><rects><li>(0,0,349,349)</li></rects></Soil>
        <WaterMovingChestDeep><rects><li>(170,0,179,349)</li></rects></WaterMovingChestDeep>
      </terrain>
      <features>
        <li><name>river</name><rects><li>(170,0,179,349)</li></rects><flowsFrom>North</flowsFrom></li>
      </features>
    </terrainShape>
    <skeleton>
      <parts>
        <li><name>westBank</name><kind>District</kind></li>
        <li><name>eastBank</name><kind>District</kind></li>
        <li><name>bridge</name><kind>Bridge</kind></li>
      </parts>
      <relations>
        <li><relation>Across</relation><a>westBank</a><b>eastBank</b><feature>river</feature></li>
        <li><relation>Adjoins</relation><a>bridge</a><b>westBank</b></li>
        <li><relation>Adjoins</relation><a>bridge</a><b>eastBank</b></li>
        <li><relation>Upstream</relation><a>palaceQuarter</a><b>core</b><feature>river</feature></li>
      </relations>
    </skeleton>
  </Mantle.TemplateDef>
</Defs>
```

The template names its kit's parts (`palaceQuarter`, `core`) without listing them again; it may list one again with
the same kind.

## Stable from R13 on

- The two definition types, their field names, the rect, layer, position and rotation forms, the part kinds and the
  relation kinds. A later entry may add kinds and fields (spec, Assumptions) but does not rename or remove these
  without a deprecation in the same pull request.
- Another expansion's definition is marked with `MayRequire` on the element that names it, as `Data/` marks its own.
- A culture is its kit's `defName`; its templates name that kit.

## May change in later entries

- The fields of `groups` and `fill`, once the maintainer has said what they hold (R-8) and R2's generation uses them.
- Further wall settings, such as the spacing of towers (glossary line 213), when generation uses them.
