#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


#  ============================================================================
#  BRICK DATA BASE DJANGO MODELS
#  ============================================================================
#  Author:      CingToo (CingToo@idbcgroup.com)
#  Version:     1.0.3
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
#   Version 1.0.2              27/06/2017
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
# ------------------------------------------------------ BRICK MODELS --------------------------------------------------

class Document(models.Model):
    documentCode = models.CharField(max_length=36, blank=True)
    transactionCode = models.CharField(max_length=36, blank=True)
    originatorCode = models.CharField(max_length=36, blank=True)
    originatorName = models.CharField(max_length=255, null=True)
    originatorType = models.CharField(max_length=255, null=True)
    receiverCode = models.CharField(max_length=36, null=True)
    receiverName = models.CharField(max_length=255, null=True)
    receiverType = models.CharField(max_length=255, null=True)
    documentType = models.CharField(max_length=255, blank=True)
    dateRequired = models.DateField(null=True)
    operationRoute = models.CharField(max_length=255, null=True)
    channelUsed = models.CharField(max_length=255, null=True)
    documentFunctionalStatus = models.CharField(max_length=255, blank=True)
    documentStatus = models.CharField(max_length=255, blank=True)
    movementReason = models.CharField(max_length=255, null=True)
    creationDate = models.DateField(blank=True)
    createdBy = models.CharField(max_length=255, blank=True)
    associatedDocumentType = models.CharField(max_length=255, null=True)
    associatedDocumentId = models.ForeignKey("self", null=True)
    referenceDocumentType = models.CharField(max_length=255, null=True)
    referenceDocumentNumber = models.CharField(max_length=255, null=True)
    referenceDocumentDate = models.DateField(null=True)
    referenceDocumentAmount = models.FloatField(null=True)
    referenceDocumentVat = models.FloatField(null=True)
    processedDateTime = models.DateField(null=True)
    lastAttempt = models.DateField(null=True)
    version = models.CharField(max_length=255, null=True)


class MovementItem(models.Model):
    documentCode = models.ForeignKey(Document, blank=True)
    transactionCode = models.CharField(max_length=255, blank=True)
    transactionDateTime = models.DateField(blank=True)
    description = models.CharField(max_length=255, null=True)
    itemFunctionalStatus = models.CharField(max_length=255, blank=True)
    itemStatus = models.CharField(max_length=255, blank=True)
    elementCode = models.ForeignKey('Product', blank=True)
    movedQuantity = models.IntegerField(blank=True)
    elementPresentation = models.CharField(max_length=255, blank=True)
    elementBmu = models.CharField(max_length=255, blank=True)
    elementUnitConversion = models.IntegerField(blank=True)
    barcode = models.CharField(max_length=255, null=True)
    salePrice = models.FloatField(blank=True)
    lastCost = models.FloatField(null=True)
    lastStdCost = models.FloatField(null=True)
    creationDate = models.DateField(blank=True)
    createdBy = models.CharField(max_length=255, blank=True)
    processedDateTime = models.DateField(null=True)
    lastAttempt = models.DateField(null=True)
    version = models.CharField(max_length=255, null=True)


class RequestItem(models.Model):
    documentCode = models.ForeignKey(Document, blank=True)
    transactionCode = models.CharField(max_length=255, blank=True)
    transactionDateTime = models.DateField(blank=True)
    description = models.CharField(max_length=255, null=True)
    itemFunctionalStatus = models.CharField(max_length=255, blank=True)
    itemStatus = models.CharField(max_length=255, blank=True)
    elementCode = models.ForeignKey('Product', null=True)
    requiredQuantity = models.IntegerField(blank=True)
    elementPresentation = models.CharField(max_length=255, blank=True)
    elementBmu = models.CharField(max_length=255, blank=True)
    elementUnitConversion = models.IntegerField(blank=True)
    processedQuantity = models.IntegerField(blank=True)
    reservedQuantity = models.IntegerField(blank=True)
    salePrice = models.FloatField(blank=True)
    inventoryAffectedDate = models.DateField(null=True)
    creationDate = models.DateField(blank=True)
    createdBy = models.CharField(max_length=255, blank=True)
    processedDateTime = models.DateField(null=True)
    lastAttempt = models.DateField(null=True)
    version = models.CharField(max_length=255, null=True)


# Values for the metadata in the table DocumentItemAttributes
# * expirationDate
# * reason
# * consignMaterial

