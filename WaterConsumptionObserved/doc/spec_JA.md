<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティ水消費量    
==========<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.WaterConsumption/blob/master/WaterConsumptionObserved/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな説明**スマート水道メーターモデルは、スマート水道メーターから発信される水使用量、顧客側の漏水アラーム、および関連する流量をキャプチャします。    
バージョン: 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## プロパティのリスト    
<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `acquisitionStageFailure[number]`: 計量器の誘導応答がない  - `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。      
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alarmFlowPersistence[string]`: 水の連続使用を示すアラーム  - `alarmInProgress[number]`: 1つ以上のアラームが進行中であることを示す  - `alarmStopsLeaks[number]`: 断続的な漏れの可能性を示すアラーム  - `alarmTamper[number]`: 機械的改ざんの可能性を示すアラーム  - `alarmWaterQuality[number]`: バックフロー発生の可能性を示すアラーム  - `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `id[*]`: エンティティの一意識別子  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `maxFlow[number]`: 直近1週間に観測された最大流量  - `minFlow[number]`: 直近1週間に観測された最低流量  - `moduleTampered[number]`: 計量装置からのモジュールの取り外し  - `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `persistenceFlowDuration[string]`: 持続流量（連続流量）がメーターによって記録される期間。分（m）、時間（h）、または日（d）で持続時間を示すテキストフィールド。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `type[string]`: WaterConsumptionObservedでなければならない。NGSIタイプ  - `waterConsumption[number]`: 水道メーターの読み取り値。注-これはメーターを通過した総量であり、従ってその時点の累計である。  - `waterType[string]`: 水温による水の種類。光熱費はお湯を区別する  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
必須プロパティ    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## プロパティのデータモデル記述    
アルファベット順（クリックで詳細表示）    
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
## ペイロードの例    
#### NGSI-v2 キー値の例    
以下はWaterConsumptionObservedをJSON-LD形式でkey-valuesとした例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。    
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
#### NGSI-v2 正規化例    
以下は、正規化された JSON-LD 形式の WaterConsumptionObserved の例である。これは、オプションを使用しない場合の NGSI-v2 と互換性があり、個々のエンティティのコンテキスト・データを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Consumer:Consumer01",  
  "type": "WaterConsumptionObserved",  
  "acquisitionStageFailure": {  
    "type": "Boolean",  
    "value": false  
  },  
  "alarmFlowPersistence": {  
    "type": "Text",  
    "value": "Nothing to report"  
  },  
  "alarmInProgress": {  
    "type": "Boolean",  
    "value": true  
  },  
  "alarmMetrology": {  
    "type": "Boolean",  
    "value": true  
  },  
  "alarmStopsLeaks": {  
    "type": "Boolean",  
    "value": false  
  },  
  "alarmSystem": {  
    "type": "Boolean",  
    "value": true  
  },  
  "alarmTamper": {  
    "type": "Boolean",  
    "value": false  
  },  
  "alarmWaterQuality": {  
    "type": "Boolean",  
    "value": false  
  },  
  "maxFlow": {  
    "type": "Number",  
    "value": 620  
  },  
  "minFlow": {  
    "type": "Boolean",  
    "value": true  
  },  
  "moduleTampered": {  
    "type": "Boolean",  
    "value": true  
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
#### NGSI-LD キー値の例    
以下はWaterConsumptionObservedをJSON-LD形式でkey-valuesとした例である。これは NGSI-LD と互換性があり、`options=keyValues` を使用すると、個々のエンティティのコンテキストデータを返す。    
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
#### NGSI-LDで正規化した例    
以下は、正規化された JSON-LD 形式の WaterConsumptionObserved の例である。これは、オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
