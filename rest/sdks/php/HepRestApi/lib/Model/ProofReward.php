<?php
/**
 * ProofReward
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
 * Swagger Codegen version: 2.4.6
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
 * ProofReward Class Doc Comment
 *
 * @category Class
 * @package  HepRestApi
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class ProofReward implements ModelInterface, ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $swaggerModelName = 'ProofReward';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerTypes = [
        'proof_hash' => 'string',
        'proof_item_id' => 'string',
        'proof_subitem_id' => 'string',
        'earn_tokens' => 'string'
    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerFormats = [
        'proof_hash' => null,
        'proof_item_id' => null,
        'proof_subitem_id' => null,
        'earn_tokens' => null
    ];

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
        'proof_hash' => 'proof_hash',
        'proof_item_id' => 'proof_item_id',
        'proof_subitem_id' => 'proof_subitem_id',
        'earn_tokens' => 'earn_tokens'
    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'proof_hash' => 'setProofHash',
        'proof_item_id' => 'setProofItemId',
        'proof_subitem_id' => 'setProofSubitemId',
        'earn_tokens' => 'setEarnTokens'
    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'proof_hash' => 'getProofHash',
        'proof_item_id' => 'getProofItemId',
        'proof_subitem_id' => 'getProofSubitemId',
        'earn_tokens' => 'getEarnTokens'
    ];

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
        $this->container['proof_hash'] = isset($data['proof_hash']) ? $data['proof_hash'] : null;
        $this->container['proof_item_id'] = isset($data['proof_item_id']) ? $data['proof_item_id'] : null;
        $this->container['proof_subitem_id'] = isset($data['proof_subitem_id']) ? $data['proof_subitem_id'] : null;
        $this->container['earn_tokens'] = isset($data['earn_tokens']) ? $data['earn_tokens'] : null;
    }

    /**
     * Show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalidProperties = [];

        if ($this->container['proof_hash'] === null) {
            $invalidProperties[] = "'proof_hash' can't be null";
        }
        if ((mb_strlen($this->container['proof_hash']) > 64)) {
            $invalidProperties[] = "invalid value for 'proof_hash', the character length must be smaller than or equal to 64.";
        }

        if ((mb_strlen($this->container['proof_hash']) < 1)) {
            $invalidProperties[] = "invalid value for 'proof_hash', the character length must be bigger than or equal to 1.";
        }

        if ($this->container['proof_item_id'] === null) {
            $invalidProperties[] = "'proof_item_id' can't be null";
        }
        if ((mb_strlen($this->container['proof_item_id']) > 64)) {
            $invalidProperties[] = "invalid value for 'proof_item_id', the character length must be smaller than or equal to 64.";
        }

        if ((mb_strlen($this->container['proof_item_id']) < 1)) {
            $invalidProperties[] = "invalid value for 'proof_item_id', the character length must be bigger than or equal to 1.";
        }

        if ($this->container['proof_subitem_id'] === null) {
            $invalidProperties[] = "'proof_subitem_id' can't be null";
        }
        if ((mb_strlen($this->container['proof_subitem_id']) > 64)) {
            $invalidProperties[] = "invalid value for 'proof_subitem_id', the character length must be smaller than or equal to 64.";
        }

        if ((mb_strlen($this->container['proof_subitem_id']) < 1)) {
            $invalidProperties[] = "invalid value for 'proof_subitem_id', the character length must be bigger than or equal to 1.";
        }

        if ($this->container['earn_tokens'] === null) {
            $invalidProperties[] = "'earn_tokens' can't be null";
        }
        if ((mb_strlen($this->container['earn_tokens']) > 64)) {
            $invalidProperties[] = "invalid value for 'earn_tokens', the character length must be smaller than or equal to 64.";
        }

        if ((mb_strlen($this->container['earn_tokens']) < 1)) {
            $invalidProperties[] = "invalid value for 'earn_tokens', the character length must be bigger than or equal to 1.";
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
     * Gets proof_hash
     *
     * @return string
     */
    public function getProofHash()
    {
        return $this->container['proof_hash'];
    }

    /**
     * Sets proof_hash
     *
     * @param string $proof_hash proof_hash
     *
     * @return $this
     */
    public function setProofHash($proof_hash)
    {
        if ((mb_strlen($proof_hash) > 64)) {
            throw new \InvalidArgumentException('invalid length for $proof_hash when calling ProofReward., must be smaller than or equal to 64.');
        }
        if ((mb_strlen($proof_hash) < 1)) {
            throw new \InvalidArgumentException('invalid length for $proof_hash when calling ProofReward., must be bigger than or equal to 1.');
        }

        $this->container['proof_hash'] = $proof_hash;

        return $this;
    }

    /**
     * Gets proof_item_id
     *
     * @return string
     */
    public function getProofItemId()
    {
        return $this->container['proof_item_id'];
    }

    /**
     * Sets proof_item_id
     *
     * @param string $proof_item_id proof_item_id
     *
     * @return $this
     */
    public function setProofItemId($proof_item_id)
    {
        if ((mb_strlen($proof_item_id) > 64)) {
            throw new \InvalidArgumentException('invalid length for $proof_item_id when calling ProofReward., must be smaller than or equal to 64.');
        }
        if ((mb_strlen($proof_item_id) < 1)) {
            throw new \InvalidArgumentException('invalid length for $proof_item_id when calling ProofReward., must be bigger than or equal to 1.');
        }

        $this->container['proof_item_id'] = $proof_item_id;

        return $this;
    }

    /**
     * Gets proof_subitem_id
     *
     * @return string
     */
    public function getProofSubitemId()
    {
        return $this->container['proof_subitem_id'];
    }

    /**
     * Sets proof_subitem_id
     *
     * @param string $proof_subitem_id proof_subitem_id
     *
     * @return $this
     */
    public function setProofSubitemId($proof_subitem_id)
    {
        if ((mb_strlen($proof_subitem_id) > 64)) {
            throw new \InvalidArgumentException('invalid length for $proof_subitem_id when calling ProofReward., must be smaller than or equal to 64.');
        }
        if ((mb_strlen($proof_subitem_id) < 1)) {
            throw new \InvalidArgumentException('invalid length for $proof_subitem_id when calling ProofReward., must be bigger than or equal to 1.');
        }

        $this->container['proof_subitem_id'] = $proof_subitem_id;

        return $this;
    }

    /**
     * Gets earn_tokens
     *
     * @return string
     */
    public function getEarnTokens()
    {
        return $this->container['earn_tokens'];
    }

    /**
     * Sets earn_tokens
     *
     * @param string $earn_tokens earn_tokens
     *
     * @return $this
     */
    public function setEarnTokens($earn_tokens)
    {
        if ((mb_strlen($earn_tokens) > 64)) {
            throw new \InvalidArgumentException('invalid length for $earn_tokens when calling ProofReward., must be smaller than or equal to 64.');
        }
        if ((mb_strlen($earn_tokens) < 1)) {
            throw new \InvalidArgumentException('invalid length for $earn_tokens when calling ProofReward., must be bigger than or equal to 1.');
        }

        $this->container['earn_tokens'] = $earn_tokens;

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