class DocumentItemAttributes(models.Model):
    itemAttributesCode = models.CharField(max_length=255, blank=True)
    itemAttributesDescriptor = models.CharField(max_length=255, blank=True)
    parentItemAttributesCode = models.ForeignKey("self", null=True)
    movementItemId = models.ForeignKey(MovementItem, null=True)
    requestItemId = models.ForeignKey(RequestItem, null=True)
    metadataChain = models.IntegerField(default=1, null=True)
    descriptorCode01 = models.CharField(max_length=255, blank=True)
    descriptorName1 = models.CharField(max_length=255, blank=True)
    additionalValue01 = models.CharField(max_length=512, blank=True)
    descriptorCode02 = models.CharField(max_length=255, null=True)
    descriptorName2 = models.CharField(max_length=255, null=True)
    additionalValue02 = models.CharField(max_length=512, null=True)
    descriptorCode03 = models.CharField(max_length=255, null=True)
    descriptorName3 = models.CharField(max_length=255, null=True)
    additionalValue03 = models.CharField(max_length=512, null=True)
    metadataStatus = models.CharField(max_length=255, null=True)


# ----- PRODUCTS BRICK MODELS -----
class Product(models.Model):
    productCode = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=True, default="PRODUCT")
    category = models.CharField(max_length=255, blank=True)
    subcategory = models.CharField(max_length=255, null=True)
    family = models.CharField(max_length=255, null=True)
    equivalenceCode = models.CharField(max_length=255, null=True)
    measuredIn = models.CharField(max_length=255, blank=True)
    baseUnitMeasure = models.CharField(max_length=255, blank=True)
    bumSuggestedPrice = models.FloatField(blank=True)
    suggestedPriceDate = models.DateField(blank=True)
    defaultSalePresentation = models.CharField(max_length=255, null=True)
    defaultPurchasePresentation = models.CharField(max_length=255, null=True)
    bumLastCost = models.FloatField(blank=True)
    bumLastInventoryCost = models.FloatField(blank=True)
    taxCategory = models.CharField(max_length=255, blank=True)
    taxHandling = models.CharField(max_length=255, null=True)
    productCondition = models.CharField(max_length=255, blank=True)
    storageCondition = models.CharField(max_length=255, blank=True)
    pilingCondition = models.IntegerField(blank=True)
    productStatus = models.CharField(max_length=255, blank=True)
    imageFileName = models.CharField(max_length=255, blank=True)
    searchName1 = models.CharField(max_length=255, null=True)
    searchName2 = models.CharField(max_length=255, null=True)
    searchName3 = models.CharField(max_length=255, null=True)
    creationDate = models.DateField(blank=True)
    createdBy = models.CharField(max_length=255, blank=True)
    processedDateTime = models.DateField(blank=True)
    lastAttempt = models.DateField(blank=True)
    version = models.CharField(max_length=255, null=True)


# Values for the metadata in the table ProductAttributes
# * purchaseUnit
# * salesUnit
# * baseMaterial
# * length
# * width
# * high
# * dimensionsUnit
# * volume
# * dangerousMaterial
# * lotHandler
# * expirationDate
# * reason
# * grossWeight
# * netWeight
# * weightUnit
# * descriptionDetail
# * descriptionContent
# * productModel
# * technicalName
# * productColor
# * productStyle
# * consignproduct
# * usage
# * instructions

class ProductAttributes(models.Model):
    productAttributesCode = models.CharField(max_length=255, blank=True)
    productAttributesDescriptor = models.CharField(max_length=255, blank=True)
    parentProductAttributesId = models.ForeignKey("self", null=True)
    productCode = models.ForeignKey('Product', blank=True)
    metadataChain = models.IntegerField(null=True)
    descriptorCode01 = models.CharField(max_length=255, blank=True)
    descriptorName1 = models.CharField(max_length=255, blank=True)
    additionalValue01 = models.CharField(max_length=512, blank=True)
    descriptorCode02 = models.CharField(max_length=255, null=True)
    descriptorName2 = models.CharField(max_length=255, null=True)
    additionalValue02 = models.CharField(max_length=512, null=True)
    descriptorCode03 = models.CharField(max_length=255, null=True)
    descriptorName3 = models.CharField(max_length=255, null=True)
    additionalValue03 = models.CharField(max_length=512, null=True)
    metadataStatus = models.CharField(max_length=255, null=True)


