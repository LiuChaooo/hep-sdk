<?php
/**
 * AuthCacheResponse
 *
 * PHP version 5
 *
 * @category Class
 * @package  HepRestApi
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */

/**
 * HEP REST API
 *
 * The REST API for HEP protocol
 *
 * OpenAPI spec version: v1
 * Contact: xiawu@zeuux.org
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 * Swagger Codegen version: 3.0.8
 */
/**
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen
 * Do not edit the class manually.
 */

namespace HepRestApi\Model;

use \ArrayAccess;
use \HepRestApi\ObjectSerializer;

/**
 * AuthCacheResponse Class Doc Comment
 *
 * @category Class
 * @package  HepRestApi
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class AuthCacheResponse implements ModelInterface, ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $swaggerModelName = 'AuthCacheResponse';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerTypes = [
        'dapp_key' => 'string',
'protocol' => 'string',
'version' => 'string',
'ts' => 'int',
'nonce' => 'string',
'os' => 'string',
'language' => 'string',
'dapp_signature_method' => 'string',
'dapp_signature' => 'string',
'sign_type' => 'string',
'signature' => 'string',
'dapp_id' => 'string',
'uuid' => 'string',
'action' => 'string',
'scope' => 'int',
'expired' => 'int',
'memo' => 'string'    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerFormats = [
        'dapp_key' => null,
'protocol' => null,
'version' => null,
'ts' => null,
'nonce' => null,
'os' => null,
'language' => null,
'dapp_signature_method' => null,
'dapp_signature' => null,
'sign_type' => null,
'signature' => null,
'dapp_id' => null,
'uuid' => null,
'action' => null,
'scope' => null,
'expired' => null,
'memo' => null    ];

    /**
     * Array of property to type mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function swaggerTypes()
    {
        return self::$swaggerTypes;
    }

    /**
     * Array of property to format mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function swaggerFormats()
    {
        return self::$swaggerFormats;
    }

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @var string[]
     */
    protected static $attributeMap = [
        'dapp_key' => 'dapp_key',
'protocol' => 'protocol',
'version' => 'version',
'ts' => 'ts',
'nonce' => 'nonce',
'os' => 'os',
'language' => 'language',
'dapp_signature_method' => 'dapp_signature_method',
'dapp_signature' => 'dapp_signature',
'sign_type' => 'sign_type',
'signature' => 'signature',
'dapp_id' => 'dapp_id',
'uuid' => 'uuid',
'action' => 'action',
'scope' => 'scope',
'expired' => 'expired',
'memo' => 'memo'    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'dapp_key' => 'setDappKey',
'protocol' => 'setProtocol',
'version' => 'setVersion',
'ts' => 'setTs',
'nonce' => 'setNonce',
'os' => 'setOs',
'language' => 'setLanguage',
'dapp_signature_method' => 'setDappSignatureMethod',
'dapp_signature' => 'setDappSignature',
'sign_type' => 'setSignType',
'signature' => 'setSignature',
'dapp_id' => 'setDappId',
'uuid' => 'setUuid',
'action' => 'setAction',
'scope' => 'setScope',
'expired' => 'setExpired',
'memo' => 'setMemo'    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'dapp_key' => 'getDappKey',
'protocol' => 'getProtocol',
'version' => 'getVersion',
'ts' => 'getTs',
'nonce' => 'getNonce',
'os' => 'getOs',
'language' => 'getLanguage',
'dapp_signature_method' => 'getDappSignatureMethod',
'dapp_signature' => 'getDappSignature',
'sign_type' => 'getSignType',
'signature' => 'getSignature',
'dapp_id' => 'getDappId',
'uuid' => 'getUuid',
'action' => 'getAction',
'scope' => 'getScope',
'expired' => 'getExpired',
'memo' => 'getMemo'    ];

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @return array
     */
    public static function attributeMap()
    {
        return self::$attributeMap;
    }

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @return array
     */
    public static function setters()
    {
        return self::$setters;
    }

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @return array
     */
    public static function getters()
    {
        return self::$getters;
    }

    /**
     * The original name of the model.
     *
     * @return string
     */
    public function getModelName()
    {
        return self::$swaggerModelName;
    }

    

    /**
     * Associative array for storing property values
     *
     * @var mixed[]
     */
    protected $container = [];

    /**
     * Constructor
     *
     * @param mixed[] $data Associated array of property values
     *                      initializing the model
     */
    public function __construct(array $data = null)
    {
        $this->container['dapp_key'] = isset($data['dapp_key']) ? $data['dapp_key'] : null;
        $this->container['protocol'] = isset($data['protocol']) ? $data['protocol'] : null;
        $this->container['version'] = isset($data['version']) ? $data['version'] : null;
        $this->container['ts'] = isset($data['ts']) ? $data['ts'] : null;
        $this->container['nonce'] = isset($data['nonce']) ? $data['nonce'] : null;
        $this->container['os'] = isset($data['os']) ? $data['os'] : null;
        $this->container['language'] = isset($data['language']) ? $data['language'] : null;
        $this->container['dapp_signature_method'] = isset($data['dapp_signature_method']) ? $data['dapp_signature_method'] : null;
        $this->container['dapp_signature'] = isset($data['dapp_signature']) ? $data['dapp_signature'] : null;
        $this->container['sign_type'] = isset($data['sign_type']) ? $data['sign_type'] : null;
        $this->container['signature'] = isset($data['signature']) ? $data['signature'] : null;
        $this->container['dapp_id'] = isset($data['dapp_id']) ? $data['dapp_id'] : null;
        $this->container['uuid'] = isset($data['uuid']) ? $data['uuid'] : null;
        $this->container['action'] = isset($data['action']) ? $data['action'] : null;
        $this->container['scope'] = isset($data['scope']) ? $data['scope'] : null;
        $this->container['expired'] = isset($data['expired']) ? $data['expired'] : null;
        $this->container['memo'] = isset($data['memo']) ? $data['memo'] : null;
    }

    /**
     * Show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalidProperties = [];

        if ($this->container['dapp_key'] === null) {
            $invalidProperties[] = "'dapp_key' can't be null";
        }
        if ($this->container['protocol'] === null) {
            $invalidProperties[] = "'protocol' can't be null";
        }
        if ($this->container['version'] === null) {
            $invalidProperties[] = "'version' can't be null";
        }
        if ($this->container['ts'] === null) {
            $invalidProperties[] = "'ts' can't be null";
        }
        if ($this->container['nonce'] === null) {
            $invalidProperties[] = "'nonce' can't be null";
        }
        if ($this->container['os'] === null) {
            $invalidProperties[] = "'os' can't be null";
        }
        if ($this->container['language'] === null) {
            $invalidProperties[] = "'language' can't be null";
        }
        if ($this->container['dapp_signature_method'] === null) {
            $invalidProperties[] = "'dapp_signature_method' can't be null";
        }
        if ($this->container['dapp_signature'] === null) {
            $invalidProperties[] = "'dapp_signature' can't be null";
        }
        if ($this->container['sign_type'] === null) {
            $invalidProperties[] = "'sign_type' can't be null";
        }
        if ($this->container['signature'] === null) {
            $invalidProperties[] = "'signature' can't be null";
        }
        if ($this->container['dapp_id'] === null) {
            $invalidProperties[] = "'dapp_id' can't be null";
        }
        if ($this->container['uuid'] === null) {
            $invalidProperties[] = "'uuid' can't be null";
        }
        if ($this->container['action'] === null) {
            $invalidProperties[] = "'action' can't be null";
        }
        if ($this->container['scope'] === null) {
            $invalidProperties[] = "'scope' can't be null";
        }
        if ($this->container['expired'] === null) {
            $invalidProperties[] = "'expired' can't be null";
        }
        return $invalidProperties;
    }

    /**
     * Validate all the properties in the model
     * return true if all passed
     *
     * @return bool True if all properties are valid
     */
    public function valid()
    {
        return count($this->listInvalidProperties()) === 0;
    }


    /**
     * Gets dapp_key
     *
     * @return string
     */
    public function getDappKey()
    {
        return $this->container['dapp_key'];
    }

    /**
     * Sets dapp_key
     *
     * @param string $dapp_key The decentralized application access key
     *
     * @return $this
     */
    public function setDappKey($dapp_key)
    {
        $this->container['dapp_key'] = $dapp_key;

        return $this;
    }

    /**
     * Gets protocol
     *
     * @return string
     */
    public function getProtocol()
    {
        return $this->container['protocol'];
    }

    /**
     * Sets protocol
     *
     * @param string $protocol The protocol name. default is 'HEP'.
     *
     * @return $this
     */
    public function setProtocol($protocol)
    {
        $this->container['protocol'] = $protocol;

        return $this;
    }

    /**
     * Gets version
     *
     * @return string
     */
    public function getVersion()
    {
        return $this->container['version'];
    }

    /**
     * Sets version
     *
     * @param string $version The protocol version such as '1.0'
     *
     * @return $this
     */
    public function setVersion($version)
    {
        $this->container['version'] = $version;

        return $this;
    }

    /**
     * Gets ts
     *
     * @return int
     */
    public function getTs()
    {
        return $this->container['ts'];
    }

    /**
     * Sets ts
     *
     * @param int $ts The current timestamp
     *
     * @return $this
     */
    public function setTs($ts)
    {
        $this->container['ts'] = $ts;

        return $this;
    }

    /**
     * Gets nonce
     *
     * @return string
     */
    public function getNonce()
    {
        return $this->container['nonce'];
    }

    /**
     * Sets nonce
     *
     * @param string $nonce The random string or auto-increment sequence
     *
     * @return $this
     */
    public function setNonce($nonce)
    {
        $this->container['nonce'] = $nonce;

        return $this;
    }

    /**
     * Gets os
     *
     * @return string
     */
    public function getOs()
    {
        return $this->container['os'];
    }

    /**
     * Sets os
     *
     * @param string $os The operating system of client such as ios, android, dweb,etc.
     *
     * @return $this
     */
    public function setOs($os)
    {
        $this->container['os'] = $os;

        return $this;
    }

    /**
     * Gets language
     *
     * @return string
     */
    public function getLanguage()
    {
        return $this->container['language'];
    }

    /**
     * Sets language
     *
     * @param string $language The i18n language code such as zh, en, etc.
     *
     * @return $this
     */
    public function setLanguage($language)
    {
        $this->container['language'] = $language;

        return $this;
    }

    /**
     * Gets dapp_signature_method
     *
     * @return string
     */
    public function getDappSignatureMethod()
    {
        return $this->container['dapp_signature_method'];
    }

    /**
     * Sets dapp_signature_method
     *
     * @param string $dapp_signature_method The signature method used by dapp.
     *
     * @return $this
     */
    public function setDappSignatureMethod($dapp_signature_method)
    {
        $this->container['dapp_signature_method'] = $dapp_signature_method;

        return $this;
    }

    /**
     * Gets dapp_signature
     *
     * @return string
     */
    public function getDappSignature()
    {
        return $this->container['dapp_signature'];
    }

    /**
     * Sets dapp_signature
     *
     * @param string $dapp_signature The signature generated by dapp.
     *
     * @return $this
     */
    public function setDappSignature($dapp_signature)
    {
        $this->container['dapp_signature'] = $dapp_signature;

        return $this;
    }

    /**
     * Gets sign_type
     *
     * @return string
     */
    public function getSignType()
    {
        return $this->container['sign_type'];
    }

    /**
     * Sets sign_type
     *
     * @param string $sign_type The signature Type,aka cryptographic algorithm.
     *
     * @return $this
     */
    public function setSignType($sign_type)
    {
        $this->container['sign_type'] = $sign_type;

        return $this;
    }

    /**
     * Gets signature
     *
     * @return string
     */
    public function getSignature()
    {
        return $this->container['signature'];
    }

    /**
     * Sets signature
     *
     * @param string $signature The signature hex string by application owner. The exclude fields is [sign_type, signature, md5].
     *
     * @return $this
     */
    public function setSignature($signature)
    {
        $this->container['signature'] = $signature;

        return $this;
    }

    /**
     * Gets dapp_id
     *
     * @return string
     */
    public function getDappId()
    {
        return $this->container['dapp_id'];
    }

    /**
     * Sets dapp_id
     *
     * @param string $dapp_id The decentralized application ID
     *
     * @return $this
     */
    public function setDappId($dapp_id)
    {
        $this->container['dapp_id'] = $dapp_id;

        return $this;
    }

    /**
     * Gets uuid
     *
     * @return string
     */
    public function getUuid()
    {
        return $this->container['uuid'];
    }

    /**
     * Sets uuid
     *
     * @param string $uuid The request uuid
     *
     * @return $this
     */
    public function setUuid($uuid)
    {
        $this->container['uuid'] = $uuid;

        return $this;
    }

    /**
     * Gets action
     *
     * @return string
     */
    public function getAction()
    {
        return $this->container['action'];
    }

    /**
     * Sets action
     *
     * @param string $action The action name which value is 'hep.auth.login'.
     *
     * @return $this
     */
    public function setAction($action)
    {
        $this->container['action'] = $action;

        return $this;
    }

    /**
     * Gets scope
     *
     * @return int
     */
    public function getScope()
    {
        return $this->container['scope'];
    }

    /**
     * Sets scope
     *
     * @param int $scope The request profile type. 1: base profile including name,head,newid; 2: advance profile including cellphone.
     *
     * @return $this
     */
    public function setScope($scope)
    {
        $this->container['scope'] = $scope;

        return $this;
    }

    /**
     * Gets expired
     *
     * @return int
     */
    public function getExpired()
    {
        return $this->container['expired'];
    }

    /**
     * Sets expired
     *
     * @param int $expired The expired timestamp
     *
     * @return $this
     */
    public function setExpired($expired)
    {
        $this->container['expired'] = $expired;

        return $this;
    }

    /**
     * Gets memo
     *
     * @return string
     */
    public function getMemo()
    {
        return $this->container['memo'];
    }

    /**
     * Sets memo
     *
     * @param string $memo The login Memo,optional.
     *
     * @return $this
     */
    public function setMemo($memo)
    {
        $this->container['memo'] = $memo;

        return $this;
    }
    /**
     * Returns true if offset exists. False otherwise.
     *
     * @param integer $offset Offset
     *
     * @return boolean
     */
    public function offsetExists($offset)
    {
        return isset($this->container[$offset]);
    }

    /**
     * Gets offset.
     *
     * @param integer $offset Offset
     *
     * @return mixed
     */
    public function offsetGet($offset)
    {
        return isset($this->container[$offset]) ? $this->container[$offset] : null;
    }

    /**
     * Sets value based on offset.
     *
     * @param integer $offset Offset
     * @param mixed   $value  Value to be set
     *
     * @return void
     */
    public function offsetSet($offset, $value)
    {
        if (is_null($offset)) {
            $this->container[] = $value;
        } else {
            $this->container[$offset] = $value;
        }
    }

    /**
     * Unsets offset.
     *
     * @param integer $offset Offset
     *
     * @return void
     */
    public function offsetUnset($offset)
    {
        unset($this->container[$offset]);
    }

    /**
     * Gets the string presentation of the object
     *
     * @return string
     */
    public function __toString()
    {
        if (defined('JSON_PRETTY_PRINT')) { // use JSON pretty print
            return json_encode(
                ObjectSerializer::sanitizeForSerialization($this),
                JSON_PRETTY_PRINT
            );
        }

        return json_encode(ObjectSerializer::sanitizeForSerialization($this));
    }
}
