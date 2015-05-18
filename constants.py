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


TypeTypes = Enum("TypeTypes", "EvoMaterial Balanced Physical Healer Dragon God Attacker Devil AwokenSkillMaterial Protected EnhanceMaterial NoType")
TypeIds = { 
    0 : TypeTypes.EvoMaterial,
    1 : TypeTypes.Balanced,
    2 : TypeTypes.Physical,
    3 : TypeTypes.Healer,
    4 : TypeTypes.Dragon,
    5 : TypeTypes.God,
    6 : TypeTypes.Attacker,
    7 : TypeTypes.Devil,
    12 : TypeTypes.AwokenSkillMaterial,
    13 : TypeTypes.Protected,
    14 : TypeTypes.EnhanceMaterial,
    None : TypeTypes.NoType,
}


XpCurveTypes = Enum("XpCurveTypes", "One OnePointFive Two TwoPointFive Three  Four Five NoCurve")
XpCurveIds = { 
    1000000 : XpCurveTypes.One,
    1500000 : XpCurveTypes.OnePointFive,
    2000000 : XpCurveTypes.Two,
    2500000 : XpCurveTypes.TwoPointFive,
    3000000 : XpCurveTypes.Three,
    4000000 : XpCurveTypes.Four,
    5000000 : XpCurveTypes.Five,
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

# FilterTypes = Enum("FilterTypes", "Hp Atk Rcv")
# class FilterTypes(Enum):
#     HP = 