class Warehouse(models.Model):
    warehouseCode = models.CharField(max_length=255, blank=True)
    warehouseName = models.CharField(max_length=255, blank=True)
    warehouseType = models.CharField(max_length=255, blank=True)
    warehouseStatus = models.CharField(max_length=255, blank=True)
    associatedRoute = models.CharField(max_length=255, null=True)
    creationDate = models.DateField(blank=True)
    createdBy = models.CharField(max_length=255, blank=True)
    processedDateTime = models.DateField(blank=True)
    lastAttempt = models.DateField(blank=True)
    version = models.CharField(max_length=255, null=True)


class ProductQuantity(models.Model):
    warehouseCode = models.ForeignKey(Warehouse, blank=True)
    productCode = models.ForeignKey('Product', blank=True)
    presentationCode = models.ForeignKey(ProductAttributes, blank=True)
    presentationName = models.CharField(max_length=255, blank=True)
    presentationContentInUbm = models.CharField(max_length=512, blank=True)
    presentationType = models.CharField(max_length=255, blank=True)
    productInventoryStatus = models.ForeignKey('InventoryStatus', blank=True)
    quantity = models.FloatField(blank=True)
    modifiedBy = models.CharField(max_length=255, blank=True)
    processedDateTime = models.CharField(max_length=255, blank=True)
    presentationPrice = models.FloatField(blank=True)


class CompositeProduct(models.Model):
    compositeProductCode = models.ForeignKey('Product', blank=True, related_name="compositeProductCode")
    componentProductCode = models.ForeignKey('Product', blank=True, related_name="componentProductCode")
    quantityComponent = models.FloatField(blank=True)
    uom = models.CharField(max_length=255, blank=True)
    modifiedBy = models.CharField(max_length=255, blank=True)
    processedDateTime = models.DateField(blank=True)


class InventoryStatus(models.Model):
    inventoryStatusCode = models.CharField(max_length=255, blank=True)
    inventoryStatusName = models.CharField(max_length=255, null=True)
    inventoryStatusAction01 = models.CharField(max_length=255, null=True)
    inventoryStatusAction02 = models.CharField(max_length=255, null=True)


# ----- USER & ACCESS BRICK MODELS -----
class LegalEntity(models.Model):
    legalEntityCode = models.CharField(max_length=255, blank=True)
    legalEntityType = models.CharField(max_length=255, blank=True)
    modificationDate = models.DateField(blank=True)
    creationDate = models.DateField(blank=True)
    createdBy = models.CharField(max_length=255, blank=True)


class User(models.Model):
    username = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    userRole = models.ForeignKey('BaseRole', blank=True)
    # legalEntityType = models.CharField(max_length=255) # This field may be accessed through legalEntityCode
    legalEntityCode = models.ForeignKey(LegalEntity, null=True)
    bpoKey = models.CharField(max_length=255, null=True)
    idDocumentNumber = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=255, null=True)
    birthday = models.DateField(null=True)
    userLogonStatus = models.CharField(max_length=255, blank=True)
    userAccountStatus = models.CharField(max_length=255, blank=True)
    loginAttempt = models.IntegerField(blank=True)
    loginAttemptTimeStamp = models.DateField(blank=True)
    sessionTimeStamp = models.DateField(blank=True)
    modificationDate = models.DateField(blank=True)
    creationDate = models.DateField(blank=True)
    createdBy = models.CharField(max_length=255, blank=True)


class BaseRole(models.Model):
    baseRoleCode = models.CharField(max_length=255, blank=True)
    baseRoleName = models.CharField(max_length=255, blank=True)
    baseRoleDescription = models.CharField(max_length=512, null=True)
    functionsDelegation = models.BooleanField(default=False)
    baseRoleStatus = models.CharField(max_length=255, blank=True, default="ACTIVE")
    baseRoleLevel = models.CharField(max_length=255, null=True)
    baseRoleAccessLevel = models.IntegerField(blank=True)
    baseRoleOperationLevel = models.CharField(max_length=255, blank=True)
    baseRoleDataAccessLevel = models.IntegerField(blank=True)
    modificationDate = models.DateField(blank=True)
    creationDate = models.DateField(blank=True)
    createdBy = models.CharField(max_length=255, blank=True)


