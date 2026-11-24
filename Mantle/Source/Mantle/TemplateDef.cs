using System.Collections.Generic;
using RimWorld;
using Verse;

namespace Mantle;

/// <summary>The reference city a template is taken from, by the mod's own name, and its pictures' labels.</summary>
public class ReferenceCity
{
    public string name;
    public List<string> pictures = new();
}

/// <summary>A template: a terrain shape and a skeleton, filled by its culture's kit (data-model.md, TemplateDef).
/// </summary>
public class TemplateDef : Def
{
    public KitDef kit;
    public ReferenceCity reference;
    public List<BiomeDef> allowedBiomes = new();
    public List<RiverDef> allowedRivers = new();
    public bool naturalEnemy;
    public bool permanentEnemy;
    public IntVec3 minMapSize;
    public TerrainShape terrainShape = new();
    public Skeleton skeleton = new();
}
