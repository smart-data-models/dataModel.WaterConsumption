from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class AlarmFlowPersistence(Enum):
    Nothing_to_report = 'Nothing to report'
    No_persistence = 'No persistence'
    In_progress_impacting_persistence = 'In progress impacting persistence'
    In_progress_persistence = 'In progress persistence'
    Past_Persistence_during_the_period = 'Past Persistence during the period'


class AlarmInProgress(Enum):
    number_0 = 0
    number_1 = 1


class AlarmStopsLeaks(Enum):
    number_0 = 0
    number_1 = 1


class AlarmTamper(Enum):
    number_0 = 0
    number_1 = 1


class AlarmWaterQuality(Enum):
    number_0 = 0
    number_1 = 1


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class PersistenceFlowDuration(Enum):
    field_15m___60m = '15m < 60m'
    field_60m___3h = '60m < 3h'
    field_3h___6h = '3h < 6h'
    field_6h___12h = '6h < 12h'
    field_12h___24h = '12h < 24h'
    field_24h___2d = '24h < 2d'
    field_2d___4d = '2d < 4d'
    field_4d___8d = '4d < 8d'
    field_8d___15d = '8d < 15d'
    field_15d___30d = '15d < 30d'
    field_30d___90d = '30d < 90d'
    field_90d___180d = '90d < 180d'
    field__180d = '> 180d'


class Type6(Enum):
    WaterConsumptionObserved = 'WaterConsumptionObserved'


class WaterType(Enum):
    hotWater = 'hotWater'
    serviceWater = 'serviceWater'


class WaterConsumptionObserved(BaseModel):
    acquisitionStageFailure: Optional[float] = Field(
        None, description='No inductive response of metering device'
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    alarmFlowPersistence: Optional[AlarmFlowPersistence] = Field(
        None, description='Alarm signifying continuous water use'
    )
    alarmInProgress: Optional[AlarmInProgress] = Field(
        None, description='Indicates that one or more alarms are in progress'
    )
    alarmStopsLeaks: Optional[AlarmStopsLeaks] = Field(
        None, description='Alarm signifying the potential for an intermittent leak'
    )
    alarmTamper: Optional[AlarmTamper] = Field(
        None,
        description='Alarm signifying the potential of mechanical tampering with the device',
    )
    alarmWaterQuality: Optional[AlarmWaterQuality] = Field(
        None, description='Alarm signifying the potential of backflows occurring'
    )
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    maxFlow: Optional[float] = Field(
        None, description='Maximum flow rate observed during the last week'
    )
    minFlow: Optional[float] = Field(
        None, description='Minimum flow rate observed during the last week'
    )
    moduleTampered: Optional[float] = Field(
        None, description='Removal of module from metering device'
    )
    name: Optional[str] = Field(None, description='The name of this item')
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    persistenceFlowDuration: Optional[PersistenceFlowDuration] = Field(
        None,
        description='The duration that persistence flow (continuous flow) is recorded by the meter. Text  field showing durations in minutes (m), hours (h) or days (d)',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type6] = Field(
        None, description='It has to be WaterConsumptionObserved. NGSI type'
    )
    waterConsumption: Optional[float] = Field(
        None,
        description='The water meter reading. Note – this is total volume passed through the meter and is therefore a cumulative total at the time',
    )
    waterType: Optional[WaterType] = Field(
        None,
        description='The type of water by water temperature. Utility bills distinguish hot water',
    )