class UserAttributes(models.Model):
    userAttributesCode = models.CharField(max_length=255, blank=True)
    userAttributesDescriptor = models.CharField(max_length=255, blank=True)
    parentUserAttributesId = models.ForeignKey("self", null=True)
    username = models.ForeignKey(User, blank=True)
    metadataChain = models.IntegerField(default=1, blank=True)
    descriptorCode01 = models.CharField(max_length=255, blank=True)
    descriptorName1 = models.CharField(max_length=255, blank=True)
    additionalValue01 = models.CharField(max_length=512, blank=True)
    descriptorCode02 = models.CharField(max_length=255, null=True)
    descriptorName2 = models.CharField(max_length=255, null=True)
    additionalValue02 = models.CharField(max_length=512, null=True)
    descriptorCode03 = models.CharField(max_length=255, null=True)
    descriptorName3 = models.CharField(max_length=255, null=True)
    additionalValue03 = models.CharField(max_length=512, null=True)
    metadataStatus = models.CharField(max_length=255, null=True)


class Function(models.Model):
    functionCode = models.CharField(max_length=255, blank=True)
    functionContext = models.CharField(max_length=255, null=True)
    functionTypeCode = models.CharField(max_length=255, blank=True, default="SERVICE")
    functionDescription = models.CharField(max_length=255, null=True)
    functionName = models.CharField(max_length=355, null=True)
    functionAccessLevel = models.IntegerField(blank=True, default=1)
    functionMenuOrder = models.CharField(max_length=255, null=True)
    functionParent = models.ForeignKey("self", null=True)
    functionStatus = models.CharField(max_length=255, blank=True, default="ACTIVE")
    authorizationType = models.CharField(max_length=255, null=True)
    operationType = models.CharField(max_length=255, blank=True)
    prodLastVersion = models.CharField(max_length=255, null=True)
    functionElectSignature = models.CharField(max_length=255, blank=True)
    modificationDate = models.DateField(blank=True)
    creationDate = models.DateField(blank=True)
    creationBy = models.CharField(max_length=255, blank=True)


class FunctionsAccessByRole(models.Model):
    functionCode = models.ForeignKey(Function, null=True, related_name="functionCode1")
    parentFunctionCode = models.ForeignKey(Function, null=True, related_name="parentFunctionCode")
    baseRoleCode = models.ForeignKey('BaseRole', blank=True)
    functionAccessLevel = models.IntegerField(blank=True)
    functionOperationLevel = models.CharField(max_length=255, blank=True)
    delegationLevel = models.IntegerField(blank=True)
    descriptorCode = models.CharField(max_length=255, blank=True)
    descriptorName = models.CharField(max_length=255, blank=True)
    additionalValue = models.CharField(max_length=512, blank=True)
    modificationDate = models.DateField(blank=True)
    creationDate = models.DateField(blank=True)
    createdBy = models.CharField(max_length=255, blank=True)


# ----- ONTOLOGY BRICK MODELS -----
class Catalog(models.Model):
    catalogName = models.CharField(max_length=255, blank=True)
    catalogType = models.CharField(max_length=255, blank=True)
    catalogDefaultValue = models.IntegerField(null=True)
    descriptorCode = models.CharField(max_length=255, null=True)
    catalogParentId = models.ForeignKey("self", null=True)
    modificationDate = models.DateField(blank=True)
    creationDate = models.DateField(blank=True)
    createdBy = models.CharField(max_length=255, blank=True)


class CatalogValues(models.Model):
    descriptorCode = models.CharField(max_length=255, blank=True)
    catalogLabel = models.CharField(max_length=255, blank=True)
    descriptorName = models.CharField(max_length=255, null=True)
    additionalValue = models.CharField(max_length=512, null=True)
    hasAdditionalValue = models.BooleanField(default=False, blank=True)
    catalogId = models.ForeignKey(Catalog, blank=True)
    catalogValueParentId = models.ForeignKey("self", null=True)
    modificationDate = models.DateField(blank=True)
    creationDate = models.DateField(blank=True)
    createdBy = models.CharField(max_length=255, blank=True)


class CatalogClassifier(models.Model):
    catalogClassifierCode = models.CharField(max_length=255, blank=True)
    catalogClassifierDescriptorCod = models.CharField(max_length=255, blank=True)
    catalogClassifierDescriptor = models.CharField(max_length=255, blank=True)
    metadataChain = models.IntegerField(default=1, blank=True)
    descriptorCode01 = models.CharField(max_length=255, blank=True)
    descriptorName1 = models.CharField(max_length=255, blank=True)
    additionalValue01 = models.CharField(max_length=512, blank=True)
    descriptorCode02 = models.CharField(max_length=255, null=True)
    descriptorName2 = models.CharField(max_length=255, null=True)
    additionalValue02 = models.CharField(max_length=512, null=True)
    descriptorCode03 = models.CharField(max_length=255, null=True)
    descriptorName3 = models.CharField(max_length=255, null=True)
    additionalValue03 = models.CharField(max_length=512, null=True)
    metadataStatus = models.BooleanField(default=True, blank=True)


