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

A reading is a reference city read onto the game's cells in the same form, set beside its reference pictures until it
matches them; the culture's template and kit are taken from it (spec FR-036; research R-7). It holds `reference`, the
name the template's `reference` gives the city, in place of `template` and `kit`, and the parts and features it reads:

```xml
<LaidOutCity>
  <reference>ExampleHillfort</reference>
  <size>(350,350)</size>
  ...
</LaidOutCity>
```

A reading from a reference that exists only as a picture also holds `scale`: the pixels one cell is, the RimWorld cells
one cell of the reference game is, and the things it was got from, at least one, and each part or feature it traces holds `from`, the region of the picture it was read
from, as pixel rects (the form of data-model.md, Common forms; spec FR-048, FR-049; research R-17):

```xml
<LaidOutCity>
  <reference>ExampleHillfort</reference>
  <size>(350,350)</size>
  <scale>
    <pixelsPerCell>9.5</pixelsPerCell>
    <referenceCell>4</referenceCell>
    <origin>(0,300)</origin>
    <measured><li><name>door</name><rect>(412,288,421,297)</rect></li></measured>
  </scale>
  ...
  <parts>
    <li><name>innerYard</name><rects><li>(120,100,160,140)</li></rects><from><li>(380,260,760,640)</li></from></li>
    <li><name>eastHouses</name><rects><li>(60,20,100,60)</li></rects><from><li>(120,60,500,440)</li></from>
      <use>Housing</use><basis>Rows of one-storey houses with small yards.</basis></li>
  </parts>
</LaidOutCity>
```

`origin` is optional: the pixel `(x,y)` of the picture where the lower left corner of cell (0, 0) lies, the picture's lower
left corner where it is left out (spec FR-051). A building or group holds `use`, one of `Housing`, `ShopFront`, `Workshop`, `Tavern`, `Market`, `Public`,
`AnnexOrAttic` or `Unclear`, and `basis`, one sentence (spec FR-049, the design's eight classes). What is done with an area of
which more than three tenths is unclear has no form (spec FR-049, marked NEEDS CLARIFICATION).

A reading from a picture in perspective also holds `ground`, at least four pairs of a pixel of the picture's ground
and the cell corner it lies on, and types its pieces (data-model.md, LaidOutCity; spec FR-052 to FR-055):

```xml
  <ground>
    <pairs>
      <li><pixel>(1056,536)</pixel><cell>(40,52)</cell></li>
      <!-- three or more pairs more -->
    </pairs>
  </ground>
  <parts>
    <li><name>squareStreet</name><kind>Road</kind><grade>SecondaryStreet</grade><line><li>(10,40)</li><li>(60,40)</li></line>
      <leadsTo>westHouse</leadsTo><wayInFrom><li>(1010,560,1020,570)</li></wayInFrom><from><li>(980,540,1120,580)</li></from></li>
    <li><name>westHouse</name><kind>House</kind><household>west</household><rects><li>(12,42,20,50)</li></rects>
      <from><li>(990,500,1030,540)</li></from><use>Housing</use><basis>A red roof with its yard behind it.</basis></li>
    <li><name>westPlot</name><kind>Plot</kind><household>west</household><rects><li>(10,42,24,56)</li></rects>
      <from><li>(985,480,1040,545)</li></from></li>
    <li><name>westYard</name><kind>Yard</kind><household>west</household><uncertain>true</uncertain>
      <because>Its far edge is under the roof's shadow.</because><rects><li>(21,42,24,50)</li></rects>
      <from><li>(1025,505,1040,540)</li></from></li>
  </parts>
```

It is kept in `readings/` at the repository root, outside both mod folders, as the template's source, so it is in
neither mod's released files (research R-7); its reference pictures are kept outside the repository (FR-028).
