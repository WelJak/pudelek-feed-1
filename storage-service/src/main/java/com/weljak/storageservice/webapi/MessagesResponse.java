package com.weljak.storageservice.webapi;


import lombok.Value;

import java.util.List;

@Value
public class MessagesResponse {
    private List<String> entries;
}