class CatAddValues(models.Model):
    catalogValue = models.BooleanField(default=True, blank=True)
    catalogLabel = models.CharField(max_length=255, blank=True)
    catalogClassifierCode = models.ForeignKey(CatalogClassifier, null=True)
    catalogValueId = models.ForeignKey(CatalogValues, blank=True)
    metadataChain = models.IntegerField(default=1, blank=True)
    descriptorCode01 = models.CharField(max_length=255, blank=True)
    descriptorName1 = models.CharField(max_length=255, blank=True)
    additionalValue01 = models.CharField(max_length=512, blank=True)
    descriptorCode02 = models.CharField(max_length=255, null=True)
    descriptorName2 = models.CharField(max_length=255, null=True)
    additionalValue02 = models.CharField(max_length=512, null=True)
    descriptorCode03 = models.CharField(max_length=255, null=True)
    descriptorName3 = models.CharField(max_length=255, null=True)
    additionalValue03 = models.CharField(max_length=512, null=True)
    metadataStatus = models.BooleanField(default=True, blank=True)


class Parameter(models.Model):
    parametGroupId = models.ForeignKey("self", null=True)
    functionCode = models.ForeignKey(Function, null=True)
    parameterLevel = models.CharField(max_length=255, blank=True)
    parametGroupCode = models.CharField(max_length=255, blank=True)
    parametGroupDescriptor = models.CharField(max_length=255, blank=True)
    parametChain = models.IntegerField(null=True)
    descriptorCode01 = models.CharField(max_length=255, blank=True)
    descriptorName1 = models.CharField(max_length=255, blank=True)
    additionalValue01 = models.CharField(max_length=512, blank=True)
    descriptorCode02 = models.CharField(max_length=255, null=True)
    descriptorName2 = models.CharField(max_length=255, null=True)
    additionalValue02 = models.CharField(max_length=512, null=True)
    descriptorCode03 = models.CharField(max_length=255, null=True)
    descriptorName3 = models.CharField(max_length=255, null=True)
    additionalValue03 = models.CharField(max_length=512, null=True)
    parametStatus = models.CharField(max_length=255, null=True)
    modificationDate = models.DateField(blank=True)
    creationDate = models.DateField(blank=True)
    createdBy = models.CharField(max_length=255, blank=True)


# class Route(models.Model):
#     routeCode = models.CharField(max_length=255, blank=True)
#     catalogValueId = models.ForeignKey(CatalogValues)
#     routeName = models.CharField(max_length=255, null=True)
#     routeStatus = models.CharField(max_length=255, blank=True)
#     modificationDate = models.DateField(blank=True)
#     creationDate = models.DateField(blank=True)
#     createdBy = models.CharField(max_length=255, blank=True)


class DescriptorsAndMessages(models.Model):
    descriptorCode = models.CharField(max_length=255, blank=True)
    parentDescriptorCode = models.ForeignKey("self", null=True)
    descriptor = models.CharField(max_length=255, blank=True)
    descriptorType = models.CharField(max_length=255, blank=True)
    descriptorText = models.CharField(max_length=255, null=True)
    messageIndications = models.CharField(max_length=255, null=True)
    language = models.CharField(max_length=255, blank=True)
    term = models.CharField(max_length=255, blank=True)
    realm = models.CharField(max_length=255, blank=True)


class DescriptorAdditionalData(models.Model):
    descriptorCode = models.ForeignKey(DescriptorsAndMessages, blank=True)
    metadataChain = models.IntegerField(blank=True, default=1)
    descriptorCode01 = models.CharField(max_length=255, blank=True)
    descriptorName1 = models.CharField(max_length=255, blank=True)
    additionalValue01 = models.CharField(max_length=512, blank=True)
    descriptorCode02 = models.CharField(max_length=255, null=True)
    descriptorName2 = models.CharField(max_length=255, null=True)
    additionalValue02 = models.CharField(max_length=512, null=True)
    descriptorCode03 = models.CharField(max_length=255, null=True)
    descriptorName3 = models.CharField(max_length=255, null=True)
    additionalValue03 = models.CharField(max_length=512, null=True)
    metadataStatus = models.CharField(max_length=255, blank=True)


