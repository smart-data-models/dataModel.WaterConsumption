<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Consumo d'acquaOsservato  
================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.WaterConsumption/blob/master/WaterConsumptionObserved/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Il modello Smart Water Meter acquisisce il consumo di acqua, gli allarmi di perdita lato cliente e la portata associata provenienti dai contatori intelligenti dell'acqua**.  
versione: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `acquisitionStageFailure[number]`: Nessuna risposta induttiva del dispositivo di misurazione  - `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.    
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alarmFlowPersistence[string]`: Allarme che segnala l'utilizzo continuo di acqua  - `alarmInProgress[number]`: Indica che sono in corso uno o più allarmi.  - `alarmStopsLeaks[number]`: Allarme che segnala la possibilità di una perdita intermittente  - `alarmTamper[number]`: Allarme che segnala la possibilità di manomissione meccanica del dispositivo.  - `alarmWaterQuality[number]`: Allarme che segnala la possibilità che si verifichino dei riflussi  - `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `maxFlow[number]`: Portata massima osservata nell'ultima settimana  - `minFlow[number]`: Portata minima osservata nell'ultima settimana  - `moduleTampered[number]`: Rimozione del modulo dal dispositivo di misurazione  - `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `persistenceFlowDuration[string]`: La durata del flusso persistente (flusso continuo) registrato dal contatore. Campo di testo che indica la durata in minuti (m), ore (h) o giorni (d).  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Deve essere WaterConsumptionObserved. Tipo NGSI  - `waterConsumption[number]`: La lettura del contatore dell'acqua. Nota: si tratta del volume totale passato attraverso il contatore ed è quindi un totale cumulativo al momento della lettura.  - `waterType[string]`: Il tipo di acqua in base alla temperatura dell'acqua. Le bollette distinguono l'acqua calda  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WaterConsumptionObserved:    
  description: 'The Smart Water Meter model captures water consumption, customer side leak alarms and associated flow rate originating from the smart water meters'    
  properties:    
    acquisitionStageFailure:    
      description: No inductive response of metering device    
      type: number    
      x-ngsi:    
        type: Property    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alarmFlowPersistence:    
      description: Alarm signifying continuous water use    
      enum:    
        - Nothing to report    
        - No persistence    
        - In progress impacting persistence    
        - In progress persistence    
        - Past Persistence during the period    
      type: string    
      x-ngsi:    
        type: Property    
    alarmInProgress:    
      description: Indicates that one or more alarms are in progress    
      enum:    
        - 0    
        - 1    
      type: number    
      x-ngsi:    
        type: Property    
    alarmStopsLeaks:    
      description: Alarm signifying the potential for an intermittent leak    
      enum:    
        - 0    
        - 1    
      type: number    
      x-ngsi:    
        type: Property    
    alarmTamper:    
      description: Alarm signifying the potential of mechanical tampering with the device    
      enum:    
        - 0    
        - 1    
      type: number    
      x-ngsi:    
        type: Property    
    alarmWaterQuality:    
      description: Alarm signifying the potential of backflows occurring    
      enum:    
        - 0    
        - 1    
      type: number    
      x-ngsi:    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
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
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    maxFlow:    
      description: Maximum flow rate observed during the last week    
      type: number    
      x-ngsi:    
        type: Property    
        units: litres/hour    
    minFlow:    
      description: Minimum flow rate observed during the last week    
      type: number    
      x-ngsi:    
        type: Property    
        units: litres/hour    
    moduleTampered:    
      description: Removal of module from metering device    
      type: number    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    persistenceFlowDuration:    
      description: 'The duration that persistence flow (continuous flow) is recorded by the meter. Text  field showing durations in minutes (m), hours (h) or days (d)'    
      enum:    
        - 15m < 60m    
        - 60m < 3h    
        - 3h < 6h    
        - 6h < 12h    
        - 12h < 24h    
        - 24h < 2d    
        - 2d < 4d    
        - 4d < 8d    
        - 8d < 15d    
        - 15d < 30d    
        - 30d < 90d    
        - 90d < 180d    
        - '> 180d'    
      type: string    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: It has to be WaterConsumptionObserved. NGSI type    
      enum:    
        - WaterConsumptionObserved    
      type: string    
      x-ngsi:    
        type: Property    
    waterConsumption:    
      description: The water meter reading. Note – this is total volume passed through the meter and is therefore a cumulative total at the time    
      type: number    
      x-ngsi:    
        type: Property    
        units: Cubic meters    
    waterType:    
      description: The type of water by water temperature. Utility bills distinguish hot water    
      enum:    
        - hotWater    
        - serviceWater    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.WaterConsumption/blob/master/WaterConsumptionObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Waterconsumption/WaterconsumptionObserved/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### WaterConsumptionObserved Valori-chiave NGSI-v2 Esempio  
Ecco un esempio di WaterConsumptionObserved in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### Consumo d'acqua osservato NGSI-v2 normalizzato Esempio  
Ecco un esempio di WaterConsumptionObserved in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### Consumo d'acqua osservato Valori chiave NGSI-LD Esempio  
Ecco un esempio di WaterConsumptionObserved in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
    "location": {  
        "type": "Point",  
        "coordinates": [  
            -4.128871,  
            50.95822  
        ]  
    },  
    "maxFlow": 620,  
    "minFlow": 1,  
    "moduleTampered": 1,  
    "persistenceFlowDuration": "3h < 6h",  
    "waterConsumption": 191051,  
    "@context": [  
        "https://raw.githubusercontent.com/easy-global-market/ngsild-api-data-models/master/WaterSmartMeter/jsonld-contexts/waterSmartMeter-compound.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterConsumption/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### Consumo d'acqua osservato Esempio normalizzato NGSI-LD  
Ecco un esempio di WaterConsumptionObserved in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
        "https://raw.githubusercontent.com/easy-global-market/ngsild-api-data-models/master/WaterSmartMeter/jsonld-contexts/waterSmartMeter-compound.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterConsumption/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
