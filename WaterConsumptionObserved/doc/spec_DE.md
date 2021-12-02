Entität: WaterConsumptionObserved  
=================================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.WaterConsumption/blob/master/WaterConsumptionObserved/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Das Smart-Water-Meter-Modell erfasst den Wasserverbrauch, kundenseitige Leckagealarme und die zugehörige Durchflussmenge, die von den intelligenten Wasserzählern stammen**  

## Liste der Eigenschaften  

- `acquisitionStageFailure`: Kein induktives Ansprechen des Dosiergeräts  - `address`: Die Postanschrift  - `alarmFlowPersistence`: Alarm, der einen kontinuierlichen Wasserverbrauch anzeigt  - `alarmInProgress`: Zeigt an, dass ein oder mehrere Alarme anstehen  - `alarmStopsLeaks`: Alarm, der das Potenzial für ein intermittierendes Leck anzeigt  - `alarmTamper`: Alarm, der auf eine mögliche mechanische Manipulation des Geräts hinweist  - `alarmWaterQuality`: Alarm, der das mögliche Auftreten von Rückflüssen anzeigt  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `maxFlow`: Maximale Durchflussrate, die in der letzten Woche beobachtet wurde  - `minFlow`: Minimale Durchflussrate, die in der letzten Woche beobachtet wurde  - `moduleTampered`: Entfernen des Moduls aus dem Dosiergerät  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `persistenceFlowDuration`: Die Dauer, in der der Nachstrom (kontinuierlicher Durchfluss) vom Zähler erfasst wird. Textfeld, das Dauern in Minuten (m), Stunden (h) oder Tagen (d) anzeigt.  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `type`: Es muss WaterConsumptionObserved sein. NGSI-Typ  - `waterConsumption`: Der Wasserzählerstand. Hinweis - dies ist das gesamte Volumen, das durch den Zähler geleitet wurde, und ist daher eine kumulierte Summe zum Zeitpunkt    
Erforderliche Eigenschaften  
- `id`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
## Beispiel-Nutzlasten  
#### WaterConsumptionObserved NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen WaterConsumptionObserved im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### WaterConsumptionObserved NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen WaterConsumptionObserved im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
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
#### WaterConsumptionObserved NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen WaterConsumptionObserved im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### WaterConsumptionObserved NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen WaterConsumptionObserved im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
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
Siehe [FAQ 10](https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht