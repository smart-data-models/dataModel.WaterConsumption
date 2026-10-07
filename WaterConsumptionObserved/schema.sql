/* (Beta) Export of data model WaterConsumptionObserved of the subject dataModel.WaterConsumption for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE WaterConsumptionObserved_alarmFlowPersistence_type AS ENUM ('Nothing to report', 'No persistence', 'In progress impacting persistence', 'In progress persistence', 'Past Persistence during the period');
CREATE TYPE WaterConsumptionObserved_alarmInProgress_type AS ENUM ('0', '1');
CREATE TYPE WaterConsumptionObserved_alarmStopsLeaks_type AS ENUM ('0', '1');
CREATE TYPE WaterConsumptionObserved_alarmTamper_type AS ENUM ('0', '1');
CREATE TYPE WaterConsumptionObserved_alarmWaterQuality_type AS ENUM ('0', '1');
CREATE TYPE WaterConsumptionObserved_persistenceFlowDuration_type AS ENUM ('15m < 60m', '60m < 3h', '3h < 6h', '6h < 12h', '12h < 24h', '24h < 2d', '2d < 4d', '4d < 8d', '8d < 15d', '15d < 30d', '30d < 90d', '90d < 180d', '> 180d');
CREATE TYPE WaterConsumptionObserved_type AS ENUM ('WaterConsumptionObserved');
CREATE TYPE WaterConsumptionObserved_waterType_type AS ENUM ('hotWater', 'serviceWater');
CREATE TABLE WaterConsumptionObserved (
  "acquisitionStageFailure" NUMERIC,
  "address" JSON,
  "alarmFlowPersistence" WaterConsumptionObserved_alarmFlowPersistence_type,
  "alarmInProgress" WaterConsumptionObserved_alarmInProgress_type,
  "alarmStopsLeaks" WaterConsumptionObserved_alarmStopsLeaks_type,
  "alarmTamper" WaterConsumptionObserved_alarmTamper_type,
  "alarmWaterQuality" WaterConsumptionObserved_alarmWaterQuality_type,
  "alternateName" TEXT,
  "areaServed" TEXT,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "id" TEXT PRIMARY KEY,
  "location" JSON,
  "maxFlow" NUMERIC,
  "minFlow" NUMERIC,
  "moduleTampered" NUMERIC,
  "name" TEXT,
  "owner" JSON,
  "persistenceFlowDuration" WaterConsumptionObserved_persistenceFlowDuration_type,
  "seeAlso" JSON,
  "source" TEXT,
  "type" WaterConsumptionObserved_type,
  "waterConsumption" NUMERIC,
  "waterType" WaterConsumptionObserved_waterType_type
);