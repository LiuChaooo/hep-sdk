/*
 * HEP REST API
 * The REST API for HEP protocol
 *
 * OpenAPI spec version: v1
 * Contact: xiawu@zeuux.org
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;

/**
 * AuthCacheRequest
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-06-12T11:49:49.487+08:00[Asia/Shanghai]")public class AuthCacheRequest {

  @SerializedName("dapp_key")
  private String dappKey = null;

  @SerializedName("protocol")
  private String protocol = null;

  @SerializedName("version")
  private String version = null;

  @SerializedName("ts")
  private Integer ts = null;

  @SerializedName("nonce")
  private String nonce = null;

  @SerializedName("os")
  private String os = null;

  @SerializedName("language")
  private String language = null;

  @SerializedName("md5")
  private String md5 = null;

  @SerializedName("sign_type")
  private String signType = null;

  @SerializedName("signature")
  private String signature = null;

  @SerializedName("dapp_id")
  private String dappId = null;

  @SerializedName("uuid")
  private String uuid = null;

  @SerializedName("action")
  private String action = null;

  @SerializedName("scope")
  private Integer scope = null;

  @SerializedName("expired")
  private Integer expired = null;

  @SerializedName("memo")
  private String memo = null;
  public AuthCacheRequest dappKey(String dappKey) {
    this.dappKey = dappKey;
    return this;
  }

  

  /**
  * The decentralized application access key
  * @return dappKey
  **/
  @Schema(required = true, description = "The decentralized application access key")
  public String getDappKey() {
    return dappKey;
  }
  public void setDappKey(String dappKey) {
    this.dappKey = dappKey;
  }
  public AuthCacheRequest protocol(String protocol) {
    this.protocol = protocol;
    return this;
  }

  

  /**
  * The protocol name. default is &#x27;HEP&#x27;.
  * @return protocol
  **/
  @Schema(required = true, description = "The protocol name. default is 'HEP'.")
  public String getProtocol() {
    return protocol;
  }
  public void setProtocol(String protocol) {
    this.protocol = protocol;
  }
  public AuthCacheRequest version(String version) {
    this.version = version;
    return this;
  }

  

  /**
  * The protocol version such as &#x27;1.0&#x27;
  * @return version
  **/
  @Schema(required = true, description = "The protocol version such as '1.0'")
  public String getVersion() {
    return version;
  }
  public void setVersion(String version) {
    this.version = version;
  }
  public AuthCacheRequest ts(Integer ts) {
    this.ts = ts;
    return this;
  }

  

  /**
  * The current timestamp
  * @return ts
  **/
  @Schema(required = true, description = "The current timestamp")
  public Integer getTs() {
    return ts;
  }
  public void setTs(Integer ts) {
    this.ts = ts;
  }
  public AuthCacheRequest nonce(String nonce) {
    this.nonce = nonce;
    return this;
  }

  

  /**
  * The random string or auto-increment sequence
  * @return nonce
  **/
  @Schema(required = true, description = "The random string or auto-increment sequence")
  public String getNonce() {
    return nonce;
  }
  public void setNonce(String nonce) {
    this.nonce = nonce;
  }
  public AuthCacheRequest os(String os) {
    this.os = os;
    return this;
  }

  

  /**
  * The operating system of client such as ios, android, dweb,etc.
  * @return os
  **/
  @Schema(required = true, description = "The operating system of client such as ios, android, dweb,etc.")
  public String getOs() {
    return os;
  }
  public void setOs(String os) {
    this.os = os;
  }
  public AuthCacheRequest language(String language) {
    this.language = language;
    return this;
  }

  

  /**
  * The i18n language code such as zh, en, etc.
  * @return language
  **/
  @Schema(required = true, description = "The i18n language code such as zh, en, etc.")
  public String getLanguage() {
    return language;
  }
  public void setLanguage(String language) {
    this.language = language;
  }
  public AuthCacheRequest md5(String md5) {
    this.md5 = md5;
    return this;
  }

  

  /**
  * The HMAC authentication md5 checksum
  * @return md5
  **/
  @Schema(required = true, description = "The HMAC authentication md5 checksum")
  public String getMd5() {
    return md5;
  }
  public void setMd5(String md5) {
    this.md5 = md5;
  }
  public AuthCacheRequest signType(String signType) {
    this.signType = signType;
    return this;
  }

  

  /**
  * The signature Type,aka cryptographic algorithm.
  * @return signType
  **/
  @Schema(required = true, description = "The signature Type,aka cryptographic algorithm.")
  public String getSignType() {
    return signType;
  }
  public void setSignType(String signType) {
    this.signType = signType;
  }
  public AuthCacheRequest signature(String signature) {
    this.signature = signature;
    return this;
  }

  

  /**
  * The signature hex string by application owner. The exclude fields is [sign_type, signature, md5].
  * @return signature
  **/
  @Schema(required = true, description = "The signature hex string by application owner. The exclude fields is [sign_type, signature, md5].")
  public String getSignature() {
    return signature;
  }
  public void setSignature(String signature) {
    this.signature = signature;
  }
  public AuthCacheRequest dappId(String dappId) {
    this.dappId = dappId;
    return this;
  }

  

  /**
  * The decentralized application ID
  * @return dappId
  **/
  @Schema(required = true, description = "The decentralized application ID")
  public String getDappId() {
    return dappId;
  }
  public void setDappId(String dappId) {
    this.dappId = dappId;
  }
  public AuthCacheRequest uuid(String uuid) {
    this.uuid = uuid;
    return this;
  }

  

  /**
  * The request uuid
  * @return uuid
  **/
  @Schema(required = true, description = "The request uuid")
  public String getUuid() {
    return uuid;
  }
  public void setUuid(String uuid) {
    this.uuid = uuid;
  }
  public AuthCacheRequest action(String action) {
    this.action = action;
    return this;
  }

  

  /**
  * The action name which value is &#x27;hep.auth.login&#x27;.
  * @return action
  **/
  @Schema(required = true, description = "The action name which value is 'hep.auth.login'.")
  public String getAction() {
    return action;
  }
  public void setAction(String action) {
    this.action = action;
  }
  public AuthCacheRequest scope(Integer scope) {
    this.scope = scope;
    return this;
  }

  

  /**
  * The request profile type. 1: base profile including name,head,newid; 2: advance profile including cellphone.
  * @return scope
  **/
  @Schema(required = true, description = "The request profile type. 1: base profile including name,head,newid; 2: advance profile including cellphone.")
  public Integer getScope() {
    return scope;
  }
  public void setScope(Integer scope) {
    this.scope = scope;
  }
  public AuthCacheRequest expired(Integer expired) {
    this.expired = expired;
    return this;
  }

  

  /**
  * The expired timestamp
  * @return expired
  **/
  @Schema(required = true, description = "The expired timestamp")
  public Integer getExpired() {
    return expired;
  }
  public void setExpired(Integer expired) {
    this.expired = expired;
  }
  public AuthCacheRequest memo(String memo) {
    this.memo = memo;
    return this;
  }

  

  /**
  * The login Memo,optional.
  * @return memo
  **/
  @Schema(description = "The login Memo,optional.")
  public String getMemo() {
    return memo;
  }
  public void setMemo(String memo) {
    this.memo = memo;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AuthCacheRequest authCacheRequest = (AuthCacheRequest) o;
    return Objects.equals(this.dappKey, authCacheRequest.dappKey) &&
        Objects.equals(this.protocol, authCacheRequest.protocol) &&
        Objects.equals(this.version, authCacheRequest.version) &&
        Objects.equals(this.ts, authCacheRequest.ts) &&
        Objects.equals(this.nonce, authCacheRequest.nonce) &&
        Objects.equals(this.os, authCacheRequest.os) &&
        Objects.equals(this.language, authCacheRequest.language) &&
        Objects.equals(this.md5, authCacheRequest.md5) &&
        Objects.equals(this.signType, authCacheRequest.signType) &&
        Objects.equals(this.signature, authCacheRequest.signature) &&
        Objects.equals(this.dappId, authCacheRequest.dappId) &&
        Objects.equals(this.uuid, authCacheRequest.uuid) &&
        Objects.equals(this.action, authCacheRequest.action) &&
        Objects.equals(this.scope, authCacheRequest.scope) &&
        Objects.equals(this.expired, authCacheRequest.expired) &&
        Objects.equals(this.memo, authCacheRequest.memo);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(dappKey, protocol, version, ts, nonce, os, language, md5, signType, signature, dappId, uuid, action, scope, expired, memo);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AuthCacheRequest {\n");
    
    sb.append("    dappKey: ").append(toIndentedString(dappKey)).append("\n");
    sb.append("    protocol: ").append(toIndentedString(protocol)).append("\n");
    sb.append("    version: ").append(toIndentedString(version)).append("\n");
    sb.append("    ts: ").append(toIndentedString(ts)).append("\n");
    sb.append("    nonce: ").append(toIndentedString(nonce)).append("\n");
    sb.append("    os: ").append(toIndentedString(os)).append("\n");
    sb.append("    language: ").append(toIndentedString(language)).append("\n");
    sb.append("    md5: ").append(toIndentedString(md5)).append("\n");
    sb.append("    signType: ").append(toIndentedString(signType)).append("\n");
    sb.append("    signature: ").append(toIndentedString(signature)).append("\n");
    sb.append("    dappId: ").append(toIndentedString(dappId)).append("\n");
    sb.append("    uuid: ").append(toIndentedString(uuid)).append("\n");
    sb.append("    action: ").append(toIndentedString(action)).append("\n");
    sb.append("    scope: ").append(toIndentedString(scope)).append("\n");
    sb.append("    expired: ").append(toIndentedString(expired)).append("\n");
    sb.append("    memo: ").append(toIndentedString(memo)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}