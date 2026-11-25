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

/// <summary>A road grade a kit allows and its widths in cells (data-model.md, KitDef.roads).</summary>
public class RoadGrade
{
    public string name;
    public List<int> widths = new();
}

/// <summary>Whether a kit allows road ends that land nowhere but a building (data-model.md, KitDef.roads).</summary>
public enum DeadEnds
{
    Allowed,
    None,
}

/// <summary>What a kit holds its culture's readings to beyond the shared road checks (spec FR-054).</summary>
public class RoadSettings
{
    public List<RoadGrade> grades = new();
    public bool eightDirections;
    public DeadEnds deadEnds = DeadEnds.Allowed;
}

/// <summary>Whether every household of the culture has a plot (spec FR-055).</summary>
public class HouseholdSettings
{
    public bool plotEach;
}

/// <summary>A culture's kit: the culture definitions it serves, its skeleton, wall settings, groups, fill, road and
/// household settings and block library (data-model.md, KitDef).</summary>
public class KitDef : Def
{
    /// <summary>The culture definitions whose factions' settlements take this kit, by their allowedCultures (spec
    /// FR-032; research R-26).</summary>
    public List<CultureDef> cultures = new();

    /// <summary>Deprecated: a settlement takes its faction's own settlementNameMaker (spec FR-006; research R-26).
    /// Still read for one version so that an older kit loads.</summary>
    public RulePackDef nameMaker;

    public Skeleton skeleton = new();
    public WallSettings wallSettings = new();
    public List<Group> groups = new();
    public Fill fill = new();
    public RoadSettings roads;
    public HouseholdSettings households;
    public List<SpecCard> blockLibrary = new();
}
