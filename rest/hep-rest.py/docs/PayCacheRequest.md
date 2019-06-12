# PayCacheRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dapp_key** | **str** | The decentralized application access key | 
**protocol** | **str** | The protocol name. default is &#x27;HEP&#x27;. | 
**version** | **str** | The protocol version such as &#x27;1.0&#x27; | 
**ts** | **int** | The current timestamp | 
**nonce** | **str** | The random string or auto-increment sequence | 
**os** | **str** | The operating system of client such as ios, android, dweb,etc. | 
**language** | **str** | The i18n language code such as zh, en, etc. | 
**md5** | **str** | The HMAC authentication md5 checksum | 
**sign_type** | **str** | The signature Type,aka cryptographic algorithm. | 
**signature** | **str** | The signature hex string by application owner. The exclude fields is [sign_type, signature, md5]. | 
**uuid** | **str** | The request uuid | 
**dapp_id** | **str** | The decentralized application ID | 
**action** | **str** | The action name which value is &#x27;hep.pay.order&#x27; | 
**expired** | **int** | The expired timestamp | 
**description** | **str** | The order description | 
**price_currency** | **str** | The symbol of fiat or digital token, such as USD, CNY, NEW,BTC,ETH. | 
**total_price** | **str** | The amount of fiat or digital token, unit is the minimum unit of given fiat or digital token. | 
**order_number** | **str** | The order number | 
**seller** | **str** | The seller&#x27;s NewID | 
**customer** | **str** | The customer&#x27;s NewID | 
**broker** | **str** | The broker&#x27;s NewID. optional. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
