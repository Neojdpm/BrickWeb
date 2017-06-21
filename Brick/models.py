#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


#  ============================================================================
#  BRICK DATA BASE DJANGO MODELS
#  ============================================================================
#  Author:      CingToo (CingToo@idbcgroup.com)
#  Version:     1.0.0
#  History:
#   Version 1.0.1              2005-10-14
#        Author:      Pedro Perez (PPerez@yahoo.com)
#                  - Removed unnecesary code and fixed some minor bugs
#  ============================================================================
#  Description: …..
#               …..
#  ============================================================================
#  Comments: 
#       …..
#       …..
#       …..
#       …..
#       
#  ============================================================================
#  History:
#   Version 1.0.0              14/04/2017
#        Author:      cingtoo (cingtoo@idbcgroup.com)
#                     rromero (rromero@idbcgroup.com)
#                - Initial Definition Phase 1 brick Data Base
#  
#  ============================================================================
#                     **** Acknowledgements ****
#
#       
#  ============================================================================
#

class LegalEntity(models.Model):
    legalEntityCode = models.CharField(max_length=36, primary_key=True)
    legalEntityType = models.CharField(max_length=60)
    dateCreated = models.DateTimeField()


class LegalEntityAddress(models.Model):
    addressId = models.AutoField(primary_key=True)
    country = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    municipality = models.CharField(max_length=60)
    parish = models.CharField(max_length=60, null=True, blank=True)
    suburb = models.CharField(max_length=60)
    streetType = models.CharField(max_length=60)
    streetName = models.CharField(max_length=60)
    housingType = models.CharField(max_length=60)
    housingName = models.CharField(max_length=255)
    housingNumber = models.CharField(max_length=6, null=True, blank=True)
    floor = models.CharField(max_length=6, null=True, blank=True)
    apartmentNumber = models.CharField(max_length=6, null=True, blank=True)
    PostaZone = models.CharField(max_length=20)
    addressreference = models.CharField(max_length=255, null=True, blank=True)
    addressLongitude = models.CharField(max_length=36, null=True, blank=True)
    addressLatitude = models.CharField(max_length=36, null=True, blank=True)
    addressInMarkedInMap = models.CharField(max_length=255, null=True, blank=True)
    legalEntityCode = models.ForeignKey('LegalEntity', on_delete=models.CASCADE)


class LegalEntityAddData(models.Model):
    legalEntityAddDataId = models.AutoField(primary_key=True)
    legalEntityCode = models.ForeignKey('LegalEntity', on_delete=models.CASCADE)
    metadataChain = models.CharField(max_length=1)
    descriptorCode01 = models.CharField(max_length=36)
    descriptorName01 = models.CharField(max_length=255)
    additionalValue01 = models.CharField(max_length=255)
    descriptorCode02 = models.CharField(max_length=36, null=True, blank=True)
    descriptorName02 = models.CharField(max_length=255, null=True, blank=True)
    additionalValue02 = models.CharField(max_length=255, null=True, blank=True)
    descriptorCode03 = models.CharField(max_length=36, null=True, blank=True)
    descriptorName03 = models.CharField(max_length=255, null=True, blank=True)
    additionalValue03 = models.CharField(max_length=255, null=True, blank=True)
    metadataStatus = models.BooleanField()


class Bpo(models.Model):
    bpoCommonKey = models.CharField(max_length=36, primary_key=True)
    bpoKey = models.CharField(max_length=60)
    bpoName = models.CharField(max_length=60)
    bpoType = models.CharField(max_length=30)
    dateCreated = models.DateTimeField()


class Bpa(models.Model):
    bpaCode = models.CharField(max_length=36, primary_key=True)
    bpaCredentialType = models.CharField(max_length=60)
    bpaName = models.CharField(max_length=60)
    bpaRol = models.CharField(max_length=30)
    dateCreated = models.DateTimeField()
    LegalEntityType = models.CharField(max_length=60)
    legalEntityCode = models.ForeignKey('LegalEntity', on_delete=models.CASCADE)

    bpoKey = models.CharField(max_length=36)