class DescriptorsVariants(models.Model):
    descriptorCode = models.ForeignKey(DescriptorsAndMessages, blank=True)
    descriptorText = models.CharField(max_length=1024, blank=True)
    messageIndications = models.CharField(max_length=1024, null=True)
    language = models.CharField(max_length=255, blank=True)
    realm = models.CharField(max_length=255, blank=True)


# ----- APPLICATION BRICK MODELS -----
class Customer(models.Model):
    customerCode = models.CharField(max_length=255, blank=True)
    legalEntityType = models.CharField(max_length=255, null=True)
    legalEntityCode = models.ForeignKey(LegalEntity, null=True)
    businessType = models.CharField(max_length=255, null=True)
    customerName = models.CharField(max_length=255, null=True)
    customerStatus = models.CharField(max_length=255, blank=True, default="ACTIVE")
    establishmentType = models.CharField(max_length=255, null=True)
    establishmentName = models.CharField(max_length=255, blank=True)
    yearsInEstablishment = models.IntegerField(blank=True)
    customerIsUser = models.BooleanField(default=True, blank=True)
    userRole = models.CharField(max_length=255, null=True)
    username = models.ForeignKey(User, null=True)
    assignedRoutecode = models.CharField(max_length=255, blank=True)
    modificationDate = models.DateField(blank=True)
    creationDate = models.DateField(blank=True)
    createdBy = models.CharField(max_length=255, blank=True)


class CustomerAttributes(models.Model):
    customerAttributesCode = models.CharField(max_length=255, blank=True)
    customerAttributesDescriptor = models.CharField(max_length=255, blank=True)
    parentCustomerAttributesId = models.ForeignKey("self", null=True)
    customerCode = models.ForeignKey(Customer, blank=True)
    metadataChain = models.IntegerField(default=1, blank=True)
    additionalValue01 = models.CharField(max_length=512, blank=True)
    descriptorCode02 = models.CharField(max_length=255, null=True)
    descriptorName2 = models.CharField(max_length=255, null=True)
    additionalValue02 = models.CharField(max_length=512, null=True)
    descriptorCode03 = models.CharField(max_length=255, null=True)
    descriptorName3 = models.CharField(max_length=255, null=True)
    additionalValue03 = models.CharField(max_length=512, null=True)
    metadataStatus = models.CharField(max_length=255, blank=True)
    modificationDate = models.DateField(blank=True)
    creationDate = models.DateField(blank=True)
    createdBy = models.CharField(max_length=255, blank=True)


class Vendor(models.Model):
    vendorCode = models.CharField(max_length=255, blank=True)
    vendorName = models.CharField(max_length=255, blank=True)
    legalEntityType = models.CharField(max_length=255, null=True)
    legalEntityCode = models.ForeignKey(LegalEntity, null=True)
    vendorResourceType = models.CharField(max_length=255, null=True)
    vendorType = models.CharField(max_length=255, blank=True, default="OUTSOURCIN")
    vendorClassification = models.CharField(max_length=255, blank=True)
    vendorStatus = models.CharField(max_length=255, blank=True, default="ACTIVE")
    vendorIsUser = models.BooleanField(default=True, blank=True)
    userRole = models.CharField(max_length=255, null=True)
    username = models.ForeignKey(User, null=True)
    assignedRouteCode = models.CharField(max_length=255, null=True)
    assignedWarehouseCode = models.CharField(max_length=255, null=True)
    modificationDate = models.DateField(blank=True)
    creationDate = models.DateField(blank=True)
    createdBy = models.CharField(max_length=255, blank=True)


class VendorAttributes(models.Model):
    vendorAttributesCode = models.CharField(max_length=255, blank=True)
    vendorAttributesDescriptor = models.CharField(max_length=255, blank=True)
    parentVendorAttributesId = models.ForeignKey("self", null=True)
    vendorCode = models.ForeignKey(Vendor, blank=True)
    metadataChain = models.IntegerField(default=1, blank=True)
    additionalValue01 = models.CharField(max_length=512, blank=True)
    descriptorCode02 = models.CharField(max_length=255, null=True)
    descriptorName2 = models.CharField(max_length=255, null=True)
    additionalValue02 = models.CharField(max_length=512, null=True)
    descriptorCode03 = models.CharField(max_length=255, null=True)
    descriptorName3 = models.CharField(max_length=255, null=True)
    additionalValue03 = models.CharField(max_length=512, null=True)
    metadataStatus = models.CharField(max_length=255, blank=True)
    modificationDate = models.DateField(blank=True)
    creationDate = models.DateField(blank=True)
    createdBy = models.CharField(max_length=255, blank=True)
