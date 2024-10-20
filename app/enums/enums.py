from enum import Enum

class Relationship(Enum):
    MYSELF = 'Myself'
    SPOUSE_OR_PARTNER = 'Spouse'
    CHILD = 'Child'
    PARENTS_IN_LAWS = 'MyParents_and_In-laws'
    MY_EXTENDED_FAMILY = 'My_Extended_Family'


class CoverType(Enum):
    MYSELF = "Myself"
    ME_AND_MY_DIRECT_FAMILY = 'Me_And_My_Direct_Family'


class FamilyMember(Enum):
    FATHER_IN_LAW = 'Father-in-law'
    MOTHER_IN_LAW = 'Mother-in-law'
    FATHER = 'Father'
    MOTHER = 'Mother'
    AUNT = 'Aunt'
    UNCLE = 'Uncle'
    BROTHER = 'Brother'
    SISTER = 'Sister'
    BROTHER_IN_LAW = 'Brother-in-law'
    SISTER_IN_LAW = 'Sister-in-law'
    SON_IN_LAW = 'Son-in-law'
    DAUGHTER_IN_LAW = 'Daughter-in-law'
    GRAND_FATHER = 'Grand-father'
    GRAND_MOTHER = 'Grand-mother'
    GRAND_SON = 'Grand-son'
    GRAND_DAUGHTER = 'Grand-daughter'
    FIRST_COUSINS = 'First cousins'
    NIECE = 'Niece'
    NEPHEW = 'Nephew'
    SON = 'Son'
    DAUGHTER = 'Daughter'
    STEP_FATHER = 'Step father'
    STEP_MOTHER = 'Step mother'
    ADOPTIVE_FATHER = 'Adoptive father'
    ADOPTIVE_MOTHER = 'Adoptive mother'
    EX_HUSBAND = 'Ex-husband'
    EX_WIFE = 'Ex-wife'
    SPOUSE = "Spouse"
    CHILD = "Child"


class Category(Enum):
    ME_AND_MY_DIRECT_FAMILY = 'Me_And_MyDirectFamily'
    MY_PARENTS_AND_INLAWS = 'My_Parents_And_InLaws'
    MY_EXTENDED_FAMILY = 'My_Extended_Family'


class AccountType(Enum):
    SAVINGS = 'Savings'
    CURRENT = 'Current'
    # Add other account types if needed