class Citizen(models.Model):
    citizenCode = models.CharField(max_length=36, primary_key=True)
    idDocumentType = models.CharField(max_length=60)
    idDocumentNumber = models.CharField(max_length=30)
    firstName = models.CharField(max_length=255)
    firstLastName = models.CharField(max_length=255)
    secondName = models.CharField(max_length=255, null=True, blank=True)
    secondLastName = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=60)
    birthDate = models.DateField()
    nationality = models.CharField(max_length=60, null=True, blank=True)
    nationalityType = models.CharField(max_length=60, null=True, blank=True)
    legalEntityCode = models.ForeignKey('LegalEntity', on_delete=models.CASCADE)


class Institution(models.Model):
    institutionCode = models.CharField(max_length=36, primary_key=True)
    institutionName = models.CharField(max_length=255)
    idDocumentNumber = models.CharField(max_length=30)
    institutionType = models.CharField(max_length=60)
    institutionDescription = models.CharField(max_length=512, null=True, blank=True)
    institutionLevel = models.CharField(max_length=60, null=True, blank=True)
    institutionTaxCode = models.CharField(max_length=36, null=True, blank=True)
    legalEntityCode = models.ForeignKey('LegalEntity', on_delete=models.CASCADE)
    institutionParent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)


class WorkingHoliday(models.Model):
    workingHolidayId = models.AutoField(primary_key=True)
    holidayDescription = models.CharField(max_length=512)
    holidayDate = models.DateField()
    institutionCode = models.ForeignKey('Institution', on_delete=models.CASCADE)
    holidayMonth = models.CharField(max_length=60)
    holidayDay = models.IntegerField()
    holidayType = models.CharField(max_length=60)


class LegalEntityContact(models.Model):
    legalEntityContactId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=255)
    firstLastName = models.CharField(max_length=255)
    availableTime = models.CharField(max_length=60, null=True, blank=True)
    contactType = models.CharField(max_length=60)
    telephoneType01 = models.CharField(max_length=60)
    countryCode01 = models.CharField(max_length=10)
    areaCode01 = models.CharField(max_length=10)
    telephoneNumber01 = models.CharField(max_length=16)
    telephoneType02 = models.CharField(max_length=60, null=True, blank=True)
    countryCode02 = models.CharField(max_length=10, null=True, blank=True)
    areaCode02 = models.CharField(max_length=10, null=True, blank=True)
    telephoneNumber02 = models.CharField(max_length=16, null=True, blank=True)
    primaryEmail = models.CharField(max_length=255, null=True, blank=True)
    alternativeEmail = models.CharField(max_length=255, null=True, blank=True)
    jobPosition = models.CharField(max_length=60, null=True, blank=True)
    contactStatus = models.CharField(max_length=60)
    descriptorCode01 = models.CharField(max_length=36, null=True, blank=True)
    descriptorName01 = models.CharField(max_length=255, null=True, blank=True)
    additionalValue01 = models.CharField(max_length=512, null=True, blank=True)
    descriptorCode02 = models.CharField(max_length=36, null=True, blank=True)
    descriptorName02 = models.CharField(max_length=255, null=True, blank=True)
    additionalValue02 = models.CharField(max_length=512, null=True, blank=True)
    legalEntityCode = models.ForeignKey('0', on_delete=models.CASCADE)


class DistributionList(models.Model):
    distributionListId = models.AutoField(primary_key=True)
    contactGroup = models.ForeignKey('LegalEntityContact', on_delete=models.CASCADE)
    contactParticipant = models.ForeignKey('LegalEntityContact', on_delete=models.CASCADE)
    contactParticipantStatus = models.CharField(max_length=60)


class Bpi(models.Model):
    bpiCode = models.CharField(max_length=36, primary_key=True)
    legalEntityCode = models.CharField(max_length=36)
    bpiName = models.CharField(max_length=255)
    bpiLogoNameRoute = models.CharField(max_length=255, null=True, blank=True)
    institutionCode = models.ForeignKey('Institution', on_delete=models.CASCADE)


class AssignedRoute(models.Model):
    AssignedRouteId = models.AutoField(primary_key=True)
    BpaCode = models.ForeignKey('Bpa', on_delete=models.CASCADE)
    CatalogClassifierCode = models.ForeignKey('CatalogClassifier', on_delete=models.CASCADE)
    descriptorCode = models.CharField(max_length=36, null=True, blank=True)
    descriptorName = models.CharField(max_length=255, null=True, blank=True)
    additionalValue = models.CharField(max_length=512, null=True, blank=True)


