from enum import Enum

ElementTypes = Enum("ElementTypes", "Fire Water Wood Dark Light NoElement")
ElementIds = {
    0 : ElementTypes.Fire,
    1 : ElementTypes.Water,
    2 : ElementTypes.Wood,
    3 : ElementTypes.Dark,
    4 : ElementTypes.Light,
    None : ElementTypes.NoElement,
}


TypeTypes = Enum("TypeTypes", "EvoMaterial Balanced Physical Healer Dragon God Attacker Devil Machine AwokenSkillMaterial Protected EnhanceMaterial NoType")
TypeIds = { 
    0 : TypeTypes.EvoMaterial,
    1 : TypeTypes.Balanced,
    2 : TypeTypes.Physical,
    3 : TypeTypes.Healer,
    4 : TypeTypes.Dragon,
    5 : TypeTypes.God,
    6 : TypeTypes.Attacker,
    7 : TypeTypes.Devil,
    8 : TypeTypes.Machine,
    12 : TypeTypes.AwokenSkillMaterial,
    13 : TypeTypes.Protected,
    14 : TypeTypes.EnhanceMaterial,
    None : TypeTypes.NoType,
}


XpCurveTypes = Enum("XpCurveTypes", "One OnePointFive Two TwoPointFive Three ThreePointFive Four FourPointFive Five FivePointFive Six SixPointFive Seven SevenPointFive Eight EightPointFive NoCurve")
XpCurveIds = { 
    1000000 : XpCurveTypes.One,
    1500000 : XpCurveTypes.OnePointFive,
    2000000 : XpCurveTypes.Two,
    2500000 : XpCurveTypes.TwoPointFive,
    3000000 : XpCurveTypes.Three,
    3500000 : XpCurveTypes.ThreePointFive,
    4000000 : XpCurveTypes.Four,
    4500000 : XpCurveTypes.FourPointFive,
    5000000 : XpCurveTypes.Five,
    5500000 : XpCurveTypes.FivePointFive,
    6000000 : XpCurveTypes.Six,
    6500000 : XpCurveTypes.SixPointFive,
    7000000 : XpCurveTypes.Seven,
    7500000 : XpCurveTypes.SevenPointFive,
    8000000 : XpCurveTypes.Eight,
    8500000 : XpCurveTypes.EightPointFive,
    None : XpCurveTypes.NoCurve,
}


class ConstraintTypes(Enum):
   Element="El"
   Type = "Ty"
   NoneSet = "Nil"

ConstraintNoneTypes = Enum("ConstraintNoneTypes", "NoConstraint")
ConstraintNoneIds = {
    None : ConstraintNoneTypes.NoConstraint
}

ConstraintIds = {
    'elem' : ConstraintTypes.Element,
    'type' : ConstraintTypes.Type,
    None : ConstraintTypes.NoneSet,
}
ConstraintMap = {
    ConstraintTypes.Element : ElementIds,
    ConstraintTypes.Type : TypeIds,
    ConstraintTypes.NoneSet : ConstraintNoneIds,
}


class FoodTypes(Enum):
    Food = "Food"
    Monster = "Mstr"

FoodIds = {
    "food" : FoodTypes.Food,
    "monsters" : FoodTypes.Monster,
}

AttributeTypes = Enum("AttributeTypes", "Hp Atk Rcv")

AttributePlusMap = {
    AttributeTypes.Hp : 10,
    AttributeTypes.Atk : 5,
    AttributeTypes.Rcv : 3,
}

EventCountryTypes = Enum("EventCountryTypes", "Jp Us")
EventCountryIds = {
    1 : EventCountryTypes.Jp,
    2 : EventCountryTypes.Us,
}
