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


package org.newtonproject.hep.rest.models;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

/**
 * CreateProofResponse
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2019-06-30T20:36:48.159+08:00")
public class CreateProofResponse {
  @SerializedName("proof_hash")
  private String proofHash = null;

  public CreateProofResponse proofHash(String proofHash) {
    this.proofHash = proofHash;
    return this;
  }

   /**
   * The proof hash
   * @return proofHash
  **/
  @ApiModelProperty(required = true, value = "The proof hash")
  public String getProofHash() {
    return proofHash;
  }

  public void setProofHash(String proofHash) {
    this.proofHash = proofHash;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CreateProofResponse createProofResponse = (CreateProofResponse) o;
    return Objects.equals(this.proofHash, createProofResponse.proofHash);
  }

  @Override
  public int hashCode() {
    return Objects.hash(proofHash);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateProofResponse {\n");
    
    sb.append("    proofHash: ").append(toIndentedString(proofHash)).append("\n");
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

