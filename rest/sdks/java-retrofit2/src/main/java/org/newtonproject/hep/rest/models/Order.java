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
import java.util.ArrayList;
import java.util.List;
import org.newtonproject.hep.rest.models.OrderItem;

/**
 * Order
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2019-06-30T20:36:48.159+08:00")
public class Order {
  @SerializedName("proof_type")
  private String proofType = null;

  @SerializedName("description")
  private String description = null;

  @SerializedName("price_currency")
  private String priceCurrency = null;

  @SerializedName("total_price")
  private String totalPrice = null;

  @SerializedName("order_number")
  private String orderNumber = null;

  @SerializedName("seller")
  private String seller = null;

  @SerializedName("customer")
  private String customer = null;

  @SerializedName("broker")
  private String broker = null;

  @SerializedName("order_items")
  private List<OrderItem> orderItems = new ArrayList<OrderItem>();

  @SerializedName("chain_txid")
  private String chainTxid = null;

  public Order proofType(String proofType) {
    this.proofType = proofType;
    return this;
  }

   /**
   * The proof type which value is &#39;order&#39;.
   * @return proofType
  **/
  @ApiModelProperty(required = true, value = "The proof type which value is 'order'.")
  public String getProofType() {
    return proofType;
  }

  public void setProofType(String proofType) {
    this.proofType = proofType;
  }

  public Order description(String description) {
    this.description = description;
    return this;
  }

   /**
   * The order description
   * @return description
  **/
  @ApiModelProperty(required = true, value = "The order description")
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }

  public Order priceCurrency(String priceCurrency) {
    this.priceCurrency = priceCurrency;
    return this;
  }

   /**
   * The symbol of fiat or digital token, such as USD, RMB, NEW,BTC,ETH.
   * @return priceCurrency
  **/
  @ApiModelProperty(required = true, value = "The symbol of fiat or digital token, such as USD, RMB, NEW,BTC,ETH.")
  public String getPriceCurrency() {
    return priceCurrency;
  }

  public void setPriceCurrency(String priceCurrency) {
    this.priceCurrency = priceCurrency;
  }

  public Order totalPrice(String totalPrice) {
    this.totalPrice = totalPrice;
    return this;
  }

   /**
   * The amount of fiat or digital token, unit is the minimum unit of given fiat or digital token.
   * @return totalPrice
  **/
  @ApiModelProperty(required = true, value = "The amount of fiat or digital token, unit is the minimum unit of given fiat or digital token.")
  public String getTotalPrice() {
    return totalPrice;
  }

  public void setTotalPrice(String totalPrice) {
    this.totalPrice = totalPrice;
  }

  public Order orderNumber(String orderNumber) {
    this.orderNumber = orderNumber;
    return this;
  }

   /**
   * The order number
   * @return orderNumber
  **/
  @ApiModelProperty(required = true, value = "The order number")
  public String getOrderNumber() {
    return orderNumber;
  }

  public void setOrderNumber(String orderNumber) {
    this.orderNumber = orderNumber;
  }

  public Order seller(String seller) {
    this.seller = seller;
    return this;
  }

   /**
   * The seller&#39;s NewID
   * @return seller
  **/
  @ApiModelProperty(required = true, value = "The seller's NewID")
  public String getSeller() {
    return seller;
  }

  public void setSeller(String seller) {
    this.seller = seller;
  }

  public Order customer(String customer) {
    this.customer = customer;
    return this;
  }

   /**
   * The customer&#39;s NewID
   * @return customer
  **/
  @ApiModelProperty(required = true, value = "The customer's NewID")
  public String getCustomer() {
    return customer;
  }

  public void setCustomer(String customer) {
    this.customer = customer;
  }

  public Order broker(String broker) {
    this.broker = broker;
    return this;
  }

   /**
   * The broker&#39;s NewID. optional.
   * @return broker
  **/
  @ApiModelProperty(required = true, value = "The broker's NewID. optional.")
  public String getBroker() {
    return broker;
  }

  public void setBroker(String broker) {
    this.broker = broker;
  }

  public Order orderItems(List<OrderItem> orderItems) {
    this.orderItems = orderItems;
    return this;
  }

  public Order addOrderItemsItem(OrderItem orderItemsItem) {
    this.orderItems.add(orderItemsItem);
    return this;
  }

   /**
   * Get orderItems
   * @return orderItems
  **/
  @ApiModelProperty(required = true, value = "")
  public List<OrderItem> getOrderItems() {
    return orderItems;
  }

  public void setOrderItems(List<OrderItem> orderItems) {
    this.orderItems = orderItems;
  }

  public Order chainTxid(String chainTxid) {
    this.chainTxid = chainTxid;
    return this;
  }

   /**
   * The seller&#39;s NewID
   * @return chainTxid
  **/
  @ApiModelProperty(value = "The seller's NewID")
  public String getChainTxid() {
    return chainTxid;
  }

  public void setChainTxid(String chainTxid) {
    this.chainTxid = chainTxid;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Order order = (Order) o;
    return Objects.equals(this.proofType, order.proofType) &&
        Objects.equals(this.description, order.description) &&
        Objects.equals(this.priceCurrency, order.priceCurrency) &&
        Objects.equals(this.totalPrice, order.totalPrice) &&
        Objects.equals(this.orderNumber, order.orderNumber) &&
        Objects.equals(this.seller, order.seller) &&
        Objects.equals(this.customer, order.customer) &&
        Objects.equals(this.broker, order.broker) &&
        Objects.equals(this.orderItems, order.orderItems) &&
        Objects.equals(this.chainTxid, order.chainTxid);
  }

  @Override
  public int hashCode() {
    return Objects.hash(proofType, description, priceCurrency, totalPrice, orderNumber, seller, customer, broker, orderItems, chainTxid);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Order {\n");
    
    sb.append("    proofType: ").append(toIndentedString(proofType)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    priceCurrency: ").append(toIndentedString(priceCurrency)).append("\n");
    sb.append("    totalPrice: ").append(toIndentedString(totalPrice)).append("\n");
    sb.append("    orderNumber: ").append(toIndentedString(orderNumber)).append("\n");
    sb.append("    seller: ").append(toIndentedString(seller)).append("\n");
    sb.append("    customer: ").append(toIndentedString(customer)).append("\n");
    sb.append("    broker: ").append(toIndentedString(broker)).append("\n");
    sb.append("    orderItems: ").append(toIndentedString(orderItems)).append("\n");
    sb.append("    chainTxid: ").append(toIndentedString(chainTxid)).append("\n");
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

