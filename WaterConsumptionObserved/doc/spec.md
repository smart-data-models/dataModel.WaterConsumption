Entity: WaterConsumptionObserved  
================================  
[Open License](https://github.com/smart-data-models//dataModel.WaterConsumption/blob/master/WaterConsumptionObserved/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **The Smart Water Meter model captures water consumption, customer side leak alarms and associated flow rate originating from the smart water meters**  

## List of properties  

- `acquisitionStageFailure`: No inductive response of metering device  - `address`: The mailing address  - `alarmFlowPersistence`: Alarm signifying continuous water use  - `alarmInProgress`: Indicates that one or more alarms are in progress  - `alarmStopsLeaks`: Alarm signifying the potential for an intermittent leak  - `alarmTamper`: Alarm signifying the potential of mechanical tampering with the device  - `alarmWaterQuality`: Alarm signifying the potential of backflows occurring  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `id`: Unique identifier of the entity  - `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `maxFlow`: Maximum flow rate observed during the last week  - `minFlow`: Minimum flow rate observed during the last week  - `moduleTampered`: Removal of module from metering device  - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `persistenceFlowDuration`: The duration that persistence flow (continuous flow) is recorded by the meter. Text  field showing durations in minutes (m), hours (h) or days (d).  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: It has to be WaterConsumptionObserved. NGSI type  - `waterConsumption`: The water meter reading. Note – this is total volume passed through the meter and is therefore a cumulative total at the time    
Required properties  
- `id`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WaterConsumptionObserved:    
  description: 'The Smart Water Meter model captures water consumption, customer side leak alarms and associated flow rate originating from the smart water meters'    
  properties:    
    acquisitionStageFailure:    
      description: 'No inductive response of metering device'    
      type: integer    
      x-ngsi:    
        type: Property    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alarmFlowPersistence:    
      description: 'Alarm signifying continuous water use'    
      enum:    
        - 'Nothing to report'    
        - 'No persistence'    
        - 'In progress impacting persistence'    
        - 'In progress persistence'    
        - 'Past Persistence during the period'    
      type: string    
      x-ngsi:    
        type: Property    
    alarmInProgress:    
      description: 'Indicates that one or more alarms are in progress'    
      enum:    
        - 0    
        - 1    
      type: integer    
      x-ngsi:    
        type: Property    
    alarmStopsLeaks:    
      description: 'Alarm signifying the potential for an intermittent leak'    
      enum:    
        - 0    
        - 1    
      type: integer    
      x-ngsi:    
        type: Property    
    alarmTamper:    
      description: 'Alarm signifying the potential of mechanical tampering with the device'    
      enum:    
        - 0    
        - 1    
      type: integer    
      x-ngsi:    
        type: Property    
    alarmWaterQuality:    
      description: 'Alarm signifying the potential of backflows occurring'    
      enum:    
        - 0    
        - 1    
      type: integer    
      x-ngsi:    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &waterconsumptionobserved_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    maxFlow:    
      description: 'Maximum flow rate observed during the last week'    
      type: integer    
      x-ngsi:    
        type: Property    
        units: litres/hour    
    minFlow:    
      description: 'Minimum flow rate observed during the last week'    
      type: integer    
      x-ngsi:    
        type: Property    
        units: litres/hour    
    moduleTampered:    
      description: 'Removal of module from metering device'    
      type: integer    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *waterconsumptionobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    persistenceFlowDuration:    
      description: 'The duration that persistence flow (continuous flow) is recorded by the meter. Text  field showing durations in minutes (m), hours (h) or days (d).'    
      enum:    
        - '15m < 60m'    
        - '60m < 3h'    
        - '3h < 6h'    
        - '6h < 12h'    
        - '12h < 24h'    
        - '24h < 2d'    
        - '2d < 4d'    
        - '4d < 8d'    
        - '8d < 15d'    
        - '15d < 30d'    
        - '30d < 90d'    
        - '90d < 180d'    
        - '> 180d'    
      type: string    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'It has to be WaterConsumptionObserved. NGSI type'    
      enum:    
        - WaterConsumptionObserved    
      type: string    
      x-ngsi:    
        type: Property    
    waterConsumption:    
      description: 'The water meter reading. Note – this is total volume passed through the meter and is therefore a cumulative total at the time'    
      type: integer    
      x-ngsi:    
        type: Property    
        units: 'Cubic meters'    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Example payloads    
#### WaterConsumptionObserved NGSI-v2 key-values Example    
Here is an example of a WaterConsumptionObserved in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:Consumer:Consumer01",  
  "type": "WaterConsumptionObserved",  
  "acquisitionStageFailure": 0,  
  "alarmFlowPersistence": "Nothing to report",  
  "alarmInProgress": 1,  
  "alarmMetrology": 1,  
  "alarmStopsLeaks": 0,  
  "alarmSystem": 1,  
  "alarmTamper": 0,  
  "alarmWaterQuality": 0,  
  "maxFlow": 620,  
  "minFlow": 1,  
  "moduleTampered": 1,  
  "persistenceFlowDuration": "3h < 6h",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -4.128871,  
      50.95822  
    ]  
  },  
  "waterConsumption": 191051  
}  
```  
#### WaterConsumptionObserved NGSI-v2 normalized Example    
Here is an example of a WaterConsumptionObserved in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:Consumer:Consumer01",  
  "type": "WaterConsumptionObserved",  
  "acquisitionStageFailure": {  
    "type": "Integer",  
    "value": 0  
  },  
  "alarmFlowPersistence": {  
    "type": "Text",  
    "value": "Nothing to report"  
  },  
  "alarmInProgress": {  
    "type": "Integer",  
    "value": 1  
  },  
  "alarmMetrology": {  
    "type": "Integer",  
    "value": 1  
  },  
  "alarmStopsLeaks": {  
    "type": "Integer",  
    "value": 0  
  },  
  "alarmSystem": {  
    "type": "Integer",  
    "value": 1  
  },  
  "alarmTamper": {  
    "type": "Integer",  
    "value": 0  
  },  
  "alarmWaterQuality": {  
    "type": "Integer",  
    "value": 0  
  },  
  "maxFlow": {  
    "type": "Number",  
    "value": 620  
  },  
  "minFlow": {  
    "type": "Number",  
    "value": 1  
  },  
  "moduleTampered": {  
    "type": "Integer",  
    "value": 1  
  },  
  "persistenceFlowDuration": {  
    "type": "Text",  
    "value": "3h < 6h"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -4.128871,  
        50.95822  
      ]  
    }  
  },  
  "waterConsumption": {  
    "type": "Number",  
    "value": 191051  
  }  
}  
```  
#### WaterConsumptionObserved NGSI-LD key-values Example    
Here is an example of a WaterConsumptionObserved in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:Consumer:Consumer01",  
  "type": "WaterConsumptionObserved",  
  "acquisitionStageFailure": 0,  
  "alarmFlowPersistence": "Nothing to report",  
  "alarmInProgress": 1,  
  "alarmMetrology": 1,  
  "alarmStopsLeaks": 0,  
  "alarmSystem": 1,  
  "alarmTamper": 0,  
  "alarmWaterQuality": 0,  
  "maxFlow": 620,  
  "minFlow": 1,  
  "moduleTampered": 1,  
  "persistenceFlowDuration": "3h < 6h",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -4.128871,  
      50.95822  
    ]  
  },  
  "waterConsumption": 191051,  
  "@context": [  
    "https://raw.githubusercontent.com/easy-global-market/ngsild-api-data-models/master/WaterSmartMeter/jsonld-contexts/waterSmartMeter-compound.jsonld",  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### WaterConsumptionObserved NGSI-LD normalized Example    
Here is an example of a WaterConsumptionObserved in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
    "id": "urn:ngsi-ld:Consumer:Consumer01",  
    "type": "WaterConsumptionObserved",  
    "acquisitionStageFailure": {  
        "type": "Property",  
        "observedBy": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Device:01"  
        },  
        "value": 0,  
        "observedAt": "2021-05-23T23:14:16.000Z"  
    },  
    "alarmFlowPersistence": {  
        "type": "Property",  
        "observedBy": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Device:01"  
        },  
        "value": "Nothing to report",  
        "observedAt": "2021-05-23T23:14:16.000Z"  
    },  
    "alarmInProgress": {  
        "type": "Property",  
        "observedBy": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Device:01"  
        },  
        "value": 1,  
        "observedAt": "2021-05-23T23:14:16.000Z"  
    },  
    "alarmMetrology": {  
        "type": "Property",  
        "observedBy": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Device:01"  
        },  
        "value": 1,  
        "observedAt": "2021-05-23T23:14:16.000Z"  
    },  
    "alarmStopsLeaks": {  
        "type": "Property",  
        "observedBy": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Device:01"  
        },  
        "value": 0,  
        "observedAt": "2021-05-23T23:14:16.000Z"  
    },  
    "alarmSystem": {  
        "type": "Property",  
        "observedBy": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Device:01"  
        },  
        "value": 1,  
        "observedAt": "2021-05-23T23:14:16.000Z"  
    },  
    "alarmTamper": {  
        "type": "Property",  
        "observedBy": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Device:01"  
        },  
        "value": 0,  
        "observedAt": "2021-05-23T23:14:16.000Z"  
    },  
    "alarmWaterQuality": {  
        "type": "Property",  
        "observedBy": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Device:01"  
        },  
        "value": 0,  
        "observedAt": "2021-05-23T23:14:16.000Z"  
    },  
    "maxFlow": {  
        "type": "Property",  
        "observedBy": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Device:01"  
        },  
        "value": 620,  
        "observedAt": "2021-05-23T23:14:16.000Z",  
        "unitCode": "E32"  
    },  
    "minFlow": {  
        "type": "Property",  
        "observedBy": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Device:01"  
        },  
        "value": 1,  
        "observedAt": "2021-05-23T23:14:16.000Z",  
        "unitCode": "E32"  
    },  
    "moduleTampered": {  
        "type": "Property",  
        "observedBy": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Device:01"  
        },  
        "value": 1,  
        "observedAt": "2021-05-23T23:14:16.000Z"  
    },  
    "persistenceFlowDuration": {  
        "type": "Property",  
        "observedBy": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Device:01"  
        },  
        "value": "3h < 6h",  
        "observedAt": "2021-05-23T23:14:16.000Z",  
        "unitCode": "HUR"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -4.128871,  
                50.95822  
            ]  
        }  
    },  
    "waterConsumption": {  
        "type": "Property",  
        "observedBy": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Device:01"  
        },  
        "value": 191051,  
        "observedAt": "2021-05-23T23:14:16.000Z",  
        "unitCode": "LTR"  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/easy-global-market/ngsild-api-data-models/master/WaterSmartMeter/jsonld-contexts/waterSmartMeter-compound.jsonld"  
    ]  
}  
```  
