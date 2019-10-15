package com.weljak.storageservice.webapi;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Value;

@Value
public class MessageMarkResponse {
    @JsonProperty
    private boolean sentSuccessfully;
}
