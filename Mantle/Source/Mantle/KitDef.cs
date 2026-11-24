using System.Collections.Generic;
using RimWorld;
using Verse;

namespace Mantle;

/// <summary>A kit's wall settings, in StructureLayoutDef's form (research R-3).</summary>
public class WallSettings
{
    public ThingDef wallDef;
}

/// <summary>What a block's plots are built with, in StructureLayoutDef's form, and the plot sets (research R-8).
/// </summary>
public class Fill
{
    public ThingDef wallDef;
    public ThingDef doorDef;
    public ThingDef doorStuffDef;
    public List<Group> plots = new();
}

/// <summary>A culture's kit: its word list, skeleton, wall settings, groups, fill and block library
/// (data-model.md, KitDef).</summary>
public class KitDef : Def
{
    public RulePackDef nameMaker;
    public Skeleton skeleton = new();
    public WallSettings wallSettings = new();
    public List<Group> groups = new();
    public Fill fill = new();
    public List<SpecCard> blockLibrary = new();
}
