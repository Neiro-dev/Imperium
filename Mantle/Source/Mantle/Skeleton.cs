using System.Collections.Generic;

namespace Mantle;

/// <summary>The fixed parts of a layout that the design and the maintainer name (research R-5).</summary>
public enum PartKind
{
    Core,
    SecondaryCore,
    PalaceQuarter,
    Gate,
    RiverGate,
    WaterGate,
    MainStreet,
    SecondaryAxis,
    District,
    Acropolis,
    Landmark,
    Bridge,
    WallLine,
    Plaza,
    PublicBuilding,
}

/// <summary>The relations the design's definitions use (research R-5, R-6).</summary>
public enum RelationKind
{
    Inside,
    Adjoins,
    Across,
    SameSide,
    Upstream,
    Farther,
}

/// <summary>A named part of a skeleton; an optional part is a slot a city may leave out.</summary>
public class Part
{
    public string name;
    public PartKind kind;
    public bool optional;
}

/// <summary>A relation between two parts or features, with the feature or third part its kind needs.</summary>
public class Relation
{
    public RelationKind relation;
    public string a;
    public string b;
    public string feature;
    public string than;
}

/// <summary>Parts and the relations between them, held by a template and by a kit.</summary>
public class Skeleton
{
    public List<Part> parts = new();
    public List<Relation> relations = new();
}
