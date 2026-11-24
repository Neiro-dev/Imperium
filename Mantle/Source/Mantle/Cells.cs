using System.Collections.Generic;
using System.Xml;
using Verse;

namespace Mantle;

/// <summary>An element of a layer: the definition it is named by and the cells it covers, in PrefabDef's terrain
/// form (research R-3).</summary>
public abstract class Rects<TDef> where TDef : Def
{
    public TDef def;
    public List<CellRect> rects = new();

    public void LoadDataFromXmlCustom(XmlNode xmlRoot)
    {
        DirectXmlCrossRefLoader.RegisterObjectWantsCrossRef(
            this, "def", xmlRoot.Name, xmlRoot.Attributes?["MayRequire"]?.Value?.ToLower(),
            xmlRoot.Attributes?["MayRequireAnyOf"]?.Value?.ToLower());
        XmlNode rectsNode = xmlRoot["rects"];
        if (rectsNode != null)
        {
            rects = DirectXmlToObject.ObjectFromXml<List<CellRect>>(rectsNode, false);
        }
    }
}

public class TerrainRects : Rects<TerrainDef>
{
}

public class RockRects : Rects<ThingDef>
{
}

public class RoofRects : Rects<RoofDef>
{
}

/// <summary>A named terrain feature; a river names the map edge it flows from.</summary>
public class Feature
{
    public string name;
    public List<CellRect> rects = new();
    public Rot4 flowsFrom = Rot4.Invalid;
}

/// <summary>A template's site: natural terrain, rock and roofs, and its named features (research R-4).</summary>
public class TerrainShape
{
    public List<TerrainRects> terrain = new();
    public List<RockRects> rocks = new();
    public List<RoofRects> roofs = new();
    public List<Feature> features = new();
}

/// <summary>A thing in PrefabDef's thing form: named by its definition, with its position, rotation, material and,
/// for a thing larger than one cell, the cells it covers (research R-3, R-8).</summary>
public class PlacedThing
{
    public ThingDef def;
    public IntVec3 position;
    public Rot4 rotation = Rot4.North;
    public ThingDef stuff;
    public CellRect rect;
    public bool hasRect;

    public void LoadDataFromXmlCustom(XmlNode xmlRoot)
    {
        DirectXmlCrossRefLoader.RegisterObjectWantsCrossRef(
            this, "def", xmlRoot.Name, xmlRoot.Attributes?["MayRequire"]?.Value?.ToLower(),
            xmlRoot.Attributes?["MayRequireAnyOf"]?.Value?.ToLower());
        XmlNode positionNode = xmlRoot["position"];
        if (positionNode != null)
        {
            position = ParseHelper.FromString<IntVec3>(positionNode.InnerText);
        }
        XmlNode rotationNode = xmlRoot["rotation"];
        if (rotationNode != null)
        {
            rotation = Rot4.FromString(rotationNode.InnerText);
        }
        XmlNode rectNode = xmlRoot["rect"];
        if (rectNode != null)
        {
            rect = ParseHelper.FromString<CellRect>(rectNode.InnerText);
            hasRect = true;
        }
        XmlNode stuffNode = xmlRoot["stuff"];
        if (stuffNode != null)
        {
            DirectXmlCrossRefLoader.RegisterObjectWantsCrossRef(
                this, "stuff", stuffNode.InnerText, stuffNode.Attributes?["MayRequire"]?.Value?.ToLower(),
                stuffNode.Attributes?["MayRequireAnyOf"]?.Value?.ToLower());
        }
    }
}

/// <summary>A set of things placed together, each from the group's own corner (research R-8).</summary>
public class Group
{
    public string name;
    public IntVec2 size;
    public List<TerrainRects> terrain = new();
    public List<PlacedThing> things = new();
}

/// <summary>A named room of a spec card.</summary>
public class Room
{
    public string name;
    public List<CellRect> rects = new();
}

/// <summary>The design card that fixes one building's plot, rooms and contents (spec FR-007).</summary>
public class SpecCard
{
    public string name;
    public IntVec2 size;
    public List<TerrainRects> terrain = new();
    public List<Room> rooms = new();
    public List<PlacedThing> things = new();
}