class CoveredRoute(models.Model):
    AssignedRouteId = models.AutoField(primary_key=True)
    BpiCode = models.ForeignKey('Bpi', on_delete=models.CASCADE)
    CatalogClassifierCode = models.ForeignKey('CatalogClassifier', on_delete=models.CASCADE)
    descriptorCode = models.CharField(max_length=36, null=True, blank=True)
    descriptorName = models.CharField(max_length=255, null=True, blank=True)
    additionalValue = models.CharField(max_length=512, null=True, blank=True)


class DatePeriod(models.Model):
    datePeriodCode = models.CharField(max_length=36, primary_key=True)
    datePeriodStart = models.DateTimeField()
    datePeriodEnd = models.DateTimeField()
    periodEvaluation = models.CharField(max_length=60)
    periodType = models.CharField(max_length=60)


class FunctionType(models.Model):
    functionTypeCode = models.CharField(max_length=36, primary_key=True)
    functionTypeCodeParent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    functionTypeName = models.CharField(max_length=60)


class FunctionalArea(models.Model):
    functionalAreaCode = models.CharField(max_length=36, primary_key=True)
    functionalAreaCodeParent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    functionalAreaLevel = models.IntegerField()
    functionalAreaOrder = models.IntegerField()
    functionalAreaName = models.CharField(max_length=255)
    functionalAreaDescription = models.CharField(max_length=512)


class Function(models.Model):
    functionCode = models.CharField(max_length=36, primary_key=True)
    functionContext = models.CharField(max_length=60, null=True, blank=True)
    functionTypeCode = models.ForeignKey('FunctionType', on_delete=models.CASCADE)
    functionDescription = models.CharField(max_length=512, null=True, blank=True)
    functionName = models.CharField(max_length=255)
    functionAccessLevel = models.IntegerField()
    functionalAreaCode = models.ForeignKey('FunctionalArea', on_delete=models.CASCADE)
    functionElectSignature = models.CharField(max_length=512, null=True, blank=True)
    functionMenuOrder = models.ForeignKey('', on_delete=models.CASCADE)
    functionParent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    functionStatus = models.CharField(max_length=60)
    prodLastVersion = models.CharField(max_length=36)
    authorizationType = models.CharField(max_length=60)
    operationType = models.CharField(max_length=60, null=True, blank=True)


class FunctionMetadata(models.Model):
    functionMetadataId = models.AutoField(primary_key=True)
    functionCode = models.ForeignKey('Function', on_delete=models.CASCADE)
    metadataChain = models.CharField(max_length=1)
    descriptorCode01 = models.CharField(max_length=36)
    descriptorName01 = models.CharField(max_length=255)
    additionalValue01 = models.CharField(max_length=512, null=True, blank=True)
    descriptorCode02 = models.CharField(max_length=36, null=True, blank=True)
    descriptorName02 = models.CharField(max_length=255, null=True, blank=True)
    additionalValue02 = models.CharField(max_length=512, null=True, blank=True)
    descriptorCode03 = models.CharField(max_length=36, null=True, blank=True)
    descriptorName03 = models.CharField(max_length=255, null=True, blank=True)
    additionalValue03 = models.CharField(max_length=512, null=True, blank=True)
    metadataStatus = models.BooleanField()


class InfoType(models.Model):
    infotypeCode = models.CharField(max_length=36, primary_key=True)
    infotypeName = models.CharField(db_index=True, max_length=255)
    descriptorCode01 = models.CharField(max_length=36)
    infotypeDescription = models.CharField(max_length=512, null=True, blank=True)
    infotypeStatus = models.CharField(max_length=60, null=True, blank=True)
    infotypeParent = models.ForeignKey('self', on_delete=models.CASCADE)


class InfoTypeSpecs(models.Model):
    infotypeSpecsId = models.AutoField(primary_key=True)
    infotypeCode = models.ForeignKey('InfoType', on_delete=models.CASCADE)
    dataType = models.CharField(max_length=60)
    dataLengthPrecision = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    validationRule = models.CharField(max_length=60, null=True, blank=True)
    validationRuleValue01 = models.CharField(max_length=255, null=True, blank=True)
    validationRuleValue02 = models.CharField(max_length=255, null=True, blank=True)
    validationRuleValue03 = models.CharField(max_length=255, null=True, blank=True)
    FormatBd = models.CharField(max_length=255, null=True, blank=True)
    FormatField = models.CharField(max_length=255, null=True, blank=True)
    measuredIn = models.CharField(max_length=60, null=True, blank=True)
    unitOfMeasure = models.CharField(max_length=60, null=True, blank=True)


class DescriptorMessage(models.Model):
    descriptorCode = models.CharField(max_length=36, primary_key=True)
    descriptor = models.CharField(db_index=True, max_length=512)
    descriptorType = models.CharField(max_length=60, null=True, blank=True)
    descriptorText = models.CharField(max_length=4096)
    messageIndications = models.CharField(max_length=512, null=True, blank=True)
    language = models.CharField(max_length=60)
    term = models.CharField(max_length=60)
    realm = models.CharField(max_length=60)


class IndexExcludedWord(models.Model):
    indexExcludedWordId = models.AutoField(primary_key=True)
    wordType = models.CharField(max_length=60, null=True, blank=True)
    word = models.CharField(max_length=255)
    language = models.CharField(max_length=60)
    realm = models.CharField(max_length=60)


class ConceptNameIndex(models.Model):
    indexTextId = models.AutoField(primary_key=True)
    indexType = models.CharField(db_index=True, max_length=255)
    indexCode = models.CharField(db_index=True, max_length=4)
    language = models.CharField(max_length=60, null=True, blank=True)
    realm = models.CharField(max_length=60, null=True, blank=True)
    descriptor = models.ForeignKey('Descriptor&Message', on_delete=models.CASCADE, null=True, blank=True)
    conceptType01 = models.CharField(db_index=True, max_length=36, null=True, blank=True)
    conceptType02 = models.CharField(db_index=True, max_length=36, null=True, blank=True)
    conceptType03 = models.CharField(db_index=True, max_length=36, null=True, blank=True)


class IndexByConcept(models.Model):
    indexByConceptId = models.AutoField(primary_key=True)
    descriptorCode = models.ForeignKey('Descriptor&Message', on_delete=models.CASCADE)
    indexTextId = models.ForeignKey('ConceptNameIndex', on_delete=models.CASCADE)


class DescriptorVariant(models.Model):
    descriptorVariantId = models.AutoField(primary_key=True)
    descriptorCode = models.ForeignKey('Descriptor&Messages', on_delete=models.CASCADE)
    descriptorText = models.CharField(max_length=4096)
    messageIndications = models.CharField(max_length=512, null=True, blank=True)
    language = models.CharField(max_length=60)
    realm = models.CharField(max_length=60)


class PmeMessage(models.Model):
    pmeMessageCode = models.CharField(max_length=36, primary_key=True)
    messageType = models.CharField(max_length=60)
    messageAction = models.CharField(max_length=60, null=True, blank=True)
    messageSeverity = models.CharField(max_length=60, null=True, blank=True)
    messageAddLog = models.BooleanField()
    messageButtonResponse01 = models.CharField(max_length=60, null=True, blank=True)
    messageButtonResponse02 = models.CharField(max_length=60, null=True, blank=True)
    messageButtonResponse03 = models.CharField(max_length=60, null=True, blank=True)
    messageCode = models.CharField(max_length=36)
    messageDescription = models.CharField(max_length=255)
    messageIndication = models.CharField(max_length=255, null=True, blank=True)
    timeShowing = models.CharField(max_length=60, null=True, blank=True)
    messageShowView = models.CharField(max_length=60, null=True, blank=True)
    messageSendMail = models.BooleanField()
    legalEntityContactId = models.ForeignKey('LegalEntityContact', on_delete=models.CASCADE, null=True)


class PmeMessageParameter(models.Model):
    pmeMessageParameterId = models.AutoField(primary_key=True)
    pmeMessageCode = models.ForeignKey('PmeMessage', on_delete=models.CASCADE)
    retries = models.IntegerField()
    periodicity = models.IntegerField()
    periodicityPot = models.CharField(max_length=60)
    triesByRetry = models.IntegerField()
    sendEmail = models.IntegerField()
    messagingMail = models.CharField(max_length=60)


class SystemErrLog(models.Model):
    systemErrorLogId = models.AutoField(primary_key=True)
    bpaCode = models.ForeignKey('Bpa', on_delete=models.CASCADE)
    datePeriodCode = models.ForeignKey('DatePeriod', on_delete=models.CASCADE)
    pmeMessageCode = models.ForeignKey('PmeMessage', on_delete=models.CASCADE)
    userName = models.CharField(max_length=255)
    systemErrorLogEventType = models.CharField(max_length=60)
    systemErrorLogTimeStamp = models.DateTimeField()
    errorData = models.CharField(max_length=4096)


class SmnMessages(models.Model):
    smnMessageCode = models.CharField(max_length=36, primary_key=True)
    smnMessageType = models.CharField(max_length=60)
    smnMessageMedia = models.CharField(max_length=60, null=True, blank=True)
    smnMessageAddLog = models.BooleanField()
    smnMessageTitleCode = models.CharField(max_length=36)
    smnMessageTitle = models.CharField(max_length=256)
    smnMessageContent = models.CharField(max_length=4096)
    smnMessageIndication = models.CharField(max_length=512, null=True, blank=True)
    legalEntityContactId = models.ForeignKey('LegalEntityContact', on_delete=models.CASCADE)


class SmnAdditionalData(models.Model):
    smnAdditionalDataId = models.AutoField(primary_key=True)
    smnMessageCode = models.ForeignKey('SmnMessages', on_delete=models.CASCADE)
    metadataChain = models.CharField(max_length=1)
    descriptorCode01 = models.CharField(max_length=36)
    descriptorName01 = models.CharField(max_length=255)
    descriptorValue01 = models.CharField(max_length=512)
    descriptorCode02 = models.CharField(max_length=36, null=True, blank=True)
    descriptorName02 = models.CharField(max_length=255, null=True, blank=True)
    additionalValue02 = models.CharField(max_length=512, null=True, blank=True)
    descriptorCode03 = models.CharField(max_length=36, null=True, blank=True)
    descriptorName03 = models.CharField(max_length=255, null=True, blank=True)
    additionalValue03 = models.CharField(max_length=512, null=True, blank=True)
    metadataStatus = models.BooleanField()


class SmnLog(models.Model):
    systemErrorLogId = models.AutoField(primary_key=True)
    bpaCodeSender = models.ForeignKey('Bpa', on_delete=models.CASCADE)
    datePeriodCode = models.ForeignKey('DatePeriod', on_delete=models.CASCADE)
    smnMessageCode = models.ForeignKey('SmnMessage', on_delete=models.CASCADE)
    bpaCodeReceiver = models.ForeignKey('Bpa', on_delete=models.CASCADE)
    logMessageType = models.CharField(max_length=60)
    logTimeStamp = models.DateTimeField()


class ParametGroup(models.Model):
    parametGroupCode = models.CharField(max_length=36, primary_key=True)
    parametGroupCodeParent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    parametGroupDescription = models.CharField(max_length=512, null=True, blank=True)
    parameterType = models.CharField(max_length=60)
    parameterLevel = models.CharField(max_length=60)
    functionCode = models.ForeignKey('Function', on_delete=models.CASCADE, null=True, blank=True)
    applicationName = models.CharField(max_length=60, null=True, blank=True)


class ParametValues(models.Model):
    parametValueId = models.AutoField(primary_key=True)
    descriptorCode = models.CharField(max_length=36)
    descriptorName = models.CharField(max_length=255)
    additionalValue = models.CharField(max_length=512)
    parameterDescription = models.CharField(max_length=512, null=True, blank=True)
    parameterDefinitionHelp = models.CharField(max_length=512, null=True, blank=True)
    parametGroupCode = models.ForeignKey('ParametGroup', on_delete=models.CASCADE)


class Catalog(models.Model):
    catalogId = models.AutoField(primary_key=True)
    catalogName = models.CharField(max_length=255)
    catalogType = models.CharField(max_length=60)
    catalogDefaultValue = models.IntegerField()
    descriptorCode = models.CharField(max_length=36)
    catalogParentId = models.ForeignKey('self', on_delete=models.CASCADE)


class CatalogValues(models.Model):
    catalogValueId = models.AutoField(primary_key=True)
    descriptorCode = models.ForeignKey('', on_delete=models.CASCADE)
    catalogLabel = models.CharField(max_length=255)
    catalogIsValue = models.BooleanField()
    descriptorName = models.CharField(max_length=255, null=True, blank=True)
    additionalValue = models.CharField(max_length=512, null=True, blank=True)
    hasAdditionalValues = models.BooleanField()
    catalogId = models.ForeignKey('Catalog', on_delete=models.CASCADE)
    catalogValueParentId = models.ForeignKey('self', on_delete=models.CASCADE, null=True)


class CatAddValues(models.Model):
    additionalValueId = models.AutoField(primary_key=True)
    catalogIsValue = models.BooleanField()
    metadataChain = models.CharField(max_length=1)
    descriptorCode01 = models.CharField(max_length=36)
    descriptorName01 = models.CharField(max_length=255)
    additionalValue01 = models.CharField(max_length=512)
    descriptorCode02 = models.CharField(max_length=36, null=True, blank=True)
    descriptorName02 = models.CharField(max_length=255, null=True, blank=True)
    additionalValue02 = models.CharField(max_length=512, null=True, blank=True)
    descriptorCode03 = models.CharField(max_length=36, null=True, blank=True)
    descriptorName03 = models.CharField(max_length=255, null=True, blank=True)
    additionalValue03 = models.CharField(max_length=512, null=True, blank=True)
    metadataStatus = models.BooleanField()
    catalogClassifierCode = models.ForeignKey('CatalogClassifier', on_delete=models.CASCADE, null=True, blank=True)
    catalogValueId = models.ForeignKey('CatalogValues', on_delete=models.CASCADE)


class IndexByCatalog(models.Model):
    indexByConceptId = models.AutoField(primary_key=True)
    catalogValueId = models.ForeignKey('CatalogValue', on_delete=models.CASCADE)
    indexTextId = models.ForeignKey('ConceptNameIndex', on_delete=models.CASCADE)


class CatalogClassifier(models.Model):
    catalogClassifierCode = models.CharField(max_length=36, primary_key=True)
    metadataChain = models.CharField(max_length=1)
    descriptorCode01 = models.CharField(max_length=36)
    descriptorName01 = models.CharField(max_length=255)
    additionalValue01 = models.CharField(max_length=255)
    descriptorCode02 = models.CharField(max_length=36, null=True, blank=True)
    descriptorName02 = models.CharField(max_length=255, null=True, blank=True)
    additionalValue02 = models.CharField(max_length=255, null=True, blank=True)
    descriptorCode03 = models.CharField(max_length=36, null=True, blank=True)
    descriptorName03 = models.CharField(max_length=255, null=True, blank=True)
    additionalValue03 = models.CharField(max_length=255, null=True, blank=True)
    metadataStatus = models.BooleanField()


class Customer(models.Model):
    customerCode = models.CharField(max_length=36, primary_key=True)
    bpaCode = models.CharField(max_length=36, null=True, blank=True)
    customerCredential = models.ForeignKey('', on_delete=models.CASCADE)
    legalEntityType = models.ForeignKey('', on_delete=models.CASCADE)
    businessType = models.CharField(max_length=60)
    customerClasification = models.CharField(max_length=60)
    customerName = models.CharField(max_length=255)
    customerStatus = models.CharField(max_length=255)
    establishmentType = models.CharField(max_length=255, null=True, blank=True)
    establishmentName = models.CharField(max_length=255, null=True, blank=True)
    yearsInEstablishment = models.CharField(max_length=255, null=True, blank=True)
    customerIsUser = models.BooleanField()
    userRol = models.DateField()
    assignedRouteCode = models.CharField(max_length=255, null=True, blank=True)
    customerSalesman = models.CharField(max_length=36)
    customerSalesmanDate = models.DateField()
    registeredDate = models.DateField()
    customerRegisteredBy = models.CharField(max_length=36)
    lastModified = models.DateField()


class CustomerAddData(models.Model):
    customerAddDataId = models.AutoField(primary_key=True)
    CustomerId = models.ForeignKey('Customer', on_delete=models.CASCADE)
    metadataChain = models.CharField(max_length=1)
    descriptorCode01 = models.CharField(max_length=36)
    descriptorName01 = models.CharField(max_length=255)
    additionalValue01 = models.CharField(max_length=512, null=True, blank=True)
    descriptorCode02 = models.CharField(max_length=36, null=True, blank=True)
    descriptorName02 = models.CharField(max_length=255, null=True, blank=True)
    additionalValue02 = models.CharField(max_length=512, null=True, blank=True)
    descriptorCode03 = models.CharField(max_length=36, null=True, blank=True)
    descriptorName03 = models.CharField(max_length=255, null=True, blank=True)
    additionalValue03 = models.CharField(max_length=512, null=True, blank=True)
    metadataStatus = models.BooleanField()


class BaseRole(models.Model):
    baseRoleCode = models.CharField(max_length=36, primary_key=True)
    baseRoleName = models.CharField(max_length=255)
    baseRoleType = models.CharField(max_length=60)
    baseRoleDescription = models.CharField(max_length=512, null=True, blank=True)
    functionsDelegation = models.BooleanField()
    baseRoleStatus = models.CharField(max_length=60)


class SingleSignOnUser(models.Model):
    singleSignOnUserId = models.CharField(max_length=36, primary_key=True)
    password = models.CharField(max_length=60)
    userName = models.CharField(db_index=True, max_length=60)
    userLogonStatus = models.CharField(max_length=60)
    userAccountStatus = models.CharField(max_length=60)
    loginAttempt = models.IntegerField(null=True)
    loginAttemptTimeStamp = models.DateTimeField()
    sessionTimeStamp = models.DateTimeField()
    bpaCode = models.ForeignKey('Bpa', on_delete=models.CASCADE)
    ssoUserLevel = models.CharField(max_length=60, null=True, blank=True)
    ssoUserAccessLevel = models.IntegerField(null=True)
    ssoUserOperationLevel = models.CharField(max_length=4, null=True, blank=True)
    lastLogonDate = models.DateTimeField()


class LogonLog(models.Model):
    logonLogId = models.AutoField(primary_key=True)
    singleSignOnUserId = models.ForeignKey('SingleSignOnUser', on_delete=models.CASCADE)
    userIdChangingData = models.ForeignKey('SingleSignOnUser', on_delete=models.CASCADE, null=True)
    logonLogEventType = models.CharField(max_length=60)
    password = models.CharField(max_length=60, null=True, blank=True)
    userName = models.CharField(max_length=255)
    loginAttempt = models.IntegerField(null=True)
    loginAttemptTimeStamp = models.DateTimeField()
    sessionTimeStamp = models.DateTimeField()
    timeStampLastLogon = models.DateTimeField()
    logonIp = models.CharField(max_length=36, null=True, blank=True)


class AccessGroup(models.Model):
    accessGroupCode = models.CharField(max_length=36, primary_key=True)
    accessGroupName = models.CharField(max_length=255, null=True, blank=True)
    accessGroupUse = models.CharField(max_length=512, null=True, blank=True)
    accessGroupUserLevel = models.CharField(max_length=60)
    accessGroupStatus = models.CharField(max_length=60)


class FunctionsByAccessGroup(models.Model):
    functionsByAccessGroupId = models.AutoField(primary_key=True)
    functionCode = models.ForeignKey('Function', on_delete=models.CASCADE)
    ParentFunctionCode = models.ForeignKey('Function', on_delete=models.CASCADE, null=True, blank=True)
    accessGroupCode = models.ForeignKey('AccessGroup', on_delete=models.CASCADE)
    functionAccessLevel = models.IntegerField()
    functionOperationLevel = models.CharField(max_length=4, null=True, blank=True)
    delegationLevel = models.IntegerField(null=True)
    descriptorCode = models.CharField(max_length=36, null=True, blank=True)
    descriptorName = models.CharField(max_length=255, null=True, blank=True)
    additionalValue = models.CharField(max_length=512, null=True, blank=True)


class FunctionsAccessByRol(models.Model):
    accessByRolId = models.AutoField(primary_key=True)
    functionCode = models.ForeignKey('Function', on_delete=models.CASCADE)
    ParentFunctionCode = models.ForeignKey('Function', on_delete=models.CASCADE, null=True, blank=True)
    baseRoleCode = models.ForeignKey('BaseRole', on_delete=models.CASCADE)
    functionAccessLevel = models.IntegerField()
    functionOperationLevel = models.CharField(max_length=4, null=True, blank=True)
    delegationLevel = models.IntegerField(null=True)
    descriptorCode = models.CharField(max_length=36, null=True, blank=True)
    descriptorName = models.CharField(max_length=255, null=True, blank=True)
    additionalValue = models.CharField(max_length=512, null=True, blank=True)


class AccessGroupAssigned(models.Model):
    accessGroupAssignedId = models.AutoField(primary_key=True)
    accessGroupCode = models.ForeignKey('AccessGroup', on_delete=models.CASCADE)
    baseRoleCode = models.ForeignKey('BaseRole', on_delete=models.CASCADE)
    accessGroupAssignedStatus = models.CharField(max_length=60)


class DataDictionary(models.Model):
    dataDictionaryCode = models.CharField(max_length=36, primary_key=True)
    infotypeCode = models.CharField(max_length=36, primary_key=True)
    useInfotypeProperties = models.BooleanField()
    dataName = models.CharField(max_length=255)
    dataNameCode = models.CharField(max_length=255)
    dataDescription = models.CharField(max_length=512, null=True, blank=True)
    dataDescriptionCode = models.ForeignKey('Descriptor&Message', on_delete=models.CASCADE)
    dataLabel = models.CharField(max_length=255)
    dataLabelCode = models.CharField(max_length=255)
    dataSourceType = models.CharField(max_length=60)
    dataSourcename = models.CharField(max_length=255, null=True, blank=True)
    dataCalculated = models.CharField(max_length=255, null=True, blank=True)
    dataType = models.CharField(max_length=60)
    dataLengthPrecision = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    dataDefaultValue = models.CharField(max_length=255, null=True, blank=True)
    dataDefaultValueCode = models.CharField(max_length=255, null=True, blank=True)
    dataMandatory = models.IntegerField()
    validationRule = models.CharField(max_length=60, null=True, blank=True)
    validationRuleValue01 = models.CharField(max_length=255, null=True, blank=True)
    validationRuleValue02 = models.CharField(max_length=255, null=True, blank=True)
    validationRuleValue03 = models.CharField(max_length=255, null=True, blank=True)
    FormatBd = models.CharField(max_length=255, null=True, blank=True)
    usedInForms = models.BooleanField()
    measuredIn = models.CharField(max_length=60, null=True, blank=True)
    unitOfMeasure = models.CharField(max_length=60, null=True, blank=True)


class DataDictMetadata(models.Model):
    DataDictMetaDataId = models.AutoField(primary_key=True)
    dataDictionaryCode = models.ForeignKey('DataDictionary', on_delete=models.CASCADE)
    metadataChain = models.CharField(max_length=1)
    descriptorCode01 = models.CharField(max_length=36)
    descriptorName01 = models.CharField(max_length=255)
    additionalValue01 = models.CharField(max_length=512, null=True, blank=True)
    descriptorCode02 = models.CharField(max_length=36, null=True, blank=True)
    descriptorName02 = models.CharField(max_length=255, null=True, blank=True)
    additionalValue02 = models.CharField(max_length=512, null=True, blank=True)
    descriptorCode03 = models.CharField(max_length=36, null=True, blank=True)
    descriptorName03 = models.CharField(max_length=255, null=True, blank=True)
    additionalValue03 = models.CharField(max_length=512, null=True, blank=True)
    metadataStatus = models.BooleanField()


class MasterDataLog(models.Model):
    masterDataLogId = models.AutoField(primary_key=True)
    bpoCommonKey = models.ForeignKey('', on_delete=models.CASCADE)
    bpoType = models.CharField(max_length=60)
    bpoName = models.CharField(max_length=255)
    datePeriod = models.ForeignKey('DatePeriod', on_delete=models.CASCADE)
    functionCode = models.CharField(max_length=36)
    operationTransaction = models.CharField(max_length=60)
    bpa = models.ForeignKey('Bpa', on_delete=models.CASCADE)
    authorizedBy = models.ForeignKey('', on_delete=models.CASCADE, null=True, blank=True)
    dateTimeTag = models.ForeignKey('', on_delete=models.CASCADE)
    authenticationKey = models.CharField(max_length=512)


class MasterAddData(models.Model):
    masterAddDataId = models.AutoField(primary_key=True)
    descriptorCode01 = models.CharField(max_length=36)
    descriptorName1 = models.CharField(max_length=255)
    AdditionalValue01 = models.CharField(max_length=60)
    descriptorCode02 = models.CharField(max_length=36, null=True, blank=True)
    descriptorName2 = models.CharField(max_length=255, null=True, blank=True)
    AdditionalValue02 = models.CharField(max_length=60, null=True, blank=True)
    AdditionalValue03 = models.CharField(max_length=255, null=True, blank=True)
    metadataStatus = models.BooleanField()
    masterDataLogId = models.ForeignKey('MasterDataLog', on_delete=models.CASCADE)


class TxAuthenticationLog(models.Model):
    txAutheLogId = models.AutoField(primary_key=True)
    bpaCode = models.ForeignKey('Bpa', on_delete=models.CASCADE)
    txCode = models.CharField(max_length=60)
    bpoCommonKey = models.CharField(max_length=36)
    dateTimeTag = models.DateTimeField()
    authenticationKey = models.CharField(max_length=512)
